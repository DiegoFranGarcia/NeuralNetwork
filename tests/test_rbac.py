from src.rbac import RBAC


def test_user_has_permission_via_role():
    rbac = RBAC()
    rbac.add_role("admin", ["read", "write"])
    rbac.add_user("alice")
    rbac.assign_role_to_user("alice", "admin")

    assert rbac.user_has_permission("alice", "read")
    assert rbac.user_has_permission("alice", "write")
    assert not rbac.user_has_permission("alice", "delete")


def test_role_permission_management():
    rbac = RBAC()
    role = rbac.add_role("editor")
    role.add_permission("edit")

    rbac.add_user("bob")
    rbac.assign_role_to_user("bob", "editor")

    assert rbac.user_has_permission("bob", "edit")
    role.remove_permission("edit")
    assert not rbac.user_has_permission("bob", "edit")
