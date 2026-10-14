# Deployment Diagram (部署图)
<!-- Generated from content/en/types/G1-deployment-diagram.md by tools/build_skill_refs.py. Do not edit. -->
> Where do the software instances and artifacts run, and how does that placement support operational needs such as capacity, failover and ownership?
Scope: One named environment (for example production), showing hosting nodes and the software instances placed on them Neighbours: C3, C8, G2, G3, G4, H2, I1.

## Meaning
- **Question:** where does each piece of software run, and what does that placement imply for scaling, failure, ownership and location?
- **Viewpoint:** a deployment or operations view in the sense of an architecture description (ISO/IEC/IEEE 42010 public scope only). UML 2.5.1 defines the formal elements (nodes, devices, execution environments, artifacts, deployment relationships). The C4 model offers a pragmatic variant that maps *instances* of software systems and containers to deployment nodes in one environment; it is a supporting diagram, not a fifth zoom level. arc42 keeps deployment (section 7) apart from runtime behaviour (section 6).
- **Deeper meaning:** it is an allocation view. Logical responsibilities from the static model are realised on execution infrastructure, and the placement carries consequences. A C4 "container" is a deployable software building block; a Docker container is only one way to run it.
- **Leaves out:** method calls, source files, business journeys, full network rule sets (G3) and cloud service trade-offs (G2).
- **Definition used here:** a *deployment node* is anything that hosts software: a device, VM, managed platform or nested execution environment. It is not necessarily a physical server. "Deployment" is allocation, not behaviour over time.

## When to use and how to choose
- **Audience:** developers, platform engineers, operators, architects, security reviewers.
- **Scenarios:** deployment readiness review of production; translating logical services onto a managed container platform; finding a shared failure domain (two "replicas" on one host or disk); planning replicas and failover for the order database; placing an edge cache or in-store device next to cloud services.
- **When not to use:** to explain a customer journey (E1 or an A-family view); to claim disaster recovery without evidence of replication and recovery behaviour.
- **vs neighbours:**
  - **C3** for the logical containers; G1 adds where they run.
  - **G2** for which cloud services and trade-offs fit.
  - **G3** for routing, segmentation, reachability.
  - **G4** for how a change reaches this environment.
  - **E1** (or arc42 runtime view) for behaviour over time.
  - Choose **C8** when the layers are code layers with dependency rules; deployment tiers are not code layers.
  - Choose **H2** when the question is how the running system is observed and who is alerted, not where it runs.
  - Choose **I1** when this deployment view is the physical view of a 4+1 description and must stay consistent with the other views.

## Notation and elements
- **Formal or informal:** UML 2.5.1 is formal; most practical diagrams are a convention. Do not decorate arbitrary boxes with UML stereotypes and imply conformance.
- **Required:**
  - Environment name and scope, plus current or proposed status.
  - Hosting nodes and, nested inside them, software instances or artifacts.
  - Clear containment (hosting) as distinct from dependency or communication.
  - Material communication paths and a legend.
- **UML option:** nodes may be specialised as devices or execution environments; artifacts are deployable information that can manifest software elements. A communication path between nodes is not a method call or a timed message.
- **C4 option:** separate deployment nodes, infrastructure nodes (load balancer, DNS, firewall) and software or container instances; nested nodes express hosting; name instances consistently with the logical model.
- **Optional when relevant:** replica count or autoscaling range, zone or region boundaries, protocols, resource limits, image version or digest, health checks, replication and failover arrows.
- **Caution:** a fixed replica count is not mandatory for managed or serverless platforms, and "two replicas" must not imply two zones without placement evidence.
- **Text budget:** node name plus technology (about 2–4 words); an instance is a short role name; ports only where operationally important.

## Best practices and anti-patterns
### Best practices
1. **Start from the logical model** and map its units explicitly onto infrastructure; a set of cloud icons without software allocation is not a deployment view.
2. **Say what the numbers are:** declared definition, desired count, observed instances or illustrative capacity. Add a ref and date and do not call a declaration "live."
3. **Use hierarchy** for complex estates and put rationale in adjacent text, not paragraphs inside nodes.
4. **Constrain instance links.** With several instances of one service, connect only the pairs that really talk; avoid all-to-all lines.
5. **Show failure domains from placement evidence** (zones, hosts, shared storage), not from repeated boxes.

### Anti-patterns
1. **Cloud icons with no software on them.**
2. **Duplicated boxes read as resilience** while storage, control plane or scheduling is a single point.
3. **Invented connections** between every instance of a service.
4. **Mixing environments** (dev, staging and production) in one picture without a clear key.
5. **Always drawing disaster recovery.** Include it only when the review needs it; otherwise link a separate view and state the scope.

## Drawing recipe
1. Pick one environment and an evidence reference (commit or date); put both in the title, for example "Online shop: production, declared at ref X".
2. List the runnable units (storefront, order service, chatbot, database, queue) and the hosting declarations; separate infrastructure from software.
3. Layout: nested containers, outermost region or site, then zone or cluster, then host or platform, then instances. Peer hosts sit side by side; keep communication paths short and local.
4. Hosting is shown by nesting only. Draw arrows for communication, labelled with protocol where it matters; use a different line style for replication or failover.
5. Add counts, ranges and zones only when evidenced; otherwise label them "illustrative" or leave them out.
6. Text: 2–4 words per node and instance; a key for line styles and for declared versus observed.
7. Colour: neutral fills, one accent for the software layer, and a distinct style for external or managed nodes. Do not use colour as the only cue.

**Self-check**
- [ ] Environment and current or proposed status are in the title.
- [ ] Every software unit sits inside a hosting node; unmapped or external units are explained.
- [ ] Hosting (nesting) and communication (arrows) are visually distinct.
- [ ] Counts are evidenced, shown as ranges, or marked illustrative.
- [ ] Zones and failure domains follow placement evidence.
- [ ] Repeated instances have no invented all-to-all connections.
- [ ] Ports and protocols appear only where they matter.
- [ ] Declared infrastructure is not presented as an observed deployment.

## Evidence in a code repository
- **Runnable units:** Dockerfiles, Compose files, Kubernetes Deployments, StatefulSets and Services, Helm or Kustomize values, process-manager units, launch scripts.
- **Infrastructure:** Terraform, CloudFormation or CDK resources, autoscaling and placement rules, and per-environment variable files.
- **Rules:** a directory is not a deployable unit and an imported SDK is not a deployed service.
- **Must come from people or the platform:** actual cloud settings, externally managed resources, real replica counts and zone placement.
- Never run an infrastructure apply or read secret-bearing state just to draw; label the result "declared".

## Guided-mode questions
1. Which environment or variant should be shown? (production)
2. Which software units and ownership boundaries matter? (the shop's own services; managed services as external nodes)
3. Are counts and placement current observations, declarations or targets? (declarations, with the ref shown)
4. Is the concern deployment, capacity, failover or operational handover? (deployment and failover)
5. Include disaster recovery here or in a separate view? (separate view, linked)

## Template
Model template: `assets/templates/G1.json` · Layout template: `statechart` · hosting segments become `boundary` groups (cluster, public and application subnets, managed data services), software instances become `component` nodes (the focus one with style `highlight`) and data services `store` nodes inside them, external nodes use the `external` style, chips carry the protocol or replica count, and communication becomes `call` or `data` edges; `evidence.status` records declared (`doc-only`) versus observed (`verified`).

## Sample
Figure: `samples/G1-deployment-diagram.svg` (published with the site)
