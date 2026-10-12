# Architecture and scoped changes

Adapted from Mokara architecture. Preserve responsibilities and existing boundaries, not its particular package names/frameworks.

## Inspect ownership first

Read project instructions, approved architecture/PRD, the engineer profile, and actual consumers. Trace routes, imports, auth, data flow, and persistence before selecting a file's home. A significant boundary decision needs a brief rationale and approved scope; a folder name alone does not require an ADR or repository reorganization.

Use the **narrowest common owner** of actual consumers:
- One route/feature's view, formatter, hook, model, or helper stays beside that feature under existing conventions.
- Promote shared UI, non-UI helpers, and lifecycle/stateful hooks only when consumers genuinely share a contract.
- Backend/domain code owns authorization, business mutations, integrations, and serialization under the existing architecture.
- Database/cache modules own infrastructure and must not import application UI internals.
- Admin, customer UI, and marketing keep their own presentation and auth/permission boundaries.

Do not create universal `packages/`, `features/`, controllers/services/repositories, or microservices to match a tutorial. A Laravel app may use its framework's routes/controllers/models/Blade layout; a Next app may use route colocation; a plain PHP project may have different conventions. Native framework-reserved entrypoints and filenames must remain valid.

## Dependency and rendering boundaries

Use intentional package/module imports; do not reach into another application's private source. Shared packages need demonstrated reuse and a coherent contract. Avoid new barrel aggregators, generic utility dumping grounds, wrappers that only forward calls, and dependency cycles; preserve existing legitimate entrypoints.

Keep pages focused on composition and extract substantial UI or pure transformations by responsibility, not arbitrary line limits. Preserve names unless renaming is part of the task. Follow the project's language/framework naming convention.

For React/server rendering, keep interactive boundaries small and inspect transitive client imports for server-only code. Do not convert an existing client model to server fetching as incidental cleanup. For Blade/Livewire/Inertia/other stacks, research native rendering/hydration boundaries rather than copying Next directives.

Preserve the approved API boundary, transport client, wire naming, error mapping, cookies/sessions, and deployment configuration. If the project uses a same-origin server proxy, preserve runtime upstream configuration and keep provider/database credentials server-side. Do not prescribe a proxy/backend split for an unrelated architecture or quietly add a second business API.

## Backend and persistence

Trace validation → authentication → scope authorization → business policy → persistence → response mapping. Preserve error precedence and avoid revealing protected resource existence. Reuse central policy/validation/constraint helpers; do not create competing entitlement or permission sources.

Keep related writes atomic; back concurrency-sensitive invariants with appropriate constraints or conditional writes. **Keep external provider calls outside open database transactions.** Use existing durable integration/idempotency/worker patterns when work must survive retries or process termination; do not introduce an outbox for every ordinary mutation. Preserve middleware/route registration order.

Use version-appropriate native facilities: for example Laravel routing/validation/transactions where selected. **If Hono is selected**, compose route groups with `app.route()` and keep typed handlers beside their path definitions where possible to preserve route inference; use supported typed handler factories when extraction is needed. Do not add controller/service/repository chains that only forward arguments, or assume every handler must remain large. See [Hono best practices](https://hono.dev/docs/guides/best-practices).

## Make one coherent change

Identify user-visible behavior, consumers, dependency direction, and persistence effects. Move one responsibility at a time, update consumers/imports and remove obsolete copies in the same change. Preserve HTTP paths, serialized fields, auth, environment contracts, migration history, data, and UI behavior unless the user approved changing them.

Verify affected routes/assets/exports, cycles, server/client leaks, authorization, transaction correctness, and retry behavior. Use the consuming project's fresh-checkout and CI rules when applicable; documentation-only skill/profile changes require content/link validation, not unrelated application builds.
