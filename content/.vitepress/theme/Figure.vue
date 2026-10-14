<script setup>
import { computed, ref, useId } from 'vue';
import { useData } from 'vitepress';
import { prepareSvg } from '../svg.mjs';
const props = defineProps({ svg: { type: String, required: true }, caption: { type: String, required: true }, model: { type: [String, Object], default: null } });
const { lang } = useData();
const uid = 'figure-' + useId().replace(/[^A-Za-z0-9_-]/g, '-');
const figure = computed(() => prepareSvg(props.svg, uid));
const full = computed(() => prepareSvg(props.svg, uid + '-full'));
const svgUrl = computed(() => 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(figure.value.svg));
const modelUrl = computed(() => props.model ? 'data:application/json;charset=utf-8,' + encodeURIComponent(typeof props.model === 'string' ? props.model : JSON.stringify(props.model, null, 2)) : null);
const dialog = ref();
const zh = computed(() => lang.value.startsWith('zh'));
</script>
<template>
  <figure class="atlas-figure">
    <div class="figure-overview" v-html="figure.svg" />
    <figcaption>{{ caption }}</figcaption>
    <p class="figure-description">{{ figure.description }}</p>
    <div class="figure-actions">
      <button type="button" @click="dialog.showModal()">{{ zh ? '查看完整图' : 'Open full size' }}</button>
      <a :href="svgUrl" download="diagram.svg">{{ zh ? '下载 SVG' : 'Download SVG' }}</a>
      <a v-if="modelUrl" :href="modelUrl" download="diagram.json">{{ zh ? '下载模型 JSON' : 'Download model JSON' }}</a>
    </div>
    <dialog ref="dialog" class="figure-dialog" :aria-label="caption">
      <button type="button" class="figure-close" @click="dialog.close()">{{ zh ? '关闭' : 'Close' }}</button>
      <div class="figure-full" v-html="full.svg" />
      <p>{{ figure.description }}</p>
    </dialog>
  </figure>
</template>
