# Engineering behavior

Adapted from Mokara engineering. The principles apply broadly; the library-specific recipes apply **only to approved compatible runtimes**. Preserve working behavior and current contracts rather than importing another project's stack.

## Official facilities first

Use the chosen framework/library's supported primitives and utilities instead of reimplementing stores, subscriptions, persistence, reset, validation, retry, or animation lifetimes. Domain-specific state/actions remain necessary; this is not a ban on application logic. Verify installed signatures and version support before use; community extensions are not built-in APIs.

Derive totals, filters, and dependent selections instead of duplicating values and synchronizing them. Keep temporary form/menu state local. Distinguish server-data caching from shared client state. Preserve current store/provider ownership and session entrypoints; do not fork readers and imperative writers into different stores. Validate persisted values and account for SSR/hydration; static generics are not runtime validation. Never persist credentials/tokens in browser storage or authenticated request data in a process-global server store.

### React + Jotai recipe — only when the profile selects it

| Need | Official API to consider |
| --- | --- |
| Read without writing | `useAtomValue` |
| Write without subscribing | `useSetAtom` |
| Read and write | `useAtom` |
| Derived state | Read-only derived `atom` |
| Coordinated action | Writable/action `atom` |
| Persist a UI preference | `atomWithStorage`, `createJSONStorage` |
| Reset state | `atomWithReset`, `useResetAtom`, `RESET` |
| Async state without Suspense | `loadable` |
| Async fallback | `unwrap` |
| Existing observable integration | `atomWithObservable` |

Use only APIs needed by the feature. Keep identity stable and definitions at module scope where appropriate. If the approved application uses a default client store, preserve it; do not add a Provider that isolates imperative writers from readers. Other SSR/store lifetimes require research and an approved topology, not a transplanted default-store policy.

`loadable`/`unwrap` are not complete server-cache/retry systems; feed failures into the central error policy. Use [official hooks](https://jotai.org/docs/core/use-atom), [storage](https://jotai.org/docs/utilities/storage), [reset](https://jotai.org/docs/utilities/resettable), and [async utilities](https://jotai.org/docs/utilities/async), matching installed support.

### Other runtimes

Use the approved native equivalents from the profile. Laravel/PHP domain/session state remains server-owned; Blade, Livewire, Alpine, Inertia, or a separate SPA determines the actual UI model. Vue/Svelte state uses their version-compatible facilities. Do not translate an atom API mechanically into a framework that does not support it.

## Effects: last choice for external synchronization

In React, first use render-derived values, event handlers/actions, and framework/library lifecycle facilities. Do not use `useEffect` for prop mirroring, derived state, form submission, chained transitions, persistence already owned by a utility, or animations.

Use an effect only for a necessary external system: subscriptions, browser events, or a genuine lifecycle integration. Comment what is synchronized and why the simpler option does not fit. Declare real dependencies, clean up, handle cancellation/stale responses, and tolerate development remounts. Do not hide an unnecessary effect inside another hook or `useLayoutEffect`. Preserve intentional boot semantics.

Apply the same ownership/cleanup principles with other frameworks' native lifecycle mechanisms; do not prescribe React hooks for PHP/Vue code. See [React effect guidance](https://react.dev/learn/you-might-not-need-an-effect) and [external synchronization](https://react.dev/learn/synchronizing-with-effects).

## Declarative, surface-appropriate animation

For an approved React/Motion surface, drive motion through render state, variants, `initial`, `animate`, `exit`, gestures, and `whileInView`. Use `AnimatePresence` for exit lifetimes and stable keys. Preserve installed `framer-motion` imports; a newer `motion/react` documentation example is not upgrade permission.

Reuse shared timings/variants and existing motion providers. Respect reduced motion with appropriate static alternatives; disabling transforms/layout does not automatically remove opacity/color transitions. Preserve position-only list animations, portal placement during exits, and excluded compact chips/heatmap elements when the adopted design has those rules. Avoid huge animated layout subtrees, effect-started animations, timeout-based unmounts, and custom frame-loop rigs.

Use approved CSS/native facilities for non-React surfaces. Do not add React/Motion to a plain HTML/PHP admin console to satisfy this recipe. Existing decorative WebGL is separate; do not replace it or introduce new GPU effects incidentally. See [presence](https://motion.dev/docs/react-animate-presence), [layout](https://motion.dev/docs/react-layout-animations), and [reduced motion](https://motion.dev/docs/react-accessibility).

## One error policy, native adapters per runtime

Reuse the established transport → normalization/classification → action handling → presentation path instead of private catch-to-message helpers per component. Keep server/client adapters separate; do not import browser/router code into a backend. In PHP/Laravel, inspect its exception/validation handling and frontend response consumers before choosing a compatible contract.

Handle render failures with the framework's established render/error boundaries and action failures through the centralized async/action path. **A render error boundary does not replace async-event/action handling.** Route local validation through the central policy as well; do not create an independent private error system. Record both mechanisms in the profile using actual native paths.

For a new failure, add a stable server code/status and safe central rule where that contract exists; do not replace response envelopes as an incidental cleanup. Expose known validation text only through explicit trusted rules. Hide unexpected exceptions, provider bodies, and stacks from UI copy; retain sanitized diagnostics. Distinguish code, status, kind, action, and retryability; unknown codes still need meaningful fallback classification.

Treat catches and parsed external input as untrusted. In TypeScript use `unknown`, schema validation, discriminated unions, `instanceof`, and property/type guards; own-registry checks prevent prototype-code lookups. A generic `TypeError` is not automatically a transport failure. In PHP and other languages use native types/exceptions plus runtime input validation and centralized safe response mapping.

Check failure results before writing success state, roll back failed optimistic changes, and clear pending state reliably. Preserve existing null/failure semantics. No swallowed failures, fake empty-success fallbacks, or automatic mutation retries without idempotency. Explicit best-effort behavior needs a documented policy.

## Type safety and meaningful verification

For TypeScript, no `as any`, explicit `any`, double assertions, non-null assertions, or suppression comments to bypass checks. Prefer real types, narrowing, schemas, and `satisfies`. For PHP/other stacks, use their agreed language/static-analysis tools and explicit types where applicable; do not invent TypeScript rules for non-TypeScript files.

Test relevant malformed input/error bodies, unknown/prototype codes, safe messages, session/permission routing, retry classification, and optimistic recovery. Check state identity/lifetime, persisted-state validation/hydration, lifecycle cleanup, and reduced motion where affected. Run permitted native checks and focused tests; report untested behavior honestly. See [TypeScript narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) and [OWASP error handling](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html).
