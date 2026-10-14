<script setup>
import { computed } from 'vue';
import { withBase, useData } from 'vitepress';
const props = defineProps({ type: { type: Object, required: true } });
const { lang } = useData();
const locale = computed(() => lang.value.startsWith('zh') ? 'zh' : 'en');
const href = computed(() => withBase((locale.value === 'zh' ? '/zh' : '') + '/types/' + props.type.path + '.html'));
const question = computed(() => typeof props.type.question === 'string' ? props.type.question : props.type.question?.[locale.value]);
</script>
<template>
  <article class="type-card">
    <span class="type-code">{{ type.code }} · {{ type.family }}</span>
    <h3 :id="'type-' + type.code.toLowerCase()"><a v-if="type.available?.[locale]" :href="href">{{ type.names[locale] }}</a><span v-else>{{ type.names[locale] }}</span></h3>
    <p>{{ question }}</p>
    <p v-if="type.aliases?.[locale]?.length" class="type-status">{{ type.aliases[locale].join(' · ') }}</p>
    <span v-if="!type.available?.[locale]" class="type-status">{{ locale === 'zh' ? '内容待接入' : 'Reference in preparation' }}</span>
  </article>
</template>
