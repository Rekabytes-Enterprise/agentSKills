# Research a compatible engineering stack

This guide is an option map, not a dependency prescription. Research before the first configuration approval and whenever the approved profile materially drifts.

## 1. Identify the actual stack

Use manifests/lockfiles and implementation evidence, not a directory name alone:
- JavaScript/TypeScript: package manifests, lockfiles, framework config, entrypoints, routes, components, and SSR/client boundaries.
- Laravel/PHP: `composer.json` / `composer.lock`, framework bootstrap/routes, Blade/templates, Livewire components, Inertia entrypoints, PHP version/extensions, and any frontend manifests.
- Other ecosystems: their native manifests, rendering/entrypoints, tests, and deployment configuration.

Confirm what is installed versus only mentioned in a PRD. Version requirements in a manifest are not proof of the exact resolved version; use lockfiles/installed declarations when available. Do not copy this library's development machine or Mokara's versions, ports, package layout, auth implementation, or environment contracts.

## 2. Separate state by responsibility

| Kind of state | Typical owner | Questions |
| --- | --- | --- |
| Temporary UI state | Component/framework local primitives | Does anything else actually need it? |
| Shareable filter/navigation state | URL/router/form model | Should reloads, links, and back navigation preserve it? |
| Cross-component client state | Existing suitable store/context/native reactive mechanism | Is sharing real, and what owns its lifetime? |
| Server-derived data | Framework fetching/query/cache facilities | What owns freshness, invalidation, retries, and optimistic rollback? |
| Identity/session and permissions | Server/framework auth boundary; minimal safe client projection | How are requests/tenants isolated, sessions revoked, and permissions enforced? |
| Durable business data | Database/domain layer | What enforces validation, transactions, concurrency, and persistence? |

A UI store is not the database, authorization layer, or a complete server-data cache. Browser persistence is not a safe place for credentials. Do not use a process-global server store for request-specific user data.

## 3. Candidate approaches — verify, do not blindly adopt

| Actual setup | Suitable starting points to research | Do not assume |
| --- | --- | --- |
| Next.js + React | Framework server/client data boundaries; local state first; retain/research Jotai for shared client state when it fits; query/cache layer only when needed | Next.js requires Jotai; client state can safely hold server-global user data |
| Vite + React | React local/reducer/context primitives; an existing or justified Jotai/store approach; router URL state and a suitable server-data cache | Vite provides state management or mandates React |
| Vite + Vue | Vue local/reactive state; Pinia for justified shared state; router/query tooling as needed | React hooks, Jotai, or Motion React belong here |
| Vite + Svelte or another client | Version-appropriate native reactive/state facilities and approved ecosystem tools | Vue/React recipes transfer directly |
| Laravel + Blade | Laravel request/session, validation, Eloquent/database, URL/form state; minimal browser state if there is interactive UI | Every PHP app needs a global JavaScript store |
| Laravel + Livewire / Alpine | Installed Livewire server/component state and hydration contracts; Alpine local/shared browser state only where warranted | A PHP component should use React atoms; all state should be duplicated in browser storage |
| Laravel + Inertia + React/Vue | Laravel server/domain/session state plus the actual frontend's primitives; inspect Inertia props/forms/history behavior before adding a store | Laravel alone selects the client state library; Inertia props are all durable domain state |
| Plain PHP with server-rendered HTML | Request/form variables, secure native/session abstractions, database persistence; native JS local/URL state for actual browser interaction | Node, React, Jotai, or a build pipeline is necessary |
| PHP API with a separate SPA | Backend state/auth native to PHP; SPA state/cache native to its actual client framework | One library can own both server and browser state |

Laravel and Vite can coexist. Frameworks, runtimes, view layers, and build tools are different dimensions; record each. For a small page, the recommendation may be **no additional state library**.

## 4. Compatibility beyond state

Check the chosen tools together:
- Language/runtime and framework versions, dependency/peer requirements, supported adapters/plugins, maintenance/security status, license, and migration burden.
- Rendering lifecycle: request scope, SSR/hydration, browser-only APIs, persisted state validation, long-lived workers, and multi-tenant isolation.
- Backend and auth integration: use the existing approved server-side enforcement. A JavaScript server auth library is not automatically executable inside PHP; a separate service/integration is an architectural choice requiring approval.
- Design/styling: current tokens and component library, CSS/Tailwind version only if present, accessible interaction primitives, actual rendering/runtime boundaries.
- Motion: approved framework-native animation or CSS; use Framer Motion only in compatible React surfaces already using/approved for it. Do not migrate `framer-motion` imports just because new docs use `motion/react`.
- Error/validation: one agreed error classification policy, runtime-appropriate adapters, schema/input validation, safe messages, and recoverable pending/optimistic state.
- Data and operations: database/driver/runtime support, file storage, migrations, deployment model, configuration exposure, backup/recovery, cache/retry ownership, and observability.
- Verification: native tools already configured; research proposals separately from commands actually permitted to run.

## 5. Evidence and approval

Prefer official documentation for the relevant installed version, package/type declarations, and verified repository evidence. Record URL/path, version, actual verification date when known, and what claim it supports. A URL alone is not proof that it was read. Never fabricate searches or current-version support.

Starting points (consult the matching version; this list is not pre-verified project research):
- [React state and effects](https://react.dev/learn) · [Next.js documentation](https://nextjs.org/docs) · [Vite guide](https://vite.dev/guide/)
- [Jotai documentation](https://jotai.org/docs) · [Vue state management](https://vuejs.org/guide/scaling-up/state-management.html) · [Pinia](https://pinia.vuejs.org/)
- [Svelte documentation](https://svelte.dev/docs) · [Laravel documentation](https://laravel.com/docs) · [Livewire](https://livewire.laravel.com/docs)
- [Alpine](https://alpinejs.dev/start-here) · [Inertia](https://inertiajs.com/) · [PHP sessions](https://www.php.net/manual/en/book.session.php)
- [Motion](https://motion.dev/docs) · [OWASP cheat sheets](https://cheatsheetseries.owasp.org/)

Compare the existing approach with relevant alternatives; give a recommendation, drawbacks, explicit not-needed items, and unresolved compatibility blockers. Present the proposal in conversation and wait for user approval before saving the project profile. Do not turn research into dependency installation or an unrequested rewrite.
