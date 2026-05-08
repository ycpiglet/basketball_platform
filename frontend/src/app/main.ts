import { createApp } from 'vue';
import App from './App.vue';
import { router } from '@/routes';
import '@/shared/styles/base.css';

createApp(App).use(router).mount('#app');
