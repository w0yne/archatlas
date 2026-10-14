// Use the upstream CJK delimiter rules in both VitePress and Markdown checks.
// The site package must pin markdown-it-cjk-friendly to 3.0.0.
import cjkFriendly from 'markdown-it-cjk-friendly';

export default function cjkEmphasis(md) {
  md.use(cjkFriendly);
}

// Inspect parsed prose, not raw Markdown: code examples containing ** are valid.
// Call after md.parse() with the same plugins used by the site.
export function unparsedEmphasis(tokens) {
  const findings = [];
  const visit = (items, lines) => {
    for (const token of items) {
      const location = token.map ?? lines;
      if (token.type === 'text' && token.content.includes('**')) {
        findings.push({ lines: location, text: token.content });
      }
      if (token.children) visit(token.children, location);
    }
  };
  visit(tokens, null);
  return findings;
}
