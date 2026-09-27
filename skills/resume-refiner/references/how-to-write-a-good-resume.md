# 如何写一份好简历(How to Write a Good Resume)

> 面向软件工程/AI 算法工程师求职的研究型指南。所有建议均追溯到一手来源:
> 美国顶尖高校就业指导中心(Harvard / Stanford / MIT / CMU)、大厂一手招聘材料(Microsoft Learn、Google/Laszlo Bock)、ATS 官方说明,以及中文高校官方就业材料(清华、北大)。
> 适用背景:本指南的常见使用场景是维护用 RenderCV(YAML→LaTeX→PDF)生成的中文与英文简历,因此末尾单列了 RenderCV/技术排版相关的注意事项。

---

## 1. 简历的本质:它不是履历表,而是"营销文件"

所有高校就业中心的第一句话几乎一致:**简历的目的只有一个——拿到面试**,而不是讲完你的一生。

- Stanford GSB: "Your resume is a marketing tool designed to communicate relevant experience and accomplishments to your target audience. A resume is not a biography."(简历是营销工具,不是传记。)[Stanford GSB – Resumes & Cover Letters](https://www.gsb.stanford.edu/alumni/career-resources/job-search/resumes)
- MIT Sloan: "Your Resume is a Marketing Document ... To generate interest from potential employers to invite you for interviews ... To tell your story in 1-page. Your resume is not a list of everything you have ever done!"(简历不是"做过的一切"的清单。)[Building Your MIT Sloan Resume (slides)](https://cdn.cdo.mit.edu/wp-content/uploads/sites/67/2020/05/Resume-Educational-Videos-2018-Slides.pdf)
- Harvard FAS: "Although it alone won't get you a job or internship, a good resume is an important factor in obtaining an interview."(简历本身拿不到工作,但它是获得面试的关键因素。)[Harvard College Guide to Creating a Strong Resume](https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/)
- CMU: "Your resume is a marketing piece ... In the job search, its purpose is to get you an interview." [CMU Graduate Student Resume Guide](https://www.cmu.edu/career/documents/sample-resumes-cover-letters/graduate_student_resume_guide_2026.pdf)
- 清华大学就业中心:"简历最基本的功用(目的)是争取面试",并强调"写什么比怎么写更重要"。 [清华大学就业指导中心《毕业生时间管理与求职简历的制作》](https://career.tsinghua.edu.cn/__local/7/81/97/92E6E3CBDF18021EDD22B0FEAF9_4789F710_81DBD.pdf?e=.pdf)

由此推出两条铁律:

1. **读者时间极短**:Stanford 说招聘者平均只扫 6-8 秒(recruiter spends six to eight seconds scanning a resume);MIT CAPD 引用行业共识为不到 6 秒甚至 "less than 6 seconds"。[Stanford GSB 同上][MIT CAPD – Interphase resume resources](https://capd.mit.edu/blog/2026/06/23/interphase-2026-resume-resources/)
2. **内容必须为特定岗位裁剪(tailor)**:同一份简历投所有岗位是最大错误之一。Harvard 明确把 "Not tailored to the position or industry" 列为头号错误(见下"常见错误")。[Harvard HES 简历手册(PDF)](https://cdn-careerservices.fas.harvard.edu/wp-content/uploads/sites/161/2024/08/2024-HES_resume-and-letter.pdf)

---

## 2. 结构与板块(Structure & Sections)

### 2.1 各校一致的"标准骨架"

Harvard / Stanford / MIT / CMU 四校指南可归纳出如下通用骨架(顺序按对目标岗位的重要度调整):

| 板块 | 内容要点 | 备注 |
|---|---|---|
| **联系方式 Header** | 姓名、电话、邮箱、LinkedIn/个人主页;CMU 建议放定制化 LinkedIn 链接 | 不写出生日期/照片/婚姻状况(Harvard 明确 Don't include a picture、Don't include age or marital status)[Harvard HES 手册同上] |
| **Education 教育背景** | 学校全称、学位全称、毕业/预计毕业年月(Month & Year)、专业;GPA 可写(带满分制) | 学生/应届/硕博申请者放最前;**有工作经验后移到 Experience 之后**(Microsoft 原文:毕业超过两三年后 education 应放底部)[Microsoft Learn – How to Get a Job At Microsoft Part II](https://learn.microsoft.com/en-us/archive/blogs/mis_laboratory/how-to-get-a-job-at-microsoft-part-ii-writing-an-awesome-resume) |
| **Experience 经历** | 职位头衔、公司、地点、起止时间(月+年);倒序 | 一个岗位的头部信息:职位 / 公司 / 时间,地点在美式简历中常见于右侧 |
| **Projects 项目** | 课程项目、研究项目、开源项目均可;写清 a) 你的角色 b) 做了什么 c) 用的技术 | Microsoft 前工程师:学生/应届简历几乎"必须有项目",而且自发的个人项目比课程项目更有说服力("Even more impressive is the work that you did on your own")[Microsoft Learn – How to Write Your First Developer Resume](https://learn.microsoft.com/en-us/archive/blogs/steverowe/how-to-write-your-first-developer-resume) |
| **Skills 技能** | 编程语言、框架、工具、语言;按子类分组、按熟练度排序 | CMU:不要在此列 soft skills(如 teamwork/leadership)[CMU Graduate Student Resume Guide 同上] |
| **荣誉/奖项等(可选)** | Honors, Publications, Patents, Leadership | MIT 建议近 3-5 条、陈旧荣誉删除(Gaba 案例见下) |

CMU 对"必选 vs 可选"板块的权威划分:
- **必选**:Contact Information、Education、Skills;
- **按经历选**:**Experience / Projects / Research**(至少一类);
- **可选**:Leadership、Activities、Honors、Publications、Objective/Summary。
[CMU Graduate Student Resume Guide](https://www.cmu.edu/career/documents/sample-resumes-cover-letters/graduate_student_resume_guide_2026.pdf)

### 2.2 板块顺序:按"对这份工作的重要度"排,不是按固定模板

- Harvard: "List headings (such as Experience) in order of importance";"If this section is more relevant ... consider moving this above your Experience section." [Harvard College Guide 同上][Harvard HES 手册同上]
- Stanford: 用**描述性标题**(Research Experience、Teaching Experience、Leadership Experience)替代笼统的 "Work Experience / Other",让读者一眼看到你的卖点。[Stanford BEAM – 4 Easy Steps handout](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/developing_your_resume_handout.pdf)
- Harvard PhD 版指南里有真实案例:一位求职者为了投生物医药咨询岗,把 "Leadership Experience" 提到 "Research Experience" 之前,因为该公司明确强调领导力与量化能力——**同一个你,顺序可以完全不同**。[Harvard GSAS – Resumes and Cover Letters for PhD Students](https://cdn-careerservices.fas.harvard.edu/wp-content/uploads/sites/161/2024/08/2024-GSAS_phd_resume_cover_letters-1.pdf)
- 对 AI/算法岗特别相关的一条(微软前招聘工程师的实战经验):**学生/应届:Education 在前;社招(约 2-3 年全职后):Experience 在前**,他讲了一个真实事故——一位有 3 年工作经验的商学院毕业生因沿用学生模板(Education 在前)而被误当在校生、简历被搁置。[Microsoft Learn – Part II 同上]

### 2.3 摘要 Summary(可选但推荐,尤其对社招)

- Stanford GSB: "Summary: Communicates your core brand and competencies. Define what's unique and relevant to your target role. It often includes your years of experience and bullet points of your key accomplishments or skills. **Limit the summary to 4 lines plus bullet points.**" [Stanford GSB 同上]
- CMU: objective/summary 可选,多数硕博简历不需要;若放,要写明"你追求的方向 + 你凭什么能带来价值",空泛的 "To pursue the computer engineering field" 应避免;不确定就删。[CMU Graduate Engineering Resume Guide](https://www.cmu.edu/career/documents/sample-resumes-cover-letters/resume_guide_college_of_engineering_graduate_students_2023.pdf)

---

## 3. 写经历的正确姿势:成就(Achievement),不是职责(Duty)

### 3.1 核心原则:每条 bullet 都以动词开头,讲"结果与影响",不讲"职责范围"

- Harvard 语言规范:**Specific > general;Active > passive;Fact-based (quantify and qualify);Written for people who scan quickly**;禁止 "duties included"/"responsible for" 式开头。[Harvard College Guide 同上]
- Stanford 的原话: "Do design your descriptions to focus on your accomplishments, using action verbs ... avoid phrases such as 'duties included'";"Do try quantifying results ... such as 'Created marketing campaign that increased club membership by 25%.'" [Stanford BEAM resume guide (PDF)](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume_and_cover_letter_examples_1.pdf)
- 中国市场的对应表述(清华/百度嘉宾):"用动词和数字说明你的成绩,你所用的动词,决定了你传递出来的能力";社会工作/实习经历要突出两个 R——**Responsibility & Result**。[清华大学《简历大家谈》同伴教育讲座](https://career.tsinghua.edu.cn/__local/B/DF/76/D3D943A391CACE5F9B5A714F487_94DB34BE_CE07E.pdf?e=.pdf)

### 3.2 可落地的结构框架:CAR / STAR / XYZ

各校推荐的bullet内部结构高度一致,只是缩写不同:

1. **Stanford 的 CAR 法**:**C**ontext(背景,你做了什么)→ **A**ction(怎么做的,用了哪些技能)→ **R**esult(结果,尽量量化)。1-2 句话一条。[Stanford BEAM – CAR Method](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/car-method-for-developing-resume-content.docx-1.pdf)
2. **MIT Sloan 的 C-A-R 法**(即 Challenge-Action-Result,或 R-A-C):先用动词、限 1-2 行,再补结果与影响;官方还给了三档改写示例:
   - Draft: "Listened to the morning market calls everyday and took notes..."
   - Better: "Summarized the daily morning market calls and distributed to team"
   - Best: "Summarized daily market calls and identified key takeaways; distributed report to team of 15"
   差别就是:去冗余、动词开头、补上"团队 15 人"这类量。[Building Your MIT Sloan Resume 同上]
3. **Laszlo Bock(前 Google 人事副总裁)的 X-Y-Z 公式**:**"Accomplished [X], as measured by [Y], by doing [Z]."** 即"完成了 X,以 Y 为度量,通过 Z 实现"。该公式被 Tech Interview Handbook 与多个求职辅导源转述为 Google 系简历的黄金句式。[Tech Interview Handbook – resume guide](https://www.techinterviewhandbook.org/resume/)(公式来源为 Bock 在 Google 期间的公开分享)

### 3.3 每条 bullet 的"行数与条数"工程标准

- MIT Sloan:每份经历 3-5 条 bullet;每条 1-2 行;删掉 a/an/the、empty modifiers("extremely""successfully""numerous""such as")。[MIT Sloan slides 同上]
- Stanford GSB:每份工作 3-4 条 bullet、每条不超过 2 行;**最有意思的事实放句首**,勾起读者读下去。[Stanford GSB 同上]
- CMU:每条 bullet 一个中心思想,尽量不超过两行;句号等标点用法保持一致(bullet 可不加句号)。[CMU Graduate Engineering Resume Guide 同上]
- MIT:每条经历的 bullet 数不必强行一致,有 1 条有意义的就写 1 条,有 3 条就写 3 条;经历数量与篇幅按"与目标岗位的相关度"分配,越相关越详细。[MIT CAPD – resume resources](https://capd.mit.edu/resources/resumes/)

### 3.4 动词时态与自我代词

- 现在的工作用一般现在时,过去的工作用过去时(CMU 的 self-review 清单: "Each phrase starts with an action verb in the appropriate tense (present for current, past for completed experiences)")。[CMU 同上]
- **不要用第一人称 I/me/my**(中美指南一致):Harvard 明确 "Do not use personal pronouns (such as I)";清华讲座也强调 "简历中不应该使用第一人称,如'我'、'我的'"。[Harvard HES 手册同上][清华《简历大家谈》同上]
- 每条以行为动词开头:动词清单可查 Harvard([Create a Strong Resume](https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/))与 Stanford([Action Verb List](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume_and_cover_letter_examples_1.pdf))官方分类动词表(Leadership/Communication/Research/Technical/Quantitative/Creative/Organizational 等)。注意动词要**多样且准确**,MIT: "Vary the verbs you choose to show a range of skills"。[MIT Sloan 同上]

---

## 4. 量化(Quantification):简历里最值钱的东西

所有一手来源都把"量化"列为区分平庸与优秀的第一要素:

- Stanford: "Be as quantitative as possible: revenue growth, money saved, market share growth, etc.";每个职位要写 "size and scope, revenue or budget managed, and number of people on your team"。[Stanford GSB 同上]
- MIT: bullets 要 "Think Result–Action–Challenge ... Capture the impact of your work wherever you can";"Quantify when possible and qualify results when you cannot"。[MIT Sloan 同上]
- 清华/百度嘉宾(中国市场):"GPA排名等信息应用数字来说明,例如专业前 5%,相对数字比绝对数字更有说服力";反例是空洞的 "提高了领导力及沟通协调能力",正例带 "7% 销售成本"。[清华《简历大家谈》同上]
- 中文简历同样要"以数字和实例说话",这是清华官方讲座给出的简历写作四大要领之一(精炼扼要 / 针对性强 / 以数字和实例说话 / 动词描述经历)。[同上]

量化无绝对数字时的替代方案(MIT):"qualify results when you cannot"——用范围、百分比、相对比较描述。Google 系求职材料对 NDA 场景也建议:用相对表述("~3M daily users (mid-tier consumer product)"、"top 3 services by RPS")。[MIT Sloan 同上][ResumeAdapter – Google Resume Guide(转述 Bock)](https://www.resumeadapter.com/companies/google)

### 实例对照(通用示例)

| 弱(职责式) | 强(成就式) |
|---|---|
| Responsible for building an agent skill for financial documents | Developed an agent skill extracting financial indicators from brokerage report PDFs, cutting LLM context consumption via heuristic + regex scoring |
| Worked on RL trading pipeline | Benchmarked DRL strategies against MVO/DJIA/S&amp;P 500 baselines; achieved ~40% annualized return in PPO backtest |
| Tuned hyperparameters | Tuned hyperparameters to reach 88% test accuracy through systematic train-test validation |

(上表两栏为通用"写法示范",非真实简历条目;改写时请以自己的真实事实为准。)

---

## 5. 针对岗位定制 + ATS 关键词处理(Tailoring & ATS)

### 5.1 针对每个岗位裁剪——先有"母版",再出"变体"

- Harvard: "Tailor your resume to the type of position you're seeking." [Harvard College Guide 同上]
- MIT CAPD 给出了最实用的工作流:**保留一份"完整版"简历作为母版,针对具体岗位再删减压缩成 1-2 页定向版**——去掉低相关细节、重复任务、压缩描述,把最相关的信息放大。[MIT CAPD – Career toolkit](https://capd.mit.edu/resources/career-toolkit-crafting-an-effective-resume/)
- Harvard PhD 指南:如果你同时投研发岗、投行量化岗、咨询岗,你可能需要三个不同版本——同一个科研项目,投研发强调工程方法,投量化强调数学建模,投咨询强调领导力与解决问题能力。[Harvard GSAS 同上]
- 微软:招聘会可以带 3-4 个不同版本(web dev / database / security ...)。[Microsoft Learn – Part II 同上]

### 5.2 ATS 关键词:真实情况比传闻温和,但基本卫生要做对

需要先澄清一个广为流传的误区:**ATS 不是"自动刷人机",关键词不会自动拒信**;真正的机制是"解析 + 检索"——简历被解析入库,招聘者用关键词搜索,匹配不到的简历根本不会被搜出来。Whali 的 ATS 指南与多篇厂商材料均确认:**"75% 简历被 ATS 自动拒绝"是一个无法溯源方法学的营销神话**;真正的问题是"解析错乱导致不可见",而不是"被系统删除"。[Whali – How to Write an ATS-Friendly CV](https://whali.com/blog/ats-friendly-cv-guide)(文中引用 Enhancv 调查:92% 招聘者确认其 ATS 不会因格式自动拒人)

Laszlo Bock 在 Google 亲自审过 2 万+ 份简历,他对"关键词"的态度是:**Google 简历被弃的主要原因是人为判断的质量问题(错别字、花哨格式、过长、泄密、撒谎),而不是关键词过滤**;Google 每周收约 5 万份简历,招聘者每份只看几秒,所以"写得清楚 + 可量化的影响"远比"堆关键词"重要。这条被多家转载 Bock 发言的来源反复确认。[ResumeAdapter 同上(转述 Bock)](https://www.resumeadapter.com/companies/google);Bock 本人 LinkedIn 长文被转载于[Nairaland 存档](https://www.nairaland.com/1909334/biggest-mistake-see-resumes-google)

关键词的**正确用法**是:
- 细读 JD,把"必须项/加分项"技能自然织入 Skills 与 Experience 正文,并**使用 JD 的原词**(比如 JD 写 "distributed systems" 就别只写 "backend")。[Tech Interview Handbook 同上]
- 不要 keyword-stuffing;关键词要挂在具体成就上,而不是干列。[Tech Interview Handbook 同上][ResumeAdapter 同上]

### 5.3 ATS 解析的格式硬规则(厂商官方口径)

以下规则来自 ATS 厂商(Greenhouse/Lever/Roche 招聘门户)与多家厂商说明,权威性高、口径一致:

- **单栏布局**(single-column),避免多栏、表格、文本框、图形、图标、页眉页脚里的联系方式;
- **标准板块标题**:Contact Information / Experience / Education / Skills(解析器靠标准标题识别字段);
- **文本型 PDF 或 DOCX,绝不能是扫描/图片型 PDF**——图片型没有文本层,解析出来是空白;
- **可选中文本测试**:全选 Ctrl+A → 复制 → 粘贴到记事本,文字顺序正常才说明可解析;
- 联系方式放正文,不要放页眉页脚(否则可能被解析进错误字段)。
[Greenhouse 官方解析故障清单与 Lever 解析指南,经 [Vecosys – Resume PDF vs DOCX for ATS](https://www.vecosys.com/resume-pdf-vs-docx-for-ats/) 转述核对];[Roche 官方 Resume Parsing FAQ](https://roche.phenompro.com/global/en/resume-parsing-faq);[Indeed – ATS-Friendly Resume](https://www.indeed.com/career-advice/resumes-cover-letters/automated-screening-resume)

**PDF 还是 Word?** 现代口径(2026):现代 ATS(Greenhouse/Lever/Workday/iCIMS/SmartRecruiters)对**文本型 PDF** 解析可靠;遗留系统(Taleo、部分 Workday 配置)对 DOCX 解析更稳。实用决策规则:
1. 招聘系统/岗位说明要求哪个就用哪个;
2. 没说明、投给系统:保守选简单 DOCX;
3. 直接邮件发给招聘者/内推人:**PDF**(锁定排版、保证对方看到你设计的样子);
4. 无论哪种,先修好版式问题(栏、文本框、图片),格式之争远小于版式问题。
[Vecosys 同上][Resumefast – PDF vs Word](https://www.resumefast.io/blog/ats-pdf-vs-word)

> 本仓库相关:RenderCV 默认输出就是**文本型 LaTeX 生成 PDF**,天然满足"有文本层、单栏、标准标题"的大部分 ATS 卫生要求——这正是 LaTeX/RenderCV 系简历的一个实际优势。

---

## 6. 长度规则(Length):一页还是两页?

**结论先行**:没有绝对的一页铁律,但"越短越好"是共识;长度取决于经验水平与岗位要求。

| 人群 | 权威建议 | 来源 |
|---|---|---|
| 本科/硕士应届、MBA | **1 页**是常态 | Harvard GSAS: "For BA/BS and MBA candidates, a one page resume is the norm." [Harvard GSAS 同上];MIT: "Stick to one page, unless you have extensive experience or an advanced degree." [MIT CAPD – resumes](https://capd.mit.edu/resources/resumes/) |
| 硕士(<10 年经验) | 1 页(CMU 工学院研究生指南原话:"Master's Degree students' resumes should be one page") | [CMU Graduate Engineering Resume Guide 同上] |
| 博士 / 博后 | 1-2 页;industry 求职可 2 页,consulting 求职 1 页 | CMU: "PhD students may have a one or two-page resume for an industry search and a one-page resume for consulting." [CMU 同上];Harvard GSAS 也确认 PhD 应聘要求博士学位的岗位时 2 页无妨,但应聘不要求 PhD 的岗位时 2 页可能释放"overqualified"信号 [Harvard GSAS 同上] |
| 资深(>10 年经验) | Bock 的经验法则:**10 年经验对应 1 页**("one page of resume for every ten years of work experience");超过 10 年可 2 页 | Laszlo Bock 公开长文 [Nairaland 转载](https://www.nairaland.com/1909334/biggest-mistake-see-resumes-google);新版书摘 "One page per decade" [Apply Within by Laszlo Bock (PDF 书摘)](https://cdn.uconnectlabs.com/wp-content/uploads/sites/554/2026/06/Apply-Within-Laszlo-Bock-1.pdf) |
| 工程师投 Google 类大厂 | 1 页(业务岗);工程岗 ≤2 页 | Google 官方招聘频道视频: "keep your resume to one page for business and internship roles and no longer than two pages for engineering roles" [Life at Google – Create Your Resume for Google](https://www.youtube.com/watch?v=BYUy1yvjHxE) |
| 中文校招/应届 | **1 页 A4**(清华:"篇幅(1页)";求职门户与高校材料均建议应届 1 页) | [清华大学就业中心讲座 PDF 同上](https://career.tsinghua.edu.cn/__local/7/81/97/92E6E3CBDF18021EDD22B0FEAF9_4789F710_81DBD.pdf?e=.pdf) |

**不要用压缩字号/缩边距来硬塞一页**:MIT 明确 "Don't shrink the font to fit more content ... if a recruiter can't easily read your font, they may just skip reading it entirely";正文小于 10pt、边距小于 0.5 英寸都是越界信号。[MIT CAPD – Career toolkit 同上][MIT CAPD – Interphase 同上]

**两页时的注意事项**(Stanford GSB / MIT):第 2 页要有名字和联系方式,防止被分开;第 2 页不要装"边角料",要把第二页当第一页一样经营;两页时第 2 页也应达到第 1 页的信息密度。[Stanford GSB 同上][MIT CAPD – Interphase 同上]

---

## 7. 版式 / 字体 / 文件格式(Design, Typography, PDF vs Word)

### 7.1 字体与字号(高校与厂商口径高度一致)

- **正文字号 10-12 pt**,全文统一一种字体;Times New Roman / Arial / Calibri 是各来源反复出现的"安全字体";姓名可稍大。[Harvard GSAS 同上][CMU 同上][Stanford GSB 同上]
- **页边距 ≥ 0.5 英寸**,Stanford GSB 建议 0.7 英寸以上("Minimum 0.70 margins. White space helps people scan.");上下左右一致。[Harvard GSAS 同上][Stanford GSB 同上]
- Bock 的格式底线:"At least ten point font. At least half-inch margins. White paper, black ink. Consistent spacing between lines, columns aligned, your name and contact information on every page." [Bock 长文转载 同上]
- 微软:正文 11-13pt 之间("Don't go smaller than 11 pt font or larger than 13 pt font for the main text"),不要用彩色文字打印版。[Microsoft Learn – Part II 同上]

### 7.2 强调手段

- 用粗体/斜体突出**职位或公司**(二选一,看哪个对读者更有冲击力),"Use bold font to highlight either your company or your title" [Stanford GSB 同上];CMU: "Bold the most important piece of information which is typically your job title or the company." [CMU 同上]
- Harvard/MIT 都提醒:**强调手段要克制且一致**,避免文本框、下划线、阴影等装饰(Harvard GSAS 原文:"avoid text boxes, underlining, or shading")。[Harvard GSAS 同上][MIT CAPD 同上]
- 通用版式检查清单:对齐一致、同一板块内倒序、板块间留白均衡、禁止大段文字、用 bullet 分隔信息。[Harvard College Guide 同上][MIT commlab – CV/Resume](https://mitcommlab.mit.edu/nse/commkit/cvresume/)

### 7.3 PDF 转换与跨平台

- 转 PDF 后务必检查格式是否错乱(Harvard: "When converting to a .pdf, check that your formatting translates correctly")[Harvard HES 手册同上];Bock 建议在 Google Docs 与 Word 里各看一遍、再以邮件附件预览打开检查("Formatting can get garbled when moving across platforms. Saving it as a PDF is a good way to go.")[Bock 长文转载同上]
- **中文简历的字体规范**(高校/求职门户通例):中文正文推荐宋体 / 微软雅黑 / 黑体,英文 Times New Roman / Arial;正文字号小四~五号(10.5-12pt);A4 纸张;投递与打印用至少 80g 纸。[worlduc 应届生指南(综合高校就业指导材料)](https://www.worlduc.com/gaokaodongtai/170108.html);清华转引许国庆英文简历讲座亦给出:A4、Times New Roman/Palatino、10-12 号、天头地脚约 2-3cm 的规范。[清华职业发展中心 – 英文简历写作技巧](https://career.tsinghua.edu.cn/info/1076/3878.htm)

### 7.4 RenderCV 相关的具体注意点

用 RenderCV 生成简历时,有几处常见设计参数值得对照上面的一手规范复核(仅提示,不改动文件):

- 正文字号若设为 `body: 9.5pt` 会略低于各校建议下限 10pt(Harvard/CMU/Bock 的底线是 10pt,微软是 11pt)——建议复核是否满足目标公司要求;
- 边距 `0.45in~0.5in` 处于"不小于 0.5 英寸"的边缘,基本合格但无余量;
- `line_spacing: 0.48em`、`space_between_regular_entries` 偏紧凑——注意 MIT 的提醒:过度压缩可读性会适得其反。
(以上仅为对照提醒,是否调整取决于目标岗位与读者。RenderCV 官方文档:[rendercv.com](https://docs.rendercv.com))

---

## 8. 常见错误清单(Common Mistakes)

### 8.1 五校 + Bock 的"官方错误榜"

**Harvard HES 版**(Top Resume Mistakes):
1. Spelling and grammar errors
2. Missing email and phone information
3. Using passive language instead of "action" words
4. Not well organized, concise, or easy to skim
5. **Not tailored to the position or industry**
[Harvard HES 手册同上]

**Laszlo Bock 版**(审过 2 万+ 份简历后的五大错误):
1. **Typos 错别字**——2013 CareerBuilder 调查:58% 的简历有错别字;招聘者把错别字解读为"不注重细节、不关心质量"。修法:从下往上读,或找人校对;
2. **Length 过长**——10 年经验配 1 页;3-4 页乃至 10 页的简历不会被细读;
3. **Formatting 版式问题**——除非应聘设计岗,否则干净易读 > 花哨;字号≥10pt、边距≥0.5 英寸、白纸黑字、行距一致、每页都有姓名联系方式;跨平台打开检查;存 PDF;
4. **Confidential information 泄密**——"Consulted to a major software company in Redmond, Washington" 这种暗示同样出局;NYT 测试:不愿见报的内容就不写;
5. **Lies 撒谎**——学历、GPA、时长、团队规模、业绩,任何一项造假都"never, ever, ever worth it",被查出来(网络/背调/前同事)即开除。
[Bock 长文转载同上]

### 8.2 其他高频问题(综合各校)

- **每行以日期开头**、把日期放在比内容更显眼的位置(Microsoft: "the date is the least important piece of information";推荐顺序:职位→公司→时长→一句职位描述→2-4 条量化成就)[Microsoft Learn – Part II 同上];
- **堆砌技术名词而没有上下文/结果**:Google 系招聘者视角 "the laundry list of languages without metrics = noise";微软:列太多技术反而招致更严 scrutiny(Business Insider 对微软工程师 Phadké 的采访: "Listing a lot of technologies ... can hurt more than help")[ResumeAdapter 同上][Business Insider – Microsoft resume strategies](https://www.businessinsider.com/resume-strategies-landed-software-engineer-job-microsoft-2025-2);
- **把不相关的一时性事件、兼职细节写上去**(MIT:避免一次性的活动,除非极度相关;微软:YMCA "created a safe pool environment" 这类不增值描述别写)[MIT CAPD – Career toolkit 同上][Microsoft Learn – First Developer Resume 同上];
- **"References available upon request" 不写**;不要在简历上直接列推荐人联系方式(CMU/Harvard 均明确)[CMU 同上][Harvard 同上];
- **陈旧荣誉不删**:拿到大厂 offer 的 Sahil Gaba 复盘时说 college honors/awards "they're very old",应该弱化,把空间让给近期经历。[Business Insider – The Résumé That Landed a Google Employee His $300,000 Job](https://www.businessinsider.com/resume-tips-google-software-engineer-skills-experience-careers-software-tech-2024-3)

### 8.3 中文简历市场特有的"雷区"(来自清华官方讲座)

清华大学就业中心邀请的百度招聘嘉宾明确指出中文简历常见问题:
- 简历"厚厚一摞",堆与岗位无关的内容(详细家庭情况、个人照片甚至明星照)——对应聘没有作用;
- 只用泛泛形容词,不用数字与实例;
- 空泛的自我评价/求职目标("寻求有挑战性的岗位"式套话);
- 不针对具体公司与职位做取舍("你的目的是告诉别人,我能做好这件工作,而不是旨在说明我能做所有的工作")。
[清华大学《简历大家谈》同上]

---

## 9. 一页 vs 两页:按经验水平的实用决策表

| 你的情况 | 建议 | 权威出处 |
|---|---|---|
| 本科/硕士应届、实习申请 | 1 页;不够满就加相关课程/项目/志愿服务/奖项,而不是放大字号加宽边距(MIT 对"内容不够"的建议) | [MIT CAPD – Interphase](https://capd.mit.edu/blog/2026/06/23/interphase-2026-resume-resources/) |
| 硕士 + <10 年工作经验 | 1 页 | [CMU 同上](https://www.cmu.edu/career/documents/sample-resumes-cover-letters/graduate_student_resume_guide_2026.pdf) |
| 博士 → 工业界研发岗 | 1-2 页均可 | [CMU 同上][Harvard GSAS 同上] |
| 博士 → 咨询/非研究岗 | 1 页,警惕 overqualified 信号 | [Harvard GSAS 同上] |
| 有 10+ 年经验 | 每 10 年经验 1 页;资深上限 2 页;更早经历压缩为一行 "Additional Experience" | [Bock 同上][Stanford GSB 同上] |
| 中文校招 | 1 页 A4 | [清华讲座 PDF 同上](https://career.tsinghua.edu.cn/__local/7/81/97/92E6E3CBDF18021EDD22B0FEAF9_4789F710_81DBD.pdf?e=.pdf) |

**雇主明确要求时,按雇主说的办**(Harvard GSAS 反复强调: "It is important to follow the directions of the employers. If they ask for a one-page resume, be sure to submit what they ask for.")。[Harvard GSAS 同上]

---

## 10. 检查清单(送审前逐项过一遍)

内容与语言(Harvard + CMU + Stanford 合并):
- [ ] 无拼写/语法错误(找别人校对,或从下往上读)[Bock 同上]
- [ ] 联系方式完整(电话+邮箱,邮箱专业;中文简历建议邮箱名用姓名拼音)[Harvard 同上][清华《简历大家谈》同上]
- [ ] 每条经历以行为动词开头,过去用过去时、现在用现在时
- [ ] 无 "responsible for / duties included" 式开头
- [ ] 无第一人称 I/me/my(中文:我/我的)
- [ ] 尽可能量化(人数、金额、百分比、延迟、准确率)
- [ ] 针对目标岗位裁剪,使用了 JD 关键词的原词
- [ ] 板块按"对该岗位的重要度"排序;同一板块内倒序
- [ ] 删掉陈旧荣誉、不相关经历与空泛形容词
- [ ] 无泄密内容(NYT 测试)、无任何夸大

版式与文件(各校 + ATS 厂商):
- [ ] 一种字体,正文 10-12pt;边距 ≥0.5 英寸(建议 0.7)
- [ ] 单栏、无文本框/表格/图形/页眉页脚联系方式
- [ ] 长度符合经验水平(应届 1 页;博士工业界可 2 页)
- [ ] 两页时第 2 页带姓名联系方式
- [ ] 转 PDF 后检查排版未错乱;投递格式遵循雇主/系统要求
- [ ] 用"全选复制粘贴到记事本"验证文本层可读
- [ ] 文件命名规范(中文求职惯例:应聘岗位+姓名+学校+联系方式)[worlduc 同上]

---

## 附:一手来源清单(Primary Sources)

**美国高校就业指导中心(一手)**
1. Harvard College – Create a Strong Resume:https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/
2. Harvard HES – 2024 Resume & Letter Handbook (PDF):https://cdn-careerservices.fas.harvard.edu/wp-content/uploads/sites/161/2024/08/2024-HES_resume-and-letter.pdf
3. Harvard GSAS – Resumes and Cover Letters for PhD Students (PDF):https://cdn-careerservices.fas.harvard.edu/wp-content/uploads/sites/161/2024/08/2024-GSAS_phd_resume_cover_letters-1.pdf
4. Stanford GSB – Resumes & Cover Letters:https://www.gsb.stanford.edu/alumni/career-resources/job-search/resumes
5. Stanford BEAM – Resume & Cover Letter Examples (PDF):https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume_and_cover_letter_examples_1.pdf
6. Stanford BEAM – CAR Method (PDF):https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/car-method-for-developing-resume-content.docx-1.pdf
7. Stanford BEAM – 4 Easy Steps to Writing Your Resume (PDF):https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/developing_your_resume_handout.pdf
8. MIT CAPD – Resumes:https://capd.mit.edu/resources/resumes/
9. MIT CAPD – Career Toolkit: Crafting an Effective Resume:https://capd.mit.edu/resources/career-toolkit-crafting-an-effective-resume/
10. MIT CAPD – Interphase Resume Resources:https://capd.mit.edu/blog/2026/06/23/interphase-2026-resume-resources/
11. MIT Sloan – Building Your MIT Sloan Resume (slides):https://cdn.cdo.mit.edu/wp-content/uploads/sites/67/2020/05/Resume-Educational-Videos-2018-Slides.pdf
12. CMU – Graduate Student Resume Guide:https://www.cmu.edu/career/documents/sample-resumes-cover-letters/graduate_student_resume_guide_2026.pdf
13. CMU – Graduate Engineering Resume Guide:https://www.cmu.edu/career/documents/sample-resumes-cover-letters/resume_guide_college_of_engineering_graduate_students_2023.pdf
14. MIT Comm Lab – CV/Resume:https://mitcommlab.mit.edu/nse/commkit/cvresume/

**大厂一手/半一手材料**
15. Microsoft Learn – How to Get a Job at Microsoft Part II: Writing an Awesome Resume(微软工程师/招聘方一手):https://learn.microsoft.com/en-us/archive/blogs/mis_laboratory/how-to-get-a-job-at-microsoft-part-ii-writing-an-awesome-resume
16. Microsoft Learn – How to Write Your First Developer Resume(微软工程师一手):https://learn.microsoft.com/en-us/archive/blogs/steverowe/how-to-write-your-first-developer-resume
17. Life at Google – Create Your Resume for Google(官方招聘频道视频):https://www.youtube.com/watch?v=BYUy1yvjHxE
18. Laszlo Bock(前 Google SVP People Operations)《The Biggest Mistake I See on Resumes》全文转载:https://www.nairaland.com/1909334/biggest-mistake-see-resumes-google
19. Laszlo Bock《Apply Within》书摘 PDF(2026):https://cdn.uconnectlabs.com/wp-content/uploads/sites/554/2026/06/Apply-Within-Laszlo-Bock-1.pdf

**ATS 官方/厂商口径**
20. Roche(使用 Phenom ATS)官方 Resume Parsing FAQ:https://roche.phenompro.com/global/en/resume-parsing-faq
21. Vecosys – Resume PDF vs DOCX for ATS(汇总核对 Greenhouse/Lever/美国劳工部口径):https://www.vecosys.com/resume-pdf-vs-docx-for-ats/
22. Indeed – ATS-Friendly Resume:https://www.indeed.com/career-advice/resumes-cover-letters/automated-screening-resume
23. Whali – How to Write an ATS-Friendly CV:https://whali.com/blog/ats-friendly-cv-guide

**中文高校官方材料**
24. 清华大学学生职业发展指导中心 – 《毕业生时间管理与求职简历的制作》(就业中心 金蕾莅):https://career.tsinghua.edu.cn/__local/7/81/97/92E6E3CBDF18021EDD22B0FEAF9_4789F710_81DBD.pdf?e=.pdf
25. 清华大学职业发展协会 – 《简历大家谈》同伴教育(嘉宾来自百度):https://career.tsinghua.edu.cn/__local/B/DF/76/D3D943A391CACE5F9B5A714F487_94DB34BE_CE07E.pdf?e=.pdf
26. 清华大学学生职业发展指导中心 – 许国庆:英文简历写作技巧:https://career.tsinghua.edu.cn/info/1076/3878.htm
27. 北京大学学生就业指导服务中心(官方职能与资源页):http://scc.pku.edu.cn/

**补充参考(社区/求职辅导,仅作补充色)**
28. Tech Interview Handbook – Software Engineer Resume Guide:https://www.techinterviewhandbook.org/resume/
29. Business Insider – The Résumé That Landed a Google Employee His $300,000 Job(附真实简历复盘):https://www.businessinsider.com/resume-tips-google-software-engineer-skills-experience-careers-software-tech-2024-3
30. Business Insider – 4 Résumé Strategies That Helped Land a Microsoft SWE Job:https://www.businessinsider.com/resume-strategies-landed-software-engineer-job-microsoft-2025-2

> 注:27 号(北大)主要为职能说明页;北大具体的简历写作方法论未获取到可直接引用的官方页面,故中文市场规范部分以清华官方材料为主要一手依据,并辅以综合高校就业指导经验的二手来源(已标注)。
