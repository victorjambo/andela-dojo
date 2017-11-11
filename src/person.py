class Person(object):
    def __init__(self, person_id, name):
        self.name = name
        self.person_id = person_id

    @property
    def email(self):
        return "{}@andela.com".format(self.name)


class Fellow(Person):
    def __init__(self, person_id, name):
        super(Fellow, self).__init__(person_id, name)


class Staff(Person):
    def __init__(self, person_id, name):
        super(Staff, self).__init__(person_id, name)
