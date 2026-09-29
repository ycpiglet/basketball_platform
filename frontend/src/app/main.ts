import { createApp } from 'vue';
import App from './App.vue';
import { router } from '@/routes';
import { initializeSentry } from '@/shared/integrations/sentry';
import '@/shared/styles/base.css';

const app = createApp(App);

initializeSentry(app, router);

app.use(router).mount('#app');
