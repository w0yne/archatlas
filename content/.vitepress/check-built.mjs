import { readFileSync, readdirSync, existsSync, statSync } from 'node:fs';
import { join, resolve, dirname, relative } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import MiniSearch from 'minisearch';
import { tokenize } from './search.mjs';
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
console.log('Built site: ' + pages.length + ' HTML pages; ' + checked + ' local links/assets/anchors verified; 2 English alias queries passed against the emitted search index.');
