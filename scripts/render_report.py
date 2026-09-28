#!/usr/bin/env python3
"""Render Markdown reports into readable HTML and DOCX files.

Markdown remains the source of truth. HTML is dependency-free; DOCX requires
python-docx. PDF is optional and can be produced by opening DOCX/HTML in Word,
WPS, or a browser and using Print / Save as PDF.
"""
from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

CSS = """
:root { color-scheme: light; }
body { margin:0; background:#f5f7fb; color:#172033; font-family:"Microsoft YaHei","Segoe UI",Arial,sans-serif; }
main { max-width:980px; margin:32px auto; padding:48px 56px; background:#fff; box-shadow:0 12px 40px rgba(20,40,80,.10); border-radius:12px; }
h1,h2,h3,h4 { color:#123b7a; line-height:1.25; margin-top:1.6em; }
h1 { font-size:30px; border-bottom:3px solid #2563eb; padding-bottom:12px; }
h2 { font-size:23px; border-bottom:1px solid #d9e2f2; padding-bottom:8px; }
h3 { font-size:18px; }
p,li,td,th { font-size:15px; line-height:1.7; }
ul,ol { padding-left:28px; }
blockquote { margin:16px 0; padding:12px 18px; background:#eef5ff; border-left:4px solid #2563eb; color:#294264; }
table { width:100%; border-collapse:collapse; margin:18px 0; }
th,td { border:1px solid #cfd8e8; padding:9px 11px; vertical-align:top; }
th { background:#edf3ff; color:#123b7a; }
code { background:#f0f3f8; padding:2px 5px; border-radius:4px; font-family:Consolas,monospace; font-size:13px; }
pre { background:#101827; color:#e7eefc; padding:16px; border-radius:8px; overflow:auto; }
pre code { background:transparent; color:inherit; padding:0; }
hr { border:0; border-top:1px solid #d9e2f2; margin:28px 0; }
@media print { body{background:#fff} main{box-shadow:none;margin:0;max-width:none;padding:16mm} h2{break-after:avoid} table{break-inside:auto} tr{break-inside:avoid} }
"""

def inline_html(s: str) -> str:
    s=html.escape(s, quote=False)
    s=re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s=re.sub(r'`(.+?)`', r'<code>\1</code>', s)
    return s

def inline_text(s: str) -> str:
    s=re.sub(r'\*\*(.+?)\*\*', r'\1', s)
    s=re.sub(r'`(.+?)`', r'\1', s)
    return s.replace('\t',' ')

def is_table_start(lines, i):
    return i+1 < len(lines) and lines[i].strip().startswith('|') and re.match(r'^\s*\|?[\s:|-]+\|?\s*$', lines[i+1])

def parse_table(lines, i):
    rows=[]
    while i < len(lines) and lines[i].strip().startswith('|'):
        raw=lines[i].strip().strip('|')
        cells=[inline_html(c.strip()) for c in raw.split('|')]
        if not re.match(r'^[\s:|-]+$', raw):
            rows.append(cells)
        i += 1
    return rows, i

def markdown_to_html(md: str) -> str:
    lines=md.splitlines()
    out=[]; i=0; list_type=None; in_code=False; code=[]
    def close_list():
        nonlocal list_type
        if list_type:
            out.append(f'</{list_type}>')
            list_type=None
    while i < len(lines):
        line=lines[i]
        if line.strip().startswith('```'):
            if in_code:
                out.append('<pre><code>'+html.escape('\n'.join(code))+'</code></pre>')
                code=[]; in_code=False
            else:
                close_list(); in_code=True
            i+=1; continue
        if in_code:
            code.append(line); i+=1; continue
        if not line.strip():
            close_list(); i+=1; continue
        if is_table_start(lines,i):
            close_list(); rows,i=parse_table(lines,i)
            if rows:
                out.append('<table><thead><tr>'+''.join(f'<th>{c}</th>' for c in rows[0])+'</tr></thead><tbody>')
                for row in rows[1:]: out.append('<tr>'+''.join(f'<td>{c}</td>' for c in row)+'</tr>')
                out.append('</tbody></table>')
            continue
        m=re.match(r'^(#{1,4})\s+(.*)$', line)
        if m:
            close_list(); level=len(m.group(1)); out.append(f'<h{level}>{inline_html(m.group(2))}</h{level}>'); i+=1; continue
        m=re.match(r'^\s*[-*]\s+(.*)$', line)
        if m:
            if list_type!='ul': close_list(); out.append('<ul>'); list_type='ul'
            out.append('<li>'+inline_html(m.group(1))+'</li>'); i+=1; continue
        m=re.match(r'^\s*\d+[.)]\s+(.*)$', line)
        if m:
            if list_type!='ol': close_list(); out.append('<ol>'); list_type='ol'
            out.append('<li>'+inline_html(m.group(1))+'</li>'); i+=1; continue
        if line.startswith('>'):
            close_list(); out.append('<blockquote>'+inline_html(line.lstrip('> ').strip())+'</blockquote>'); i+=1; continue
        if line.strip() in ('---','***'):
            close_list(); out.append('<hr>'); i+=1; continue
        close_list(); out.append('<p>'+inline_html(line.strip())+'</p>'); i+=1
    close_list()
    return '\n'.join(out)

def markdown_to_docx(md: str, path: Path) -> tuple[bool,str]:
    try:
        from docx import Document
        from docx.shared import Pt, Inches
    except Exception as exc:
        return False, f'python-docx not installed: {exc}'
    doc=Document()
    for section in doc.sections:
        section.top_margin=Inches(0.65); section.bottom_margin=Inches(0.65)
        section.left_margin=Inches(0.72); section.right_margin=Inches(0.72)
    style=doc.styles['Normal']; style.font.name='Microsoft YaHei'; style.font.size=Pt(10.5)
    lines=md.splitlines(); i=0; in_code=False; code=[]
    while i < len(lines):
        line=lines[i]
        if line.strip().startswith('```'):
            if in_code:
                p=doc.add_paragraph('\n'.join(code)); p.style=doc.styles['No Spacing']
                for run in p.runs: run.font.name='Consolas'; run.font.size=Pt(9)
                code=[]; in_code=False
            else: in_code=True
            i+=1; continue
        if in_code: code.append(line); i+=1; continue
        if not line.strip(): i+=1; continue
        if is_table_start(lines,i):
            rows,i=parse_table(lines,i)
            if rows:
                table=doc.add_table(rows=len(rows), cols=max(len(r) for r in rows))
                try: table.style='Light Grid Accent 1'
                except Exception: table.style='Table Grid'
                for ri,row in enumerate(rows):
                    for ci,cell in enumerate(row):
                        table.cell(ri,ci).text=re.sub(r'<[^>]+>','',cell)
            continue
        m=re.match(r'^(#{1,4})\s+(.*)$', line)
        if m:
            doc.add_heading(inline_text(m.group(2)), level=min(len(m.group(1)),4)); i+=1; continue
        m=re.match(r'^\s*[-*]\s+(.*)$', line)
        if m:
            p=doc.add_paragraph(style='List Bullet'); p.add_run(inline_text(m.group(1))); i+=1; continue
        m=re.match(r'^\s*\d+[.)]\s+(.*)$', line)
        if m:
            p=doc.add_paragraph(style='List Number'); p.add_run(inline_text(m.group(1))); i+=1; continue
        if line.startswith('>'):
            p=doc.add_paragraph(); p.paragraph_format.left_indent=Inches(0.25); p.add_run(inline_text(line.lstrip('> ').strip())).italic=True; i+=1; continue
        if line.strip() in ('---','***'):
            doc.add_paragraph('────────────────────'); i+=1; continue
        doc.add_paragraph(inline_text(line.strip())); i+=1
    doc.save(path)
    return True,''

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('input', nargs='+')
    ap.add_argument('--output-dir', default=None)
    ap.add_argument('--formats', nargs='+', default=['html'], choices=['html','docx'])
    args=ap.parse_args()
    for raw in args.input:
        src=Path(raw)
        out=Path(args.output_dir) if args.output_dir else src.parent
        out.mkdir(parents=True,exist_ok=True)
        md=src.read_text(encoding='utf-8')
        if 'html' in args.formats:
            title=next((inline_text(x.lstrip('# ').strip()) for x in md.splitlines() if x.startswith('# ')),src.stem)
            page=f'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><style>{CSS}</style></head><body><main>{markdown_to_html(md)}</main></body></html>'
            p=out/(src.stem+'.html'); p.write_text(page,encoding='utf-8'); print('HTML',p)
        if 'docx' in args.formats:
            p=out/(src.stem+'.docx'); ok,msg=markdown_to_docx(md,p)
            print('DOCX',p if ok else 'SKIPPED '+msg)
    return 0

if __name__=='__main__': raise SystemExit(main())