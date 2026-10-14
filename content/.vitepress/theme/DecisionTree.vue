<script setup>
import { computed } from 'vue';
import { useData, withBase } from 'vitepress';
import { ui } from '../i18n.mjs';
const { theme, lang } = useData();
const locale = computed(() => lang.value.startsWith('zh') ? 'zh' : 'en');
const t = computed(() => ui[locale.value]);
const typeFor = code => theme.value.catalogue.types.find(type => type.code === code);
const linkFor = type => withBase((locale.value === 'zh' ? '/zh' : '') + '/types/' + type.path + '.html');
</script>
<template>
 <div class="decision-tree" :aria-label="t.choose">
  <details v-for="(branches, key, index) in theme.selection.tree" :key="key" class="decision-branch" :open="index === 0">
   <summary>{{ theme.selection.facets.asks[key][locale] }}</summary>
   <ul>
    <li v-for="(branch, n) in branches" :key="n">
     <p class="branch-question">{{ branch.when[locale] }}</p>
     <ul :aria-label="t.recommendations" class="recommendations">
      <li v-for="code in branch.types" :key="code">
       <a v-if="typeFor(code).available[locale]" :href="linkFor(typeFor(code))">{{ code }} · {{ typeFor(code).names[locale] }}</a>
       <span v-else>{{ code }} · {{ typeFor(code).names[locale] }} <span class="coming-soon">({{ t.coming }})</span></span>
      </li>
     </ul>
     <p v-if="branch.hint" class="branch-hint">{{ branch.hint[locale] }}</p>
    </li>
   </ul>
  </details>
 </div>
</template>
