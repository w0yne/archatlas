# Expected: data flow with trust boundaries (F2)

**Audience:** security reviewers and architects. **Question:** which data flows cross a trust boundary during checkout?

A correct output has:
- four dashed frames (internet, public edge, internal network, payment provider); every element inside exactly one frame;
- numbered data flows named with nouns (what moves), each crossing at most the boundaries it really crosses;
- stores drawn as stores, external parties in the external style; the automatic legend entry for the dashed frame;
- no threat lists or mitigation text on the figure (those go in the accompanying review table).
