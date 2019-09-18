
class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("sub_child")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
  
    if isinstance(group, Group):
        if user in group.get_users():
            return True
        else:
            if len(group.get_groups()) == 0:
                return False
            else:
                for group_item in group.get_groups():
                    return is_user_in_group(user, group_item)

    else:
        print(f"{group} is not a group")


print(is_user_in_group(sub_child_user, parent))

