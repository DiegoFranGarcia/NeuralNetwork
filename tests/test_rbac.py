from src.rbac import RBAC


def test_rbac_allows_permissions_via_roles():
    rbac = RBAC()
    rbac.add_role("admin")
    rbac.assign_permission_to_role("admin", "delete")
    rbac.assign_role_to_user("alice", "admin")

    assert rbac.user_has_permission("alice", "delete")


def test_rbac_denies_missing_permissions():
    rbac = RBAC()
    rbac.add_role("viewer")
    rbac.assign_permission_to_role("viewer", "read")
    rbac.assign_role_to_user("bob", "viewer")

    assert not rbac.user_has_permission("bob", "write")
