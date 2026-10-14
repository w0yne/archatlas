<script setup>
import { computed } from 'vue';
import { useData } from 'vitepress';
import { terms } from '../glossary-terms.mjs';
const { lang } = useData();
const locale = computed(() => lang.value.startsWith('zh') ? 'zh' : 'en');
</script>
<template><dl class="concept-glossary"><template v-for="term in terms" :key="term.id"><dt :id="term.id">{{ term.name[locale] }}</dt><dd>{{ term.meaning[locale] }}</dd></template></dl></template>
