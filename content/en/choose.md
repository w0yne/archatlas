---
title: How to choose a diagram
description: Pick the right architecture diagram by audience and by the question it must answer.
---

# How to choose a diagram

Start small: [C2](/types/c2-system-context) → [C3](/types/c3-container-diagram) → [E1](/types/e1-sequence-diagram) → [G1](/types/g1-deployment-diagram). Add [F1 identity delegation](/types/e1-sequence-diagram#variant-f1) and [F2 threat modelling](/types/d2-data-flow-diagram#variant-f2) when the question needs them. There are 25 core entries, 10 named variants and 5 method references; all 40 stable codes and old links remain supported.

Most diagram problems start before the first box is drawn: the figure tries to answer
several questions at once, or it uses the right notation for the wrong reader. This page
helps you pick **one type per question**. If a reader needs two answers, draw two figures.

Use the common requests below for a first recommendation. The full tree and reference lists help with less familiar cases. [Unfamiliar terms? Read the glossary.](/glossary)

Terms used in the catalogue: [application estate](/glossary#estate), [persona](/glossary#persona), [BPMN](/glossary#bpmn), [trust boundary](/glossary#trust-boundary), [promotion gate](/glossary#promotion-gate), [Lean](/glossary#lean), [bounded context](/glossary#bounded-context), [ArchiMate](/glossary#archimate), [Rummler–Brache swimlane](/glossary#rummler-brache).

<!-- Maintainers: edit types.yaml and selection-tree.yaml, not generated blocks. -->

## Common requests: start here

<!-- BEGIN GENERATED: common -->
- **Onboard a developer**: Start with: [C2 System context diagram (C4 model level 1)](/types/c2-system-context). Then consider: [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram), [E1 Sequence diagram](/types/e1-sequence-diagram). Start with the system and its neighbours; then show running parts and one request.
- **Show a technical executive the big picture**: Start with: [C2 System context diagram (C4 model level 1)](/types/c2-system-context). Then consider: [C1 Application landscape](/types/c1-application-landscape). Use C1 instead when the subject is a portfolio of applications, not one system.
- **Explain a solution to business readers**: Start with: [A7 Conceptual architecture (solution overview)](/types/c5-logical-architecture#variant-a7). Then consider: [A1 Business capability map](/types/a1-capability-map). Show the main solution blocks; use A1 when the question is business abilities or investment.
- **Model order status**: Start with: [E3 State machine diagram](/types/e3-state-machine). Then consider: [E2 Activity diagram or flowchart](/types/e2-activity-flowchart). Show states and allowed changes; use E2 for the processing steps instead.
- **Explain who may access what**: Start with: [F3 Access-control model](/types/f3-access-control-model). Then consider: [F1 Authentication and authorization flow](/types/e1-sequence-diagram#variant-f1). Start with permissions and scope; add F1 to explain identity verification and enforcement.
- **Plan a migration**: Start with: [A8 Target architecture and transition roadmap](/types/a8-target-roadmap). Then consider: [G1 Deployment & cloud architecture](/types/g1-deployment-diagram), [G2 Cloud infrastructure architecture](/types/g1-deployment-diagram#variant-g2). Show coherent transition states; use paired current/target deployment or cloud views for detail.
- **Draw a database or schema diagram**: Start with: [D1 Entity-relationship diagram](/types/d1-entity-relationship). Then consider: [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership). Show entities and relationships; add D3 when lineage and ownership matter.
- **Explain the release process**: Start with: [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline). Then consider: [G1 Deployment & cloud architecture](/types/g1-deployment-diagram). Show build, checks and promotion; add G1 for the resulting deployment.
<!-- END GENERATED: common -->

## Start with four questions

<!-- BEGIN GENERATED: questions -->
1. Who will read it, and what should they do afterwards (decide, approve, build, operate, review)?
2. Which question must the figure answer? Pick one branch below.
3. What is the scope: all applications in an organisation, one system, or one part inside it?
4. Current state, target state, or both (as separate figures)?
<!-- END GENERATED: questions -->

## Decision tree: what must the figure answer?

Find the reader's question, then follow it to one or two types. When two types are listed,
the note says how to choose between them.

<!-- BEGIN GENERATED: tree -->
- **Why invest, and where is the value?**
  - What the organisation can do, and where to invest → [A1 Business capability map](/types/a1-capability-map)
  - Which stages deliver value to a stakeholder → [A2 Value stream (business architecture)](/types/a2-value-stream), [A9 Lean value-stream map (VSM)](/types/a2-value-stream#variant-a9). A2 has no timings and maps stages to capabilities; A9 measures process and waiting time.
  - What the solution is, in business terms → [A7 Conceptual architecture (solution overview)](/types/c5-logical-architecture#variant-a7)
  - How to get from today to the target, step by step → [A8 Target architecture and transition roadmap](/types/a8-target-roadmap)
  - What a typical user experiences → [A6 Customer or user journey map](/types/a6-journey-map)
- **What must it do, for whom, and what is in or out?**
  - What is in or out of scope, and who connects to us → [B4 Scope diagram](/types/c2-system-context#variant-b4), [C2 System context diagram (C4 model level 1)](/types/c2-system-context). B4 when the point is the boundary of this phase; C2 when the subject is a software system and its neighbours.
  - Which outside parties the business deals with, and what is exchanged → [A3 Business context diagram](/types/c2-system-context#variant-a3)
  - Which roles do what, in which release → [A4 Business scenario matrix (role × activity)](/types/b2-user-story-map#variant-a4), [B2 User story map](/types/b2-user-story-map). A4 shows coverage across several roles; B2 tells one end-to-end story with release slices.
  - How a business case runs across participants → [A5 Business process diagram (BPMN)](/types/a5-bpmn-process)
  - What a typical user needs at each stage of one task → [A6 Customer or user journey map](/types/a6-journey-map)
- **What are the parts and how are they organised?**
  - Applications across the organisation, and who owns them → [C1 Application landscape](/types/c1-application-landscape)
  - Main blocks, for non-technical readers → [A7 Conceptual architecture (solution overview)](/types/c5-logical-architecture#variant-a7)
  - One system: users and neighbouring systems → [C2 System context diagram (C4 model level 1)](/types/c2-system-context)
  - One system: its running applications and data stores → [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram)
  - Inside one application: its components → [C4 Component diagram (C4 model level 3)](/types/c4-component-diagram)
  - Responsibilities and interfaces, without technology → [C5 Logical architecture diagram](/types/c5-logical-architecture)
  - Where different teams use different business models → [C7 Bounded context map (DDD)](/types/c7-bounded-context-map)
  - Code layers and allowed dependencies → [C8 Layered architecture diagram](/types/c4-component-diagram#variant-c8)
- **How do the parts and systems connect?**
  - What interfaces exchange, how they authenticate, and what happens on failure → [C6 Integration and interface diagram](/types/c6-integration-interface)
  - Dependencies between applications across the organisation → [C1 Application landscape](/types/c1-application-landscape)
  - How the running parts of one system talk → [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram)
  - Message order in one scenario → [E1 Sequence diagram](/types/e1-sequence-diagram)
  - Relationships between domain models and teams → [C7 Bounded context map (DDD)](/types/c7-bounded-context-map)
- **What data is there, where does it flow, who owns it?**
  - Which business objects exist and how they relate → [D1 Entity-relationship diagram](/types/d1-entity-relationship)
  - How data moves between processes and stores → [D2 Data flow diagram (DFD)](/types/d2-data-flow-diagram)
  - Where a dataset came from, and who owns it → [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership)
  - Which data crosses a change in control or access rights → [F2 Threat-model data-flow diagram with trust boundaries](/types/d2-data-flow-diagram#variant-f2)
- **What happens, in which order, with which states?**
  - Messages between participants, in order → [E1 Sequence diagram](/types/e1-sequence-diagram)
  - Steps, decisions and parallel branches of one piece of logic → [E2 Activity diagram or flowchart](/types/e2-activity-flowchart)
  - The lifecycle of one object → [E3 State machine diagram](/types/e3-state-machine)
  - Hand-offs between roles or systems → [E4 Swimlane or cross-functional flowchart](/types/e2-activity-flowchart#variant-e4), [A5 Business process diagram (BPMN)](/types/a5-bpmn-process). E4 for simple hand-offs; A5 when the diagram needs strict rules for process events and messages (BPMN).
  - How sign-in and access decisions happen → [F1 Authentication and authorization flow](/types/e1-sequence-diagram#variant-f1)
  - Where a delivery process waits → [A9 Lean value-stream map (VSM)](/types/a2-value-stream#variant-a9)
- **Who may do what, and what could go wrong?**
  - Sign-in, tokens, and where access is decided → [F1 Authentication and authorization flow](/types/e1-sequence-diagram#variant-f1)
  - What could go wrong when data crosses a change in control → [F2 Threat-model data-flow diagram with trust boundaries](/types/d2-data-flow-diagram#variant-f2)
  - Who may do what, in which scope → [F3 Access-control model](/types/f3-access-control-model)
  - Network exposure and paths → [G3 Network topology and connectivity view](/types/g3-network-topology)
- **Where does it run and how does it ship?**
  - How to migrate from today's system to the target → [A8 Target architecture and transition roadmap](/types/a8-target-roadmap)
  - Where the software runs → [G1 Deployment & cloud architecture](/types/g1-deployment-diagram)
  - Which cloud services, and their failure boundaries → [G2 Cloud infrastructure architecture](/types/g1-deployment-diagram#variant-g2)
  - Network segments and paths → [G3 Network topology and connectivity view](/types/g3-network-topology)
  - How a change ships to production → [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline)
  - How the running system is observed → [H2 Observability view](/types/h2-observability-view)
- **Who is responsible, and how is it run and watched?**
  - Who is responsible for each activity → [H1 RACI matrix](/types/h1-raci-matrix)
  - How problems are detected and answered → [H2 Observability view](/types/h2-observability-view)
  - Who owns which data → [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership)
  - Hand-offs in an operating procedure → [E4 Swimlane or cross-functional flowchart](/types/e2-activity-flowchart#variant-e4)
  - Owners and lifecycle state of applications → [C1 Application landscape](/types/c1-application-landscape)
  - Checks and approvals before releasing a change → [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline)
<!-- END GENERATED: tree -->

## Audience × question

The same question needs different figures for different readers. Cells include curated starting points as well as catalogue matches; they are recommendations, not mandatory checklists. On small screens, use the per-audience lists below.

<!-- BEGIN GENERATED: matrix -->
| Question | Leaders and sponsors | Business owners and analysts | Product and design | Architects | Developers and testers | Operations and SRE | Security and compliance |
|---|---|---|---|---|---|---|---|
| Why invest, and where is the value? | [A1 Business capability map](/types/a1-capability-map), [A2 Value stream (business architecture)](/types/a2-value-stream), [A6 Customer or user journey map](/types/a6-journey-map), [A8 Target architecture and transition roadmap](/types/a8-target-roadmap) | [A1 Business capability map](/types/a1-capability-map), [A2 Value stream (business architecture)](/types/a2-value-stream), [A6 Customer or user journey map](/types/a6-journey-map) | [A6 Customer or user journey map](/types/a6-journey-map) | [A1 Business capability map](/types/a1-capability-map), [A2 Value stream (business architecture)](/types/a2-value-stream), [A8 Target architecture and transition roadmap](/types/a8-target-roadmap) | – | – | – |
| What must it do, for whom, and what is in or out? | [A6 Customer or user journey map](/types/a6-journey-map), [C2 System context diagram (C4 model level 1)](/types/c2-system-context) | [A5 Business process diagram (BPMN)](/types/a5-bpmn-process), [A6 Customer or user journey map](/types/a6-journey-map), [B2 User story map](/types/b2-user-story-map), [C2 System context diagram (C4 model level 1)](/types/c2-system-context) | [A5 Business process diagram (BPMN)](/types/a5-bpmn-process), [A6 Customer or user journey map](/types/a6-journey-map), [B2 User story map](/types/b2-user-story-map) | [C2 System context diagram (C4 model level 1)](/types/c2-system-context) | [A5 Business process diagram (BPMN)](/types/a5-bpmn-process), [B2 User story map](/types/b2-user-story-map), [C2 System context diagram (C4 model level 1)](/types/c2-system-context) | – | [C2 System context diagram (C4 model level 1)](/types/c2-system-context) |
| What are the parts and how are they organised? | [A1 Business capability map](/types/a1-capability-map), [C1 Application landscape](/types/c1-application-landscape), [C2 System context diagram (C4 model level 1)](/types/c2-system-context) | [A1 Business capability map](/types/a1-capability-map), [C2 System context diagram (C4 model level 1)](/types/c2-system-context), [C7 Bounded context map (DDD)](/types/c7-bounded-context-map) | [C5 Logical architecture diagram](/types/c5-logical-architecture) | [A1 Business capability map](/types/a1-capability-map), [C1 Application landscape](/types/c1-application-landscape), [C2 System context diagram (C4 model level 1)](/types/c2-system-context), [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram), [C4 Component diagram (C4 model level 3)](/types/c4-component-diagram), [C5 Logical architecture diagram](/types/c5-logical-architecture), [C7 Bounded context map (DDD)](/types/c7-bounded-context-map) | [C2 System context diagram (C4 model level 1)](/types/c2-system-context), [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram), [C4 Component diagram (C4 model level 3)](/types/c4-component-diagram), [C5 Logical architecture diagram](/types/c5-logical-architecture), [C7 Bounded context map (DDD)](/types/c7-bounded-context-map) | [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram) | [C2 System context diagram (C4 model level 1)](/types/c2-system-context), [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram) |
| How do the parts and systems connect? | [C1 Application landscape](/types/c1-application-landscape) | [C7 Bounded context map (DDD)](/types/c7-bounded-context-map) | – | [C1 Application landscape](/types/c1-application-landscape), [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram), [C6 Integration and interface diagram](/types/c6-integration-interface), [C7 Bounded context map (DDD)](/types/c7-bounded-context-map), [E1 Sequence diagram](/types/e1-sequence-diagram) | [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram), [C6 Integration and interface diagram](/types/c6-integration-interface), [C7 Bounded context map (DDD)](/types/c7-bounded-context-map), [E1 Sequence diagram](/types/e1-sequence-diagram) | [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram), [C6 Integration and interface diagram](/types/c6-integration-interface) | [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram) |
| What data is there, where does it flow, who owns it? | – | [D1 Entity-relationship diagram](/types/d1-entity-relationship), [D2 Data flow diagram (DFD)](/types/d2-data-flow-diagram), [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership) | – | [D1 Entity-relationship diagram](/types/d1-entity-relationship), [D2 Data flow diagram (DFD)](/types/d2-data-flow-diagram), [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership) | [D1 Entity-relationship diagram](/types/d1-entity-relationship) | – | [D2 Data flow diagram (DFD)](/types/d2-data-flow-diagram), [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership) |
| What happens, in which order, with which states? | – | [A5 Business process diagram (BPMN)](/types/a5-bpmn-process), [E2 Activity diagram or flowchart](/types/e2-activity-flowchart) | [A5 Business process diagram (BPMN)](/types/a5-bpmn-process), [E3 State machine diagram](/types/e3-state-machine) | [E1 Sequence diagram](/types/e1-sequence-diagram) | [A5 Business process diagram (BPMN)](/types/a5-bpmn-process), [E1 Sequence diagram](/types/e1-sequence-diagram), [E2 Activity diagram or flowchart](/types/e2-activity-flowchart), [E3 State machine diagram](/types/e3-state-machine) | – | – |
| Who may do what, and what could go wrong? | – | [F3 Access-control model](/types/f3-access-control-model) | – | [F3 Access-control model](/types/f3-access-control-model), [G3 Network topology and connectivity view](/types/g3-network-topology) | [F3 Access-control model](/types/f3-access-control-model) | [G3 Network topology and connectivity view](/types/g3-network-topology) | [F3 Access-control model](/types/f3-access-control-model), [G3 Network topology and connectivity view](/types/g3-network-topology) |
| Where does it run and how does it ship? | [G2 Cloud infrastructure architecture](/types/g1-deployment-diagram#variant-g2), [G1 Deployment & cloud architecture](/types/g1-deployment-diagram), [A8 Target architecture and transition roadmap](/types/a8-target-roadmap) | – | – | [G1 Deployment & cloud architecture](/types/g1-deployment-diagram), [G3 Network topology and connectivity view](/types/g3-network-topology) | [G1 Deployment & cloud architecture](/types/g1-deployment-diagram), [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline), [A8 Target architecture and transition roadmap](/types/a8-target-roadmap) | [G1 Deployment & cloud architecture](/types/g1-deployment-diagram), [G2 Cloud infrastructure architecture](/types/g1-deployment-diagram#variant-g2), [G3 Network topology and connectivity view](/types/g3-network-topology), [A8 Target architecture and transition roadmap](/types/a8-target-roadmap) | [G1 Deployment & cloud architecture](/types/g1-deployment-diagram), [G3 Network topology and connectivity view](/types/g3-network-topology), [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline) |
| Who is responsible, and how is it run and watched? | [C1 Application landscape](/types/c1-application-landscape), [H1 RACI matrix](/types/h1-raci-matrix), [H2 Observability view](/types/h2-observability-view) | [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership), [H1 RACI matrix](/types/h1-raci-matrix) | – | [C1 Application landscape](/types/c1-application-landscape), [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership) | [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline), [H2 Observability view](/types/h2-observability-view) | [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline), [H1 RACI matrix](/types/h1-raci-matrix), [H2 Observability view](/types/h2-observability-view) | [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership), [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline) |
| How do I organise several diagrams into one description? | – | – | – | – | – | – | – |
<!-- END GENERATED: matrix -->

## Browse by audience

<!-- BEGIN GENERATED: audiences -->
<details><summary>Leaders and sponsors</summary>

- **Why invest, and where is the value?** : [A1 Business capability map](/types/a1-capability-map), [A2 Value stream (business architecture)](/types/a2-value-stream), [A6 Customer or user journey map](/types/a6-journey-map), [A8 Target architecture and transition roadmap](/types/a8-target-roadmap)
- **What must it do, for whom, and what is in or out?** : [A6 Customer or user journey map](/types/a6-journey-map), [C2 System context diagram (C4 model level 1)](/types/c2-system-context)
- **What are the parts and how are they organised?** : [A1 Business capability map](/types/a1-capability-map), [C1 Application landscape](/types/c1-application-landscape), [C2 System context diagram (C4 model level 1)](/types/c2-system-context)
- **How do the parts and systems connect?** : [C1 Application landscape](/types/c1-application-landscape)
- **Where does it run and how does it ship?** : [G2 Cloud infrastructure architecture](/types/g1-deployment-diagram#variant-g2), [G1 Deployment & cloud architecture](/types/g1-deployment-diagram), [A8 Target architecture and transition roadmap](/types/a8-target-roadmap)
- **Who is responsible, and how is it run and watched?** : [C1 Application landscape](/types/c1-application-landscape), [H1 RACI matrix](/types/h1-raci-matrix), [H2 Observability view](/types/h2-observability-view)

</details>

<details><summary>Business owners and analysts</summary>

- **Why invest, and where is the value?** : [A1 Business capability map](/types/a1-capability-map), [A2 Value stream (business architecture)](/types/a2-value-stream), [A6 Customer or user journey map](/types/a6-journey-map)
- **What must it do, for whom, and what is in or out?** : [A5 Business process diagram (BPMN)](/types/a5-bpmn-process), [A6 Customer or user journey map](/types/a6-journey-map), [B2 User story map](/types/b2-user-story-map), [C2 System context diagram (C4 model level 1)](/types/c2-system-context)
- **What are the parts and how are they organised?** : [A1 Business capability map](/types/a1-capability-map), [C2 System context diagram (C4 model level 1)](/types/c2-system-context), [C7 Bounded context map (DDD)](/types/c7-bounded-context-map)
- **How do the parts and systems connect?** : [C7 Bounded context map (DDD)](/types/c7-bounded-context-map)
- **What data is there, where does it flow, who owns it?** : [D1 Entity-relationship diagram](/types/d1-entity-relationship), [D2 Data flow diagram (DFD)](/types/d2-data-flow-diagram), [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership)
- **What happens, in which order, with which states?** : [A5 Business process diagram (BPMN)](/types/a5-bpmn-process), [E2 Activity diagram or flowchart](/types/e2-activity-flowchart)
- **Who may do what, and what could go wrong?** : [F3 Access-control model](/types/f3-access-control-model)
- **Who is responsible, and how is it run and watched?** : [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership), [H1 RACI matrix](/types/h1-raci-matrix)

</details>

<details><summary>Product and design</summary>

- **Why invest, and where is the value?** : [A6 Customer or user journey map](/types/a6-journey-map)
- **What must it do, for whom, and what is in or out?** : [A5 Business process diagram (BPMN)](/types/a5-bpmn-process), [A6 Customer or user journey map](/types/a6-journey-map), [B2 User story map](/types/b2-user-story-map)
- **What are the parts and how are they organised?** : [C5 Logical architecture diagram](/types/c5-logical-architecture)
- **What happens, in which order, with which states?** : [A5 Business process diagram (BPMN)](/types/a5-bpmn-process), [E3 State machine diagram](/types/e3-state-machine)

</details>

<details><summary>Architects</summary>

- **Why invest, and where is the value?** : [A1 Business capability map](/types/a1-capability-map), [A2 Value stream (business architecture)](/types/a2-value-stream), [A8 Target architecture and transition roadmap](/types/a8-target-roadmap)
- **What must it do, for whom, and what is in or out?** : [C2 System context diagram (C4 model level 1)](/types/c2-system-context)
- **What are the parts and how are they organised?** : [A1 Business capability map](/types/a1-capability-map), [C1 Application landscape](/types/c1-application-landscape), [C2 System context diagram (C4 model level 1)](/types/c2-system-context), [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram), [C4 Component diagram (C4 model level 3)](/types/c4-component-diagram), [C5 Logical architecture diagram](/types/c5-logical-architecture), [C7 Bounded context map (DDD)](/types/c7-bounded-context-map)
- **How do the parts and systems connect?** : [C1 Application landscape](/types/c1-application-landscape), [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram), [C6 Integration and interface diagram](/types/c6-integration-interface), [C7 Bounded context map (DDD)](/types/c7-bounded-context-map), [E1 Sequence diagram](/types/e1-sequence-diagram)
- **What data is there, where does it flow, who owns it?** : [D1 Entity-relationship diagram](/types/d1-entity-relationship), [D2 Data flow diagram (DFD)](/types/d2-data-flow-diagram), [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership)
- **What happens, in which order, with which states?** : [E1 Sequence diagram](/types/e1-sequence-diagram)
- **Who may do what, and what could go wrong?** : [F3 Access-control model](/types/f3-access-control-model), [G3 Network topology and connectivity view](/types/g3-network-topology)
- **Where does it run and how does it ship?** : [G1 Deployment & cloud architecture](/types/g1-deployment-diagram), [G3 Network topology and connectivity view](/types/g3-network-topology)
- **Who is responsible, and how is it run and watched?** : [C1 Application landscape](/types/c1-application-landscape), [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership)

</details>

<details><summary>Developers and testers</summary>

- **What must it do, for whom, and what is in or out?** : [A5 Business process diagram (BPMN)](/types/a5-bpmn-process), [B2 User story map](/types/b2-user-story-map), [C2 System context diagram (C4 model level 1)](/types/c2-system-context)
- **What are the parts and how are they organised?** : [C2 System context diagram (C4 model level 1)](/types/c2-system-context), [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram), [C4 Component diagram (C4 model level 3)](/types/c4-component-diagram), [C5 Logical architecture diagram](/types/c5-logical-architecture), [C7 Bounded context map (DDD)](/types/c7-bounded-context-map)
- **How do the parts and systems connect?** : [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram), [C6 Integration and interface diagram](/types/c6-integration-interface), [C7 Bounded context map (DDD)](/types/c7-bounded-context-map), [E1 Sequence diagram](/types/e1-sequence-diagram)
- **What data is there, where does it flow, who owns it?** : [D1 Entity-relationship diagram](/types/d1-entity-relationship)
- **What happens, in which order, with which states?** : [A5 Business process diagram (BPMN)](/types/a5-bpmn-process), [E1 Sequence diagram](/types/e1-sequence-diagram), [E2 Activity diagram or flowchart](/types/e2-activity-flowchart), [E3 State machine diagram](/types/e3-state-machine)
- **Who may do what, and what could go wrong?** : [F3 Access-control model](/types/f3-access-control-model)
- **Where does it run and how does it ship?** : [G1 Deployment & cloud architecture](/types/g1-deployment-diagram), [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline), [A8 Target architecture and transition roadmap](/types/a8-target-roadmap)
- **Who is responsible, and how is it run and watched?** : [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline), [H2 Observability view](/types/h2-observability-view)

</details>

<details><summary>Operations and SRE</summary>

- **What are the parts and how are they organised?** : [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram)
- **How do the parts and systems connect?** : [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram), [C6 Integration and interface diagram](/types/c6-integration-interface)
- **Who may do what, and what could go wrong?** : [G3 Network topology and connectivity view](/types/g3-network-topology)
- **Where does it run and how does it ship?** : [G1 Deployment & cloud architecture](/types/g1-deployment-diagram), [G2 Cloud infrastructure architecture](/types/g1-deployment-diagram#variant-g2), [G3 Network topology and connectivity view](/types/g3-network-topology), [A8 Target architecture and transition roadmap](/types/a8-target-roadmap)
- **Who is responsible, and how is it run and watched?** : [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline), [H1 RACI matrix](/types/h1-raci-matrix), [H2 Observability view](/types/h2-observability-view)

</details>

<details><summary>Security and compliance</summary>

- **What must it do, for whom, and what is in or out?** : [C2 System context diagram (C4 model level 1)](/types/c2-system-context)
- **What are the parts and how are they organised?** : [C2 System context diagram (C4 model level 1)](/types/c2-system-context), [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram)
- **How do the parts and systems connect?** : [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram)
- **What data is there, where does it flow, who owns it?** : [D2 Data flow diagram (DFD)](/types/d2-data-flow-diagram), [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership)
- **Who may do what, and what could go wrong?** : [F3 Access-control model](/types/f3-access-control-model), [G3 Network topology and connectivity view](/types/g3-network-topology)
- **Where does it run and how does it ship?** : [G1 Deployment & cloud architecture](/types/g1-deployment-diagram), [G3 Network topology and connectivity view](/types/g3-network-topology), [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline)
- **Who is responsible, and how is it run and watched?** : [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership), [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline)

</details>

<!-- END GENERATED: audiences -->

## By lifecycle phase

<!-- BEGIN GENERATED: phases -->
- **Initiate** : [A1 Business capability map](/types/a1-capability-map), [C5 Logical architecture diagram](/types/c5-logical-architecture), [C1 Application landscape](/types/c1-application-landscape)
<details><summary>Also useful</summary>

[A2 Value stream (business architecture)](/types/a2-value-stream), [A6 Customer or user journey map](/types/a6-journey-map), [A8 Target architecture and transition roadmap](/types/a8-target-roadmap), [C2 System context diagram (C4 model level 1)](/types/c2-system-context), [H1 RACI matrix](/types/h1-raci-matrix)

</details>

- **Requirements** : [B2 User story map](/types/b2-user-story-map), [C2 System context diagram (C4 model level 1)](/types/c2-system-context), [D1 Entity-relationship diagram](/types/d1-entity-relationship)
<details><summary>Also useful</summary>

[A5 Business process diagram (BPMN)](/types/a5-bpmn-process), [A6 Customer or user journey map](/types/a6-journey-map), [D2 Data flow diagram (DFD)](/types/d2-data-flow-diagram)

</details>

- **Design** : [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram), [D1 Entity-relationship diagram](/types/d1-entity-relationship), [E1 Sequence diagram](/types/e1-sequence-diagram)
<details><summary>Also useful</summary>

[A5 Business process diagram (BPMN)](/types/a5-bpmn-process), [A8 Target architecture and transition roadmap](/types/a8-target-roadmap), [C1 Application landscape](/types/c1-application-landscape), [C2 System context diagram (C4 model level 1)](/types/c2-system-context), [C4 Component diagram (C4 model level 3)](/types/c4-component-diagram), [C5 Logical architecture diagram](/types/c5-logical-architecture), [C6 Integration and interface diagram](/types/c6-integration-interface), [C7 Bounded context map (DDD)](/types/c7-bounded-context-map), [D2 Data flow diagram (DFD)](/types/d2-data-flow-diagram), [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership), [E2 Activity diagram or flowchart](/types/e2-activity-flowchart), [E3 State machine diagram](/types/e3-state-machine), [F3 Access-control model](/types/f3-access-control-model), [G1 Deployment & cloud architecture](/types/g1-deployment-diagram), [G3 Network topology and connectivity view](/types/g3-network-topology)

</details>

- **Build** : [C4 Component diagram (C4 model level 3)](/types/c4-component-diagram), [E1 Sequence diagram](/types/e1-sequence-diagram), [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline)
<details><summary>Also useful</summary>

[C3 Container diagram (C4 model level 2)](/types/c3-container-diagram), [C6 Integration and interface diagram](/types/c6-integration-interface), [D1 Entity-relationship diagram](/types/d1-entity-relationship), [E2 Activity diagram or flowchart](/types/e2-activity-flowchart), [E3 State machine diagram](/types/e3-state-machine), [F3 Access-control model](/types/f3-access-control-model)

</details>

- **Release and operate** : [G1 Deployment & cloud architecture](/types/g1-deployment-diagram), [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline), [H2 Observability view](/types/h2-observability-view)
<details><summary>Also useful</summary>

[D3 Data lineage and ownership map](/types/d3-data-lineage-ownership), [G3 Network topology and connectivity view](/types/g3-network-topology), [H1 RACI matrix](/types/h1-raci-matrix)

</details>

<!-- END GENERATED: phases -->

## What people call it

Some everyday names do not identify one diagram. When someone asks for one of these, ask
which meaning they have in mind, or choose one and say which.

<!-- BEGIN GENERATED: terms -->
- *system architecture diagram* → [C2 System context diagram (C4 model level 1)](/types/c2-system-context), [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram), [A7 Conceptual architecture (solution overview)](/types/c5-logical-architecture#variant-a7), [G1 Deployment & cloud architecture](/types/g1-deployment-diagram). Start with C2 for the system and its neighbours, then C3 for running parts. A7 is a conceptual solution overview; G1 shows deployment.
- *technical architecture diagram* → [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram), [G1 Deployment & cloud architecture](/types/g1-deployment-diagram), [G2 Cloud infrastructure architecture](/types/g1-deployment-diagram#variant-g2). Containers with technology labels (C3), or the infrastructure views (G1, G2).
- *application architecture diagram* → [C1 Application landscape](/types/c1-application-landscape), [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram). Portfolio of many applications (C1) or the running applications and data stores of one system (C3). Inside one running application is C4, not C3.
- *business architecture diagram* → [A1 Business capability map](/types/a1-capability-map), [A2 Value stream (business architecture)](/types/a2-value-stream), [A5 Business process diagram (BPMN)](/types/a5-bpmn-process). A family, not one diagram: capabilities (A1), value streams (A2), processes (A5).
- *context diagram* → [C2 System context diagram (C4 model level 1)](/types/c2-system-context), [A3 Business context diagram](/types/c2-system-context#variant-a3), [B4 Scope diagram](/types/c2-system-context#variant-b4). Software system and its neighbours (C2); business exchanges (A3); in/out of scope (B4).
- *DFD level 0* → [D2 Data flow diagram (DFD)](/types/d2-data-flow-diagram), [C2 System context diagram (C4 model level 1)](/types/c2-system-context). Two numbering conventions exist: some authors call the context-level DFD (one process, C2-like) 'level 0', others mean the first decomposition below it (D2). Say 'context-level DFD' or 'first-level DFD' instead.
- *flowchart* → [E2 Activity diagram or flowchart](/types/e2-activity-flowchart), [A5 Business process diagram (BPMN)](/types/a5-bpmn-process), [E4 Swimlane or cross-functional flowchart](/types/e2-activity-flowchart#variant-e4). Logic of one procedure (E2); business process with BPMN semantics (A5); hand-offs between roles or systems (E4).
- *swimlane diagram* → [E4 Swimlane or cross-functional flowchart](/types/e2-activity-flowchart#variant-e4), [A5 Business process diagram (BPMN)](/types/a5-bpmn-process). Lightweight hand-offs (E4) or BPMN pools and lanes with message flows (A5).
- *physical architecture diagram* → [G1 Deployment & cloud architecture](/types/g1-deployment-diagram), [G3 Network topology and connectivity view](/types/g3-network-topology). Software placed on infrastructure (G1) or the network (G3). State which.
- *module diagram* → [C4 Component diagram (C4 model level 3)](/types/c4-component-diagram), [C5 Logical architecture diagram](/types/c5-logical-architecture), [C8 Layered architecture diagram](/types/c4-component-diagram#variant-c8). Components inside one container (C4), technology-neutral responsibilities (C5) or code layers (C8).
- *functional architecture diagram* → [C5 Logical architecture diagram](/types/c5-logical-architecture), [B3 Feature tree (functional decomposition)](/types/b3-feature-tree). Logical responsibilities (C5); a function tree in the systems-engineering sense (B3).
- *value stream map* → [A2 Value stream (business architecture)](/types/a2-value-stream), [A9 Lean value-stream map (VSM)](/types/a2-value-stream#variant-a9). Business-architecture value stream without times (A2) or Lean value-stream map with process and lead times (A9).
- *reference architecture* → [G2 Cloud infrastructure architecture](/types/g1-deployment-diagram#variant-g2), [A7 Conceptual architecture (solution overview)](/types/c5-logical-architecture#variant-a7), [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram). A reuse status (reference, proposed, implemented, observed), not a diagram type. Pick the view, then state the status.
- *interaction diagram* → [E1 Sequence diagram](/types/e1-sequence-diagram). In UML the family name for sequence, communication, timing and interaction-overview diagrams; the sequence diagram is the usual pick.
- *layered diagram* → [C8 Layered architecture diagram](/types/c4-component-diagram#variant-c8), [A7 Conceptual architecture (solution overview)](/types/c5-logical-architecture#variant-a7), [I2 ArchiMate layered view](/types/i2-archimate-layered-view). Code layers with a dependency rule (C8), conceptual bands (A7) or ArchiMate business/application/technology layers (I2).
- *data map* → [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership), [D2 Data flow diagram (DFD)](/types/d2-data-flow-diagram). Where data comes from and who owns it (D3), or how it moves between processes (D2).
- *big picture / architecture overview / system overview* → [C2 System context diagram (C4 model level 1)](/types/c2-system-context), [C1 Application landscape](/types/c1-application-landscape), [A7 Conceptual architecture (solution overview)](/types/c5-logical-architecture#variant-a7). Start with C2 for one system, C1 for many applications, or A7 for a business-level solution overview.
- *database diagram / schema* → [D1 Entity-relationship diagram](/types/d1-entity-relationship). Choose the conceptual, logical or physical level before adding fields and keys.
- *AWS / Azure / GCP architecture diagram* → [G2 Cloud infrastructure architecture](/types/g1-deployment-diagram#variant-g2). Cloud service composition; use G1 when software placement is the real question.
- *Kubernetes diagram* → [G1 Deployment & cloud architecture](/types/g1-deployment-diagram). Start with workload placement; add G3 only when routing and network isolation matter.
- *microservices diagram* → [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram). Use C3 for running services and stores; E1 for one cross-service interaction.
- *workflow / user flow* → [E2 Activity diagram or flowchart](/types/e2-activity-flowchart), [E4 Swimlane or cross-functional flowchart](/types/e2-activity-flowchart#variant-e4), [A5 Business process diagram (BPMN)](/types/a5-bpmn-process), [A6 Customer or user journey map](/types/a6-journey-map). Ask whether this means logic, hand-offs, a formal business process, or the user's experience.
- *infrastructure diagram* → [G1 Deployment & cloud architecture](/types/g1-deployment-diagram), [G2 Cloud infrastructure architecture](/types/g1-deployment-diagram#variant-g2), [G3 Network topology and connectivity view](/types/g3-network-topology). Choose placement, cloud service composition or connectivity; they answer different questions.
- *tech stack diagram* → [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram), [G2 Cloud infrastructure architecture](/types/g1-deployment-diagram#variant-g2). Tie technologies to runnable responsibilities or cloud services, rather than drawing a logo list.
<!-- END GENERATED: terms -->

Other names that do map to a single type:

<!-- BEGIN GENERATED: aliases -->
- 4+1 architectural view model → [I1 4+1 view model](/types/i1-four-plus-one)
- ABAC policy model → [F3 Access-control model](/types/f3-access-control-model)
- activity diagram → [E2 Activity diagram or flowchart](/types/e2-activity-flowchart)
- actor–goal matrix → [A4 Business scenario matrix (role × activity)](/types/b2-user-story-map#variant-a4)
- actor–use-case diagram → [B1 Use case diagram](/types/b1-use-case-diagram)
- API landscape → [C6 Integration and interface diagram](/types/c6-integration-interface)
- Application Architecture (portfolio sense) → [C1 Application landscape](/types/c1-application-landscape)
- application communication diagram → [C1 Application landscape](/types/c1-application-landscape)
- Application Cooperation View → [C1 Application landscape](/types/c1-application-landscape)
- application interaction matrix → [C6 Integration and interface diagram](/types/c6-integration-interface)
- Application Landscape Map → [C1 Application landscape](/types/c1-application-landscape)
- application portfolio view → [C1 Application landscape](/types/c1-application-landscape)
- ArchiMate layered viewpoint → [I2 ArchiMate layered view](/types/i2-archimate-layered-view)
- architecture on a page → [A7 Conceptual architecture (solution overview)](/types/c5-logical-architecture#variant-a7)
- architecture roadmap → [A8 Target architecture and transition roadmap](/types/a8-target-roadmap)
- as-is / to-be roadmap → [A8 Target architecture and transition roadmap](/types/a8-target-roadmap)
- as-is to-be roadmap → [A8 Target architecture and transition roadmap](/types/a8-target-roadmap)
- authorization model → [F3 Access-control model](/types/f3-access-control-model)
- baseline / target / transition architecture → [A8 Target architecture and transition roadmap](/types/a8-target-roadmap)
- block diagram → [A7 Conceptual architecture (solution overview)](/types/c5-logical-architecture#variant-a7)
- BPMN collaboration diagram → [A5 Business process diagram (BPMN)](/types/a5-bpmn-process)
- BPMN diagram → [A5 Business process diagram (BPMN)](/types/a5-bpmn-process)
- BPMN process diagram → [A5 Business process diagram (BPMN)](/types/a5-bpmn-process)
- bubble chart → [D2 Data flow diagram (DFD)](/types/d2-data-flow-diagram)
- building block view (level 1) → [C5 Logical architecture diagram](/types/c5-logical-architecture)
- Building Block View Level 1 (arc42) → [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram)
- Building Block View Level 2 (arc42) → [C4 Component diagram (C4 model level 3)](/types/c4-component-diagram)
- business capability model → [A1 Business capability map](/types/a1-capability-map)
- business context → [A3 Business context diagram](/types/c2-system-context#variant-a3)
- business context (arc42 §3.1) → [A3 Business context diagram](/types/c2-system-context#variant-a3)
- business environment diagram → [A3 Business context diagram](/types/c2-system-context#variant-a3)
- business scenario map → [A4 Business scenario matrix (role × activity)](/types/b2-user-story-map#variant-a4)
- business-application-technology view → [I2 ArchiMate layered view](/types/i2-archimate-layered-view)
- C4 deployment diagram → [G1 Deployment & cloud architecture](/types/g1-deployment-diagram)
- C4 dynamic diagram → [E1 Sequence diagram](/types/e1-sequence-diagram)
- C4 dynamic diagram (sequence style) → [E1 Sequence diagram](/types/e1-sequence-diagram)
- C4 model Level 1 → [C2 System context diagram (C4 model level 1)](/types/c2-system-context)
- C4 model Level 2 → [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram)
- C4 model Level 3 → [C4 Component diagram (C4 model level 3)](/types/c4-component-diagram)
- call-flow diagram → [E1 Sequence diagram](/types/e1-sequence-diagram)
- capability heat map → [A1 Business capability map](/types/a1-capability-map)
- capability landscape → [A1 Business capability map](/types/a1-capability-map)
- capability map → [A1 Business capability map](/types/a1-capability-map)
- capability roadmap → [A8 Target architecture and transition roadmap](/types/a8-target-roadmap)
- CI/CD pipeline → [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline)
- CJM → [A6 Customer or user journey map](/types/a6-journey-map)
- clean architecture → [C8 Layered architecture diagram](/types/c4-component-diagram#variant-c8)
- clean architecture (variant) → [C8 Layered architecture diagram](/types/c4-component-diagram#variant-c8)
- cloud architecture diagram → [G2 Cloud infrastructure architecture](/types/g1-deployment-diagram#variant-g2)
- cloud reference architecture → [G2 Cloud infrastructure architecture](/types/g1-deployment-diagram#variant-g2)
- cloud solution architecture → [G2 Cloud infrastructure architecture](/types/g1-deployment-diagram#variant-g2)
- Cluster Map → [C1 Application landscape](/types/c1-application-landscape)
- component view → [C4 Component diagram (C4 model level 3)](/types/c4-component-diagram)
- conceptual data model → [D1 Entity-relationship diagram](/types/d1-entity-relationship)
- connectivity view → [G3 Network topology and connectivity view](/types/g3-network-topology)
- container view → [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram)
- context map → [C7 Bounded context map (DDD)](/types/c7-bounded-context-map)
- context-level DFD → [C2 System context diagram (C4 model level 1)](/types/c2-system-context)
- control flow diagram → [E2 Activity diagram or flowchart](/types/e2-activity-flowchart)
- control-flow diagram → [E2 Activity diagram or flowchart](/types/e2-activity-flowchart)
- cross-functional flowchart → [E4 Swimlane or cross-functional flowchart](/types/e2-activity-flowchart#variant-e4)
- cross-layer enterprise view → [I2 ArchiMate layered view](/types/i2-archimate-layered-view)
- crow's foot diagram → [D1 Entity-relationship diagram](/types/d1-entity-relationship)
- current-state map → [A9 Lean value-stream map (VSM)](/types/a2-value-stream#variant-a9)
- customer journey map → [A6 Customer or user journey map](/types/a6-journey-map)
- data asset map → [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership)
- data domain map → [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership)
- data flow chart → [D2 Data flow diagram (DFD)](/types/d2-data-flow-diagram)
- data flow model → [D2 Data flow diagram (DFD)](/types/d2-data-flow-diagram)
- data lineage diagram → [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership)
- data lineage graph → [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership)
- data model diagram → [D1 Entity-relationship diagram](/types/d1-entity-relationship)
- data ownership map → [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership)
- data provenance graph → [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership)
- data stewardship map → [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership)
- DDD context map → [C7 Bounded context map (DDD)](/types/c7-bounded-context-map)
- delegated access flow → [F1 Authentication and authorization flow](/types/e1-sequence-diagram#variant-f1)
- delegated API access flow → [F1 Authentication and authorization flow](/types/e1-sequence-diagram#variant-f1)
- deployment pipeline → [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline)
- deployment view → [G1 Deployment & cloud architecture](/types/g1-deployment-diagram)
- DFD → [D2 Data flow diagram (DFD)](/types/d2-data-flow-diagram)
- DFD with trust boundaries → [F2 Threat-model data-flow diagram with trust boundaries](/types/d2-data-flow-diagram#variant-f2)
- domain model (UML class style) → [D1 Entity-relationship diagram](/types/d1-entity-relationship)
- ER diagram → [D1 Entity-relationship diagram](/types/d1-entity-relationship)
- ERD → [D1 Entity-relationship diagram](/types/d1-entity-relationship)
- event topology → [C6 Integration and interface diagram](/types/c6-integration-interface)
- feature breakdown → [B3 Feature tree (functional decomposition)](/types/b3-feature-tree)
- finite-state machine (FSM) diagram → [E3 State machine diagram](/types/e3-state-machine)
- functional bands (Visio 2007) → [E4 Swimlane or cross-functional flowchart](/types/e2-activity-flowchart#variant-e4)
- functional decomposition → [B3 Feature tree (functional decomposition)](/types/b3-feature-tree)
- functional diagram → [A7 Conceptual architecture (solution overview)](/types/c5-logical-architecture#variant-a7)
- functional flowchart → [E4 Swimlane or cross-functional flowchart](/types/e2-activity-flowchart#variant-e4)
- functional view → [C5 Logical architecture diagram](/types/c5-logical-architecture)
- future-state map → [A9 Lean value-stream map (VSM)](/types/a2-value-stream#variant-a9)
- GitOps delivery view → [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline)
- GitOps flow → [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline)
- hexagonal architecture → [C8 Layered architecture diagram](/types/c4-component-diagram#variant-c8)
- hexagonal architecture (variant) → [C8 Layered architecture diagram](/types/c4-component-diagram#variant-c8)
- high-level architecture → [A7 Conceptual architecture (solution overview)](/types/c5-logical-architecture#variant-a7)
- High-level System Diagram → [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram)
- high-level technical architecture diagram → [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram)
- High-level Technical Architecture Diagram (loose) → [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram)
- hybrid connectivity diagram → [G3 Network topology and connectivity view](/types/g3-network-topology)
- identity flow → [F1 Authentication and authorization flow](/types/e1-sequence-diagram#variant-f1)
- in-scope out-of-scope diagram → [B4 Scope diagram](/types/c2-system-context#variant-b4)
- information model → [D1 Entity-relationship diagram](/types/d1-entity-relationship)
- integration architecture → [C6 Integration and interface diagram](/types/c6-integration-interface)
- integration diagram → [C6 Integration and interface diagram](/types/c6-integration-interface)
- integration landscape → [C6 Integration and interface diagram](/types/c6-integration-interface)
- interface catalog → [C6 Integration and interface diagram](/types/c6-integration-interface)
- interface map → [C6 Integration and interface diagram](/types/c6-integration-interface)
- internal structure diagram → [C4 Component diagram (C4 model level 3)](/types/c4-component-diagram)
- IT landscape → [C1 Application landscape](/types/c1-application-landscape)
- journey map → [A6 Customer or user journey map](/types/a6-journey-map)
- Kruchten 4+1 → [I1 4+1 view model](/types/i1-four-plus-one)
- ladder diagram → [E1 Sequence diagram](/types/e1-sequence-diagram)
- layer diagram → [C8 Layered architecture diagram](/types/c4-component-diagram#variant-c8)
- lean value stream mapping → [A9 Lean value-stream map (VSM)](/types/a2-value-stream#variant-a9)
- lifecycle diagram → [E3 State machine diagram](/types/e3-state-machine)
- lineage DAG → [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership)
- lineage graph → [D3 Data lineage and ownership map](/types/d3-data-lineage-ownership)
- logical application architecture → [C5 Logical architecture diagram](/types/c5-logical-architecture)
- logical building-block view → [C5 Logical architecture diagram](/types/c5-logical-architecture)
- logical data model → [D1 Entity-relationship diagram](/types/d1-entity-relationship)
- logical network diagram → [G3 Network topology and connectivity view](/types/g3-network-topology)
- logical view → [C5 Logical architecture diagram](/types/c5-logical-architecture)
- material and information flow diagram → [A9 Lean value-stream map (VSM)](/types/a2-value-stream#variant-a9)
- message sequence chart → [E1 Sequence diagram](/types/e1-sequence-diagram)
- migration roadmap → [A8 Target architecture and transition roadmap](/types/a8-target-roadmap)
- migration view → [A8 Target architecture and transition roadmap](/types/a8-target-roadmap)
- monitoring architecture diagram → [H2 Observability view](/types/h2-observability-view)
- MSC → [E1 Sequence diagram](/types/e1-sequence-diagram)
- n-layer architecture → [C8 Layered architecture diagram](/types/c4-component-diagram#variant-c8)
- network diagram → [G3 Network topology and connectivity view](/types/g3-network-topology)
- network topology diagram → [G3 Network topology and connectivity view](/types/g3-network-topology)
- OAuth flow → [F1 Authentication and authorization flow](/types/e1-sequence-diagram#variant-f1)
- observability architecture diagram → [H2 Observability view](/types/h2-observability-view)
- OIDC flow → [F1 Authentication and authorization flow](/types/e1-sequence-diagram#variant-f1)
- onion architecture → [C8 Layered architecture diagram](/types/c4-component-diagram#variant-c8)
- onion architecture (variant) → [C8 Layered architecture diagram](/types/c4-component-diagram#variant-c8)
- permission model → [F3 Access-control model](/types/f3-access-control-model)
- physical network diagram → [G3 Network topology and connectivity view](/types/g3-network-topology)
- plateau diagram → [A8 Target architecture and transition roadmap](/types/a8-target-roadmap)
- ports and adapters (variant) → [C8 Layered architecture diagram](/types/c4-component-diagram#variant-c8)
- power-interest grid → [H3 Stakeholder map (power-interest grid)](/types/h3-stakeholder-map)
- presentation-domain-data layering → [C8 Layered architecture diagram](/types/c4-component-diagram#variant-c8)
- process flow diagram → [A5 Business process diagram (BPMN)](/types/a5-bpmn-process)
- process flow diagram (informal) → [E2 Activity diagram or flowchart](/types/e2-activity-flowchart)
- process map → [A5 Business process diagram (BPMN)](/types/a5-bpmn-process)
- process model (structured analysis) → [D2 Data flow diagram (DFD)](/types/d2-data-flow-diagram)
- program flowchart → [E2 Activity diagram or flowchart](/types/e2-activity-flowchart)
- provider infrastructure view → [G2 Cloud infrastructure architecture](/types/g1-deployment-diagram#variant-g2)
- provider-specific infrastructure view → [G2 Cloud infrastructure architecture](/types/g1-deployment-diagram#variant-g2)
- RACI chart → [H1 RACI matrix](/types/h1-raci-matrix)
- RASCI matrix → [H1 RACI matrix](/types/h1-raci-matrix)
- RBAC model → [F3 Access-control model](/types/f3-access-control-model)
- ReBAC graph → [F3 Access-control model](/types/f3-access-control-model)
- relationship-based authorization graph → [F3 Access-control model](/types/f3-access-control-model)
- release pipeline → [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline)
- requirements breakdown structure → [B3 Feature tree (functional decomposition)](/types/b3-feature-tree)
- responsibility assignment matrix → [H1 RACI matrix](/types/h1-raci-matrix)
- role-activity matrix → [A4 Business scenario matrix (role × activity)](/types/b2-user-story-map#variant-a4)
- role-permission matrix → [F3 Access-control model](/types/f3-access-control-model)
- role–activity scope matrix → [A4 Business scenario matrix (role × activity)](/types/b2-user-story-map#variant-a4)
- routing view → [G3 Network topology and connectivity view](/types/g3-network-topology)
- Rummler-Brache diagram → [E4 Swimlane or cross-functional flowchart](/types/e2-activity-flowchart#variant-e4)
- runtime building-block view → [C3 Container diagram (C4 model level 2)](/types/c3-container-diagram)
- runtime infrastructure view → [G1 Deployment & cloud architecture](/types/g1-deployment-diagram)
- runtime view → [E1 Sequence diagram](/types/e1-sequence-diagram)
- runtime-view scenario → [E1 Sequence diagram](/types/e1-sequence-diagram)
- scenario coverage matrix → [A4 Business scenario matrix (role × activity)](/types/b2-user-story-map#variant-a4)
- scope and context diagram → [B4 Scope diagram](/types/c2-system-context#variant-b4)
- scope boundary map → [B4 Scope diagram](/types/c2-system-context#variant-b4)
- security data-flow diagram → [F2 Threat-model data-flow diagram with trust boundaries](/types/d2-data-flow-diagram#variant-f2)
- sign-in flow → [F1 Authentication and authorization flow](/types/e1-sequence-diagram#variant-f1)
- software delivery pipeline → [G4 CI/CD and deployment pipeline](/types/g4-delivery-pipeline)
- software-to-infrastructure mapping → [G1 Deployment & cloud architecture](/types/g1-deployment-diagram)
- solution concept diagram → [A7 Conceptual architecture (solution overview)](/types/c5-logical-architecture#variant-a7)
- solution overview → [A7 Conceptual architecture (solution overview)](/types/c5-logical-architecture#variant-a7)
- SSO flow → [F1 Authentication and authorization flow](/types/e1-sequence-diagram#variant-f1)
- stakeholder grid → [H3 Stakeholder map (power-interest grid)](/types/h3-stakeholder-map)
- stakeholder matrix → [H3 Stakeholder map (power-interest grid)](/types/h3-stakeholder-map)
- state diagram → [E3 State machine diagram](/types/e3-state-machine)
- state transition diagram → [E3 State machine diagram](/types/e3-state-machine)
- state-transition diagram → [E3 State machine diagram](/types/e3-state-machine)
- statechart → [E3 State machine diagram](/types/e3-state-machine)
- statechart diagram → [E3 State machine diagram](/types/e3-state-machine)
- story map → [B2 User story map](/types/b2-user-story-map)
- story mapping → [B2 User story map](/types/b2-user-story-map)
- strategic design map → [C7 Bounded context map (DDD)](/types/c7-bounded-context-map)
- STRIDE diagram → [F2 Threat-model data-flow diagram with trust boundaries](/types/d2-data-flow-diagram#variant-f2)
- Structured-analysis Context Diagram → [C2 System context diagram (C4 model level 1)](/types/c2-system-context)
- swim-lane flowchart → [E4 Swimlane or cross-functional flowchart](/types/e2-activity-flowchart#variant-e4)
- swimlane flowchart → [E4 Swimlane or cross-functional flowchart](/types/e2-activity-flowchart#variant-e4)
- swimlane process diagram → [A5 Business process diagram (BPMN)](/types/a5-bpmn-process)
- system context diagram → [C2 System context diagram (C4 model level 1)](/types/c2-system-context)
- system environment diagram → [C2 System context diagram (C4 model level 1)](/types/c2-system-context)
- system landscape diagram → [C1 Application landscape](/types/c1-application-landscape)
- System Landscape Diagram (C4 model) → [C1 Application landscape](/types/c1-application-landscape)
- team map (organisational variant) → [C7 Bounded context map (DDD)](/types/c7-bounded-context-map)
- technology-neutral component diagram → [C5 Logical architecture diagram](/types/c5-logical-architecture)
- telemetry pipeline diagram → [H2 Observability view](/types/h2-observability-view)
- threat-model DFD → [F2 Threat-model data-flow diagram with trust boundaries](/types/d2-data-flow-diagram#variant-f2)
- transition architecture → [A8 Target architecture and transition roadmap](/types/a8-target-roadmap)
- trust boundary diagram → [F2 Threat-model data-flow diagram with trust boundaries](/types/d2-data-flow-diagram#variant-f2)
- trust-boundary diagram → [F2 Threat-model data-flow diagram with trust boundaries](/types/d2-data-flow-diagram#variant-f2)
- UML activity diagram → [E2 Activity diagram or flowchart](/types/e2-activity-flowchart)
- UML sequence diagram → [E1 Sequence diagram](/types/e1-sequence-diagram)
- UML use case diagram → [B1 Use case diagram](/types/b1-use-case-diagram)
- user journey map → [A6 Customer or user journey map](/types/a6-journey-map)
- UX journey map → [A6 Customer or user journey map](/types/a6-journey-map)
- value stream → [A2 Value stream (business architecture)](/types/a2-value-stream)
- value stream / capability cross-map → [A2 Value stream (business architecture)](/types/a2-value-stream)
- value stream capability cross-map → [A2 Value stream (business architecture)](/types/a2-value-stream)
- value stream diagram → [A2 Value stream (business architecture)](/types/a2-value-stream)
- value stream map (TOGAF artifact) → [A2 Value stream (business architecture)](/types/a2-value-stream)
- value stream stages → [A2 Value stream (business architecture)](/types/a2-value-stream)
- VPC or VNet topology → [G3 Network topology and connectivity view](/types/g3-network-topology)
- VPC topology → [G3 Network topology and connectivity view](/types/g3-network-topology)
- VSM → [A9 Lean value-stream map (VSM)](/types/a2-value-stream#variant-a9)
- white-box view of a container → [C4 Component diagram (C4 model level 3)](/types/c4-component-diagram)
- workflow diagram (informal) → [E2 Activity diagram or flowchart](/types/e2-activity-flowchart)
<!-- END GENERATED: aliases -->

## All types

<!-- BEGIN GENERATED: catalogue -->
| Code | Type | Answers |
|---|---|---|
| [A1](/types/a1-capability-map) | Business capability map | What can the organisation do, independent of who or what does it, and where should it invest? |
| [A2](/types/a2-value-stream) | Value stream (business architecture) | Which stages does a stakeholder pass through, from trigger to delivered value, and which capabilities enable each stage? |
| [A5](/types/a5-bpmn-process) | Business process diagram (BPMN) | How does a business case run from start to end, who does each step, where does it branch, and what passes between participants? |
| [A6](/types/a6-journey-map) | Customer or user journey map | For one persona in one scenario, which stages do they go through, what do they do, think and feel, and where are the opportunities? |
| [A8](/types/a8-target-roadmap) | Target architecture and transition roadmap | What does it look like today, where is it going, which coherent transition states lead there, and what value does each state deliver? |
| [B2](/types/b2-user-story-map) | User story map | What does the user do end to end, what is the smallest useful first release, and how are later releases sliced? |
| [C1](/types/c1-application-landscape) | Application landscape | Which applications exist in the estate, who owns them, what state are they in, and how do they depend on each other? |
| [C2](/types/c2-system-context) | System context diagram (C4 model level 1) | What is the software system, who uses it, and which other systems does it depend on? |
| [C3](/types/c3-container-diagram) | Container diagram (C4 model level 2) | Which separately running applications and data stores make up the system, what technology does each use, and how do they communicate? |
| [C4](/types/c4-component-diagram) | Component diagram (C4 model level 3) | Inside one container, which components exist, what is each responsible for, and which calls which? |
| [C5](/types/c5-logical-architecture) | Logical architecture diagram | Seen by responsibility and without technology choices, which modules and interfaces must the system have? |
| [C6](/types/c6-integration-interface) | Integration and interface diagram | Which interfaces connect the systems, in which integration style and direction, with which protocol, authentication and failure semantics? |
| [C7](/types/c7-bounded-context-map) | Bounded context map (DDD) | Which model boundaries exist in the domain, and which relationship patterns connect them? |
| [D1](/types/d1-entity-relationship) | Entity-relationship diagram | Which business objects does the system manage, and how are they related, with which cardinalities? |
| [D2](/types/d2-data-flow-diagram) | Data flow diagram (DFD) | Where does data come from, which processes transform it, where is it stored, and where does it go? |
| [D3](/types/d3-data-lineage-ownership) | Data lineage and ownership map | Where did a dataset or result come from, what derives from it, and who is accountable for it? |
| [E1](/types/e1-sequence-diagram) | Sequence diagram | For one scenario, in what order do the participants exchange which messages? |
| [E2](/types/e2-activity-flowchart) | Activity diagram or flowchart | Which steps, decisions and parallel branches make up one piece of logic? |
| [E3](/types/e3-state-machine) | State machine diagram | Which states can one object be in, which events move it between them, and which transitions are not allowed? |
| [F3](/types/f3-access-control-model) | Access-control model | Under which rules can a subject perform an action on a resource, in which scope? |
| [G1](/types/g1-deployment-diagram) | Deployment & cloud architecture | Where do the software instances run, in which environment, and how does their placement support operational needs? |
| [G3](/types/g3-network-topology) | Network topology and connectivity view | What can communicate with what, through which paths and controls, in normal and failure conditions? |
| [G4](/types/g4-delivery-pipeline) | CI/CD and deployment pipeline | How does a change become a trusted release, which evidence allows each promotion, and what happens when it fails? |
| [H1](/types/h1-raci-matrix) | RACI matrix | For each activity or decision, who is Responsible, Accountable, Consulted and Informed? |
| [H2](/types/h2-observability-view) | Observability view | Which evidence shows how the service behaves for users, how does it reach analysis and alerting, and how does a finding reach someone who can act? |

### Named variants and method references

- [A3 Business context diagram](/types/c2-system-context#variant-a3) · variant
- [A4 Business scenario matrix (role × activity)](/types/b2-user-story-map#variant-a4) · variant
- [A7 Conceptual architecture (solution overview)](/types/c5-logical-architecture#variant-a7) · variant
- [A9 Lean value-stream map (VSM)](/types/a2-value-stream#variant-a9) · variant
- [B1 Use case diagram](/types/b1-use-case-diagram) · reference
- [B3 Feature tree (functional decomposition)](/types/b3-feature-tree) · reference
- [B4 Scope diagram](/types/c2-system-context#variant-b4) · variant
- [C8 Layered architecture diagram](/types/c4-component-diagram#variant-c8) · variant
- [E4 Swimlane or cross-functional flowchart](/types/e2-activity-flowchart#variant-e4) · variant
- [F1 Authentication and authorization flow](/types/e1-sequence-diagram#variant-f1) · variant
- [F2 Threat-model data-flow diagram with trust boundaries](/types/d2-data-flow-diagram#variant-f2) · variant
- [G2 Cloud infrastructure architecture](/types/g1-deployment-diagram#variant-g2) · variant
- [H3 Stakeholder map (power-interest grid)](/types/h3-stakeholder-map) · reference
- [I1 4+1 view model](/types/i1-four-plus-one) · reference
- [I2 ArchiMate layered view](/types/i2-archimate-layered-view) · reference
<!-- END GENERATED: catalogue -->
