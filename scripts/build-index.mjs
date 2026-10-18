#!/usr/bin/env node
// Builds index.json, the catalog QisPlay reads, from collections.json and
// templates/<id>/template.json. The app fetches index.json and then each file it
// lists, so run this after every change to a template and commit the result.
//
//   node scripts/build-index.mjs           write index.json
//   node scripts/build-index.mjs --check   fail if index.json is missing or stale (CI)
import { createHash } from "node:crypto";
import { existsSync, readdirSync, readFileSync, statSync, writeFileSync } from "node:fs";
import { join, relative } from "node:path";

const ROOT = join(import.meta.dirname, "..");
const TEMPLATES = join(ROOT, "templates");
const INDEX = join(ROOT, "index.json");
const SCHEMA = 1;
const ID = /^[a-z0-9][a-z0-9-]*$/;
const JUNK = /(^|\/)(__pycache__|\.DS_Store|Thumbs\.db|\.ipynb_checkpoints)(\/|$)|\.pyc$/;
const LEVELS = ["beginner", "intermediate", "advanced"];
const MAX_FILE_BYTES = 5 * 1024 * 1024;

const errors = [];
const fail = (msg) => errors.push(msg);

function readJson(path) {
  try {
    return JSON.parse(readFileSync(path, "utf8"));
  } catch (err) {
    fail(`${relative(ROOT, path)}: ${err.message}`);
    return null;
  }
}

function walk(dir, base = dir) {
  return readdirSync(dir, { withFileTypes: true }).flatMap((e) => {
    const full = join(dir, e.name);
    const rel = relative(base, full).split("\\").join("/");
    if (JUNK.test(rel)) return [];
    return e.isDirectory() ? walk(full, base) : [rel];
  });
}

const collections = readJson(join(ROOT, "collections.json")) ?? [];
const collectionIds = new Set();
for (const c of collections) {
  if (!ID.test(c.id ?? "")) fail(`collections.json: bad id ${JSON.stringify(c.id)}`);
  if (collectionIds.has(c.id)) fail(`collections.json: duplicate id "${c.id}"`);
  if (!c.title) fail(`collections.json: "${c.id}" needs a title`);
  collectionIds.add(c.id);
}

const templates = [];
for (const id of readdirSync(TEMPLATES).sort()) {
  const dir = join(TEMPLATES, id);
  if (!statSync(dir).isDirectory()) continue;
  const where = `templates/${id}`;
  if (!ID.test(id)) fail(`${where}: folder name must be lowercase letters, digits and dashes`);
  const meta = readJson(join(dir, "template.json"));
  if (!meta) continue;

  if (!meta.title) fail(`${where}: "title" is required`);
  if (!meta.description) fail(`${where}: "description" is required`);
  if (!Number.isInteger(meta.version) || meta.version < 1) fail(`${where}: "version" must be a positive integer`);
  if (meta.level && !LEVELS.includes(meta.level)) fail(`${where}: "level" must be one of ${LEVELS.join(", ")}`);
  for (const c of meta.collections ?? []) {
    if (!collectionIds.has(c)) fail(`${where}: unknown collection "${c}" (add it to collections.json)`);
  }

  const files = walk(dir).filter((p) => p !== "template.json").sort();
  if (!files.length) fail(`${where}: no files besides template.json`);
  const hash = createHash("sha256");
  const entries = files.map((path) => {
    const bytes = readFileSync(join(dir, path));
    if (bytes.length > MAX_FILE_BYTES) fail(`${where}/${path}: larger than 5 MB`);
    hash.update(path).update("\0").update(bytes).update("\0");
    return { path, size: bytes.length };
  });
  for (const p of meta.open ?? []) {
    if (!files.includes(p)) fail(`${where}: "open" lists "${p}", which doesn't exist`);
  }

  templates.push({
    id,
    title: meta.title,
    description: meta.description,
    version: meta.version,
    order: meta.order ?? 0,
    collections: meta.collections ?? [],
    tags: meta.tags ?? [],
    ...(meta.level ? { level: meta.level } : {}),
    ...(meta.changes ? { changes: meta.changes } : {}),
    open: meta.open ?? [],
    files: entries,
    hash: hash.digest("hex").slice(0, 16),
  });
}
templates.sort((a, b) => a.order - b.order || a.id.localeCompare(b.id));

if (errors.length) {
  console.error(errors.map((e) => `error: ${e}`).join("\n"));
  process.exit(1);
}

const next = JSON.stringify({ schema: SCHEMA, collections, templates }, null, 2) + "\n";
const previous = existsSync(INDEX) ? readFileSync(INDEX, "utf8") : null;

if (process.argv.includes("--check")) {
  if (previous !== next) {
    console.error("index.json is out of date. Run `node scripts/build-index.mjs` and commit the result.");
    process.exit(1);
  }
  console.log(`index.json is up to date (${templates.length} templates).`);
  process.exit(0);
}

// Students only see "update available" when a version goes up, so point out
// content changes that kept the old version number.
const before = new Map((previous ? JSON.parse(previous).templates : []).map((t) => [t.id, t]));
for (const t of templates) {
  const old = before.get(t.id);
  if (old && old.hash !== t.hash && old.version === t.version) {
    console.warn(`note: ${t.id} changed but is still version ${t.version}. Bump "version" if students should be told.`);
  }
}
writeFileSync(INDEX, next);
console.log(`Wrote index.json (${templates.length} templates).`);
