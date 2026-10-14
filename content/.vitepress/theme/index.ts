import DefaultTheme from 'vitepress/theme-without-fonts';
import Layout from './Layout.vue';
import Figure from './Figure.vue';
import TypeCard from './TypeCard.vue';
import DecisionTree from './DecisionTree.vue';
import Catalogue from './Catalogue.vue';
import './style.css';
import './content.css';
export default { extends: DefaultTheme, Layout, enhanceApp({ app }) { app.component('Figure', Figure); app.component('TypeCard', TypeCard); app.component('DecisionTree', DecisionTree); app.component('Catalogue', Catalogue); } };
