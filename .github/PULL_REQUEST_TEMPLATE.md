<!-- 
  PR TITLE must follow Conventional Commits:
  type(scope): short description

  type   → feat | fix | breaking | refactor | docs | test | chore
  scope  → must match the module name, e.g. community.postgis

  Examples:
    feat(community.postgis): add ST_Within geometry filter
    fix(community.postgis): handle null geometry in WHERE clause
    breaking(community.postgis): rename spatial_ref to srid
    docs(community.postgis): update PostGIS 3.4 setup guide

  The title becomes the changelog entry — write it for the end user.
-->

## What

<!-- What does this PR change or add? One to three sentences. -->

## Why

<!-- Why is this change needed? Bug, missing feature, user request? -->

## Checklist

- [ ] PR title follows `type(community.modulename): description`
- [ ] Only files from `modules/community.<name>/` are changed
- [ ] `docs/index.md` has all required sections (Overview, Prerequisites, Setup, Quick Example)
- [ ] `docs/syntax.md` documents every new syntax element
- [ ] Unit tests cover the translator output
- [ ] Validator tests cover blocked patterns (if `native_validator.py` changed)
- [ ] Grammar tests cover every new rule (if `grammar_extension.lark` changed)
- [ ] `uv run pytest` passes locally

## Notes for reviewer

<!-- Anything the reviewer should pay special attention to. Optional. -->
