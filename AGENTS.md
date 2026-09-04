# Repository Instructions for Codex and Other AI Agents

## Required reading order

Before editing anything, read:

1. `MASTER_PROMPT.md`
2. `PROJECT-DECISIONS.yaml`
3. `DISCLAIMER.md`
4. `THEOLOGICAL-COMMITMENTS.md`
5. `ACADEMIC-STANDARDS.md`
6. `SOURCE-POLICY.md`
7. `WRITING-STYLE-GUIDE.md`
8. `ASSESSMENT-POLICY.md`
9. `AI-USE-POLICY.md`
10. The active numbered prompt in `prompts/`

The active numbered prompt defines the permitted write scope. The root constitution defines rules that the active prompt cannot relax.

## Operating rules

- Inspect the current repository and `git status` before editing.
- Never overwrite substantive user work with boilerplate.
- Treat the canonical spreadsheet and `curriculum/curriculum.lock.yaml` as immutable except under the dedicated import/reconciliation prompts.
- Never invent a course code, title, credit value, prerequisite, book, edition, ISBN, DOI, page range, quotation, author, journal, video, URL, or institutional requirement.
- If verification cannot be completed, write a clearly scoped `TODO-VERIFY` and stop that dependency chain. Do not guess.
- Never call generated content official Wheaton, Gordon-Conwell, or Princeton material.
- Present important opposing positions accurately and charitably before confessional evaluation.
- Never advocate abandonment of Christianity or ridicule the student's faith. Academic challenge and accurate presentation of objections are required; coercive deconversion is not.
- Do not copy copyrighted books, articles, answer keys, or transcripts into the repository beyond lawful quotation.
- Produce lectures before assignments that depend on those lectures.
- Default production unit: one course design or one course-week. Semester-wide shell generation is allowed; semester-wide full content generation is not.
- Run validation after every scoped generation task.
- Record provenance for every AI generation run.
- Report changed files, validation results, unresolved items, and the next permitted prompt. Do not begin the next prompt automatically.

## Git rules

- Default branch is `main`.
- Use focused feature branches.
- A prompt must explicitly say `COMMIT_ALLOWED: true` before an agent creates a commit.
- Never push or merge without direct owner authorization.
- Never amend, rebase, reset, clean, or force operations unless explicitly authorized.

## Student-work integrity

AI may explain instructions, generate practice questions, and critique an existing student draft. AI may not write graded student essays, sermon manuscripts, translations, exams, research papers, comprehensive responses, prospectus prose, dissertation chapters, or defense answers for submission as the student's own work.
