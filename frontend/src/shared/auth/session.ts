import type { Role } from '@/shared/types/roles';
import { roles } from '@/shared/types/roles';

const DEV_ROLE_STORAGE_KEY = 'basketball_platform_dev_role';

export interface SessionSnapshot {
  role: Role;
  isAuthenticated: boolean;
}

export function getDevSession(): SessionSnapshot {
  const storedRole = window.localStorage.getItem(DEV_ROLE_STORAGE_KEY);
  const role = roles.includes(storedRole as Role) ? (storedRole as Role) : 'guest';

  return {
    role,
    isAuthenticated: role !== 'guest',
  };
}

export function setDevRole(role: Role): void {
  window.localStorage.setItem(DEV_ROLE_STORAGE_KEY, role);
}
