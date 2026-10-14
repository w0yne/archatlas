import { DOMParser, XMLSerializer } from '@xmldom/xmldom';
const tags = new Set(['svg','g','defs','marker','path','rect','line','polyline','polygon','circle','ellipse','text','tspan','title','desc','clipPath','linearGradient','radialGradient','stop','use']);
const attrs = new Set(['xmlns','id','viewBox','width','height','x','y','x1','y1','x2','y2','cx','cy','r','rx','ry','d','points','transform','fill','fill-opacity','fill-rule','stroke','stroke-width','stroke-opacity','stroke-dasharray','stroke-linecap','stroke-linejoin','opacity','font-family','font-size','font-weight','font-style','text-anchor','dominant-baseline','dx','dy','marker-start','marker-mid','marker-end','markerWidth','markerHeight','refX','refY','orient','markerUnits','clip-path','clipPathUnits','gradientUnits','gradientTransform','offset','stop-color','stop-opacity','preserveAspectRatio','href','role','aria-label','aria-labelledby','aria-describedby','data-id']);
export function prepareSvg(source, prefix) {
  if (typeof source !== 'string' || source.length > 2_000_000 || !/^[A-Za-z][A-Za-z0-9_-]*$/.test(prefix)) throw new Error('Invalid SVG input or prefix');
  if (/<!DOCTYPE|<!ENTITY|<\?(?!xml\s)/i.test(source)) throw new Error('SVG declarations are not allowed');
  const doc = new DOMParser({ onError: (level, message) => { throw new Error('Invalid SVG: ' + message); } }).parseFromString(source, 'image/svg+xml');
  const root = doc.documentElement;
  if (root?.tagName !== 'svg' || !root.getAttribute('viewBox')) throw new Error('SVG needs a viewBox');
  const elements = [root, ...Array.from(root.getElementsByTagName('*'))];
  const ids = new Map();
  for (const el of elements) {
    if (!tags.has(el.tagName)) throw new Error('Unsupported SVG element: ' + el.tagName);
    const id = el.getAttribute('id');
    if (id) { if (!/^[A-Za-z_][A-Za-z0-9_.:-]*$/.test(id) || ids.has(id)) throw new Error('Invalid or duplicate SVG id'); ids.set(id, prefix + '-' + id); }
  }
  const ref = id => { if (!ids.has(id)) throw new Error('Unresolved SVG reference: ' + id); return ids.get(id); };
  for (const el of elements) for (const attr of Array.from(el.attributes)) {
    const name = attr.name; let value = attr.value;
    if (/^on/i.test(name)) throw new Error('SVG event handlers are not allowed');
    if (!attrs.has(name)) { el.removeAttribute(name); continue; }
    if (name === 'xmlns' && value !== 'http://www.w3.org/2000/svg') throw new Error('Unexpected SVG namespace');
    if ((/javascript:|data:|https?:/i.test(value) || value.includes('//')) && name !== 'xmlns') throw new Error('External SVG resources are not allowed');
    if (name === 'id') value = ref(value);
    if (name === 'href') { if (!value.startsWith('#')) throw new Error('SVG href must be local'); value = '#' + ref(value.slice(1)); }
    if (name === 'aria-labelledby' || name === 'aria-describedby') value = value.split(/\s+/).map(ref).join(' ');
    if (/url\s*\(/i.test(value)) {
      if (!/^url\(#[A-Za-z_][A-Za-z0-9_.:-]*\)$/.test(value)) throw new Error('SVG URL must be a local fragment');
      value = 'url(#' + ref(value.slice(5, -1)) + ')';
    }
    el.setAttribute(name, value);
  }
  root.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
  root.setAttribute('role', 'img');
  const title = root.getElementsByTagName('title')[0]?.textContent?.trim();
  const description = root.getElementsByTagName('desc')[0]?.textContent?.trim();
  if (!title || !description) throw new Error('SVG needs a title and description');
  root.setAttribute('aria-label', title);
  return { svg: new XMLSerializer().serializeToString(root), description };
}
