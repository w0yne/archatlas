# Entity-Relationship Diagram (实体关系图)
<!-- Generated from content/en/types/D1-entity-relationship.md by tools/build_skill_refs.py. Do not edit. -->
> Which business things does the system keep information about, how are they related, and how many of each can take part in a relationship?
Scope: One subject area or bounded context, about 5-15 entities, drawn at one stated level (conceptual or logical) Neighbours: D2, D3, E3, F3.

## Meaning
- **Question:** which business things does the system keep information about, and how are they related (and how many of each)? This is the "what is true about the domain" view, independent of process and time.
- **Viewpoint:** the information view. ArchiMate's counterpart is the Information Structure example viewpoint. TOGAF lists a Conceptual Data diagram and a Logical Data diagram as separate Phase C artifacts. C4 has no data level; the C4 site points to ER or class diagrams as supplements.
- **Origin:** Peter Chen, "The Entity-Relationship Model", ACM TODS 1(1), 1976. Crow's foot traces to Gordon Everest's 1976 "inverted arrow"; Barker notation came from CACI around 1981 and was popularised by Oracle; IDEF1X is US federal standard FIPS PUB 184 of 1993; UML class diagrams are defined in UML 2.5.1. None is "the" ER standard.
- **Definition used here:** *conceptual* = entities, relationships, cardinality, no keys or types; *logical* = adds identifiers, key attributes and resolved N:M relationships, still platform-independent; *physical* = tables, columns, types, indexes. The physical level is database design: generate it from the schema, do not hand-draw it.
- **Leaves out:** behaviour (E2, E3), data movement (D2), lineage and ownership (D3), where stores run (G1), access rules (F3).

## When to use and how to choose
- **Audience:** architects, developers, analysts, governance leads; product owners and business experts for the conceptual level only.
- **Scenarios:** agreeing the shop vocabulary (customer, order, payment, shipment) before building; a new service's persistence boundary; explaining an existing schema (reverse-engineered logical view); migration mapping of two systems' entities; tenancy and sharing relations.
- **When not to use:** who does what when (E1, E2, A5); a dump of every table of a large database (generate it with a schema tool); how data moves between systems (D2, C6).
- **vs neighbours:**
  - **D2 Data Flow Diagram** when data is moving; D1 shows structure.
  - **E3 State Machine** for one entity's lifecycle; a common pair is D1 plus one E3 per entity with a status field.
  - **C7 Bounded Context Map** for how contexts relate; draw one D1 per context, not one enterprise ER.
  - **F3 Access-control model** for permissions.
  - Choose **D3 Data lineage and ownership map** when the question is where data comes from, what derives from it and who owns it, rather than how entities relate.

## Notation and elements
- **Formal or informal:** each notation is defined, but the level is a convention. Pick one notation, state it in a legend, never mix Chen diamonds with crow's feet.
- **Required:**
  - **Entities:** singular business nouns (`Customer`, `Order`), capitalised consistently.
  - **Relationships:** lines labelled with a verb phrase readable in one direction ("Customer *places* Order").
  - **Cardinality at both ends,** minimum and maximum. In crow's foot the outer symbol is the maximum and the inner the minimum; Mermaid's `erDiagram` documents `|o` zero or one, `||` exactly one, `}o` zero or more, `}|` one or more.
- **Optional (logical level):** primary-key and a few defining attributes; identifying (solid) vs non-identifying (dashed) relationships; associative entities for N:M; sub- and supertypes. Foreign keys are a relational device and belong to the logical or physical level only.
- **UML variant:** classes with multiplicities (`0..1`, `1`, `*`, `1..*`), composition, aggregation, generalisation.
- **Legend:** notation ("crow's foot; min inner, max outer") and level ("conceptual" or "logical").
- **Size:** conceptual about 5-15 entities per view (a rule of thumb, not a standard); logical shows only attributes that explain meaning ("often a small subset of attributes is enough").
- **Naming:** user language, not table prefixes (`tbl_cust`); verbs on lines, not a generic "has" where a precise verb exists.

## Best practices and anti-patterns
### Best practices
1. **State the level in the title** ("Conceptual model: order management") and draw to it.
2. **One subject area per diagram.** Slice by bounded context or business function; reference shared entities instead of duplicating them.
3. **Model with domain experts** and read every relationship aloud ("Each Order is placed by exactly one Customer").
4. **Show optionality** (minimum 0 vs 1); it holds business rules that would otherwise hide in code.
5. **Resolve N:M only at the logical level,** naming the associative entity after the real thing (`OrderLine`, not `OrderProduct`). Note cross-cutting patterns (tenant key, soft delete, audit) once instead of on every entity.

### Anti-patterns
1. **The database dump:** 100+ tables with all columns; comprehensiveness is the enemy of comprehensibility.
2. **Mixed levels:** foreign keys, types and indexes on a business-facing conceptual model.
3. **Unlabelled lines or cardinality missing at one end.**
4. **Technical or meaningless names:** `data`, `info`, `item2`, table prefixes.
5. **Process encoded as entities** (`ApprovalStep1`, `ApprovalStep2`) or mixed notations without a legend. Also avoid a prose entity list where a real diagram would show the chain.

## Drawing recipe
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

## Evidence in a code repository
- **Strong:** DDL plus the latest migrations (the current schema wins over the first DDL); ORM or entity classes and their relationship declarations; GraphQL and OpenAPI resource schemas; foreign keys and unique constraints (cardinality evidence).
- **Weak, mark as inferred:** an `xxx_id` column without a foreign key, JSON blobs, document stores.
- **Must come from people:** business names for technical tables, optionality the business intends, which entities matter to the audience.

## Guided-mode questions
1. Who is the reader: business stakeholders (conceptual) or engineers (logical)? Should attributes or keys appear? (engineers, logical, key attributes only)
2. Which subject area or bounded context, and should neighbouring areas be stubs or omitted? (one context, neighbours as stubs)
3. Is there a source of truth to follow (schema, ORM, glossary) or are we designing the target model? (follow the existing schema, marked inferred)
4. Which notation does your organisation use? (crow's foot)
5. Should tenancy, ownership, audit or versioning be shown on entities or noted once? (noted once)

## Template
Model template: `assets/templates/D1.json` · Layout template: `er` · entities become `nodes` of kind `entity` (attribute strings in `attributes`, key markers such as `PK`/`FK` first), a bounded context or subject area becomes a `boundary` group, relationships become edges with `dir` `--` whose `cardinality{from,to}` carries min/max and whose `label` is the verb; the level goes in the title.

## Sample
Figure: `samples/D1-entity-relationship.svg` (published with the site)
