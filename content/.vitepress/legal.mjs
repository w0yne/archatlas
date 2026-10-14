// Audit modules actually emitted by the client build, not every installed package.
import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';
const here = dirname(fileURLToPath(import.meta.url));
const repo = resolve(here, '../..');
const require = createRequire(import.meta.url);
const overrides = JSON.parse(readFileSync(join(here,'licenses/overrides.json'),'utf8'));
export function packageNotice(dir) {
 const pkg = JSON.parse(readFileSync(join(dir, 'package.json'), 'utf8'));
 const files = readdirSync(dir).filter(name => /^(license|licence|copying|notice)([.-].*)?$/i.test(name)).sort();
 const override = overrides[pkg.name+'@'+pkg.version];
 if (!files.length && !override) throw new Error('Missing full licence text for ' + pkg.name);
 return { name: pkg.name, version: pkg.version, license: pkg.license,
  ...(override ? {source:override.source} : {}),
  text: files.length ? files.map(name => readFileSync(join(dir, name), 'utf8').trim()).join('\n\n') : readFileSync(join(here,'licenses',override.file),'utf8').trim() };
}
function packageRoot(id) {
 if (id.startsWith('\0vite/')) return dirname(require.resolve('vite/package.json'));
 if (!id.includes('/node_modules/')) return null;
 let dir = dirname(id.split('?')[0].replace(/^\0/, ''));
 while (dir !== dirname(dir)) {
  const path = join(dir, 'package.json');
  if (existsSync(path) && JSON.parse(readFileSync(path, 'utf8')).name) return dir;
  dir = dirname(dir);
 }
 throw new Error('Cannot identify bundled package: ' + id);
}
export function siteLegal() {
 let ssr = false;
 return {
  name: 'archatlas-site-legal', apply: 'build',
  configResolved(config) { ssr = Boolean(config.build.ssr); },
  generateBundle(_, bundle) {
   if (ssr) return;
   const roots = new Set();
   for (const output of Object.values(bundle)) {
    if (/\.(woff2?|ttf|otf)$/.test(output.fileName)) throw new Error('Unexpected font distribution: audit its licence first');
    if (output.type !== 'chunk') continue;
    for (const [id, module] of Object.entries(output.modules)) {
     if (!module.renderedLength && !/\.css(?:\?|$)/.test(id)) continue;
     const root = packageRoot(id); if (root) roots.add(root);
    }
   }
   const notices = [...roots].map(packageNotice).sort((a,b) => a.name.localeCompare(b.name));
   if (!notices.some(n => n.name === 'vitepress') || !notices.some(n => n.name === '@vue/runtime-dom')) throw new Error('Incomplete client module audit');
   // VitePress embeds Lucide/Feather icons in CSS, so no npm module ID identifies them.
   for (const [name, license, source] of [
    ['Lucide icons in VitePress', 'ISC', 'https://github.com/lucide-icons/lucide/blob/0.468.0/LICENSE'],
    ['Feather portions of Lucide', 'MIT', 'https://github.com/feathericons/feather/blob/v4.29.2/LICENSE']
   ]) notices.push({name, version:'vendored by VitePress 1.6.4', license, source,
    text:readFileSync(join(here,'licenses',license === 'ISC' ? 'lucide.txt' : 'feather.txt'),'utf8').trim()});
   const emit = (fileName, source) => this.emitFile({ type:'asset', fileName, source });
   emit('THIRD_PARTY_LICENSES.txt', 'Third-party code distributed with this documentation build\n\n'+notices.map(n => n.name+' — '+n.version+' ('+n.license+')\n'+(n.source ? n.source+'\n' : '')+'\n'+n.text).join('\n\n========================================\n\n')+'\n');
   emit('third-party-manifest.json', JSON.stringify(notices.map(({text,...item})=>item),null,2)+'\n');
   for (const [from,to] of [['LICENSE','LICENSE.txt'],['NOTICE','NOTICE.txt'],['THIRD_PARTY_NOTICES.md','THIRD_PARTY_NOTICES.txt'],['evals/reports/2026-10-14-first-full.md','evaluation-report.txt']]) emit(to,readFileSync(join(repo,from),'utf8'));
  }
 };
}
