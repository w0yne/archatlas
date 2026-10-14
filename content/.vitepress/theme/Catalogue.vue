<script setup>
import { computed, ref, onMounted, onUnmounted, watch } from 'vue';
import { useData, useRoute, withBase } from 'vitepress';
import { filterTypes } from '../catalogue-view.mjs';
import { ui } from '../i18n.mjs';
const { theme, lang } = useData();
const route = useRoute();
const locale = computed(() => lang.value.startsWith('zh') ? 'zh' : 'en');
const t = computed(() => ui[locale.value]);
const applied = ref({}), draft = ref({});
const fields = ['family','audience','level','phase'];
const options = field => field === 'family' ? theme.value.catalogue.families : theme.value.catalogue.facets[field === 'audience' ? 'audiences' : field === 'level' ? 'levels' : 'phases'];
function sync() {
 if (typeof window === 'undefined') return;
 const params = new URLSearchParams(window.location.search), values = {};
 for (const field of fields) values[field] = options(field)?.[params.get(field)] ? params.get(field) : '';
 applied.value = values; draft.value = { ...values };
}
onMounted(() => { sync(); window.addEventListener('popstate',sync); window.addEventListener('hashchange',sync); });
onUnmounted(() => { window.removeEventListener('popstate',sync); window.removeEventListener('hashchange',sync); });
watch(() => route.path, sync);
const types = computed(() => filterTypes(theme.value.catalogue.types, applied.value));
const families = computed(() => Object.entries(theme.value.catalogue.families).filter(([key]) => types.value.some(type => type.family === key)));
const href = computed(() => withBase(locale.value === 'zh' ? '/zh/types/' : '/types/'));
</script>
<template>
 <div class="catalogue">
  <form class="catalogue-filters" method="get" :action="href">
   <label v-for="field in fields" :key="field">{{ t[field] }}
    <select :name="field" v-model="draft[field]"><option value="">{{ t.all }}</option><option v-for="(label, key) in options(field)" :key="key" :value="key">{{ label[locale] }}</option></select>
   </label>
   <button type="submit">{{ t.apply }}</button><a :href="href">{{ t.reset }}</a>
  </form>
  <p class="catalogue-count" aria-live="polite">{{ types.length }} / {{ theme.catalogue.types.length }} · {{ types.filter(type => type.available[locale]).length }} {{ t.ready }}</p>
  <nav class="family-jumps" :aria-label="t.family"><a v-for="[key, label] in families" :key="key" :href="'#family-' + key">{{ key }} · {{ label[locale] }}</a></nav>
  <p v-if="!types.length">{{ t.empty }}</p>
  <section v-for="[key, label] in families" :key="key" class="catalogue-family">
   <h2 :id="'family-' + key">{{ key }} · {{ label[locale] }}</h2>
   <div class="atlas-grid"><TypeCard v-for="type in types.filter(type => type.family === key)" :key="type.code" :type="type" /></div>
  </section>
 </div>
</template>
