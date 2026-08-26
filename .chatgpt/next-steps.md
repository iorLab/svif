# Next Steps

1. Review and tighten the normative language in `SPECIFICATION.md`, especially the exact meaning of `MUST`, `SHOULD`, and the human/local-tooling boundary.
2. Decide the v0.1 conformance model: a single ZeroLocal Core plus optional RPM/Continuous Delivery profiles, or a layered mandatory profile set.
3. Define a minimal machine-readable conformance manifest so a repository can declare its ZeroLocal version, RPM paths, CI workflow, deployment workflow, production environment, and verification endpoints without binding to one provider.
4. Bootstrap `iorLab/zerolocal-cloudflare-starter` from the v0.1 draft with GitHub Actions CI, exact-SHA deployment, serialized production delivery, Cloudflare Workers deployment, optional D1 provisioning/migrations, and health/readiness verification.
5. Add conformance checks to the starter and use failures to refine ambiguous specification language rather than encoding undocumented behavior.
6. Extract a concise founding case study from `mattamior/awesome-fame-slider`, clearly separating generic ZeroLocal invariants from application-specific voting/X decisions.
7. Define threat-model guidance for untrusted pull requests, repository write authority, workflow permissions, production secrets, provider tokens, dependency execution, and deployment provenance.
8. Decide how repositories with mandatory production approval gates qualify: ZeroLocal should not require a local environment, but may permit a deliberate human approval at a trust boundary.
9. Add examples for at least one non-Cloudflare deployment profile to test whether the Core is genuinely provider-neutral.
10. Once the spec and starter agree on observable behavior, tag the first v0.1 draft checkpoint and update RPM with validated conformance claims.
