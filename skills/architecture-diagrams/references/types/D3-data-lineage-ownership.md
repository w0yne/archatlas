# Data Lineage and Ownership Map (数据血缘与数据归属图)
<!-- Generated from content/en/types/D3-data-lineage-ownership.md by tools/build_skill_refs.py. Do not edit. -->
> Where did this dataset or answer come from, what breaks downstream if it changes, and who is accountable for it?
Scope: One anchor (a dataset, report or answer) with a bounded upstream or downstream trace, about 20 nodes, at dataset granularity; ownership shown as an overlay Neighbours: D1, D2, H1.

## Meaning
- **Questions:** *lineage* asks where a dataset, report or answer came from, what transformed it and what breaks downstream if it changes. *Ownership* asks who is accountable for its definition, quality and access.
- **Viewpoint:** the governance and trust view: provenance, impact, accountability. A DFD (D2) is a design model of how data *should* move; lineage is evidence of how it *did* move, at dataset, job or column level, sometimes per run.
- **Standards:** no graphical standard. The metadata is standardised by OpenLineage (LF AI & Data): a **Job** consumes and produces **Datasets**, a **Run** is one execution of a job with a client-generated UUID run id, and **facets** extend all three (schema, source-code location, statistics and more). Marquez is the reference implementation. dbt derives a DAG from model references; DataHub ingests and lets users edit lineage, including column level.
- **Definition used here:** two variants share one id. The *lineage graph* answers provenance and impact; the *ownership map* overlays Owner (accountable) and Steward (operational) roles, as in data-governance practice and data mesh domain ownership. Role definitions come from a secondary summary of DAMA-DMBOK, not verified against the DMBOK text.
- **Leaves out:** processing logic (E2), data structure (D1), runtime infrastructure (G1), access policy (F3).

## When to use and how to choose
- **Audience:** data governance, owners and stewards, privacy and compliance officers, data engineers, analytics consumers, architects.
- **Scenarios:** impact analysis ("if `customer.email` changes type, what breaks?"); trust in an answer (which sources, jobs and indices fed a chatbot reply, who owns each); audit evidence for personal data; data mesh domain ownership; incident triage (failed upstream job, stale downstream datasets).
- **When not to use:** the logical design of a new system (D2); hand-drawn column-level lineage for a large estate (generate, then summarise); when nobody will maintain it, since a stale map is worse than none.
- **vs neighbours:**
  - **D2 Data Flow Diagram** for designed flow; D3 for observed or derived provenance.
  - **H1 RACI Matrix** if ownership is the only question.
  - **F3 Access-control model** for who may read or write; ownership is accountability, not permission.
  - **E2 Activity Flowchart** for job ordering and triggers.
  - Choose **D1 Entity-relationship diagram** for the structure of the entities themselves; D3 shows where datasets come from and who owns them.

## Notation and elements
- **Formal or informal:** informal convention. The defensible default is a left-to-right DAG using OpenLineage semantics.
- **Required:**
  - **Datasets** (sources, intermediates, outputs): rectangles with a business name plus a technical locator, for example "Customer master (crm.customers)".
  - **Jobs:** a distinct shape (rounded or chevron) with a verb-object name.
  - **Directed edges** dataset to job to dataset: jobs consume inputs and produce outputs.
  - **Consumers** at the right edge: reports, applications, models, people.
- **Ownership overlay (ownership variant):** an Owner and a Steward under each dataset or domain; optionally one band or colour per owning domain; a role legend.
- **Optional:** granularity marker (dataset or column); freshness or run status; classification chips (personal, confidential); markers for derived data such as embeddings and indices; CRUD letters on application-to-data links, as in the TOGAF Application/Data matrix.
- **Arrow semantics:** "is derived from / feeds", never "calls" or "triggers".
- **Related TOGAF artifacts:** Data Dissemination, Data Lifecycle and Data Security diagrams, and the Application/Data matrix (TOGAF 10 naming not verified against the primary text).
- **Size and naming:** about 20 nodes per diagram; show column-level lineage only for one critical field.

## Best practices and anti-patterns
### Best practices
1. **Generate, then curate.** Capture lineage from pipelines and catalogs (OpenLineage, dbt, ingestion) and draw a readable summary for people.
2. **Attach owners to nodes,** per dataset or domain, using the organisation's governance roles.
3. **Include derived and secondary stores:** caches, search and vector indices, extracts. Provenance usually gets lost there.
4. **Show version or run when trust matters:** which version of a source fed which output.
5. **Scope by question:** one consumer's upstream or one source's downstream, never the whole estate. Tag sensitive data so privacy reviews can reuse the map.

### Anti-patterns
1. **Technical lineage with no owners;** nobody can act on it.
2. **Hand-drawn estate-wide lineage** that is stale within weeks.
3. **Edges drawn as control or calls;** that is orchestration, not provenance.
4. **Hidden derived data:** indices or embeddings not traced back to source documents.
5. **Ownership mixed with access permissions,** or an application that only *displays* data drawn as if it owned it. Data shown in one app but maintained by another is owned by the maintainer.

## Drawing recipe
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

## Evidence in a code repository
- **Pipelines:** dbt models and `ref()` calls, workflow or orchestrator DAGs, ETL scripts, SQL `INSERT ... SELECT` and `CREATE TABLE AS`.
- **Producers and consumers:** ingestion jobs, event publishers and subscribers.
- **Metadata:** OpenLineage emitter configuration, catalog configuration, data-contract files.
- **Derived stores:** index-building jobs (search or vector) and their source paths.
- **Ownership hints:** `CODEOWNERS`, catalog metadata, data-contract owners.
- **Must come from people or the catalog:** the accountable business owner, classification and legal basis, and consumers outside the repository.

## Guided-mode questions
1. What must the map answer: where something came from, what breaks if it changes, or who is responsible? (what breaks if it changes)
2. Which dataset, report or answer is the anchor, and how far up or downstream? (one report, two hops upstream)
3. Dataset-level or column-level? (dataset)
4. Show owners and stewards, and where is the authoritative list? (yes, from the catalog or data contracts)
5. Highlight personal data or derived stores such as indices? (derived stores yes, personal data as chips)

## Template
Model template: `assets/templates/D3.json` · Layout template: `layered` · datasets are `store` nodes and jobs are `component` nodes (owner and steward in `sub`, classification in `tags`), owning domains are `lane` or `layer` groups, "feeds" relations are `data` edges `->` from producer to consumer, and the evidence source and date go in `meta.description`.

## Sample
Figure: `samples/D3-data-lineage-ownership.svg` (published with the site)
