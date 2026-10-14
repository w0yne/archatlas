---
code: G4
slug: delivery-pipeline
family: G
names:
  en: CI/CD and Deployment Pipeline
  zh: CI/CD 流水线图
  aliases:
    en: [CI/CD pipeline, deployment pipeline, software delivery pipeline, release pipeline, GitOps delivery view]
    zh: [部署流水线图, 软件交付管道图, 发布流水线图, 持续交付流水线]
question: "How does a change become a trusted release, which evidence allows each promotion, and what happens when something fails?"
audiences: [developers, release and platform engineers, operators, quality and security reviewers, change-control owners]
level: logical
phases: [design, delivery, review]
scope: "One release path from change source to target environments, with artifacts, gates, outcomes and, where relevant, the controller that reconciles desired state"
formal:
  kind: convention
  ref: "No graphical standard. Fowler's deployment-pipeline description and Humble and Farley's Continuous Delivery are the practice references; UML activity or BPMN may be used if their semantics are respected; SLSA supplies supply-chain assurance concepts, not notation"
neighbours: [G1, E3, H1]
status: draft
---

# CI/CD and Deployment Pipeline (CI/CD 流水线图)

> A picture of the path a change takes to production: stages, artifacts, gates, and what stops or recovers when a check fails.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
- **Question:** how does a change become a trusted release, which evidence permits each promotion, and what happens on failure?
- **Viewpoint:** delivery, operations and governance. Stages increase confidence step by step, and artifact identity, gates and authority matter more than tool logos [1]. Declare whether the drawing is a process view, a dependency graph or a release-state view.
- **Deeper meaning:** a pipeline stage is not necessarily an environment or an application component; some stages run in parallel and some deployment controllers reconcile independently of the pipeline. A GitOps controller pulls desired state from a repository, so CI may never deploy anything itself [7].
- **Leaves out:** individual shell commands, every unit test, and application internals.
- **Definition used here:** *continuous delivery* means a change is always in a releasable state and release is a business decision; *continuous deployment* automatically releases every qualifying change to production. They are not synonyms; deployment requires delivery first [1][2]. SLSA v1.2 defines Build and Source tracks for assessing supply-chain security and is not a drawing notation; a "sign" box on a pipeline does not earn a SLSA level [3].

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** developers, release and platform engineers, operators, reviewers and change-control owners.
- **Classic scenarios:**
  1. Explaining the build-and-release path for the shop's storefront and order service.
  2. Finding why feedback or approval is slow.
  3. Promoting one tested container image from staging to production.
  4. Progressive delivery and recovery for a risky release.
  5. A GitOps flow where a controller applies manifests to the cluster.
- **When not to use:** to present a simple build workflow as a full delivery system when deployment, authorisation or verification happen elsewhere.
- **vs neighbours:**
  - Choose **G1** for where the result runs.
  - Choose **E3** for release states and their transitions.
  - Choose **H1** when the question is who is accountable for each step.
  - If build identities and attestations dominate, a separate supply-chain trust view is more suitable than a job diagram.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Formal or informal:** informal process or dependency-graph convention. A vendor's pipeline UI has its own model [5][6]; do not present it as universal.
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

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices
1. **Put fast confidence-building checks early** and slower ones later or in parallel; that is the pipeline's rationale, not a fixed list of products [1].
2. **Promote the tested immutable artifact,** with its identity or digest visible. Configuration can vary per environment; a platform-specific build is a different tested artifact, not "build once" in disguise.
3. **Separate human approval, automated policy checks and deployment health.** An environment name in a workflow file does not prove reviewers are required; protection rules are a property of the environment, configured separately [4].
4. **Model recovery honestly.** A failure before deployment stops promotion; after rollout, recovery may be rollback, roll-forward, traffic switch or restore. "Always roll back" is unsafe for irreversible data changes.
5. **For GitOps, draw the repository update and the controller's reconciliation,** not a direct CI-to-cluster arrow [7].

### Anti-patterns
1. **A linear row of boxes** that hides dependencies, artifacts and parallel branches.
2. **Generating an attestation drawn as trust:** an attestation that nobody verifies downstream assures nothing [3].
3. **Gates drawn from tool names:** "production" implies an approval that may not exist.
4. **Rollback as the only failure path.**
5. **One arrow for everything:** trigger, dependency and artifact flow mixed.

## Exemplars {#exemplars}
<!-- skill: omit -->
- [AWS CodePipeline: pipeline structure reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html) — stage and action diagrams with serial and parallel actions and an explicit manual approval; a product model, not a universal notation.
- [Google Cloud: CI/CD for containerised apps](https://docs.cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke) — separates build, registry, staging promotion and production approval.
- [Google Cloud: Modern CI/CD with GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-reference-architecture) — distinguishes infrastructure and application delivery and contrasts a demo with an isolated multi-project variant.
- [Argo CD: architectural overview](https://argo-cd.readthedocs.io/en/stable/operator-manual/architecture/) — the deployment-side complement: repository state and a reconciliation controller explain pull-based delivery.
- Vendor material: link only, and check each page's licence before adapting graphics. A reference may contain learning shortcuts unsuitable for production.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
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

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **Pipeline definitions:** workflow files for the CI system, reusable workflows, job dependency (`needs`) and conditions, artifact upload and download.
- **Release path:** registry references and digests, deploy commands and manifests, GitOps application and controller settings, migrations, health gates, recovery scripts.
- **Limits:** declaring `environment: production` is not proof of approval; branch protection, environment reviewers, runner isolation and cloud permissions often live outside the repository.
- **Must come from people:** who approves, which policies are enforced, recovery practice.
- Do not run a pipeline to discover its architecture.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Is the scope CI only, release on demand, or automatic production deployment? (release on demand)
2. Which change source and artifact should be traced? (the order service container image)
3. Which approvals and environment policies exist outside the workflow files? (ask; mark unknown until confirmed)
4. Push-based deployment or a controller reconciling desired state? (as found in the repository)
5. How are failed rollouts and incompatible data migrations handled? (show roll-forward and restore separately)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/G4.json` · Layout template: `tree` · the trigger is the root, stages and jobs are nodes laid out left to right along `dependency` edges, artifacts and registries use `data` edges, deploy or reconcile steps use `call` edges, and controllers or approvers become `lane` groups; gate status maps to node `evidence`.

## Sources {#sources}
<!-- skill: omit -->
1. M. Fowler, "Deployment Pipeline" (30 May 2013) — https://www.martinfowler.com/bliki/DeploymentPipeline.html — accessed 2026-10-14
2. M. Fowler, "Continuous Delivery" (discusses Humble and Farley, 2010; checked 2026-10-14 for the delivery versus deployment distinction) — https://martinfowler.com/bliki/ContinuousDelivery.html — accessed 2026-10-14
3. OpenSSF, "SLSA specification v1.2" and "Build: Provenance" — https://slsa.dev/spec/v1.2/ ; https://slsa.dev/spec/v1.2/build-provenance — accessed 2026-10-14
4. GitHub Docs, "Deployments and environments" — https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments — accessed 2026-10-14
5. AWS, "CodePipeline concepts" and "Pipeline structure reference" — https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html ; https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html — accessed 2026-10-14
6. Google Cloud, "CI/CD pipeline for developing and delivering containerized apps" — https://docs.cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke — accessed 2026-10-14
7. Argo CD, "Architectural Overview" — https://argo-cd.readthedocs.io/en/stable/operator-manual/architecture/ — accessed 2026-10-14
8. Google Cloud, "Modern CI/CD with GKE: Build a CI/CD system" — https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-reference-architecture — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![G4 sample: online shop release path from commit through build, tests and scan to a registry image promoted to staging and then production after a manual approval, with a GitOps controller applying the manifests](/samples/G4-delivery-pipeline.svg)
*Sample pending (generated by the renderer from `examples/`).*
