<script setup>
import { useData } from 'vitepress';
const { frontmatter, lang } = useData();
</script>
<template>
  <header v-if="frontmatter.code" class="type-page-header">
    <span class="type-code">{{ frontmatter.code }} · {{ frontmatter.family }}</span>
    <p v-if="frontmatter.question">{{ typeof frontmatter.question === 'string' ? frontmatter.question : frontmatter.question[lang.startsWith('zh') ? 'zh' : 'en'] }}</p>
    <p class="type-definition">{{ lang.startsWith('zh') ? '从含义到记法、绘图步骤、源码证据与原创样例。' : 'Meaning, notation, drawing recipe, repository evidence and an original sample.' }}</p>
  </header>
</template>
