from src.room import Room, Office, LivingSpace
from src.person import Person, Fellow, Staff
import random


class Dojo(object):
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

    def allocate_random_room(self, new_person, designation, wants_accomodation):
        """loops through all rooms and returns a random available room"""
        selected_room = {}
        office_rooms = [room for room in self.all_rooms if room.room_type == "office"]
        livingspace_rooms = [room for room in self.all_rooms if room.room_type == "livingspace"]
        available_office = self.available_room(office_rooms, self.office_with_occupants)
        if len(available_office):
            selected_room['office'] = random.choice(available_office)
            self.office_with_occupants[selected_room['office']].append(new_person)
            print("{} has been allocated the office {}."
                  .format(new_person.name, selected_room['office'].room_name))
        else:
            print('No room available')
        if wants_accomodation and designation == 'fellow':
            available_livingspace = self.available_room(livingspace_rooms, self.livingspace_with_occupants)
            if len(available_livingspace):
                selected_room['livingspace'] = random.choice(available_livingspace)
                self.livingspace_with_occupants[selected_room['livingspace']].append(new_person)
                print("{} has been allocated the livingspace {}."
                      .format(new_person.name, selected_room['livingspace'].room_name))
            else:
                print('No room available_office')

    @staticmethod
    def available_room(rooms, rooms_with_occupants):
        """returns all available rooms"""
        available_rooms = []
        for room in rooms:
            if room.room_capacity >= len(rooms_with_occupants[room]):
                available_rooms.append(room)
        return available_rooms

    def print_room(self, args):
        room_name = args["<room_name>"]
        print(self.room_hash_map[room_name])

    def print_allocations(self, args):
        """Prints a list of allocations onto the screen"""
        print(self.room_hash_map)
        if args['-o']:
            try:
                f = open('room_allocations.txt', 'w')
                f.write('self.room_hash_map')
                f.close()
                print('successfully created file')
            except TypeError:
                print("Couldn't save it to file")

    @property
    def room_hash_map(self):
        self.office_with_occupants.update(self.livingspace_with_occupants)
        return {room.room_name: self.office_with_occupants[room] for room in self.office_with_occupants.keys()}

    def print_all_rooms(self, args):
        print(self.all_rooms)
