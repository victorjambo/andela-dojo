class Room(object):
    def __init__(self, room_name):
        self.room_name = room_name

    @property
    def get_room_name(self):
        return "Room Name: {}".format(self.room_name)


class Office(Room):
    def __init__(self, room_name):
        super(Office, self).__init__(room_name)


class LivingSpace(Room):
    def __init__(self, room_name):
        super(LivingSpace, self).__init__(room_name)
