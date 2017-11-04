from src.room import Room, Office, LivingSpace
from src.person import Person, Fellow,


class Dojo(object):
    def __init_(self):
        self.room_occupants = []

    def create_room(self, args):
        room_type = args["<room_type>"]
        room_name = args["<room_name>"]
        map_room = {'office': Office, 'livingspace': LivingSpace}
        try:
            list_name = [(x, room_type) for x in room_name]
            for item in list_name:
                new_room = map_room[item[1]](item[0])
                return ("An "
                        + room_type.title()
                        + " called "
                        + new_room.room_name
                        + " has been successfully created!")
        except:
            return room_type + " invalid command!!! try office or livingspace"

    def add_person(self, args):
        person_name = args["<first_name>"] + " " + args["<last_name>"]
        person_type = args['Fellow'] if args['Fellow'] else args['Staff']
        can_accomodate = True if args.get("<wants_space>") is "Y" else False
        new_person = Staff(person_name) if args['Staff'] else Fellow(person_name)
        return new_person + " has been successfully added."


"""
{'<first_name>': 'vi',
 '<last_name>': 'mu',
 '<wants_space>': 'Y',
 'Fellow': False,
 'Staff': True}
"""