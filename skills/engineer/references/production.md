# Production-sensitive engineering

Adapted from Mokara production guidance. Apply only concerns relevant to the task and approved stack; this is not permission to change infrastructure or live data.

## Configuration and exposure

Inspect actual framework/runtime rules for environment configuration and public bundles. Keep database/provider credentials server-side, out of images/build arguments and public client variables. Preserve the project's approved API/proxy and cookie/session boundaries. Validate required settings; optional integrations must be honestly unavailable when incomplete. Trust forwarded headers only according to an explicit trusted-ingress policy.

For self-hosted Next.js where selected, follow current [reverse-proxy/self-hosting guidance](https://nextjs.org/docs/app/guides/self-hosting) and check runtime versus build-time/public configuration and SSR behavior. For Vite where selected, inspect client-exposed configuration and build-time replacement. For Laravel/PHP, inspect server configuration/cache and long-lived worker lifetimes. Do not transplant one framework's environment semantics into another.

Keep user-specific responses out of shared caches. Review proxy/streaming behavior for actual subscriptions/SSE. Add multi-instance cache coordination only when the deployment needs it, not by default for client UI state.

## Errors, logs, and recovery

Use safe user-facing copy and controlled, sanitized diagnostics. Exclude credentials, session identifiers, cookies, OAuth codes/callback secrets, sensitive bodies, and raw provider dumps. Bound/redact untrusted log fields. Preserve useful operation/code/status/correlation context without duplicate reports or exposing raw causes to UI/telemetry. See [OWASP logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html).

Distinguish validation/auth/conflict failures from unexpected faults. Retry only appropriate transient work with bounded ownership/backoff; mutations require idempotency or explicit user retry. No unbounded validation/auth/rate-limit retry loops or retry multiplication across client, proxy, and workers. Telemetry failure must not break the original operation.

## Data and lifecycle

Use database constraints and transactions for race-sensitive invariants, bounded provider timeouts, and durable work patterns when required. **Keep external provider calls outside open database transactions.** Do not launch untracked promises/jobs for work that must survive termination.

Distinguish process liveness from dependency readiness; a health response is not proof every provider is healthy. For authorized lifecycle changes, stop accepting new work, allow bounded request draining, then close workers/connections deliberately using the selected runtime's supported mechanisms. Inspect actual implementation before claiming this lifecycle already works; preserve request-scoped isolation and appropriate resets for long-lived workers. Backup restoration and multi-instance readiness also require their own evidence.

## Delivery and verification

Preserve locked dependencies, CI gates, migration history, and deployment ownership. Review backward compatibility with overlapping application versions and a concrete rollback plan; rolling back an image does not undo database migrations. For explicitly authorized deployments, pin release images where supported and verify staging acceptance before calling a deployment successful. Do not run destructive migrations, live callbacks, provider mutations, or production probes without explicit authorization.

Follow repository rules for permitted local checks versus CI-owned builds. Do not start owner-managed servers, infrastructure containers, or preview environments unprompted. Run exit-once native checks only when allowed; state when a build/live check was not performed and what remains for CI or the owner. Typechecks/lint/focused tests prove only their tested scope, not production readiness or UAT acceptance. Do not commit, push, release, or deploy without an explicit request.
