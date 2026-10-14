# Network Topology and Connectivity View (网络拓扑图)
<!-- Generated from content/en/types/G3-network-topology.md by tools/build_skill_refs.py. Do not edit. -->
> What can communicate with what, through which paths and controls, in normal and in failure conditions?
Scope: One declared view (physical links, logical adjacency, or one traffic path) over the networks, segments, gateways and endpoints that matter Neighbours: F2, G1, G2.

## Meaning
- **Question:** what can communicate with what, through which paths and controls, and what happens when a link or zone fails?
- **Viewpoint:** a connectivity, isolation and operations concern. The view can be physical (cables, sites, devices), logical (networks and adjacency) or a single traffic path; each needs its own legend. It is an informal family, not cloud-only and not a single notation.
- **Deeper meaning:** logical connectivity is not physical cabling and not permission to use an application. A peering line may give only limited adjacency; routes, forwarding and filters decide the usable paths. Reachability does not prove that a user is authorised.
- **Leaves out:** business logic, application internals and full rule tables; those belong in an evidence table.
- **Definition used here:** *topology* shows which elements are connected; a *traffic flow* shows a path that a given kind of traffic takes. Addresses follow RFC 1918 for private IPv4 and, in public examples, the documentation ranges of RFC 5737 (IPv4) and RFC 3849 (IPv6). Configuration shows intent; observed behaviour needs separate, authorised evidence.

## When to use and how to choose
- **Audience:** network and security engineers, platform operators, architects, partners who must connect to the estate.
- **Scenarios:** a private link between head office and the cloud network; hub-and-spoke or peering between storefront, back-office and data networks; private egress to a payment provider; troubleshooting why the chatbot service cannot reach the order API; reviewing segmentation and failover between zones.
- **When not to use:** to claim application permissions, service health or measured traffic without evidence; to answer a cloud routing question with a cabling drawing.
- **vs neighbours:**
  - **G1** for which software runs where.
  - **G2** for cloud services and trade-offs.
  - **F2** for trust boundaries and threats.
  - **E1** for request sequencing over time.

## Notation and elements
- **Formal or informal:** informal. Declare the type of view in the title: physical, logical or traffic path.
- **Required:**
  - Scope and view type.
  - The networks or segments, gateways and endpoints that matter.
  - Connections, and the route, forwarding or filter boundaries needed to explain the chosen path.
  - Direction semantics and a legend.
- **Lines:** in a topology view a line means adjacency and need not imply packet direction. In a traffic-flow view, state whether an arrow shows who initiates the connection, the routed path or a two-way exchange. A one-way request arrow must not suggest that replies are impossible. Overlay a numbered example path on the topology instead of mixing both.
- **Optional:** sanitised CIDRs, VLAN or VRF, ports and protocols, route-table references, DNS, address translation, peering or transit gateways, VPN or private circuits, IPv6 egress, failure domains, inspection devices.
- **Caution:** "public, private and data subnets" is not a required three-part taxonomy, and a public subnet route alone does not prove a workload has a public address or an open port. A control-plane hub is not necessarily a packet-transit network.
- **Text budget:** a network name and, if safe, its documentation-range CIDR; rules go in a table.

## Best practices and anti-patterns
### Best practices
1. **Show real paths,** including return routing, DNS and egress when they matter, not only inbound arrows.
2. **Do not infer transitive reachability from peering lines.** Check the provider's peering and transit behaviour; Google Cloud's hub-and-spoke page states that VPC peering is not transitive.
3. **Treat NAT as one mechanism.** Private endpoints, IPv6 egress and deliberately isolated networks need different paths.
4. **Keep facts separate:** topology adjacency, firewall permission and observed traffic are three different things.
5. **Use documentation ranges** in public examples and never publish real address plans or rule inventories by default.

### Anti-patterns
1. **Inventing a direct line** to simplify routing; simplify by choosing a path instead.
2. **Peering drawn as a full mesh** without a stated transit mechanism.
3. **Arrows with no meaning:** adjacency, request and flow mixed in one style.
4. **Cloud-specific boundaries copied across providers** (a VPC drawing reused for another provider's network model).
5. **A permitted path read as a healthy service:** a firewall rule does not prove that the destination listens.

## Drawing recipe
1. Decide the view type first: physical links, logical connectivity or one traffic path. Put it in the title, for example "Online shop network: logical, intended".
2. Inventory scopes (sites, accounts, networks), segments, gateways, and the endpoints the question needs; leave out the rest.
3. Read route, filter and forwarding declarations; keep declared and observed apart and say which you draw.
4. Layout: nested boundaries for networks and segments; hub-and-spoke or layered placement only when the topology really is that shape. External networks (internet, office, partner) sit outside, left or top.
5. Lines: one style for connectivity; for a traffic path, add numbered arrows and say who initiates. Show response, DNS and egress when the path depends on them.
6. Text: short names plus a documentation-range CIDR if useful; ports and rules go in an attached table.
7. Colour: neutral for internal, one accent for the path being explained, a distinct style for external networks; do not rely on colour alone for allow versus deny.

**Self-check**
- [ ] The view is declared as physical, logical or traffic path.
- [ ] Every line or arrow has a defined meaning in the legend.
- [ ] Route, filter and forwarding constraints behind each shown path are evidenced.
- [ ] Return path, DNS and egress are considered where the path depends on them.
- [ ] Peering is not drawn or described as transitive without a mechanism.
- [ ] NAT or public exposure is not inferred from a subnet name alone.
- [ ] Boundaries use the semantics of the stated provider or protocol.
- [ ] Addresses are safe to publish (documentation ranges) and assumptions are stated.

## Evidence in a code repository
- **Network declarations:** Terraform, CloudFormation or CDK networks, subnets, route tables and associations, peering and transit attachments.
- **Controls:** security groups, network ACLs, firewall policies, Kubernetes NetworkPolicy, Ingress and Service objects, DNS configuration.
- **Limits:** Kubernetes names alone do not establish the underlying routing.
- **Must come from people:** physical links, provider circuits, real address plans, observed traffic, validated failover.
- State files and firewall exports can be sensitive; ask for sanitised, authorised evidence and never scan to discover.

## Guided-mode questions
1. Physical links, logical connectivity or one request path? (logical connectivity)
2. Which sites, networks, providers and environments are in scope? (office, cloud network, one payment provider)
3. Which ingress, egress, private connectivity and inspection needs matter? (private egress to the payment provider)
4. May real addresses and rules be shown? (no, documentation ranges only)
5. Is this configuration intent or a validated operational topology? (intent)

## Template
Model template: `assets/templates/G3.json` · Layout template: `nested` · networks and segments become nested `boundary` groups, gateways and endpoints become `component` nodes, connectivity uses `assoc` edges (`dir` `--`) and a traffic path uses `call` or `data` edges with `step` numbers; CIDRs go in `sub` and the view type goes in the title.

## Sample
Figure: `samples/G3-network-topology.svg` (published with the site)
