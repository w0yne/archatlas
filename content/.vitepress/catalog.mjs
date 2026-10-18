import { readFileSync, existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { parse } from 'yaml';
export function normalizeCatalog(raw) {
  const rows = Array.isArray(raw) ? raw : raw?.types;
  if (!Array.isArray(rows) || !rows.length) throw new Error('Catalogue must contain a nonempty types array');
  const codes = new Set(), paths = new Set();
  return rows.map(row => {
    if (!/^[A-I][1-9][0-9]*$/.test(row.code) || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(row.slug)) throw new Error('Invalid catalogue code/slug');
    if (!row.names?.en || !row.names?.zh || !row.family) throw new Error('Catalogue needs names.en, names.zh and family');
    const path = row.code.toLowerCase() + '-' + row.slug;
    if (codes.has(row.code) || paths.has(path)) throw new Error('Duplicate catalogue identity');
    codes.add(row.code); paths.add(path);
    return { ...row, path };
  });
}
export function loadCatalog(contentRoot) {
  const actual = join(contentRoot, 'data/types.yaml');
  const fixture = !existsSync(actual);
  const data = parse(readFileSync(fixture ? join(contentRoot, '.vitepress/fixtures/types.yaml') : actual, 'utf8'));
  const types = normalizeCatalog(data);
  const pages = { en: new Map(), zh: new Map() };
  for (const lang of ['en', 'zh']) {
    const dir = join(contentRoot, lang, 'types');
    if (!existsSync(dir)) continue;
    for (const file of readdirSync(dir).filter(file => file.endsWith('.md'))) {
      const text = readFileSync(join(dir, file), 'utf8');
      const frontmatter = /^---\r?\n([\s\S]*?)\r?\n---/.exec(text)?.[1];
      const code = frontmatter ? parse(frontmatter)?.code : undefined;
      if (!code) throw new Error('Type page needs a catalogue code: ' + file);
      if (pages[lang].has(code)) throw new Error('Duplicate type page: ' + code);
      pages[lang].set(code, lang + '/types/' + file);
    }
  }
  return { fixture, families: data.families || {}, facets: data.facets || {}, types: types.map(type => ({ ...type,
    available: { en: pages.en.has(type.code), zh: pages.zh.has(type.code) },
    source: { en: pages.en.get(type.code), zh: pages.zh.get(type.code) }
  })) };
}
export function typeRewrites(catalog) {
  const rewrites = {};
  for (const type of catalog.types) for (const lang of ['en', 'zh']) {
    if (type.source[lang]) rewrites[type.source[lang]] = (lang === 'zh' ? 'zh/' : '') + 'types/' + type.path + '.md';
  }
  return rewrites;
}
export function typeSidebar(catalog, lang) {
  const groups = new Map();
  for (const type of catalog.types.filter(t => t.available[lang] && (!t.catalogRole || t.catalogRole === 'core'))) {
    if (!groups.has(type.family)) groups.set(type.family, []);
    groups.get(type.family).push({ text: type.code + ' · ' + type.names[lang], link: (lang === 'zh' ? '/zh' : '') + '/types/' + type.path });
  }
  return [...groups].map(([family, items]) => ({ text: family + (catalog.families?.[family]?.[lang] ? ' · ' + catalog.families[family][lang] : ''), collapsed: true, items }));
}
