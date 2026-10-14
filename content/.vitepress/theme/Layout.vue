<script setup>
import DefaultTheme from 'vitepress/theme-without-fonts';
import { useData } from 'vitepress';
import TypePage from './TypePage.vue';
const { frontmatter, lang } = useData();
</script>
<template>
  <DefaultTheme.Layout>
    <template #doc-before>
      <p v-if="lang.startsWith('zh') && frontmatter.reviewed !== true" class="translation-banner" role="note">中文翻译待审校 · Translation under review</p>
      <TypePage />
    </template>
  </DefaultTheme.Layout>
</template>
