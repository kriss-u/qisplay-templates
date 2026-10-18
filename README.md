# QisPlay templates

Starter projects for [QisPlay](https://qisplay.nepcodex.com). Students open them
from **Project menu → New project from template…**, with no account or sign-in.

QisPlay reads this repository through jsDelivr's CDN at the newest version tag
(`vX.Y.Z`). Nothing runs on a server.

## Layout

```
collections.json              groups shown in the gallery (e.g. a course)
templates/<id>/template.json  title, version, tags, ...
templates/<id>/...            the files a new project starts with
index.json                    generated catalog; don't edit by hand
scripts/build-index.mjs       builds and checks index.json
CHANGELOG.md                  written by semantic-release
.releaserc.json               semantic-release config
```

## template.json

```json
{
  "title": "Lab 1 · Qiskit Basics",
  "description": "One or two sentences for the gallery card.",
  "version": 1,
  "order": 1,
  "collections": ["intro-to-quantum-computing"],
  "tags": ["basics", "circuits"],
  "level": "beginner",
  "open": ["README.md", "lab01.py"],
  "changes": "What changed in this version (shown with the update notice)."
}
```

| Field         | Required | Meaning |
| ------------- | -------- | ------- |
| `title`       | yes      | Card title and the new project's name. |
| `description` | yes      | Card text. |
| `version`     | yes      | Positive integer. **Bump it** to show "update available" to students who opened an older version. |
| `order`       | no       | Sort order within the gallery. |
| `collections` | no       | Ids from `collections.json`. A template can belong to several. |
| `tags`        | no       | Free-form topic labels, used for filtering. |
| `level`       | no       | `beginner`, `intermediate` or `advanced`. |
| `open`        | no       | Files to open as tabs; the last one is active. |
| `changes`     | no       | Short note shown next to the update notice. |

The folder name is the template's id. Never rename it once students use it,
because update notices match on it.

## Workflow

Requires Node 24.15+. Run `npm install` once; it also installs the Git hooks.

1. Edit or add files under `templates/`.
2. Run `npm run build`. It validates everything and rewrites `index.json`, and
   warns when a template changed but its `version` didn't.
3. Commit with a [Conventional Commit](https://www.conventionalcommits.org/)
   message and push to `main` (or merge a PR, whose title becomes the commit).

The Release workflow then runs semantic-release, which reads the commits since the
last tag, picks the next version, updates `CHANGELOG.md`, tags `vX.Y.Z` and creates
a GitHub release. QisPlay picks up the new tag within a few minutes.

| Commit                                   | Release |
| ---------------------------------------- | ------- |
| `fix: correct the Grover hint`           | patch   |
| `feat: add lab 9 on VQE`                 | minor   |
| `feat!: ...` or a `BREAKING CHANGE:` footer | major   |
| `docs:`, `chore:`, `ci:`, `refactor:` ...   | none    |

The repo version and a template's `version` are separate. The repo version says
which catalog is newest. A template's `version` decides whether students who
already opened that template see "Template updated", so bump it only when they
should take a fresh copy.

Pushing to the `beta` branch makes prereleases (`vX.Y.Z-beta.N`). QisPlay only loads
full releases, so you can preview a beta with `?templates=<tag>`.

### Hooks and CI

- **Local hooks:** `commit-msg` runs commitlint, and `pre-commit` runs `npm run check`.
- **Test** (on PRs and before every release): checks `index.json` and compiles the
  lab files.
- **Commitlint:** checks PR titles.

To preview without releasing, push a commit and open
`https://qisplay.nepcodex.com/?templates=<commit-sha>`. That loads the catalog at
that exact commit.

## Linking students to a collection

`https://qisplay.nepcodex.com/?collection=intro-to-quantum-computing` opens the gallery
filtered to that collection. `?template=<id>` opens it with one template selected.
