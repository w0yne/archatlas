import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { join } from 'node:path';
import { sections } from './sections.mjs';
import { loadCatalog } from './catalog.mjs';
import MarkdownIt from 'markdown-it';
import cjkEmphasis, { unparsedEmphasis } from './cjk-emphasis.mjs';
const root=fileURLToPath(new URL('..',import.meta.url));
const catalog=loadCatalog(root);
let pages=0;
for(const lang of ['en','zh']){
 const dir=join(root,lang,'types');if(!existsSync(dir))continue;
 for(const file of readdirSync(dir).filter(n=>n.endsWith('.md'))){
  const text=readFileSync(join(dir,file),'utf8');
  for(const [id] of sections) if(!text.includes('{#'+id+'}')&&!text.includes('id="'+id+'"'))throw new Error(file+' missing section #'+id);
  pages++;
 }
}
console.log('Catalogue: '+catalog.types.length+' types ('+(catalog.fixture?'scaffold fixture':'canonical registry')+'); '+pages+' type pages checked.');
if(catalog.fixture)console.log('Integration pending: canonical catalogue and type pages are not present.');
const md = new MarkdownIt({ html: true }).use(cjkEmphasis);
let proseErrors = 0, checkedPages = 0;
function checkProse(dir) {
 for (const entry of readdirSync(dir, { withFileTypes: true })) {
  const file = join(dir, entry.name);
  if (entry.isDirectory()) checkProse(file);
  else if (entry.name.endsWith('.md')) {
   const body = readFileSync(file, 'utf8').replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, '');
   const findings = unparsedEmphasis(md.parse(body, {})); checkedPages++;
   for (const finding of findings) { console.error(file.slice(root.length) + ': literal ** in prose: ' + finding.text); proseErrors++; }
  }
 }
}
for (const lang of ['en', 'zh']) checkProse(join(root, lang));
console.log('Parsed prose emphasis: ' + checkedPages + ' pages, ' + proseErrors + ' findings.');
if (proseErrors) process.exitCode = 1;
