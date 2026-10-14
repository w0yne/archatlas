# Expected: entity-relationship diagram (D1, logical)

**Audience:** developers and analysts. **Question:** which business objects does the shop keep, and how are they related?

A correct output has:
- four core entities (well under 15), each with its key attributes (PK/FK first) and no types, indexes or storage details;
- every relationship line labelled with a verb and with cardinality at both ends (1 / N);
- the many-to-many between orders and products resolved into the `order_line` entity;
- no crossing lines; names singular and consistent.
