class RBAC:
    def __init__(self) -> None:
        self._roles: dict[str, set[str]] = {}
        self._user_roles: dict[str, set[str]] = {}

    def add_role(self, role: str) -> None:
        if role not in self._roles:
            self._roles[role] = set()

    def assign_permission_to_role(self, role: str, permission: str) -> None:
        self._roles.setdefault(role, set()).add(permission)

    def assign_role_to_user(self, user: str, role: str) -> None:
        self._roles.setdefault(role, set())
        self._user_roles.setdefault(user, set()).add(role)

    def user_has_permission(self, user: str, permission: str) -> bool:
        roles = self._user_roles.get(user, set())
        return any(permission in self._roles.get(role, set()) for role in roles)
