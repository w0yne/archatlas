import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { posix } from 'node:path';
import { loadCatalog } from '../catalog.mjs';
import { integrateContent, validateSelection } from '../integrate-content.mjs';
import { filterTypes } from '../catalogue-view.mjs';
const root = fileURLToPath(new URL('../..', import.meta.url));
const catalog = loadCatalog(root);
const selection = JSON.parse(readFileSync(new URL('../../data/choose.json', import.meta.url),'utf8'));
test('the reader tree covers core and variants; method references stay explicitly addressable', () => {
 const result = validateSelection(selection,catalog);
 const covered = new Set(Object.values(result.tree).flatMap(branches => branches.flatMap(branch => branch.types)));
 assert.deepEqual([...covered].sort(),catalog.types.filter(type => type.catalogRole !== 'reference').map(type => type.code).sort());
 const bad = structuredClone(selection);bad.tree.value[0].types = ['Z99'];
 assert.throws(() => validateSelection(bad,catalog),/Invalid recommendation/);
});
test('missing known pages become coming-soon text, not ignored dead links', () => {
 const fixture = structuredClone(catalog);
 fixture.types[0].available.en = false;
 const absent = fixture.types[0];
 const present = fixture.types.find(type => type.available.en);
 const input = '[Waiting](/types/' + absent.path + ') [Ready](/types/' + present.path + ') [Unknown](/types/not-a-type)';
 const output = integrateContent(input,'en/choose.md',fixture,root);
 assert.match(output,/Coming soon/);assert.ok(!output.includes('](/types/'+absent.path+ ')'));
 assert.ok(output.includes('](/types/'+present.path+ ')'));assert.ok(output.includes('](/types/not-a-type)'));
});
test('relative type links follow canonical routes and preserve anchors', () => {
 const [a,b] = catalog.types.filter(type => type.available.en);
 const target = './' + posix.basename(b.source.en);
 const output = integrateContent('[Other](' + target + '#meaning)',a.source.en,catalog,root);
 assert.equal(output,'[Other](/types/' + b.path + '#meaning)');
});
test('choose rendering uses the data component without editing generated markdown', () => {
 const input = '# Choose\n<!-- BEGIN GENERATED: tree -->\nold\n<!-- END GENERATED: tree -->';
 const output = integrateContent(input,'en/choose.md',catalog,root);
 assert.match(output,/<DecisionTree \/>/);assert.ok(!output.includes('old'));
});
test('missing sample images are explicit placeholders with escaped alt text', () => {
 const output = integrateContent('![A <test>](/samples/not-present.svg)','en/types/example.md',catalog,root);
 assert.match(output,/sample-pending/);assert.match(output,/&lt;test&gt;/);assert.doesNotMatch(output,/<img/);
});
test('catalogue facets combine rather than widening the selection', () => {
 const family = catalog.types[0].family, audience = catalog.types[0].audiences[0];
 const result = filterTypes(catalog.types,{family,audience});
 assert.ok(result.length);assert.ok(result.every(type => type.family===family && type.audiences.includes(audience)));
 assert.deepEqual(filterTypes(catalog.types,{family:'not-a-family'}),[]);
});
