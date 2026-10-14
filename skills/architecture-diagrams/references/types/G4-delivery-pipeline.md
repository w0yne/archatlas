# CI/CD and Deployment Pipeline (CI/CD 流水线图)
<!-- Generated from content/en/types/G4-delivery-pipeline.md by tools/build_skill_refs.py. Do not edit. -->
> How does a change become a trusted release, which evidence allows each promotion, and what happens when something fails?
Scope: One release path from change source to target environments, with artifacts, gates, outcomes and, where relevant, the controller that reconciles desired state Neighbours: A9, G1, G2, H2.

## Meaning
- **Question:** how does a change become a trusted release, which evidence permits each promotion, and what happens on failure?
- **Viewpoint:** delivery, operations and governance. Stages increase confidence step by step, and artifact identity, gates and authority matter more than tool logos. Declare whether the drawing is a process view, a dependency graph or a release-state view.
- **Deeper meaning:** a pipeline stage is not necessarily an environment or an application component; some stages run in parallel and some deployment controllers reconcile independently of the pipeline. A GitOps controller pulls desired state from a repository, so CI may never deploy anything itself.
- **Leaves out:** individual shell commands, every unit test, and application internals.
- **Definition used here:** *continuous delivery* means a change is always in a releasable state and release is a business decision; *continuous deployment* automatically releases every qualifying change to production. They are not synonyms; deployment requires delivery first. SLSA v1.2 defines Build and Source tracks for assessing supply-chain security and is not a drawing notation; a "sign" box on a pipeline does not earn a SLSA level.

## When to use and how to choose
- **Audience:** developers, release and platform engineers, operators, reviewers, change-control owners.
- **Scenarios:** the build-and-release path of the storefront and order service; finding why feedback or approval is slow; promoting one tested image from staging to production; progressive delivery and recovery for a risky release; a GitOps flow where a controller applies manifests.
- **When not to use:** presenting a simple build workflow as the full delivery system when deployment, authorisation or verification happen elsewhere.
- **vs neighbours:**
  - **G1** for where the result runs.
  - **E3** for release states and transitions.
  - **H1** for who is accountable for each step.
  - If build identities and attestations dominate, use a separate supply-chain trust view.
  - Choose **A9** when the question is where time is lost in the flow from request to production (lead time, waiting time).
  - Choose **G2** for the cloud services and failure boundaries the pipeline deploys into.
  - Choose **H2** for the signals that verify a release after deployment and trigger recovery.

## Notation and elements
- **Formal or informal:** informal process or dependency-graph convention. A vendor's pipeline UI has its own model; do not present it as universal.
- **Required for a release-path view:**
  - Trigger or change source.
  - Stages and actions with their dependencies.
  - Artifact identity and where it is stored.
  - Automated and manual gates, and target environments.
  - Success, failure and stop outcomes; verification and recovery responsibility.
- **Edge meanings:** label each edge as *trigger*, *depends on*, *produces or consumes artifact*, *promotes digest* or *deploys or reconciles*. Do not use one arrow for both order and artifact flow.
- **Lanes:** separate actors or controllers (CI system, registry, approver, GitOps controller) when responsibility matters.
- **Branches:** fan-out and fan-in need declared conditions; do not imply that every branch always runs.
- **Optional:** provenance or signature verification, scans, approver identity, concurrency control, traffic percentages, feature flags, roll-forward or rollback, database compatibility, drift reconciliation. Keep timings and percentages illustrative unless evidenced.
- **Text budget:** stage or action name (2–4 words); artifact label short (name plus digest or tag).

## Best practices and anti-patterns
### Best practices
1. **Put fast confidence-building checks early** and slower ones later or in parallel; that is the pipeline's rationale, not a fixed list of products.
2. **Promote the tested immutable artifact,** with its identity or digest visible. Configuration can vary per environment; a platform-specific build is a different tested artifact, not "build once" in disguise.
3. **Separate human approval, automated policy checks and deployment health.** An environment name in a workflow file does not prove reviewers are required; protection rules are a property of the environment, configured separately.
4. **Model recovery honestly.** A failure before deployment stops promotion; after rollout, recovery may be rollback, roll-forward, traffic switch or restore. "Always roll back" is unsafe for irreversible data changes.
5. **For GitOps, draw the repository update and the controller's reconciliation,** not a direct CI-to-cluster arrow.

### Anti-patterns
1. **A linear row of boxes** that hides dependencies, artifacts and parallel branches.
2. **Generating an attestation drawn as trust:** an attestation that nobody verifies downstream assures nothing.
3. **Gates drawn from tool names:** "production" implies an approval that may not exist.
4. **Rollback as the only failure path.**
5. **One arrow for everything:** trigger, dependency and artifact flow mixed.

## Drawing recipe
1. Choose one change path and its trigger; state in the title whether it is current or proposed, for example "Online shop order service: current release path".
2. Trace job dependencies and actual artifact production and consumption; read what each job needs, not what the tool is called.
3. Mark target environments, approvers or controllers, and the gaps that live outside the repository (branch protection, environment reviewers).
4. Layout: left to right as a dependency graph; stages as columns, parallel jobs stacked, a separate lane per controller when responsibility matters. Artifact store and registry sit below the main row.
5. Edges: solid for dependency and trigger, a distinct style for artifact flow, a third for deploy or reconcile. Label branch conditions.
6. Show stop behaviour at each gate, and a separate, labelled post-deployment recovery path.
7. Text: 2–4 words per stage; artifact label with tag or digest. Colour: neutral for automated stages, one accent for manual gates, a distinct style for unverified or unknown gates. Do not rely on colour alone.

**Self-check**
- [ ] Continuous integration, continuous delivery and automatic deployment are distinguished.
- [ ] Triggers, dependencies and artifact flow use separately labelled edges.
- [ ] The tested artifact's identity is visible through promotion.
- [ ] Each manual or automatic gate has evidence, or is marked unknown.
- [ ] Parallel branches and joins state their conditions.
- [ ] Failure before deployment stops promotion; the stop is shown.
- [ ] Post-deployment recovery respects data and state constraints.
- [ ] GitOps reconciliation or external release machinery is not omitted.
- [ ] No assurance level is implied by the drawing alone.

## Evidence in a code repository
- **Pipeline definitions:** workflow files for the CI system, reusable workflows, job dependency (`needs`) and conditions, artifact upload and download.
- **Release path:** registry references and digests, deploy commands and manifests, GitOps application and controller settings, migrations, health gates, recovery scripts.
- **Limits:** declaring `environment: production` is not proof of approval; branch protection, environment reviewers, runner isolation and cloud permissions often live outside the repository.
- **Must come from people:** who approves, which policies are enforced, recovery practice.
- Do not run a pipeline to discover its architecture.

## Guided-mode questions
1. Is the scope CI only, release on demand, or automatic production deployment? (release on demand)
2. Which change source and artifact should be traced? (the order service container image)
3. Which approvals and environment policies exist outside the workflow files? (ask; mark unknown until confirmed)
4. Push-based deployment or a controller reconciling desired state? (as found in the repository)
5. How are failed rollouts and incompatible data migrations handled? (show roll-forward and restore separately)

## Template
Model template: `assets/templates/G4.json` · Layout template: `tree` · the trigger is an `event` node, stages and jobs are `task` nodes laid out left to right along `dependency` edges, artifacts and registries are `store` nodes reached by `data` edges, deploy or reconcile steps use `call` edges, controllers or approvers become `lane` groups; gate status is shown with node `style` (`planned` for not yet passed) or `tags`.

## Sample
Figure: `samples/G4-delivery-pipeline.svg` (published with the site)
