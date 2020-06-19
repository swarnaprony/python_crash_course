#exercise_9_11
#imported_admin
#main_class_sub_class
#date: 17/06/2020

from user import Users


class Privileges:
    """Represent a aspects of Users class, specific to admin"""

    def __init__(self, admins_privilege = ['Can add post', 'Can delete post', 'Can ban user']):
        """Initialize the attributes of the parent class
        then intialize the attributes specific to admin class"""
        self.admins_privilege = admins_privilege

    def show_privileges(self):
        """Print the privileges of an admin"""
        for privilege in self.admins_privilege:
            print(f" An admin {privilege}")


class Admin(Users):
    """Represent a aspects of Users class, specific to admin"""

    def __init__(self, first_name, last_name, age):
        """Initialize the attributes of the parent class
        then intialize the attributes specific to admin class"""
        super().__init__(first_name, last_name, age)
        self.new_privilege = Privileges()

new_user = Admin('Mir', 'Asif', 30)
new_user.new_privilege.show_privileges()
