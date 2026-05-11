import 'vue-router';
import type { Role } from '@/shared/types/roles';

declare module 'vue-router' {
  interface RouteMeta {
    minimumRole?: Role;
    publicDisplay?: boolean;
  }
}
