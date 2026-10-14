import DefaultTheme from 'vitepress/theme-without-fonts';
import Layout from './Layout.vue';
import Figure from './Figure.vue';
import TypeCard from './TypeCard.vue';
import './style.css';
export default { extends: DefaultTheme, Layout, enhanceApp({ app }) { app.component('Figure', Figure); app.component('TypeCard', TypeCard); } };
