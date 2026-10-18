import { readFileSync, readdirSync, existsSync, statSync } from 'node:fs';
import { join, resolve, dirname, relative } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import MiniSearch from 'minisearch';
import { tokenize } from './search.mjs';
import { checkAnchorCompatibility } from './anchor-compat.mjs';
const root = fileURLToPath(new URL('./dist/', import.meta.url));
const base = process.env.SITE_BASE || '/archatlas/';
const pages = [];
function walk(dir) {
 for (const entry of readdirSync(dir, { withFileTypes: true })) {
  if (entry.name === 'static-preview') continue;
  const path = join(dir, entry.name);
  if (entry.isDirectory()) walk(path);
  else if (entry.name.endsWith('.html')) pages.push(path);
 }
}
walk(root);
const compatibility = checkAnchorCompatibility(root,
 JSON.parse(readFileSync(new URL('./fixtures/anchors-2eabce8.json', import.meta.url), 'utf8')));
if (compatibility.missingPages.length || compatibility.missingCount)
 throw new Error('Baseline page/anchor compatibility failed: ' + JSON.stringify(compatibility));
console.log('Baseline compatibility: ' + compatibility.oldPages + ' pages / ' + compatibility.checkedIds + ' IDs retained.');
let checked = 0;
for (const page of pages) for (const [, raw] of readFileSync(page, 'utf8').matchAll(/(?:href|src)="([^"]+)"/g)) {
 if (/^(?:[a-z][a-z0-9+.-]*:|\/\/)/i.test(raw)) continue;
 const href = raw.replace(/&amp;/g, '&');
 const [address, hash] = href.split('#');
 const pathname = decodeURIComponent(address.split('?')[0]);
 let target;
 if (!pathname) target = page;
 else if (pathname.startsWith(base) && base !== './') target = resolve(root, pathname.slice(base.length));
 else if (pathname.startsWith('/')) throw new Error('Link outside configured base: ' + href);
 else target = resolve(dirname(page), pathname);
 if (relative(root,target).startsWith('..')) throw new Error('Link escapes built site: ' + href);
 if (existsSync(target) && statSync(target).isDirectory()) target = join(target, 'index.html');
 if (!existsSync(target) && existsSync(target + '.html')) target += '.html';
 if (!existsSync(target)) throw new Error('Broken built link: ' + relative(root,page) + ' -> ' + href);
 if (hash && target.endsWith('.html')) {
  const id = decodeURIComponent(hash);
  const ids = [...readFileSync(target,'utf8').matchAll(/\bid="([^"]+)"/g)].map(match => match[1]);
  if (!ids.includes(id)) throw new Error('Missing anchor: ' + relative(root,page) + ' -> ' + href);
 }
 checked++;
}
const chunks = join(root, 'assets/chunks');
const indexFile = readdirSync(chunks).find(file => file.startsWith('@localSearchIndexroot.'));
if (!indexFile) throw new Error('Missing built local search index');
const { default: data } = await import(pathToFileURL(join(chunks,indexFile)).href);
const index = MiniSearch.loadJSON(data, { fields: ['title','titles','text'], storeFields: ['title','titles'], tokenize });
for (const [query, code] of [['context diagram','c2'],['permission matrix','f3']]) {
 const results = index.search(query);
 if (!results.some(result => result.id.endsWith('#type-' + code))) throw new Error('Catalogue alias not discoverable: ' + query);
}
const legalText = readFileSync(join(root,'THIRD_PARTY_LICENSES.txt'),'utf8');
const legalManifest = JSON.parse(readFileSync(join(root,'third-party-manifest.json'),'utf8'));
for (const entry of legalManifest) if (!legalText.includes(entry.name) || !legalText.includes(entry.version)) throw new Error('Missing distributed notice: '+entry.name);
for (const file of ['LICENSE.txt','NOTICE.txt','THIRD_PARTY_NOTICES.txt','evaluation-report.txt']) if (!readFileSync(join(root,file),'utf8').trim()) throw new Error('Empty distribution file: '+file);
if (!legalText.includes('Permission is hereby granted') || !legalText.includes('Lucide Contributors') || !legalText.includes('Cole Bemis')) throw new Error('Incomplete licence texts');
console.log('Distributed notices: '+legalManifest.length+' entries; full texts and legal/report assets present.');
console.log('Built site: ' + pages.length + ' HTML pages; ' + checked + ' local links/assets/anchors verified; 2 English alias queries passed against the emitted search index.');
