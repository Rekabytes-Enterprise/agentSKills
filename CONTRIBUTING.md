# Contributing to Reka Bytes Agent Skills

Thanks for helping make these skills clearer, safer, and more useful across projects. Contributions can add a skill, improve instructions/templates, fix validation, or clarify documentation.

Start with the [README](README.md), the existing [skill catalog](README.md#skill-catalog), and the [Agent Skills specification](https://agentskills.io). This library is licensed under [MIT](LICENSE).

## Development workflow

- `main` is the published branch used by the default installation command.
- `dev` is the integration branch. Base feature branches and pull requests on `dev` unless a maintainer asks otherwise.
- Keep each pull request focused. Do not combine a new skill with unrelated refactors, dependency changes, or visual redesigns.

After cloning your fork and checking out `dev`, create a feature branch:

```bash
git switch dev
git switch -c feat/my-skill
```

Update your branch against the current `dev` before submitting. Do not force-push shared branches. Open a pull request targeting this repository's `dev` branch; publication to `main` is a separate maintainer decision.

## Add or update a skill

Keep each skill self-contained:

```text
skills/<skill-name>/
├── SKILL.md
├── references/     # Optional supporting guidance
└── templates/      # Optional reusable outputs
```

### Metadata

`SKILL.md` must begin with frontmatter containing:

```yaml
---
name: example-skill
description: "Describe what this skill does and when an agent should use it."
---
```

- The name must match the folder, contain 1–64 lowercase letters/digits with single hyphens, and not start/end with a hyphen.
- Use a meaningful, nonempty, single-line description of at most 1024 characters. The repository validator supports this simple scalar format, not general YAML features.
- Keep references/templates inside the same skill folder. Use relative links for local files; do not depend on a separate checkout or a personal-machine path.
- Update the README catalog and relevant usage examples when a skill is added or its behavior materially changes.

### Instruction quality

- State when the skill applies, what it reads, what it writes, and what is out of scope.
- Make approval gates explicit. Installing or invoking a skill must not silently authorize implementation, infrastructure changes, package upgrades, account creation, or deployment.
- Separate advice, approved decisions, implementation evidence, test execution, and user acceptance. Never mark planned work or unexecuted tests as complete.
- Prefer official, version-compatible APIs and sources. Do not claim research or live verification that was not performed.
- Keep globally reusable guidance separate from project-local configuration. Do not mutate a shared global skill to specialize one consuming project.
- Preserve the consuming project's approved stack, design, data, and behavior. Compare alternatives before recommending a change; do not force a framework or state library into unrelated runtimes.
- For templates, identify the output destination, placeholders to replace, expected evidence, and approval/sign-off state. Do not include fabricated results or approvals.

For the current skills, retain project-manager's proposal/document approval gates and engineer's research/configuration approval gate. Keep implementation and UAT acceptance separate.

## Documentation and assets

Preserve the primary installation command:

```bash
npx skills add Rekabytes-Enterprise/agentSKills
```

Keep README links, navigation, catalog entries, and actual skill behavior aligned. Label install/download metrics accurately; do not replace unavailable data with invented counters. Keep images accessible and local SVGs static, without scripts or external asset dependencies.

Do not commit credentials, private data, personal state, or local agent installations. Use synthetic examples and environment variable names instead of real secrets. Respect third-party licenses and retain required attribution; a reference to another project is not permission to copy its private source, fonts, or assets.

## Validate locally

Contributor checks require Python 3.9+ and Git. There are no Python dependencies to install, and no npm package needs to be published for this library.

Run from the repository root:

```bash
python3 -B scripts/validate_skills.py
python3 -B -m unittest discover -s tests -v
git diff --check
```

The [CI workflow](.github/workflows/validate.yml) runs package validation and tests. These checks cover metadata, local links, portability, README markup, and static instruction contracts—not live model behavior or external badge availability.

For workflow changes, also explain the expected behavior for relevant scenarios: missing/unapproved requirements, declined approval, unsupported or changed stacks, existing project configuration, failed verification, and failed UAT. State which scenarios you reviewed versus actually exercised with an agent. Do not start consuming-project servers or touch production merely to test a documentation change.

## Pull request checklist

- [ ] The change has a clear purpose and bounded scope.
- [ ] Skill metadata, references, templates, and README links are consistent.
- [ ] Approval boundaries and project-local persistence are preserved.
- [ ] Validation and tests pass; results and unperformed checks are reported accurately.
- [ ] Relevant workflow scenarios and compatibility limits are described.
- [ ] No credentials, private data, generated caches, or unauthorized third-party material are included.
- [ ] The pull request targets `dev`, unless a maintainer requested another branch.

In the PR description, explain the problem, the change, affected skills/files, validation performed, and any compatibility or migration implications.

## Report issues

Include the affected skill, agent/installer versions when relevant, sanitized project context, expected versus actual behavior, and steps to reproduce. Clearly distinguish an instruction issue from an agent's failure to follow it. Do not put credentials or private project data in public reports.

## Licensing contributions

Only submit material you have the right to contribute. Contributions are provided under this repository's [MIT License](LICENSE); retain the required copyright and permission notices when redistributing substantial portions.
