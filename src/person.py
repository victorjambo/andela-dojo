class Person(object):
    def __init__(self, name):
        self.name = name

    @property
    def email(self):
        return "{}@andela.com".format(self.name)


class Fellow(Person):
    def __init__(self, name):
        super(Fellow, self).__init__(name)


class Staff(Person):
    def __init__(self, name):
        super(Staff, self).__init__(name)
