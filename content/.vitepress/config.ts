import { defineConfig } from 'vitepress';
import { fileURLToPath } from 'node:url';
import { readFileSync } from 'node:fs';
import { join, relative, sep } from 'node:path';
import { createRequire } from 'node:module';
import { loadCatalog, typeSidebar, typeRewrites } from './catalog.mjs';
import { tokenize, catalogSearchHtml } from './search.mjs';
import { integrateContent, validateSelection } from './integrate-content.mjs';
import cjkEmphasis from './cjk-emphasis.mjs';
import { navFor, sidebarFor } from './navigation.mjs';
const contentRoot = fileURLToPath(new URL('..', import.meta.url));
const catalogue = loadCatalog(contentRoot);
const selection = validateSelection(JSON.parse(readFileSync(join(contentRoot, 'data/choose.json'), 'utf8')), catalogue);
const base = process.env.SITE_BASE || '/archatlas/';
if (!(base.startsWith('/') && base.endsWith('/')) && base !== './') throw new Error('SITE_BASE must be a directory path');
export default defineConfig({
  title: 'archatlas', description: 'Choose the right architecture view. Draw it from evidence.',
  srcDir: '.', outDir: './.vitepress/dist', cacheDir: './.vitepress/cache', base,
  rewrites: { ...typeRewrites(catalogue), 'en/use/glossary.md': 'glossary.md', 'en/use/catalogue.md': 'types/index.md', 'zh/use/catalogue.md': 'zh/types/index.md', 'en/:rest*': ':rest*' },
  markdown: { config(md) { md.use(cjkEmphasis); md.core.ruler.before('block', 'atlas-content-integration', state => { state.src = integrateContent(state.src, state.env.realPath ? relative(contentRoot, state.env.realPath).split(sep).join('/') : state.env.relativePath || '', catalogue, contentRoot); }); } },
  cleanUrls: false, lastUpdated: false,
  locales: { root: { label: 'English', lang: 'en' }, zh: { label: '简体中文', lang: 'zh-Hans', title: 'archatlas', description: '选对架构视图，以证据绘图。', themeConfig: { nav: navFor('zh'), sidebar: sidebarFor('zh', typeSidebar(catalogue, 'zh')), outline: { level: [2, 3], label: '本页内容' } } } },
  head: [['meta', { name: 'theme-color', content: '#0d766e' }]],
  themeConfig: {
    logo: undefined, siteTitle: 'archatlas', i18nRouting: false,
    nav: navFor('en'),
    sidebar: sidebarFor('en', typeSidebar(catalogue, 'en')),
    search: { provider: 'local', options: { _render: (src, env, md) => { const html = md.render(src, env); return env.frontmatter?.search === false ? '' : html + (env.relativePath === 'en/use/catalogue.md' ? catalogSearchHtml(catalogue) : ''); }, miniSearch: { options: { tokenize } }, locales: { zh: { translations: { button: { buttonText: '搜索', buttonAriaLabel: '搜索文档' }, modal: { noResultsText: '没有找到结果', resetButtonTitle: '清除搜索', footer: { selectText: '选择', navigateText: '切换', closeText: '关闭' } } } } } } },
    outline: { level: [2, 3], label: 'On this page' },
    footer: { message: 'Original code, documentation and examples: Apache-2.0.', copyright: 'Copyright © 2026 archatlas contributors' },
    catalogue, selection
  },
  vite: {
    server: { host: '127.0.0.1' }, preview: { host: '127.0.0.1' },
    resolve: { alias: [
      { find: 'vue/server-renderer', replacement: createRequire(import.meta.url).resolve('vue/server-renderer') },
      { find: /^vue$/, replacement: createRequire(import.meta.url).resolve('vue/dist/vue.runtime.esm-bundler.js') }
    ] },
    build: { chunkSizeWarningLimit: 1100 }
  }
});
