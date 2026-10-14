---
code: D1
slug: entity-relationship
family: D
names:
  en: Entity-relationship diagram
  zh: 实体关系图
  aliases:
    en: [ER diagram, ERD, data model diagram, conceptual data model, logical data model, information model, domain model (UML class style), crow's foot diagram]
    zh: [ER 图, 数据模型图, 概念数据模型, 逻辑数据模型, E-R 图, 信息模型, 领域模型]
question: Which business things does the system keep information about, how are they related, and how many of each can take part in a relationship?
audiences: [architects, developers, business]
levels: [concept, logical]
phases: [design, build]
scope: One subject area or bounded context, about 5-15 entities, drawn at one stated level (conceptual or logical)
formal: {kind: method, ref: 'Chen 1976; crow''s foot (Everest 1976), Barker, IDEF1X (FIPS PUB 184, 1993) and UML 2.5.1 class diagrams are separate defined notations; the conceptual/logical/physical levels are a modelling convention'}
neighbours: [D2, D3, E3, F3]
status: draft
---

# Entity-Relationship Diagram (实体关系图)

> A map of the things a system keeps data about and how they relate, drawn at one stated level of detail and in one notation.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
- **Question:** which business things does the system keep information about, and how are they related (and how many of each)? This is the "what is true about the domain" view, independent of process and time.
- **Viewpoint:** the information view. ArchiMate's counterpart is the Information Structure example viewpoint [12]. TOGAF lists a Conceptual Data diagram and a Logical Data diagram as separate Phase C artifacts [10][11]. C4 has no data level; the C4 site points to ER or class diagrams as supplements.
- **Origin:** Peter Chen, "The Entity-Relationship Model", ACM TODS 1(1), 1976 [1][2]. Crow's foot traces to Gordon Everest's 1976 "inverted arrow" [3]; Barker notation came from CACI around 1981 and was popularised by Oracle [5]; IDEF1X is US federal standard FIPS PUB 184 of 1993 [4]; UML class diagrams are defined in UML 2.5.1 [7]. None is "the" ER standard.
- **Definition used here:** *conceptual* = entities, relationships, cardinality, no keys or types; *logical* = adds identifiers, key attributes and resolved N:M relationships, still platform-independent; *physical* = tables, columns, types, indexes [8][9]. The physical level is database design: generate it from the schema, do not hand-draw it.
- **Leaves out:** behaviour (E2, E3), data movement (D2), lineage and ownership (D3), where stores run (G1), access rules (F3).

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
<!-- skill-text
- **Audience:** architects, developers, analysts, governance leads; product owners and business experts for the conceptual level only.
- **Scenarios:** agreeing the shop vocabulary (customer, order, payment, shipment) before building; a new service's persistence boundary; explaining an existing schema (reverse-engineered logical view); migration mapping of two systems' entities; tenancy and sharing relations.
- **When not to use:** who does what when (E1, E2, A5); a dump of every table of a large database (generate it with a schema tool); how data moves between systems (D2, C6).
- **vs neighbours:**
  - **D2 Data Flow Diagram** when data is moving; D1 shows structure.
  - **E3 State Machine** for one entity's lifecycle; a common pair is D1 plus one E3 per entity with a status field.
  - **C7 Bounded Context Map** for how contexts relate; draw one D1 per context, not one enterprise ER.
  - **F3 Access-control model** for permissions.
  - Choose **D3 Data lineage and ownership map** when the question is where data comes from, what derives from it and who owns it, rather than how entities relate.
-->
- **Audience:** architects, developers, analysts and governance leads; product owners and business experts for the conceptual level only.
- **Classic scenarios:**
  1. Agreeing the vocabulary of the shop (customer, order, payment, shipment) with the business before building.
  2. Drawing a new service's persistence boundary and aggregates.
  3. Explaining an existing schema to a new team or an integrator (reverse-engineered logical view).
  4. Data migration or consolidation: mapping two systems' entities.
  5. Tenancy or permission design: making tenant, owner and sharing relations explicit.
- **When not to use:** who does what when (E1, E2, A5); a dump of every table in a large database (generate it with SchemaSpy or tbls [13][14]); how data moves between systems (D2, C6).
- **vs neighbours:**
  - Choose **D2 Data Flow Diagram** when data is *moving*; D1 shows data *structure*.
  - Choose **E3 State Machine** for one entity's lifecycle. A common pair: D1 plus one E3 per entity with a status field.
  - Choose **C7 Bounded Context Map** to show how contexts relate; draw one D1 per context, not one enterprise-wide ER.
  - Choose **F3 Access-control model** for permissions; the chain user-role-permission-resource is a small ER.
  - Choose **D3 Data lineage and ownership map** when the question is where data comes from, what derives from it and who owns it, rather than how entities relate.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Formal or informal:** each notation is defined, but the level is a convention [8][9]. Pick one notation, state it in a legend, never mix Chen diamonds with crow's feet.
- **Required:**
  - **Entities:** singular business nouns (`Customer`, `Order`), capitalised consistently.
  - **Relationships:** lines labelled with a verb phrase readable in one direction ("Customer *places* Order").
  - **Cardinality at both ends,** minimum and maximum. In crow's foot the outer symbol is the maximum and the inner the minimum; Mermaid's `erDiagram` documents `|o` zero or one, `||` exactly one, `}o` zero or more, `}|` one or more [6].
- **Optional (logical level):** primary-key and a few defining attributes; identifying (solid) vs non-identifying (dashed) relationships [6]; associative entities for N:M; sub- and supertypes. Foreign keys are a relational device and belong to the logical or physical level only.
- **UML variant:** classes with multiplicities (`0..1`, `1`, `*`, `1..*`), composition, aggregation, generalisation [7].
- **Legend:** notation ("crow's foot; min inner, max outer") and level ("conceptual" or "logical").
- **Size:** conceptual about 5-15 entities per view (a rule of thumb, not a standard); logical shows only attributes that explain meaning ("often a small subset of attributes is enough" [6]).
- **Naming:** user language, not table prefixes (`tbl_cust`); verbs on lines, not a generic "has" where a precise verb exists.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices
1. **State the level in the title** ("Conceptual model: order management") and draw to it [8][9].
2. **One subject area per diagram.** Slice by bounded context or business function; reference shared entities instead of duplicating them.
3. **Model with domain experts** and read every relationship aloud ("Each Order is placed by exactly one Customer").
4. **Show optionality** (minimum 0 vs 1); it holds business rules that would otherwise hide in code.
5. **Resolve N:M only at the logical level,** naming the associative entity after the real thing (`OrderLine`, not `OrderProduct`). Note cross-cutting patterns (tenant key, soft delete, audit) once instead of on every entity.

### Anti-patterns
1. **The database dump:** 100+ tables with all columns; comprehensiveness is the enemy of comprehensibility [15].
2. **Mixed levels:** foreign keys, types and indexes on a business-facing conceptual model.
3. **Unlabelled lines or cardinality missing at one end.**
4. **Technical or meaningless names:** `data`, `info`, `item2`, table prefixes.
5. **Process encoded as entities** (`ApprovalStep1`, `ApprovalStep2`) or mixed notations without a legend. Also avoid a prose entity list where a real diagram would show the chain.

## Exemplars {#exemplars}
<!-- skill: omit -->
- [Chen's original paper (1976, author PDF)](https://www.csc.lsu.edu/~chen/pdf/erd-5-pages.pdf) — the defining text; shows why entities and relationships, not records, are the primitives.
- [Mermaid entity relationship diagrams](https://mermaid.js.org/syntax/entityRelationshipDiagram.html) — a concise crow's-foot reference with a cardinality table; a good diagram-as-code model.
- [Chinook sample database](https://github.com/lerocha/chinook-database) — a small realistic schema (artists, albums, tracks, invoices) for learning to read ERDs; MIT licence (LICENSE file checked 2026-10-14).
- [IDEF1X, FIPS PUB 184](https://www.idef.com/wp-content/uploads/2016/02/Idef1x.pdf) — a rigorous logical-model standard that shows what "logical" can mean; US government publication.
- [Barker's notation (Wikipedia)](https://en.wikipedia.org/wiki/Barker's_notation) — sub-type boxes inside super-types and optional/mandatory half-lines, an alternative to crow's foot.
- [SchemaSpy](https://github.com/schemaspy/schemaspy) and [tbls](https://github.com/k1LoW/tbls) — generated physical ER and table docs; show where the physical level belongs.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Fix level and scope. Default to conceptual for business audiences and logical for engineers; choose one subject area or bounded context.
2. Harvest candidate entities from requirement nouns or from schema and ORM models; merge synonyms; drop technical tables (migrations, locks, caches) unless they are the topic.
3. Cap at about 12 entities; move the rest to another view or a "see diagram X" stub.
4. Write the relationship sentences first ("each Order is placed by exactly one Customer"), then draw them.
5. Layout: the most connected entity in the middle; parents above children so one-to-many flows downward; associative entities between their two parents; orthogonal lines, crossings removed by reordering.
6. Text: entity name plus 3-5 defining attributes (logical) or none (conceptual); a verb on every line.
7. Colour: 2-3 meaningful fills at most (for example core, reference, externally owned data), each in the legend; no decorative colour.
8. Add a legend with notation and level, and one note for each cross-cutting pattern.

**Self-check**
- [ ] The title states the level and scope.
- [ ] Every line has a verb label and a cardinality at both ends.
- [ ] No foreign key, type or index detail on a conceptual diagram.
- [ ] N:M relationships are consistently either kept (conceptual) or resolved into named associative entities (logical).
- [ ] Names are business terms; the same thing has the same name on every diagram.
- [ ] At most about 15 entities, or the diagram is split.
- [ ] One notation, with a legend.
- [ ] Relationship sentences read correctly aloud and are confirmed by an expert or by code evidence.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **Strong:** DDL plus the latest migrations (the current schema wins over the first DDL); ORM or entity classes and their relationship declarations; GraphQL and OpenAPI resource schemas; foreign keys and unique constraints (cardinality evidence).
- **Weak, mark as inferred:** an `xxx_id` column without a foreign key, JSON blobs, document stores.
- **Must come from people:** business names for technical tables, optionality the business intends, which entities matter to the audience.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Who is the reader: business stakeholders (conceptual) or engineers (logical)? Should attributes or keys appear? (engineers, logical, key attributes only)
2. Which subject area or bounded context, and should neighbouring areas be stubs or omitted? (one context, neighbours as stubs)
3. Is there a source of truth to follow (schema, ORM, glossary) or are we designing the target model? (follow the existing schema, marked inferred)
4. Which notation does your organisation use? (crow's foot)
5. Should tenancy, ownership, audit or versioning be shown on entities or noted once? (noted once)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/D1.json` · Layout template: `er` · entities become `nodes` of kind `entity` (attribute strings in `attributes`, key markers such as `PK`/`FK` first), a bounded context or subject area becomes a `boundary` group, relationships become edges with `dir` `--` whose `cardinality{from,to}` carries min/max and whose `label` is the verb; the level goes in the title.

## Sources {#sources}
<!-- skill: omit -->
1. P. P.-S. Chen, "The entity-relationship model — toward a unified view of data", ACM TODS 1(1):9–36, 1976 — https://dl.acm.org/doi/10.1145/320434.320440 — accessed 2026-10-14
2. Chen 1976, author PDF — https://www.csc.lsu.edu/~chen/pdf/erd-5-pages.pdf — accessed 2026-10-14
3. Redgate, "Crow's Foot Notation" (history: Everest 1976, secondary source) — https://www.red-gate.com/blog/crow-s-foot-notation/ — accessed 2026-10-14
4. NIST FIPS PUB 184, Integration Definition for Information Modeling (IDEF1X), 21 December 1993 (date from the publication record; the PDF text was not machine-readable in this check) — https://www.idef.com/wp-content/uploads/2016/02/Idef1x.pdf — accessed 2026-10-14
5. Wikipedia, "Barker's notation" (secondary source) — https://en.wikipedia.org/wiki/Barker's_notation — accessed 2026-10-14
6. Mermaid, "Entity Relationship Diagrams" (cardinality table, identifying lines, attribute quote re-checked) — https://mermaid.js.org/syntax/entityRelationshipDiagram.html — accessed 2026-10-14
7. OMG, Unified Modeling Language 2.5.1 — https://www.omg.org/spec/UML/2.5.1/About-UML — accessed 2026-10-14
8. AWS, "Logical vs Physical Data Model" — https://aws.amazon.com/compare/the-difference-between-logical-and-physical-data-model/ — accessed 2026-10-14
9. ThoughtSpot, "Conceptual vs Logical vs Physical Data Models" — https://www.thoughtspot.com/data-trends/data-modeling/conceptual-vs-logical-vs-physical-data-models — accessed 2026-10-14
10. The Open Group, TOGAF V9 sample catalogs, matrices and diagrams (Phase C data; TOGAF 10 naming not verified against the primary text) — http://www.togaf.info/togaf9/togafSlides9/TOGAF-V9-Sample-Catalogs-Matrics-Diagrams-v2.pdf — accessed 2026-10-14
11. QualiWare CoE, "TOGAF Artifacts" — https://coe.qualiware.com/resources/togaf/togaf-artifacts/ — accessed 2026-10-14
12. The Open Group, ArchiMate 3.2 Specification, Example Viewpoints — https://pubs.opengroup.org/architecture/archimate3-doc/ch-Example-Viewpoints.html — accessed 2026-10-14
13. SchemaSpy — https://github.com/schemaspy/schemaspy — accessed 2026-10-14
14. tbls — https://github.com/k1LoW/tbls — accessed 2026-10-14
15. M. Fowler, "UmlAsSketch" — https://martinfowler.com/bliki/UmlAsSketch.html — accessed 2026-10-14
16. Chinook database (MIT licence file checked) — https://github.com/lerocha/chinook-database — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![D1 sample: online shop logical model with Customer, Order, OrderLine, Product, Payment and Shipment in crow's foot notation](/samples/D1-entity-relationship.svg)
*Sample pending (generated by the renderer from `examples/`).*
