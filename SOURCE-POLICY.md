# Source and Bibliographic Policy

## Source hierarchy

1. Scripture and primary historical texts.
2. Critical editions and primary-source collections.
3. Peer-reviewed academic monographs from reputable scholarly publishers.
4. Peer-reviewed journal articles.
5. Grammars, lexicons, reference works, and recognized academic databases.
6. University, seminary, scholarly-society, museum, or publisher lectures by identifiable experts.
7. Carefully selected confessional scholarship.
8. Responsible popular-level works only when appropriate to the learning objective.

Agreement with the project's theology does not establish academic quality. Disagreement with it does not disqualify a source.

## Verification requirements

Never invent or infer bibliographic facts. Before assigning a source, verify the relevant fields against an authoritative record.

## Canonical acquisition designations

Every source record `access_category` and every course `required_texts`
`designation` must use the same canonical vocabulary:

- `required-purchase`: the student is expected to obtain a personal lawful copy
  because the course makes substantial pedagogical use of the work;
- `required-free`: the source is required and a verified lawful route provides
  the assigned content to the student for USD 0;
- `required-access`: the source is required, but a personal purchase is not;
  lawful borrowing, library or licensed access, or another documented access
  mechanism satisfies the requirement;
- `recommended`: useful but not required for successful completion;
- `optional-reference`: a reference or enrichment resource that is not required;
  and
- `not-applicable`: a research, catalog, or administrative source that is not a
  student reading.

Only the three `required-*` designations belong in a course's `required_texts`.
Do not create media-, format-, or ownership-specific variants when `source_type`,
`access_note`, and the canonical designation already carry that information.
`required-free` records must identify the verified free route and record a
required curriculum cost of USD 0. `required-access` records must document the
lawful access mechanism.

## Purchase-efficiency rule

`required-purchase` is a pedagogical decision, not merely a statement that a
work is sold commercially. A course may require purchase when it reads a work
largely or completely, uses a substantial portion, repeatedly assigns an
anthology's selections, relies on a recurring reference work, or requires a
primary or critical edition central to the course.

A complete book must not be `required-purchase` merely for one isolated excerpt,
one minor chapter, a few pages, one quotation, one week of incidental use, or
another small selection that does not reasonably justify buying the whole work.
For such material, prefer in academically appropriate order:

1. verified lawful free access;
2. a public-domain or openly licensed edition;
3. lawful library or borrowing access;
4. lawful chapter or article access;
5. an anthology consolidating multiple genuinely required selections;
6. an academically comparable free or lower-cost source; or
7. `recommended` or `optional-reference` status when the item is not necessary
   to the learning outcomes.

Do not lower academic quality merely to make all resources free. There is no
arbitrary maximum number of required purchases: eight books can be justified
when each is used substantially, while eight full-book purchases for eight
isolated excerpts are not. Every required purchase must independently record:

- `use_extent`: `whole-work`, `substantial-portion`, `multiple-selections`,
  `recurring-reference`, or `isolated-excerpt`;
- the instructional weeks in which the work is materially used; and
- a concise `purchase_justification` connecting that use to the course.

`isolated-excerpt` is never compatible with `required-purchase`. An academically
necessary exception that cannot justify a personal-copy requirement should
normally be `required-access`.

## Scripture access and cost

The Bible is always free to the student for curriculum purposes. No source with
`source_type: scripture` may be `required-purchase`, and Scripture contributes
USD 0 to every required-purchase count and cost calculation. Required Scripture
must be `required-free`, must identify a verified lawful free-access route, and
must record `required_cost_usd: 0`.

A student may choose to buy a print, Kindle, Logos, study-Bible, or other Bible
edition, but that purchase is optional and cannot be a course requirement. Keep
the preferred ESV, NASB 2020, NIV, and NLT roles when verified free access makes
them possible. If a specifically required translation lacks a satisfactory
lawful free route, do not call it free; make the smallest design adjustment
needed so the required Scripture work can be completed with a verified freely
accessible translation.

## Bibliographic verification by source type

### Books

Verify author/editor, exact title, edition, publisher, publication year, ISBN when applicable, and chapter titles or page ranges actually assigned. Mark each item as:

- `required-purchase`
- `required-free`
- `required-access`
- `recommended`
- `optional-reference`
- `not-applicable`

Prefer chapter assignments over page ranges unless the exact edition and pagination have been checked.

### Articles

Verify author, article title, journal, year, volume, issue, pagination, and DOI or stable record where available. A paid article must have a free alternative where academically feasible.

### Videos and podcasts

Open and verify the item. Record exact title, presenter, host/channel, publication date when available, URL, duration, transcript availability, and access date. Reputable YouTube and podcast material is permitted. Guided questions should accompany assigned media where possible. No arbitrary duration cap applies when the quality and workload justify the assignment.

### Web sources

Use authoritative and stable sources. Record access date. Do not use search-result snippets as evidence. Broken or changed links must be flagged.

## Access and cost

Choose quality first while avoiding unnecessary expense. Print, Kindle, and Logos editions are acceptable. Use a public library where available. Do not assume access to ATLA, JSTOR, ProQuest, or other subscription databases. When an expensive critical edition or language tool is academically justified, identify it clearly and provide a genuinely comparable lower-cost alternative when one exists. If no comparable alternative exists, say so.

Research must distinguish verified access and price facts from the later course-design decision to require a personal purchase. Production may use additional verified scholarship without making it a student purchase. The independent source audit must compare each structured purchase-use claim with the syllabus, schedule, and actual assigned readings; an unjustified purchase for an isolated excerpt and any required-purchase Scripture source are blocking findings.

## Copyright

Do not upload copyrighted books, articles, unauthorized scans, complete proprietary answer keys, or copied transcripts. Store citations, lawful excerpts, original notes, and links. Public-domain and properly licensed works may be included with license documentation.

## Required claim labels in generated lectures

Use explicit signals when material could be confused:

- **Primary-source claim**
- **Broad scholarly consensus**
- **Contested interpretation**
- **Confessional conclusion**
- **Curriculum synthesis**

## Failure behavior

If a required bibliographic detail or source cannot be verified, mark it `TODO-VERIFY` and stop dependent content. Do not guess. A course cannot advance to `ready-for-audit` or `released` while required sources remain unverified.

## Freshness and re-verification

Verification has a time dimension. Before a course is released, required source records must satisfy the freshness limits in `QUALITY-ASSURANCE.md`.

- Catalogs, websites, videos, and podcasts must have been rechecked within 180 days.
- Books, articles, chapters, primary texts, reference works, and Scripture records must have been rechecked within 730 days when they are release-critical.

Reverification updates `accessed_at` and confirms current access, URL, edition, transcript/media availability, and licensing or copyright facts where applicable. It does not require pretending that stable historical bibliographic facts have changed.

Draft work may continue with an aging source when its underlying bibliographic identity remains verified, but release validation must block stale required-source access evidence until it is refreshed.
