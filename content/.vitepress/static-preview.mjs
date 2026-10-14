// Export the already-built content as a script-free, relocatable reading preview.
// Interactive search/navigation remain features of the normal VitePress build.
import { readFileSync, readdirSync, mkdirSync, writeFileSync, existsSync } from 'node:fs';
import { join, relative, dirname, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
const dist = fileURLToPath(new URL('./dist/', import.meta.url));
const out = join(dist, 'static-preview');
const contentCSS = readFileSync(new URL('./theme/content.css', import.meta.url), 'utf8');
const base = process.env.SITE_BASE || '/archatlas/';
const files = [];
const flat = name => name.split(sep).join('--');
function walk(dir) {
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === 'static-preview' || entry.name === 'assets') continue;
    const path = join(dir, entry.name);
    if (entry.isDirectory()) walk(path);
    else if (path.endsWith('.html') && entry.name !== '404.html') files.push(path);
  }
}
walk(dist);
const css = `:root{--vp-c-brand-1:#0b7169;--vp-c-divider:#d9e3e0;--vp-c-bg:#fff;--vp-c-bg-soft:#f3f7f6;--vp-c-text-2:#475b57}*{box-sizing:border-box}body{margin:0;background:#f5f8f7;color:#183a34;font:16px/1.75 system-ui,'Noto Sans CJK SC',sans-serif}header.preview-nav,main,footer{max-width:1050px;margin:auto;padding:20px 28px}header.preview-nav{display:flex;gap:18px;flex-wrap:wrap;border-bottom:1px solid #d9e3e0}a{color:#0b7169}h1{font-size:28px;line-height:1.35;margin:20px 0}h2{font-size:23px;margin-top:36px}h3{font-size:18px}p,li{max-width:85ch}pre{overflow:auto;padding:16px;background:#eaf1ef;border-radius:8px;font-size:14px}code{font-family:ui-monospace,monospace}table{display:block;overflow:auto;border-collapse:collapse}td,th{padding:10px;border:1px solid #ccd9d5;text-align:left}button,.header-anchor,.line-numbers-wrapper{display:none}.custom-block{padding:12px 18px;border-left:3px solid #b7791f;background:#fff7e6}.custom-block-title{font-weight:700}.translation-banner{padding:12px;background:#fff7e6;border-left:3px solid #b7791f}.atlas-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px}.type-card{padding:20px;background:white;border:1px solid #d9e3e0;border-radius:10px}.type-code,.atlas-kicker{font-size:12px;font-weight:700;letter-spacing:.07em;color:#0b7169}.type-status{font-size:13px;color:#475b57}.atlas-intro{font-size:19px}.atlas-figure{margin:26px 0;padding:18px;border:1px solid #d9e3e0;border-radius:10px;background:white}.figure-overview{overflow:auto}.figure-overview svg{display:block;width:100%;min-width:560px;height:auto}.figure-description,figcaption{font-size:14px}.figure-description{color:#475b57}.figure-actions{display:none}.preview-note{font-size:13px;color:#475b57}footer{font-size:13px;border-top:1px solid #d9e3e0}@media(max-width:640px){header.preview-nav,main,footer{padding:16px}.atlas-grid{grid-template-columns:1fr}.figure-overview svg{display:none}h1{font-size:25px}.atlas-figure{padding:12px}}`;
for (const file of files) {
  const name = relative(dist, file), directory = dirname(name);
  const prefix = '.';
  const html = readFileSync(file, 'utf8');
  const title = /<title>([\s\S]*?)<\/title>/.exec(html)?.[1] || 'archatlas';
  let body = /<main\b[^>]*>([\s\S]*?)<\/main>/.exec(html)?.[1];
  if (!body) throw new Error('No prerendered main content: ' + name);
  body = body.replace(/<dialog\b[\s\S]*?<\/dialog>/g, '').replace(/<script\b[\s\S]*?<\/script>/g, '').replace(/<button\b[\s\S]*?<\/button>/g, '');
  body = body.replace(/<div class="figure-actions">[\s\S]*?<\/div>/g, '');
  body = body.replace(/<form class="catalogue-filters"[\s\S]*?<\/form>/g, '<p class="preview-note">All types are shown in this reading preview. Query filters are available in the regular site build.</p>');
  // Export the same sanitized, server-rendered SVG for full-size access.
  let index = 0;
  body = body.replace(/<svg\b[\s\S]*?<\/svg>/g, svg => {
    const asset = flat(name).replace(/\.html$/, '') + '-figure-' + (++index) + '.svg';
    const target = join(out, asset); mkdirSync(dirname(target), {recursive:true}); writeFileSync(target, svg);
    const link = asset;
    return svg + '<p class="preview-note"><a href="' + link + '" target="_blank" rel="noopener noreferrer">Open full-size SVG / 查看完整图</a></p>';
  });
  body = body.replace(/href="([^"#][^"]*)"/g, (match, href) => {
    if (/^(?:https?:|mailto:|data:)/.test(href)) return match;
    let destination = href;
    if (base !== './' && destination.startsWith(base)) destination = '/' + destination.slice(base.length);
    const [pathname, fragment] = destination.split('#');
    if (pathname.endsWith('.svg')) return 'href="' + pathname + '"';
    let local = pathname.startsWith('/') ? pathname.slice(1) : relative(dist, resolve(dist, directory, pathname));
    if (!local || local.endsWith('/')) local += 'index.html';
    if (!local.endsWith('.html')) local += '.html';
    return 'href="' + flat(local) + (fragment ? '#' + fragment : '') + '"';
  });
  const output = '<!doctype html><html lang="' + (name.startsWith('zh/') ? 'zh-Hans' : 'en') + '"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + title + '</title><style>' + css + contentCSS + '</style></head><body><header class="preview-nav"><a href="' + prefix + '/index.html">archatlas</a><a href="' + prefix + '/use--index.html">Use the skill</a><a href="' + prefix + '/improve--index.html">Improve</a><a href="' + prefix + '/zh--index.html">简体中文</a></header><main><p class="preview-note">Static reading preview · Search and interactive controls are available in the normal site build.</p>' + body + '</main><footer>archatlas · Original material Apache-2.0 · Pre-release scaffold</footer></body></html>';
  const target = join(out, flat(name)); mkdirSync(dirname(target), {recursive:true}); writeFileSync(target, output);
}
// Verify local page/figure links in the exported snapshot.
for (const file of files) {
  const target = join(out, flat(relative(dist, file)));
  for (const [, href] of readFileSync(target, 'utf8').matchAll(/href="([^"]+)"/g)) {
    if (/^(?:https?:|mailto:|data:|#)/.test(href)) continue;
    const path = resolve(dirname(target), href.split('#')[0].split('?')[0]);
    if (!path.startsWith(out + sep) || !existsSync(path)) throw new Error('Broken preview link: ' + relative(out,target) + ' → ' + href);
  }
}
console.log('Static preview: ' + files.length + ' pages; local links verified. Output: ' + out);
