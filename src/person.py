class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return "{}.{}@andela.com".format(self.first_name, self.last_name)


class Fellow(Person):
    def __init__(self, first_name, last_name):
        super(Fellow, self).__init__(first_name, last_name)


class Staff(Person):
    def __init__(self, first_name, last_name):
        super(Staff, self).__init__(first_name, last_name)
