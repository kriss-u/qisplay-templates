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

1. Edit or add files under `templates/`.
2. Run `node scripts/build-index.mjs` (Node 20.11+). It validates everything and
   rewrites `index.json`. It also warns when a template changed but its
   `version` didn't.
3. Commit, then tag and push:

   ```sh
   git tag v1.1.0
   git push origin main --tags
   ```

   QisPlay finds the new tag within a few minutes (jsDelivr caches version lookups
   briefly).

To preview before tagging, open
`https://qisplay.nepcodex.com/?templates=<commit-sha>` after pushing. That loads
the catalog at that exact commit.

## Linking students to a collection

`https://qisplay.nepcodex.com/?collection=intro-to-quantum-computing` opens the gallery
filtered to that collection. `?template=<id>` opens it with one template selected.
