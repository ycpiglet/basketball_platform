import * as Sentry from '@sentry/vue';
import type { App } from 'vue';
import type { Router } from 'vue-router';

const sentryDsn = import.meta.env.VITE_SENTRY_DSN as string | undefined;
const sentryEnvironment = import.meta.env.VITE_SENTRY_ENVIRONMENT ?? import.meta.env.VITE_APP_ENV;
const sentryRelease = import.meta.env.VITE_SENTRY_RELEASE as string | undefined;
const tracesSampleRate = Number(import.meta.env.VITE_SENTRY_TRACES_SAMPLE_RATE ?? 0);

export function initializeSentry(app: App, router: Router): void {
  if (!sentryDsn) {
    return;
  }

  Sentry.init({
    app,
    dsn: sentryDsn,
    environment: sentryEnvironment,
    release: sentryRelease,
    tracesSampleRate,
    integrations: [Sentry.browserTracingIntegration({ router })],
  });
}
