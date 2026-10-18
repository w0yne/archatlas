import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, mkdirSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { checkAnchorCompatibility } from '../anchor-compat.mjs';

test('compatibility includes catalogue and non-type pages, even unreferenced IDs', () => {
 const root = mkdtempSync(join(tmpdir(), 'atlas-anchors-'));
 try {
  mkdirSync(join(root, 'types'));
  writeFileSync(join(root, 'types/index.html'), '<a id="type-f1" href="e1.html#variant-f1">F1</a>');
  writeFileSync(join(root, 'choose.html'), '<h1 id="choose">Choose</h1>');
  const baseline = { baseline: 'fixture', pages: {
   'types/index.html': ['type-f1', 'family-I'], 'choose.html': ['choose', 'old-choice'], 'about.html': ['about']
  } };
  const result = checkAnchorCompatibility(root, baseline);
  assert.equal(result.oldPages, 3);
  assert.equal(result.checkedIds, 5);
  assert.deepEqual(result.missingPages, ['about.html']);
  assert.deepEqual(result.missingAnchors, { 'types/index.html': ['family-I'], 'choose.html': ['old-choice'] });
  assert.equal(result.missingCount, 2);
 } finally { rmSync(root, { recursive: true, force: true }); }
});
