import { describe, expect, it } from 'vitest';
import { hasMinimumRole } from '@/shared/types/roles';

describe('hasMinimumRole', () => {
  it('allows a system administrator to access team manager routes', () => {
    expect(hasMinimumRole('system_admin', 'team_manager')).toBe(true);
  });

  it('blocks guests from restricted operational routes', () => {
    expect(hasMinimumRole('guest', 'team_manager')).toBe(false);
  });
});
