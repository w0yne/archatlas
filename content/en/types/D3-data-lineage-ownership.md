---
code: D3
slug: data-lineage-ownership
family: D
names:
  en: Data lineage and ownership map
  zh: 数据血缘与归属图
  aliases:
    en: [data lineage diagram, lineage graph, data ownership map, data asset map, data lineage graph, lineage DAG, data provenance graph, data domain map, data stewardship map]
    zh: [数据血缘图, 数据归属图, 数据资产地图, 血缘关系图, 数据溯源图, 数据责任图, 数据分布图]
question: Where did this dataset or answer come from, what breaks downstream if it changes, and who is accountable for it?
audiences: [architects, security, business]
levels: [logical]
phases: [design, operate]
scope: One anchor (a dataset, report or answer) with a bounded upstream or downstream trace, about 20 nodes, at dataset granularity; ownership shown as an overlay
formal: {kind: convention, ref: 'No graphical standard. Runtime lineage metadata is standardised by OpenLineage (Job, Run, Dataset, facets); ownership roles follow data-governance practice (owner, steward)'}
neighbours: [D1, D2, H1]
status: draft
---

# Data Lineage and Ownership Map (数据血缘与数据归属图)

> A left-to-right graph of how datasets are derived from one another by jobs, with an owner and steward attached to each dataset or domain.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
- **Questions:** *lineage* asks where a dataset, report or answer came from, what transformed it and what breaks downstream if it changes. *Ownership* asks who is accountable for its definition, quality and access.
- **Viewpoint:** the governance and trust view: provenance, impact, accountability. A DFD (D2) is a design model of how data *should* move; lineage is evidence of how it *did* move, at dataset, job or column level, sometimes per run [2].
- **Standards:** no graphical standard. The metadata is standardised by OpenLineage (LF AI & Data): a **Job** consumes and produces **Datasets**, a **Run** is one execution of a job with a client-generated UUID run id, and **facets** extend all three (schema, source-code location, statistics and more) [1][2]. Marquez is the reference implementation [3]. dbt derives a DAG from model references [4]; DataHub ingests and lets users edit lineage, including column level [5].
- **Definition used here:** two variants share one id. The *lineage graph* answers provenance and impact; the *ownership map* overlays Owner (accountable) and Steward (operational) roles, as in data-governance practice [6] and data mesh domain ownership [7]. Role definitions come from a secondary summary of DAMA-DMBOK, not verified against the DMBOK text.
- **Leaves out:** processing logic (E2), data structure (D1), runtime infrastructure (G1), access policy (F3).

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
<!-- skill-text
- **Audience:** data governance, owners and stewards, privacy and compliance officers, data engineers, analytics consumers, architects.
- **Scenarios:** impact analysis ("if `customer.email` changes type, what breaks?"); trust in an answer (which sources, jobs and indices fed a chatbot reply, who owns each); audit evidence for personal data; data mesh domain ownership; incident triage (failed upstream job, stale downstream datasets).
- **When not to use:** the logical design of a new system (D2); hand-drawn column-level lineage for a large estate (generate, then summarise); when nobody will maintain it, since a stale map is worse than none.
- **vs neighbours:**
  - **D2 Data Flow Diagram** for designed flow; D3 for observed or derived provenance.
  - **H1 RACI Matrix** if ownership is the only question.
  - **F3 Access-control model** for who may read or write; ownership is accountability, not permission.
  - **E2 Activity Flowchart** for job ordering and triggers.
  - Choose **D1 Entity-relationship diagram** for the structure of the entities themselves; D3 shows where datasets come from and who owns them.
-->
- **Audience:** data governance, owners and stewards, privacy and compliance officers, data engineers, analytics consumers, architects.
- **Classic scenarios:**
  1. Impact analysis: "if we change the `customer.email` type, which dashboards and models break?" [4][5].
  2. Trust in an answer: show which source documents, extraction jobs and search indices fed a support chatbot's answer, and who owns each source.
  3. Audit and regulatory evidence: where personal data originates, where it is copied and who is responsible [10][11].
  4. Data mesh and domain design: which domain owns which data products and who depends on them [7].
  5. Incident triage: a failed upstream job, and which downstream datasets are stale (run-level lineage) [2][3].
- **When not to use:** the logical design of a new system (D2); hand-drawing table- or column-level lineage for a large estate (generate it, then summarise); when nobody will maintain it, since a stale map is worse than none.
- **vs neighbours:**
  - Choose **D2 Data Flow Diagram** for how data is designed to flow; choose D3 for observed or derived provenance.
  - Choose **H1 RACI Matrix** if ownership is the only question; D3 is the right place when owners must sit on a flow.
  - Choose **F3 Access-control model** for who may read or write; ownership is accountability, not permission.
  - Choose **E2 Activity Flowchart** or the orchestrator's DAG for job ordering and triggers.
  - Choose **D1 Entity-relationship diagram** for the structure of the entities themselves; D3 shows where datasets come from and who owns them.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Formal or informal:** informal convention. The defensible default is a left-to-right DAG using OpenLineage semantics [1][2].
- **Required:**
  - **Datasets** (sources, intermediates, outputs): rectangles with a business name plus a technical locator, for example "Customer master (crm.customers)".
  - **Jobs:** a distinct shape (rounded or chevron) with a verb-object name.
  - **Directed edges** dataset to job to dataset: jobs consume inputs and produce outputs.
  - **Consumers** at the right edge: reports, applications, models, people.
- **Ownership overlay (ownership variant):** an Owner and a Steward under each dataset or domain; optionally one band or colour per owning domain; a role legend.
- **Optional:** granularity marker (dataset or column); freshness or run status; classification chips (personal, confidential); markers for derived data such as embeddings and indices; CRUD letters on application-to-data links, as in the TOGAF Application/Data matrix [8].
- **Arrow semantics:** "is derived from / feeds", never "calls" or "triggers".
- **Related TOGAF artifacts:** Data Dissemination, Data Lifecycle and Data Security diagrams, and the Application/Data matrix [8][9] (TOGAF 10 naming not verified against the primary text).
- **Size and naming:** about 20 nodes per diagram; show column-level lineage only for one critical field.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices
1. **Generate, then curate.** Capture lineage from pipelines and catalogs (OpenLineage, dbt, ingestion) and draw a readable summary for people.
2. **Attach owners to nodes,** per dataset or domain, using the organisation's governance roles.
3. **Include derived and secondary stores:** caches, search and vector indices, extracts. Provenance usually gets lost there.
4. **Show version or run when trust matters:** which version of a source fed which output.
5. **Scope by question:** one consumer's upstream or one source's downstream, never the whole estate. Tag sensitive data so privacy reviews can reuse the map [10].

### Anti-patterns
1. **Technical lineage with no owners;** nobody can act on it.
2. **Hand-drawn estate-wide lineage** that is stale within weeks.
3. **Edges drawn as control or calls;** that is orchestration, not provenance.
4. **Hidden derived data:** indices or embeddings not traced back to source documents.
5. **Ownership mixed with access permissions,** or an application that only *displays* data drawn as if it owned it. Data shown in one app but maintained by another is owned by the maintainer.

## Exemplars {#exemplars}
<!-- skill: omit -->
- [OpenLineage object model](https://openlineage.io/docs/spec/object-model) — the clearest vocabulary for lineage (Job, Run, Dataset, facets) and why per-run evidence matters. Open standard.
- [Marquez](http://marquezproject.ai/) — the reference implementation, with a lineage UI showing job and dataset dependencies and run metadata.
- [dbt: getting started with data lineage](https://www.getdbt.com/blog/getting-started-with-data-lineage) — a DAG inferred from model references; the canonical "generated, always current" case. Vendor content.
- [DataHub lineage docs](https://docs.datahub.com/docs/features/feature-guides/lineage) — dataset and column lineage with manual editing; guidance on mixing automated and curated lineage.
- [Data Mesh Principles and Logical Architecture](https://martinfowler.com/articles/data-mesh-principles.html) — ownership by domain and data as a product; the basis for the ownership overlay.
- [ICO guidance on documenting processing activities](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/documentation/how-do-we-document-our-processing-activities/) — how a regulator expects data flows and responsibilities to be recorded; tabular, but maps directly onto this diagram.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Pick the question and direction: upstream trace ("where did X come from?"), downstream impact ("what depends on X?") or ownership overview ("who owns what?"); put it in the title.
2. Choose granularity: dataset by default, column only for one critical field.
3. Collect nodes: sources, jobs, intermediates, outputs, consumers, plus derived stores (indices, caches, embeddings).
4. Layout: a left-to-right DAG; for the ownership variant add horizontal bands, one per owning domain. Keep job shapes visibly different from dataset shapes.
5. Overlay ownership: an Owner and Steward label under each dataset or on each domain band, with a role legend.
6. Text: business name plus locator on datasets, verb-object on jobs; classification as small chips.
7. Colour: one colour per owning domain, or one accent for sensitive data; never both without a legend.
8. Mark evidence in a footer: generated from tool X on date Y, inferred from code, or confirmed by the owner.

**Self-check**
- [ ] The question (upstream, downstream or ownership) is in the title.
- [ ] Edges mean "derived from / feeds", not "calls / triggers".
- [ ] Every dataset has an owner or is marked "owner unknown".
- [ ] Derived stores (indices, caches, embeddings) are traced to their sources.
- [ ] Granularity is consistent (dataset or column, not both).
- [ ] A source and date for the lineage is shown (generated or inferred).
- [ ] At most about 20 nodes; otherwise split by domain or consumer.
- [ ] Sensitive-data tags and colours are explained in the legend.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **Pipelines:** dbt models and `ref()` calls, workflow or orchestrator DAGs, ETL scripts, SQL `INSERT ... SELECT` and `CREATE TABLE AS`.
- **Producers and consumers:** ingestion jobs, event publishers and subscribers.
- **Metadata:** OpenLineage emitter configuration, catalog configuration, data-contract files.
- **Derived stores:** index-building jobs (search or vector) and their source paths.
- **Ownership hints:** `CODEOWNERS`, catalog metadata, data-contract owners.
- **Must come from people or the catalog:** the accountable business owner, classification and legal basis, and consumers outside the repository.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. What must the map answer: where something came from, what breaks if it changes, or who is responsible? (what breaks if it changes)
2. Which dataset, report or answer is the anchor, and how far up or downstream? (one report, two hops upstream)
3. Dataset-level or column-level? (dataset)
4. Show owners and stewards, and where is the authoritative list? (yes, from the catalog or data contracts)
5. Highlight personal data or derived stores such as indices? (derived stores yes, personal data as chips)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/D3.json` · Layout template: `layered` · datasets are `store` nodes and jobs are `component` nodes (owner and steward in `sub`, classification in `tags`), owning domains are `lane` or `layer` groups, "feeds" relations are `data` edges `->` from producer to consumer, and the evidence source and date go in `meta.description`.

## Sources {#sources}
<!-- skill: omit -->
1. OpenLineage, Object Model (Job, Run with UUID run id, Dataset, facets; re-checked) — https://openlineage.io/docs/spec/object-model — accessed 2026-10-14
2. OpenLineage, specification (GitHub) — https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.md — accessed 2026-10-14
3. Marquez Project — http://marquezproject.ai/ — accessed 2026-10-14
4. dbt Labs, "Getting started with data lineage" — https://www.getdbt.com/blog/getting-started-with-data-lineage — accessed 2026-10-14
5. DataHub, "About DataHub Lineage" — https://docs.datahub.com/docs/features/feature-guides/lineage — accessed 2026-10-14
6. OvalEdge, "The DAMA-DMBOK Data Governance Framework" (secondary summary of owners vs stewards) — https://www.ovaledge.com/blog/dama-dmbok-data-governance-framework — accessed 2026-10-14
7. Z. Dehghani, "Data Mesh Principles and Logical Architecture", martinfowler.com — https://martinfowler.com/articles/data-mesh-principles.html — accessed 2026-10-14
8. The Open Group, TOGAF V9 sample catalogs, matrices and diagrams — http://www.togaf.info/togaf9/togafSlides9/TOGAF-V9-Sample-Catalogs-Matrics-Diagrams-v2.pdf — accessed 2026-10-14
9. QualiWare CoE, "TOGAF Artifacts" (Data Lifecycle diagram; the artifact list also appears in third-party TOGAF study guides) — https://coe.qualiware.com/resources/togaf/togaf-artifacts/ — accessed 2026-10-14
10. ICO, "How do we document our processing activities?" — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/documentation/how-do-we-document-our-processing-activities/ — accessed 2026-10-14
11. Data Protection Commission (Ireland), "Records of Processing (Article 30) Guidance" — https://www.dataprotection.ie/en/dpc-guidance/records-of-processing-article-30-guidance — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![D3 · Enterprise Service Assistant](/samples/ai-service-assistant/D3/en/diagram.svg)
*Steward accountability, technical custody and tenant-confidential versus deidentified classification are specified in AS-data. Ownership is not a read grant, and derived chunks retain source ACL restrictions.*

[SVG](/samples/ai-service-assistant/D3/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/D3/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

[Historical shop regression sample](/samples/D3-data-lineage-ownership.svg) · [All 29 views](/use/ai-service-assistant) · [Illustrative assumptions](/use/ai-service-assistant-assumptions).
