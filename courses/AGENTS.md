# Course-Tree Agent Rules

- Do not create a course folder until its record exists in the locked curriculum manifest.
- Do not change course identity metadata here.
- The active prompt may write to only one named course or one named week unless it is a shell/index operation.
- Generate lectures before dependent assignments and graded assessments.
- Instructor materials remain separate from student-facing files.
- Every substantive generation task creates a provenance record.
- Course status must advance in order: `shell` → `researching` → `designed` → `in-production` → `ready-for-audit` → `released`.
