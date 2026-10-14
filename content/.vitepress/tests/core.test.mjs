import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, mkdtempSync, mkdirSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { parse } from 'yaml';
import { normalizeCatalog, loadCatalog, typeSidebar, typeRewrites } from '../catalog.mjs';
import { prepareSvg } from '../svg.mjs';
import { tokenize, catalogSearchHtml } from '../search.mjs';
import MiniSearch from 'minisearch';
const source = readFileSync(new URL('../fixtures/workflow.svg', import.meta.url), 'utf8');
const fixtureText = readFileSync(new URL('../fixtures/types.yaml', import.meta.url), 'utf8');
const rows = parse(fixtureText);
test('catalogue identities are validated and cannot escape a route', () => {
 assert.equal(normalizeCatalog(rows).length, 3);
 assert.throws(() => normalizeCatalog({types:[rows.types[0],rows.types[0]]}), /Duplicate/);
 assert.throws(() => normalizeCatalog({types:[{...rows.types[0],slug:'../escape'}]}), /Invalid/);
});
test('actual registry replaces fixture; only existing pages get links', () => {
 const root=mkdtempSync(join(tmpdir(),'atlas-catalog-'));
 try {
  mkdirSync(join(root,'.vitepress/fixtures'),{recursive:true});writeFileSync(join(root,'.vitepress/fixtures/types.yaml'),fixtureText);
  assert.equal(loadCatalog(root).fixture,true);
  mkdirSync(join(root,'data'));writeFileSync(join(root,'data/types.yaml'),JSON.stringify({types:[rows.types[1]]}));
  mkdirSync(join(root,'en/types'),{recursive:true});writeFileSync(join(root,'en/types/E1-sequence.md'),'---\ncode: E1\n---\n# Sequence');
  const cat=loadCatalog(root);assert.equal(cat.fixture,false);assert.equal(cat.types.length,1);
  assert.equal(typeSidebar(cat,'en')[0].items[0].link,'/types/e1-sequence');assert.deepEqual(typeSidebar(cat,'zh'),[]);
  assert.equal(typeRewrites(cat)['en/types/E1-sequence.md'],'types/e1-sequence.md');
 } finally {rmSync(root,{recursive:true,force:true});}
});
test('SVG ids, marker references and descriptions survive independent embeddings', () => {
 const a=prepareSvg(source,'first'),b=prepareSvg(source,'second');
 assert.match(a.svg,/id="first-arrow"/);assert.match(a.svg,/url\(#first-arrow\)/);assert.doesNotMatch(b.svg,/first-arrow/);
 assert.match(a.description,/question and audience/);assert.equal(prepareSvg(source,'first').svg,a.svg);
});
test('SVG rejects scripts, handlers, foreign objects and external URLs', () => {
 for(const insert of ['<script>alert(1)</script>','<foreignObject/>','<rect onclick="alert(1)"/>','<use href="https://example.com/a.svg"/>'])
  assert.throws(()=>prepareSvg(source.replace('</svg>',insert+'</svg>'),'safe'));
 assert.throws(()=>prepareSvg('<!DOCTYPE svg>'+source,'safe'));
 assert.throws(()=>prepareSvg(source.replace('url(#arrow)','url(#missing)'),'safe'),/Unresolved/);
 assert.throws(()=>prepareSvg(source.replace('</svg>','<g id="arrow"/></svg>'),'safe'),/duplicate/);
});
test('Chinese phrases and English aliases have useful search tokens', () => {
 assert.ok(tokenize('权限模型').includes('权限'));assert.ok(tokenize('上下文图').includes('上下文'));
 assert.deepEqual(tokenize('System Context Diagram'),['system','context','diagram']);
});
test('local search retrieves an English alias and Chinese phrase', () => {
 const index = new MiniSearch({ fields: ['text'], tokenize });
 index.addAll([{id:'context',text:'System context diagram'}, {id:'access',text:'权限模型：谁能做什么'}]);
 assert.equal(index.search('context diagram')[0].id,'context');
 assert.equal(index.search('权限')[0].id,'access');
 assert.match(catalogSearchHtml({types:normalizeCatalog(rows)}),/id="type-c2"/);
 assert.match(catalogSearchHtml({types:normalizeCatalog(rows)}),/context diagram/);
});
