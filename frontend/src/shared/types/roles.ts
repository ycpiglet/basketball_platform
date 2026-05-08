export const roles = ['guest', 'user', 'team_manager', 'system_admin'] as const;

export type Role = (typeof roles)[number];

const roleRank: Record<Role, number> = {
  guest: 0,
  user: 1,
  team_manager: 2,
  system_admin: 3,
};

export function hasMinimumRole(currentRole: Role, requiredRole: Role): boolean {
  return roleRank[currentRole] >= roleRank[requiredRole];
}
