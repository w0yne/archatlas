export function catalogSearchHtml(catalog) {
  const escape = text => String(text).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  return catalog.types.map(type => '<h3 id="type-' + type.code.toLowerCase() + '">' + escape(type.names.en) + '</h3><p>' + escape((type.aliases?.en || []).join(' ')) + '</p>').join('');
}
export function tokenize(text) {
  const segmenter = new Intl.Segmenter('und', { granularity: 'word' });
  return [...segmenter.segment(text.toLowerCase())].filter(s => s.isWordLike).map(s => s.segment);
}
