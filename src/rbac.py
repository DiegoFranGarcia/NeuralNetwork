class Role:
    def __init__(self, name, permissions=None):
        self.name = name
        self.permissions = set(permissions or [])

    def add_permission(self, permission):
        self.permissions.add(permission)

    def remove_permission(self, permission):
        self.permissions.discard(permission)

    def has_permission(self, permission):
        return permission in self.permissions


class User:
    def __init__(self, username):
        self.username = username
        self.roles = set()

    def assign_role(self, role):
        self.roles.add(role)

    def revoke_role(self, role):
        self.roles.discard(role)

    def has_permission(self, permission):
        return any(role.has_permission(permission) for role in self.roles)


class RBAC:
    def __init__(self):
        self.roles = {}
        self.users = {}

    def add_role(self, name, permissions=None):
        role = Role(name, permissions)
        self.roles[name] = role
        return role

    def add_user(self, username):
        user = User(username)
        self.users[username] = user
        return user

    def assign_role_to_user(self, username, role_name):
        user = self.users[username]
        role = self.roles[role_name]
        user.assign_role(role)

    def user_has_permission(self, username, permission):
        return self.users[username].has_permission(permission)
