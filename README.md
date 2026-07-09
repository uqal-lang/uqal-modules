# uqal-modules

Community and standard database modules for [UQAL](https://uqal-lang.github.io/uqal-docs).

Each module teaches the UQAL engine how to speak a specific database's native query language. You install only what you need.

---

## Available Modules

### Standard (included in uqal-core)

| Module | Database | Status |
|--------|----------|--------|
| `standard.postgresql` | PostgreSQL | ✓ Stable |
| `standard.mongodb` | MongoDB | ✓ Stable |
| `standard.neo4j` | Neo4j | ✓ Stable |

### Community

| Module | Database | Author |
|--------|----------|--------|
| *(none yet — be the first)* | | |

Browse the full list: [uqal-lang.github.io/uqal-docs/modules](https://uqal-lang.github.io/uqal-docs/modules)

---

## Installing a Community Module

```bash
uv add uqal-postgis
uqal add-module community.postgis
```

---

## Contributing a Module

Community modules live in this repository under `modules/community.<name>/`.

**Quick start:**

```bash
# 1. Fork this repo
# 2. Create your staging branch
git checkout -b dev/community.mymodule

# 3. Create your feature branch
git checkout -b feat/community.mymodule/initial-implementation

# 4. Build your module, open a PR to dev/community.mymodule
# 5. When ready, open a PR from dev/community.mymodule to main
```

Full guide: [Module Development](https://uqal-lang.github.io/uqal-docs/contributing/module-development)  
Standards & structure: [Module Standards](https://uqal-lang.github.io/uqal-docs/contributing/module-standards)  
Workflow & versioning: [Community Workflow](https://uqal-lang.github.io/uqal-docs/contributing/community-workflow)

---

## Module Structure

```
modules/community.mymodule/
├── module.json          ← metadata, version, compatible_with
├── __init__.py
├── translator.py        ← UQAL AST → native query
├── native_validator.py  ← blocks unsafe queries
├── tests/
│   ├── unit/
│   └── grammar/
└── docs/
    ├── index.md
    └── syntax.md
```

---

## License

[MIT](LICENSE)
