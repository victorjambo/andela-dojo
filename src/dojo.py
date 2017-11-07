from src.room import Room, Office, LivingSpace
from src.person import Person, Fellow, Staff
import random


class Dojo(object):
    all_rooms = []
    all_people = []
    living_spaces = {"None": []}
    office_spaces = {"None": []}

    def create_room(self, args):
        room_type = args["<room_type>"]
        room_name = args["<room_name>"]
        map_room = {'office': Office, 'livingspace': LivingSpace}

        list_name = [(x, room_type) for x in room_name]
        for item in list_name:
            new_room = map_room[item[1]](item[0])
            Dojo().all_rooms.append(new_room)
            print ("An {} called {} has been successfully created!"
                   .format(room_type.title(), new_room.room_name))

    def add_person(self, args):
        person_name = args["<first_name>"] + " " + args["<last_name>"]
        map_people = {'staff': Staff, 'fellow': Fellow}
        designation = args["<designation>"]
        wants_accomodation = args["-w"]
        new_person = map_people[designation](person_name)

        allocated_room = self.allocate(new_person, designation, wants_accomodation)

        print("{} {} has been successfully added."
              .format(new_person.__class__.__name__, new_person.name))
        print("{} has been allocated the office {}."
              .format(new_person.name, allocated_room.room_name))

    def allocate(self, new_person, designation, wants_accomodation):
        office_room = [room for room in self.all_rooms if room.room_type == "office"]
        livingspace_room = [room for room in self.all_rooms if room.room_type == "livingspace"]

        available_room = []

        for room in office_room:
            if room.room_capacity > len(self.office_spaces[room.room_name]):
                available_room.append(room.room_name)

        selected_room = "None"

        if len(available_room):
            selected_room = random.choice(available_room)
        return selected_room


"""
{'-w': True,
 '<designation>': 'staff',
 '<first_name>': 'vdf',
 '<last_name>': 'dfv'}
 return ("An "
        + room_type.title()
        + " called "
        + new_room.room_name
        + " has been successfully created!")
can_accomodate = True if args.get("<wants_space>") is "Y" else False



"""