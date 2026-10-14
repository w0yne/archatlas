import { existsSync } from 'node:fs';
import { join, posix } from 'node:path';
import { ui } from './i18n.mjs';
const escape = text => text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
export function integrateContent(source, relativePath, catalog, contentRoot) {
 const locale = relativePath.startsWith('zh/') ? 'zh' : 'en';
 if (relativePath === 'en/choose.md' || relativePath === 'zh/choose.md') {
  source = source.replace(/<!-- BEGIN GENERATED: tree -->[\s\S]*?<!-- END GENERATED: tree -->/, '<DecisionTree />');
  for (const name of ['matrix','terms','aliases','catalogue']) {
   const pattern = new RegExp('<!-- BEGIN GENERATED: ' + name + ' -->([\\s\\S]*?)<!-- END GENERATED: ' + name + ' -->');
   source = source.replace(pattern, (_, text) => '<details class="reference-details"><summary>' + (locale === 'zh' ? '展开参考列表' : 'Expand reference list') + '</summary>\n\n' + text.trim() + '\n\n</details>');
  }
 }
 source = source.replace(/(?<!!)\[([^\]]+)\]\((\.{1,2}\/[^)\s#]+\.md)(#[^)\s]*)?\)/g, (match, label, path, hash) => {
  const target = posix.normalize(posix.join(posix.dirname(relativePath), path));
  const type = catalog.types.find(type => type.source?.[locale] === target);
  return type ? '[' + label + '](' + (locale === 'zh' ? '/zh' : '') + '/types/' + type.path + (hash || '') + ')' : match;
 });
 source = source.replace(/(?<!!)\[([^\]]+)\]\((\/(?:zh\/)?types\/[^)\s]+)\)/g, (match, label, target) => {
  const path = target.split('#')[0].replace(/^\/(?:zh\/)?types\//, '').replace(/\.html$/, '');
  const type = catalog.types.find(type => type.path === path);
  const targetLocale = target.startsWith('/zh/') ? 'zh' : 'en';
  return type && !type.available[targetLocale] ? label + ' <span class="coming-soon">(' + ui[locale].coming + ')</span>' : match;
 });
 source = source.replace(/!\[([^\]]*)\]\((\/samples\/[A-Za-z0-9_./-]+\.svg)\)/g, (match, alt, path) => {
  if (path.includes('..')) throw new Error('Invalid sample path');
  return existsSync(join(contentRoot, 'public', path.slice(1))) ? match : '<div class="sample-pending" role="note"><strong>' + ui[locale].sample + '</strong><p>' + escape(alt) + '</p></div>';
 });
 return source;
}
export function validateSelection(selection, catalog) {
 if (!selection?.tree || !selection?.facets?.asks) throw new Error('Selection needs tree and question facets');
 const codes = new Set(catalog.types.map(type => type.code));
 for (const [key, branches] of Object.entries(selection.tree)) {
  if (!selection.facets.asks[key]?.en || !selection.facets.asks[key]?.zh || !Array.isArray(branches)) throw new Error('Invalid decision branch');
  for (const branch of branches) if (!branch.when?.en || !branch.when?.zh || !Array.isArray(branch.types) || branch.types.some(code => !codes.has(code))) throw new Error('Invalid recommendation');
 }
 return { tree: selection.tree, facets: selection.facets, first_questions: selection.first_questions };
}
