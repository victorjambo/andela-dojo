import random
from src.room import *
from src.person import *


class Dojo(object):
    """Class Dojo to represent the building
    Creates room, adds people to rooms and saves all that
    """
    all_rooms = []
    all_people = []
    livingspace_with_occupants = {}
    office_with_occupants = {}

    def create_room(self, args):
        """Create room"""
        room_type = args["<room_type>"]
        room_name = args["<room_name>"]
        map_room = {'office': Office, 'livingspace': LivingSpace}
        list_name = [(x, room_type) for x in room_name]
        for item in list_name:
            new_room = map_room[item[1]](item[0])
            self.all_rooms.append(new_room)
            if room_type == 'office':
                self.office_with_occupants[new_room] = []
            else:
                self.livingspace_with_occupants[new_room] = []
            print ("An {} called {} has been successfully created!"
                   .format(room_type.title(), new_room.room_name))

    def add_person(self, args):
        """add person and allocate a random room"""
        person_name = args["<first_name>"] + " " + args["<last_name>"]
        map_people = {'staff': Staff, 'fellow': Fellow}
        designation = args["<designation>"]
        wants_accomodation = args["-w"]
        new_person = map_people[designation](person_name)

        print("{} {} has been successfully added."
              .format(new_person.__class__.__name__, new_person.name))
        self.allocate_random_room(new_person, designation, wants_accomodation)

    def allocate_random_room(self,
                             new_person,
                             designation,
                             wants_accomodation):
        """loops through all rooms and returns a random available room"""
        office_rooms = [room for room in self.all_rooms
                        if room.room_type == "office"]
        livingspace_rooms = [room for room in self.all_rooms
                             if room.room_type == "livingspace"]
        available_office = self.available_room(office_rooms,
                                               self.office_with_occupants)
        self.selected_room(available_office,
                           'office',
                           new_person,
                           self.office_with_occupants)
        if wants_accomodation and designation == 'fellow':
            available_livingspace = self.available_room(
                livingspace_rooms, self.livingspace_with_occupants)
            self.selected_room(available_livingspace,
                               'livingspace',
                               new_person,
                               self.livingspace_with_occupants)

    @staticmethod
    def selected_room(available_room, room, new_person, room_with_occupants):
        selected_room = {}
        if len(available_room):
            selected_room[room] = random.choice(available_room)
            room_with_occupants[selected_room[room]].append(new_person)
            print("{} has been allocated the office {}."
                  .format(new_person.name, selected_room[room].room_name))
        else:
            print('No {} available'.format(room))

    @staticmethod
    def available_room(rooms, rooms_with_occupants):
        """returns all available rooms"""
        available_rooms = []
        for room in rooms:
            if room.room_capacity > len(rooms_with_occupants[room]):
                available_rooms.append(room)
        return available_rooms

    def print_room(self, args):
        room_name = args["<room_name>"]
        print(self.room_name_map[room_name])

    def print_allocations(self, args):
        """Prints a list of allocations onto the screen"""
        print(self.room_name_map)
        if args['-o']:
            try:
                file = open('room_allocations.txt', 'w')
                file.write('self.room_name_map')
                file.close()
                print('successfully created file and saved into it')
            except TypeError:
                print("Couldn't save it to file")

    @property
    def room_name_map(self):
        self.office_with_occupants.update(self.livingspace_with_occupants)
        return {room.room_name: self.office_with_occupants[room]
                for room in self.office_with_occupants.keys()}
