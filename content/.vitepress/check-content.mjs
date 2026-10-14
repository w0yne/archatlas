import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { join } from 'node:path';
import { sections } from './sections.mjs';
import { loadCatalog } from './catalog.mjs';
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
