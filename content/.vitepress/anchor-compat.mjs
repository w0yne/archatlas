// A pinned public-build inventory, independent of the current navigation model.
import { readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';

export function checkAnchorCompatibility(root, baseline) {
 const missingPages = [], missingAnchors = {};
 let checkedIds = 0;
 for (const [page, ids] of Object.entries(baseline.pages)) {
  checkedIds += ids.length;
  const path = join(root, page);
  if (!existsSync(path)) { missingPages.push(page); continue; }
  const actual = new Set([...readFileSync(path, 'utf8').matchAll(/\bid="([^"]+)"/g)].map(m => m[1]));
  const missing = ids.filter(id => !actual.has(id));
  if (missing.length) missingAnchors[page] = missing;
 }
 return { baseline: baseline.baseline, oldPages: Object.keys(baseline.pages).length,
  checkedIds, missingPages, missingAnchors,
  missingCount: Object.values(missingAnchors).reduce((n, ids) => n + ids.length, 0) };
}
