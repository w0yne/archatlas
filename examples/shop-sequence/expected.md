# Expected: sequence diagram (E1)

**Audience:** developers. **Question:** in what order do the participants exchange messages when a customer places an order?

A correct output has:
- four lifelines that are real, nameable systems, the person on the left; messages numbered in time order;
- request arrows solid, replies dashed; activation bars from first call to the last reply;
- one `loop` frame around the reserve/reserved round trip (the whole round trip, not a single arrow);
- the happy path only; no error branches (they belong in their own figure); no endpoint names or protocols.
