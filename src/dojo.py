from src.room import Room, Office, LivingSpace
from src.person import Person, Fellow, Staff
import random


class Dojo(object):
    rooms = []

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
                Dojo().rooms.append(new_room)
                print ("An {} called {} has been successfully created!"
                       .format(room_type.title(), new_room.room_name))
        except:
            print(room_type + " invalid command!!! try office or livingspace")

    def add_person(self, args):
        person_name = args["<first_name>"] + " " + args["<last_name>"]
        new_person = Staff(person_name) if args['Staff'] else Fellow(person_name)
        allocated_room = self.allocate(new_person)

        print("{} {} has been successfully added."
              .format(type(new_person), new_person.name))
        print("{} has been allocated the office {}."
              .format(new_person.name, allocated_room))

    def allocate(self, person_instance):
        selected_room = random.choice(self.rooms)
        return selected_room.room_name


"""
{'<first_name>': 'vi',
 '<last_name>': 'mu',
 '<wants_space>': 'Y',
 'Fellow': False,
 'Staff': True}
 return ("An "
                        + room_type.title()
                        + " called "
                        + new_room.room_name
                        + " has been successfully created!")
can_accomodate = True if args.get("<wants_space>") is "Y" else False

        

"""