class PolicyConfiguration:
    def __init__(self, user, version, statement):
        self.user = user
        self.version = version
        self.statement = statement
class Statement:
    def __init__(self, effect, action, resource):
        self.effect = effect
        self.action = action
        self.resource = resource
class IAMService:
    def __init__(self):
        self.users = {}
        self.groups = {}
        self.mfa_enabled_users = set()
        self.root_user = None

    def add_user(self, user_name, is_root=False):
        self.users[user_name] = {"policies": [], "groups": [], "role": "root" if is_root else "user"}
        if is_root:
            self.root_user = user_name

    def add_group(self, group_name):
        self.groups[group_name] = {"users": [], "policies": []}

    def add_user_to_group(self, user_name, group_name):
        if user_name in self.users and group_name in self.groups:
            self.groups[group_name]["users"].append(user_name)
            self.users[user_name]["groups"].append(group_name)

    def enable_mfa_for_user(self, user_name):
        if user_name in self.users:
            self.mfa_enabled_users.add(user_name)
            print(f"MFA enabled for user '{user_name}'.")
        else:
            print(f"Denied: User '{user_name}' does not exist.")

    def is_mfa_enabled_for_user(self, user_name):
        return user_name in self.mfa_enabled_users

    def assign_json_policy_to_user(self, user_name, policy_json):
        if user_name in self.users:
            self.users[user_name]["policies"].append(policy_json)
            print(f"JSON policy assigned to user '{user_name}'.")
        else:
            print(f"Denied: User '{user_name}' does not exist.")

    def assign_json_policy_to_group(self, group_name, policy_json):
        if group_name in self.groups:
            self.groups[group_name]["policies"].append(policy_json)
            print(f"JSON policy assigned to group '{group_name}'.")
        else:
            print(f"Denied: Group '{group_name}' does not exist.")


class Permissions:
    def __init__(self, iam_service):
        self.iam_service = iam_service

    def check_permission(self, user_name, action, resource):
        # Check MFA
        if not self.iam_service.is_mfa_enabled_for_user(user_name):
            return "Access denied: MFA not enabled for user."

        # Check user's policies
        if user_name in self.iam_service.users:
            for policy in self.iam_service.users[user_name]["policies"]:
                if self._is_action_allowed(policy, action, resource):
                    return "Access granted"

        # Check user's group policies
        for group_name in self.iam_service.users[user_name]["groups"]:
            group = self.iam_service.groups[group_name]
            for policy in group["policies"]:
                if self._is_action_allowed(policy, action, resource):
                    return "Access granted"

        return "Access denied"

    def _is_action_allowed(self, policy, action, resource):
        for statement in policy['Statement']:
            if statement['Action'] == action and statement['Resource'] == resource:
                return statement['Effect'] == "Allow"
        return False


# Ejemplo de uso
example_policy_admin = {
    "Version": "2024-06-06",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::example_bucket"
        },
        {
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::example_bucket/*"
        }
    ]
}

example_policy_tester = {
    "Version": "2024-06-06",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::example_bucket/*"
        }
    ]
}

iam_service = IAMService()
iam_service.add_user("root", is_root=True)
iam_service.add_user("alice")
iam_service.add_group("admin")
iam_service.add_group("tester")

iam_service.add_user_to_group("alice", "admin")
iam_service.assign_json_policy_to_group("admin", example_policy_admin)
iam_service.enable_mfa_for_user("alice")

permissions = Permissions(iam_service)

print(permissions.check_permission("alice", "s3:ListBucket", "arn:aws:s3:::example_bucket"))  # Debe permitir acceso
print(permissions.check_permission("alice", "s3:GetObject",
                                   "arn:aws:s3:::example_bucket/test_file"))  # Denegado, no está en política admin
print(permissions.check_permission("alice", "s3:PutObject",
                                   "arn:aws:s3:::example_bucket/test_file"))  # Debe permitir acceso

# Verificación de roles
print(f"Alice's role: {iam_service.users['alice']['role']}")
print(f"Root's role: {iam_service.users['root']['role']}")
