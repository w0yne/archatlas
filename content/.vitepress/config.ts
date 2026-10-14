import { defineConfig } from 'vitepress';
import { fileURLToPath } from 'node:url';
import { existsSync } from 'node:fs';
import { join } from 'node:path';
import { createRequire } from 'node:module';
import { loadCatalog, typeSidebar, typeRewrites } from './catalog.mjs';
import { tokenize, catalogSearchHtml } from './search.mjs';
const contentRoot = fileURLToPath(new URL('..', import.meta.url));
const catalogue = loadCatalog(contentRoot);
const present = (path: string) => existsSync(join(contentRoot, 'en', path + '.md'));
const base = process.env.SITE_BASE || '/archatlas/';
if (!(base.startsWith('/') && base.endsWith('/')) && base !== './') throw new Error('SITE_BASE must be a directory path');
export default defineConfig({
  title: 'archatlas', description: 'Choose the right architecture view. Draw it from evidence.',
  srcDir: '.', outDir: './.vitepress/dist', cacheDir: './.vitepress/cache', base,
  rewrites: { ...typeRewrites(catalogue), 'en/:rest*': ':rest*' },
  cleanUrls: false, lastUpdated: false,
  locales: { root: { label: 'English', lang: 'en' }, zh: { label: '简体中文', lang: 'zh-Hans', title: 'archatlas', description: '选对架构视图，以证据绘图。' } },
  head: [['meta', { name: 'theme-color', content: '#0d766e' }]],
  themeConfig: {
    logo: undefined, siteTitle: 'archatlas', i18nRouting: false,
    nav: [{ text: 'Explore', link: '/#explore' }, ...(present('choose') ? [{ text: 'Choose a view', link: '/choose' }] : []), { text: 'Use the skill', link: '/use/' }, { text: 'Improve', link: '/improve/' }],
    sidebar: { '/zh/': [{ text: '开始', items: [{ text: '中文首页', link: '/zh/' }] }], '/': [
      ...(present('choose') ? [{ text: 'Start here', items: [{ text: 'Choose a view', link: '/choose' }] }] : []),
      ...typeSidebar(catalogue, 'en'),
      { text: 'Use the skill', items: [{ text: 'Install and first run', link: '/use/' }, { text: 'Autonomous or guided', link: '/use/modes' }, { text: 'From code to diagrams', link: '/use/code-to-diagram' }, { text: 'Formats and troubleshooting', link: '/use/formats' }] },
      { text: 'Improve', items: [{ text: 'Contribute', link: '/improve/' }, { text: 'Evaluate changes', link: '/improve/evals' }] }
    ] },
    search: { provider: 'local', options: { _render: (src, env, md) => { const html = md.render(src, env); return env.frontmatter?.search === false ? '' : html + (env.relativePath === 'en/index.md' ? catalogSearchHtml(catalogue) : ''); }, miniSearch: { options: { tokenize } }, locales: { zh: { translations: { button: { buttonText: '搜索', buttonAriaLabel: '搜索文档' }, modal: { noResultsText: '没有找到结果', resetButtonTitle: '清除搜索', footer: { selectText: '选择', navigateText: '切换', closeText: '关闭' } } } } } } },
    outline: { level: [2, 3], label: 'On this page' },
    footer: { message: 'Original code, documentation and examples: Apache-2.0.', copyright: 'Copyright © 2026 archatlas contributors' },
    catalogue
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
