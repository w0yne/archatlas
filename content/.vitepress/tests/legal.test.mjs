import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, writeFileSync, rmSync, readFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { packageNotice, siteLegal } from '../legal.mjs';
test('missing licence text fails closed; supplied text is preserved in full', () => {
 const dir=mkdtempSync(join(tmpdir(),'archatlas-legal-'));
 try {
  writeFileSync(join(dir,'package.json'),JSON.stringify({name:'fixture',version:'1',license:'MIT'}));
  assert.throws(()=>packageNotice(dir),/Missing full licence/);
  const text='Copyright fixture\nPermission is hereby granted\nALL TERMS RETAINED';
  writeFileSync(join(dir,'LICENSE'),text);
  assert.equal(packageNotice(dir).text,text);
 } finally {rmSync(dir,{recursive:true,force:true});}
});
test('site notice output covers emitted code, embedded icons and original legal files', () => {
 const plugin=siteLegal(), assets=new Map();plugin.configResolved({build:{ssr:false}});
 const module=(name)=>new URL('../node_modules/'+name,import.meta.url).pathname;
 plugin.generateBundle.call({emitFile(asset){assets.set(asset.fileName,asset.source)}},{},{app:{type:'chunk',fileName:'app.js',modules:{
  [module('vitepress/dist/client/app/index.js')]:{renderedLength:100},
  [module('@vue/runtime-dom/dist/runtime-dom.esm-bundler.js')]:{renderedLength:100}
 }}});
 const notices=assets.get('THIRD_PARTY_LICENSES.txt');
 assert.match(notices,/Permission is hereby granted/);assert.match(notices,/THE SOFTWARE IS PROVIDED/);
 assert.match(notices,/Lucide Contributors/);assert.match(notices,/Cole Bemis/);
 assert.equal(assets.get('LICENSE.txt'),readFileSync(new URL('../../../LICENSE',import.meta.url),'utf8'));
 assert.ok(assets.get('third-party-manifest.json'));assert.ok(assets.get('evaluation-report.txt'));
});
