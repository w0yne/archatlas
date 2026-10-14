import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import MarkdownIt from 'markdown-it';
import cjkEmphasis, { unparsedEmphasis } from '../cjk-emphasis.mjs';
import { navFor, sidebarFor } from '../navigation.mjs';
import { integrateContent } from '../integrate-content.mjs';
const data = JSON.parse(readFileSync(new URL('../../data/choose.json',import.meta.url),'utf8'));
test('CJK emphasis renders without changing code or ordinary English', () => {
 const md = new MarkdownIt().use(cjkEmphasis);
 assert.match(md.render('**定义：**正文'), /<strong>定义：<\/strong>正文/);
 assert.deepEqual(unparsedEmphasis(md.parse('**定义：**正文',{})), []);
 assert.equal(md.render('**Definition:** text'), new MarkdownIt().render('**Definition:** text'));
 assert.deepEqual(unparsedEmphasis(md.parse('    **literal code**',{})), []);
});
test('beginner defaults and curated cells cover the review requests', () => {
 assert.equal(data.common_requests.length,8);
 assert.ok(data.common_requests.some(row=>row.first==='C2' && row.next.includes('C3') && row.next.includes('E1')));
 assert.ok(data.tree.runtime.some(row=>row.types.includes('A8')));
 assert.ok(data.matrix.leaders.runtime.includes('G2'));
 assert.ok(data.matrix.business.security.includes('F3'));
 for (const picks of Object.values(data.phase_picks)) assert.ok(picks.length>=2 && picks.length<=4);
 assert.ok(data.terms.some(term=>term.en==='application architecture diagram' && term.note.en.includes('running applications and data stores')));
});
test('multiline reference blocks collapse without losing content', () => {
 const body = '<!-- BEGIN GENERATED: matrix -->\n| Question | Types |\n| Runtime | G2 |\n<!-- END GENERATED: matrix -->';
 const result = integrateContent(body,'en/choose.md',{types:[]},'.');
 assert.match(result, /<details class="reference-details">/);
 assert.ok(result.includes('| Runtime | G2 |'));
 assert.ok(!result.includes('BEGIN GENERATED'));
});
test('Chinese navigation exposes choose, reader glossary and terminology table', () => {
 assert.ok(navFor('zh').some(item=>item.link==='/zh/choose'));
 assert.ok(navFor('zh').some(item=>item.link==='/zh/use/glossary'));
 assert.ok(sidebarFor('zh',[])[0].items.some(item=>item.link==='/zh/glossary'));
 assert.ok(navFor('en').some(item=>item.link==='/glossary'));
});
