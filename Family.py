##########
class Father(object):
    def __init__(self, father_name, father_age):
        self.father_name = str(father_name)
        self.father_age = father_age

    def set_father_name(self, name):
        self.father_name = name

    def set_father_age(self, age):
        self.father_age = age

    def get_father_name(self):
        return self.father_name

    def get_father_age(self):
        return self.father_age

        ###########


class Mother(object):
    def __init__(self, mother_name, mother_age):
        self.mother_name = str(mother_name)
        self.mother_age = mother_age

    def set_mother_name(self, name):
        self.mother_name = name

    def set_mother_age(self, age):
        self.mother_age = age

    def get_mother_name(self):
        return self.mother_name

    def get_mother_age(self):
        return self.mother_age

    ###########


class Child(Father, Mother):
    def __init__(self, child_name, child_age, father, mother):
        self.child_name = child_name
        self.child_age = child_age
        self.father = Father(father)
        self.mother = Mother(mother)

    def set_child_name(self, name):
        self.child_name = name

    def set_child_age(self, age):
        self.child_age = age

    def get_child_name(self):
        return self.child_name

    def get_child_age(self):
        return self.child_age

    def set_father(self, father_name, father_age):
        self.set_father_name(father_name)
        self.set_father_age(father_age)

    def set_mother(self, mother_name, mother_age):
        self.set_mother_name(mother_name)
        self.set_mother_age(mother_age)

    def set_parents(self, father_details, mother_details):
        self.set_father(father_details["name"], father_details["age"])
        self.set_mother(mother_details["name"], mother_details["age"])

    ###########


class Family(Child):
    def __init__(self, parents, children, last_name=""):
        self.parents = dict(parents)
        self.children = dict(children)
        self.last_name = str(last_name)

    def add_child(self, child_name, child_age):
        self.children[child_name] = child_age

    def get_children(self):
        return self.children

    def get_child(self, i):
        return

    # ????????????????????????
    #     def get_child(self):
    #     (list(self.children.keys())[-1]

    def get_parents_names(self):
        return self.parents.keys()

    def __str__(self):
        print('the parents is :{0} \n the children is :{1} \n the last name is :{2} \n '
              .format(self.parents, self.children, self.last_name))


def main():
    father_name, father_age = input("Enter a name and age of a father").split()
    father_details = {father_name: father_age}
    mother_name, mother_age = input("Enter a name and age of a mother").split()
    mother_details = {mother_name: mother_age}
    parents = {"father": father_details, "mother": mother_details}
    my_family = Family(parents, {}, "")
    num_of_children = int(input("Enter num of children"))
    for i in range(num_of_children):
        child_name, child_age = input("Enter a name and age of children").split()
        my_family.add_child(child_name, child_age)

    last_name = input("Enter a last name. not must!")
    my_family.last_name = last_name

    print(my_family)


if __name__ == '__main__':
    main()
