---
name: resume-refiner
description: Improve existing resumes with better wording, structure, and visual polish. Use this skill whenever the user asks to "improve my resume", "polish my CV", "review my resume", "make my resume stand out", "update my resume", "rewrite my resume bullet points", or mentions having a resume file they want enhanced. Also trigger when the user talks about job application documents, career documents, or asks for resume writing help — even if they don't explicitly say "resume."
---
# Resume Refiner — Execution Map

## 在“简历雷达”中的职责边界

**负责：** 从简历中提取事实、标记证据状态、逐句改写、重组结构、提出 ATS 与视觉优化建议。

**不负责：** 不计算 JD 匹配分，不选择优秀简历模式，不生成面试题库。

**交叉验证：**
- 从 `job-application-assistant` 接收 JD 要求与证据缺口。
- 从 `excellent-resume-patterns` 接收结构参考和质量基准。
- 改写后把高风险声明交给 `interview-prep` 做可解释性压力测试。
- 任何无法追溯的事实都必须标记 `[待补]`，不得用漂亮措辞掩盖。


You improve an existing resume in seven phases. **Run them in order; each ends with a gate — a check you pass before moving on. Never edit before the P2 gate.** The core rule on every edit: **never fabricate.** Every word in the output must trace to a fact explicitly stated in the source material. You are an editor, not an author.

## Evidence base (open when a branch needs it)

`references/how-to-write-a-good-resume.md` holds the sourced research behind every rule below (Harvard/Stanford/MIT/CMU career offices, Google & Microsoft recruiters, ATS vendors, Tsinghua). Read it when:

- the **user asks why** a rule exists, or wants to override a floor — cite the source,
- the resume targets the **Chinese market** (中文) — its Chinese sections cover A4 one page, pinyin email, no photo, no 我/我的, no generic self-evaluation,
- you need the **full frameworks** — CAR / X-Y-Z detail, action-verb lists, ATS parsing specifics.

The rules below are the distilled floors; the reference file is the evidence behind them.

## Run map

```
Input: PDF · DOCX · LaTeX .tex · Markdown
  │
  ▼
P1 EXTRACT ───────────────► fact note + structure note (the truth source)
  │
  ▼
P2 SCOPE ─────────────────► focus · target · format on record   [gate: no editing before this]
  │
  ▼
P3 EDIT ──────────────────► every bullet processed · hard rules intact · scope respected
  │
  ▼
P4 POLISH ────────────────► (only if visual work was scoped) branch applied · metrics recorded
  │
  ▼
P5 REPORT ────────────────► what changed · what was preserved · structural decisions
  │
  ▼
P6 GAP REPORT ────────────► each compliance gap surfaced as a user decision
  │
  ▼
P7 FINAL AUDIT ───────────► checklist green → deliver
```

---

## P1 — Extract: turn the source into a truth source

**Do:**
1. Read the resume end to end. Branch on the source format:
   - **PDF** — load the `pdf` skill, then extract text:
     ```python
     import pdfplumber
     with pdfplumber.open("resume.pdf") as pdf:
         text = "\n".join(page.extract_text() for page in pdf.pages)
     ```
     Scanned image? The `pdf` skill also covers OCR (`pytesseract` + `pdf2image`).
   - **DOCX** — load the `docx` skill, extract with `pandoc resume.docx -o resume.md`, or use its unpack script for raw access.
   - **LaTeX `.tex`** — parse directly: content between `\begin{document}` and `\end{document}`, stripping commands to isolate text facts.
2. Observe the **original structure**: compile/`.tex` to PDF (or render the source) and record — page count, section order, item order within sections, user-created names and abbreviations. You will preserve all of these.
3. Extract **every verifiable fact** into a structured note: personal info, education, experience, projects, skills, extras (activities, awards, publications). Vague facts stay vague in the note — they are flagged later, not invented around.
4. Save both notes. This pair is your truth source: **you will not deviate from it.**

✅ **Gate:** a fact note and a structure note exist and are complete — every fact and every structural feature of the source is accounted for. Nothing unread, nothing inferred.

## P2 — Scope: understand the assignment before touching content

**Do:** Ask the user only what their request does not already answer:
1. **Focus area** — content improvement (rewording, restructuring), visual design (layout, typography), or both?
2. **Target context** (optional but recommended) — role, industry, or company type. Tailors language and emphasis without fabricating.
3. **Output format** — PDF, DOCX, LaTeX, or Markdown. Uncertain → default to the input's format.

Also record **tailoring intent**: is this document headed for a specific posting/role? If yes, P3 offers the master-resume workflow.

**Don't assume.** If the request is just "improve my resume" with no specifics, ask before proceeding.

✅ **Gate:** focus, target, and format are on record and confirmed by the user. Content is still untouched.

## P3 — Edit: the main pass

### 3.1 Hard rules — read these before editing anything

**Never fabricate (non-negotiable):**
- No job, project, degree, or skill that is not in the source.
- No inflated titles — "Research Assistant" stays "Research Assistant", not "Lead Researcher".
- No invented metrics — "improved performance" never becomes "improved performance by 40%".
- No added technologies — Python and Git in the source never become "Docker, Kubernetes, AWS".
- Dates, GPAs, and numerical facts are preserved exactly.
- No embellished institution or company names — "Tsinghua University" gains "AI Lab" only if "AI Lab" appears in the source.
- No new sections (Summary, Research Interests, Selected Coursework…) unless the user explicitly asks.
- Vague in the source stays vague — or is flagged for the user to clarify.
- User-created names and abbreviations appear verbatim — project code names ("MyGO"), custom acronyms, informal labels. Never "improve" or delete them.

**Structure is the user's, not yours:**
1. Preserve section order unless the user asks to reorder.
2. Preserve item order within sections unless the user asks. If they do, default to **descending chronological** (most recent first).
3. Never exceed the source's page count. Overflowing → tighten wording or ask "I'd need another page — is that OK?" Never silently overflow.
4. Never add page breaks where the source had none. Need one → ask.
5. Follow the source's formatting style, but make it neat: fix inconsistent spacing/alignment; a too-long project heading (name + stack on one line) may wrap to two lines. The constraint is **structural** — no redesigning sections, fonts, or layouts unless asked.

### 3.2 The bullet pass — process every experience/project entry

For each entry, apply in order:

**Step 1 — One-line check.** Each bullet should fit on a single line; multi-line bullets lose a skimmer. **Split, don't cut:** when a bullet is too long, break it into 2-3 self-contained bullets instead of deleting content.

> Source (too long): "Implemented audio captioning metrics (BLEU, METEOR, ROUGE-L, CIDEr, SPICE) with JSON logging for reproducibility"
> Split into:
> - "Implemented audio captioning metrics (BLEU, METEOR, ROUGE-L, CIDEr, SPICE)"
> - "Enhanced reproducibility with structured JSON logging for experiment results"

Each resulting bullet gets its own action verb and stands alone — a reader understands any one without its neighbors. Trim redundant descriptors first (3.2, last item); split only what still overflows.

**Step 2 — Rewrite against the playbook** (below).

**Step 3 — Redundancy sweep.** Merge or cut bullets that say the same thing in different words — but never delete user-created names, abbreviations, or unique project identifiers.

#### The rewriting playbook (consult per bullet)

**Accomplishment, not duty.** Shape each bullet as **Accomplished [X], as measured by [Y], by doing [Z]** (X-Y-Z, a.k.a. CAR: Challenge → Action → Result). Open with the most interesting fact so a skimmer keeps reading.

**Verb-first.** Start with an action verb that shows ownership:

| Weak                | Strong                            |
| ------------------- | --------------------------------- |
| Worked on           | Led, Architected, Designed, Built |
| Helped with         | Drove, Coordinated, Spearheaded   |
| Was responsible for | Managed, Owned, Directed          |
| Used / Utilized     | Leveraged, Applied, Deployed      |

**Results before method.** A skimmer should grasp impact immediately:
- Weak: "Used LSTM networks to predict power grid load based on time-series data"
- Better: "Built an LSTM-based prediction system for residential power grid load, achieving 88% test accuracy"

**Surface quantified results.** Numbers in the source come forward:
- Weak: "Collected and cleaned large-scale carbon emission data"
- Better: "Curated carbon emission datasets spanning 100+ power stations for real-time intensity analysis"

**Make the scope explicit.** Scale in the source becomes the headline:
- Weak: "Provided technical coordination for debate teams"
- Better: "Managed remote sessions for 100+ debate teams across a nationwide competition"

No measurable result in the source? Qualify with scale ("team of 15") or a relative comparison — surface what is implicit; never invent a number.

**Mirror the source's technical depth.** Don't make descriptions more technical or more simplified than the source. "Built a Deep Q-Network (DQN) model from scratch with PyTorch" stays at that level unless the user asks otherwise.

**Tense and voice.** Present tense for current work, past for completed. No first person — never I/me/my (中文: never 我/我的); the subject is implied, verbs carry it.

**Dates never lead.** The date is the least important information in a bullet. It lives in the entry header (role / company / dates), never at the start of a description bullet, never more prominent than the content.

**Trim redundant descriptors.** Two words for one thing → keep the more specific:
- "multimodal audio captioning" → "audio captioning"
- "high-frequency real-time carbon intensity" → "high-frequency carbon intensity"
- "modular Generator, Reflector, and Curator agents for multimodal audio" → "…for audio"

**Worked example** (same facts, stronger frame, one line):
> Source: "Analyzed the performance of a high-frequency carbon intensity (CI) database for power sector monitoring"
> Improved: "Evaluated a high-frequency carbon intensity (CI) database for real-time power sector emissions monitoring"

### 3.3 Consistency sweep — across the whole document

Enforce one format ruthlessly: date formats (Sep 2023 vs 09/2023 — pick one), bullet punctuation (periods or none — pick one), typeface, bullet glyphs, spacing, and alignment. Mixed signals read as carelessness.

### 3.4 Section-level changes — only what P2 allowed

If tailoring was scoped, adjust **emphasis and wording, not structure**:
- **Master-resume workflow** (recommended for tailoring): keep the user's current document as the **master**, produce the tailored **variant** as a separate output, and say the master stays for future variants. Never silently delete from the master — a variant may drop or compress, the master keeps the full record. Shifting emphasis is editing, not fabrication.
- **Order sections by importance to the target role** — suggest it, don't impose it. Education leads for students/new grads; after ~2-3 years of full-time experience, Experience leads (an experienced candidate with Education first gets misread as a student).
- **Rename sections for tone** only on request: "Experience" → "Research Experience" (academic), "Projects" → "Key Projects & Initiatives" (PM). No new sections.
- **Skills section**: group by category (Languages / Frameworks / Tools); drop filler words ("etc."); no soft skills (teamwork, leadership).
- **Summary/Objective**: only if the user asks. Then: cap near 4 lines plus a few bullets, specific to the target role — never generic ("seeking a challenging position").

✅ **Gate:** every experience and project bullet has been through 3.2; the consistency sweep (3.3) is done; no hard rule (3.1) was broken; anything outside the P2 scope is untouched — and if it is a compliance-floor gap, it is queued for the P6 report.

## P4 — Polish: visual design, only if P2 scoped it

If visual work was **not** scoped → note "no visual work scoped" and go straight to P5.

If scoped, follow the source's formatting patterns — no imposed redesign unless asked — and branch on output format:

**LaTeX output** (sb2nov-style templates are already clean — improve subtly): consistent spacing between sections; professional font choice (FiraSans/Roboto for modern, Charter/Garamond for traditional); balanced margins; `\usepackage{hyperref}` with `hidelinks`.

**DOCX output** — load the `docx` skill for full guidance (`docx-js`): page size US Letter (12240 × 15840 DXA) or A4 (11906 × 16838 DXA), 1-inch margins; built-in heading styles overridden by exact IDs; `LevelFormat.BULLET` for bullets (never manual Unicode); tab stops for date/role alignment; paragraph bottom borders for dividers (never tables); validate with `python scripts/office/validate.py`. Arial/Calibri 10-11pt body, 14-16pt name.

**PDF from scratch** — load the `pdf` skill, use `reportlab` (SimpleDocTemplate + Paragraph + Spacer): name 18-22pt bold centered; contact one line 9-10pt centered; section headers 12-14pt with subtle rule; body 10-11pt; proper hanging-indent bullets; consistent 0.7-1in margins. Match the source's page count.

**Whatever the format, respect the floors** (minimums, never design below — and never shrink the font to fit a page; an unreadable resume is skipped):
- Body ≥ 10pt (Microsoft's recruiters say 11pt); one typeface — Times New Roman / Arial / Calibri are safe; name may be larger.
- Margins ≥ 0.5in (Stanford recommends 0.7in), consistent on all sides.
- Single column, standard section headings (Contact Information / Experience / Education / Skills) — ATS parsers expect this; no content in tables, text boxes, images, or headers/footers.
- Bold the job title **or** the company (the one with more impact) — no underlining, shading, or text boxes.
- Deliver a text-based PDF (LaTeX/RenderCV output qualifies) unless the employer or system asks for DOCX; after conversion verify the layout held and the text layer is selectable.
- Length by experience: 1 page for students/new grads; PhD industry searches may run 1-2; ~1 page per 10 years beyond that. Page 2 (if any) carries the name + contact and stays as dense as page 1.
- Chinese-market target? The evidence file carries the specifics (A4 one page, 宋体/微软雅黑 with Times New Roman for Latin, pinyin email, no photo / birth date / marital status).

**Record the metrics** you will audit in P6: body font size, margins, page count, layout (columns/tables/boxes), where contact info sits.

✅ **Gate:** the format branch is applied; floors respected; metrics recorded; page count equals the source's — or the page-add question was asked and answered at P5.

## P5 — Report and hand back

Deliver the improved resume, then report:
1. **What changed** — e.g., "Rewrote 8 bullets with stronger action verbs, tightened the skills section, split 3 long bullets into one-liners."
2. **What you preserved** — quirks kept intact ("GPA: TBD", custom project name "MyGO") noted explicitly.
3. **Structural decisions** — original section order confirmed, or N bullets split, or variant-vs-master produced.
4. **Ask for feedback** — invite adjustments.

## P6 — Compliance gap report (every job, after P5)

The floors are advisory: the user owns the document, so you don't silently change what they didn't ask to change. Audit the P4 metrics against the floors and surface **every gap as a user decision**. For each gap state: **the floor + its source**, **what the document does**, **the fix**, then ask whether to apply it.

Gap examples:
- Body below 10pt: "Body is 9.5pt; the 10pt floor comes from Harvard/MIT/CMU career offices and Google's Bock. Raise it? This may add a page."
- Margins below 0.5in.
- Overlength for the experience level (2-page resume for a new grad).
- Multi-column layout, tables, or text boxes carrying content.
- Contact info only in headers/footers.
- Chinese-market target carrying photo, birth date, marital status, or a generic objective.

Present the gaps as a short checklist — the user decides each. If the improvements silently pushed past the source's page count, this report is where that surfaces. If a gap has no fix short of undoing an explicit user instruction, just report it.

## P7 — Final audit (the "done" gate)

Run every check before calling the job complete (condensed; the sourced list lives in the evidence file):
- [ ] No spelling/grammar errors — proofread bottom-up or have someone else read it
- [ ] Contact info complete; email professional (pinyin-based for Chinese targets); no photo / birth date / marital status
- [ ] Every bullet starts with an action verb; present tense for current work, past for completed
- [ ] No "responsible for / duties included" phrasing; no I/me/my (or 我/我的)
- [ ] Quantified where facts exist; scope explicit; no invented metrics
- [ ] No date-led bullets; dates in entry headers as month + year
- [ ] Section and item order serve the target role; items reverse-chronological within sections
- [ ] Stale honors, irrelevant one-off events, generic self-evaluation removed (asked first)
- [ ] No confidential information (the NYT test: if you wouldn't see it in print, it doesn't belong); no exaggerations
- [ ] One typeface; body ≥ 10pt; margins ≥ 0.5in; single column; standard section headings
- [ ] Length matches the experience level; page 2 (if any) carries name + contact
- [ ] Text-layer PDF or the employer's required format; layout verified after conversion

✅ **Gate:** every box is checked, or an unchecked box was explicitly waived by the user in P6. Then — and only then — say the resume is done.

---

## Escalation playbook (fires anywhere between P3 and P6)

Stop and ask the user when you hit any of these; don't guess past them:

| Condition | Action |
|---|---|
| A bullet says "Worked on various projects" | Flag: "Too vague. Can you name a specific project and your contribution?" |
| A section is nearly empty | Suggest removing or filling it |
| The resume is 3+ pages | Recommend trimming |
| Improvements would push to an extra page | Ask: "Should I trim to fit, or is the extra page OK?" |
| Section order could better serve the goals | Suggest: "Reorder projects with the most relevant first for this role?" — don't just do it |
| No numbers anywhere | Flag: quantified results are the single highest-leverage improvement; ask whether the facts exist to surface them |
| An entry lacks dates | Flag: "This entry has no dates. Can you provide them?" Headers without month/year look like gaps |
| One generic resume aimed at a specific role | Offer the master-variant workflow (3.4) instead of silently rewriting toward one job |
