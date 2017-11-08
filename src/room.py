class Room(object):
    def __init__(self, room_name=None, room_type=None, room_capacity=None):
        self.room_name = room_name
        self.room_type = room_type
        self.room_capacity = room_capacity

    @property
    def get_room_name(self):
        return "Room Name: {}".format(self.room_name)


class Office(Room):
    def __init__(self, room_name):
        super(Office, self).__init__(room_name, room_type="office", room_capacity=6)


class LivingSpace(Room):
    def __init__(self, room_name):
        super(LivingSpace, self).__init__(room_name, room_type="livingspace", room_capacity=4)
