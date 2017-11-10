import random
from src.room import *
from src.person import *


class Dojo(object):
    """Class Dojo to represent the building
    Creates room, adds people to rooms and saves all that
    """
    unallocated_people = []

    def __init__(self):
        self.all_rooms = []
        self.all_people = []
        self.livingspace_with_occupants = {}
        self.office_with_occupants = {}

    def create_room(self, args):
        """ Creates rooms in the Dojo.
        Using this command, the user should be able to create as many rooms
        as possible by specifying multiple room names
        after the create_room command.
        """
        room_type = args["<room_type>"][0].lower()
        room_name = args["<room_name>"]
        map_room = {'o': Office, 'l': LivingSpace}
        list_name = [(x, room_type) for x in room_name]
        for item in list_name:
            new_room = map_room[item[1]](item[0])
            self.all_rooms.append(new_room)
            if room_type == 'o':
                self.office_with_occupants[new_room] = []
            else:
                self.livingspace_with_occupants[new_room] = []
            print ("An {} called {} has been successfully created!"
                   .format(new_room.__class__.__name__, new_room.room_name))

    def add_person(self, args):
        """Adds a person to the system and allocates the person to a random room
        """
        person_name = args["<first_name>"] + " " + args["<last_name>"]
        map_people = {'staff': Staff, 'fellow': Fellow}
        designation = args["<designation>"].lower()
        wants_accomodation = args["-w"]
        new_person = map_people[designation](person_name)

        print("{} {} has been successfully added."
              .format(new_person.__class__.__name__, new_person.name))
        self.allocate_random_room(new_person, designation, wants_accomodation)

    def allocate_random_room(self,
                             new_person,
                             designation,
                             wants_accomodation):
        """Allocates the new person to a random room.
        wants_accommodation here is an optional argument
        which can be either True or False.
        The default value if it is not provided is False.
        Called in:
            add_person
        """
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
    def selected_room(available_room,
                      room,
                      new_person,
                      room_with_occupants):
        """Appends the new_person to dictionary of rooms
        It is called everytime we create a new_person and want to allocate
        either livingspace or office to avoid repetition
        Used in:
            allocate_random_room
        """
        selected_room = {}
        if len(available_room):
            selected_room[room] = random.choice(available_room)
            room_with_occupants[selected_room[room]].append(new_person)
            print("{} has been allocated the office {}."
                  .format(new_person.name, selected_room[room].room_name))
        else:
            print('No {} available'.format(room))
            Dojo().unallocated_people.append(new_person)

    @staticmethod
    def available_room(rooms, rooms_with_occupants):
        """returns all available rooms
        Used in:
            allocate_random_room
        """
        available_rooms = []
        for room in rooms:
            if room.room_capacity > len(rooms_with_occupants[room]):
                available_rooms.append(room)
        return available_rooms

    def print_room(self, room_name):
        """Prints the names of all the people in room_name.
        """
        members = self.room_name_map[room_name]
        print(room_name)
        print("-" * 30)
        for member in members:
            print(member + ", "),
        print("\n")

    def print_allocations(self):
        """Prints a list of allocations onto the screen.
        Specifying the optional -o option here outputs the
        registered allocations to a txt file"""
        for room in self.room_name_map:
            self.print_room(room)
        print("\n")

    def print_unallocated(self):
        """Prints a list of unallocated people to the screen.
        Specifying the -o option outputs the info to the txt file provided
        """
        for person in self.unallocated_people:
            print(person.name),
        print("\n")

    @property
    def room_name_map(self):
        """Returns a Dictionary of rooms and people in rooms
        This is done because dict office_with_occupants
        hold objects not names of objects
        Used in:
            print_room
            print_allocations
            print_unallocated
        """
        self.office_with_occupants.update(self.livingspace_with_occupants)
        new_list = {}
        for key, value in self.office_with_occupants.iteritems():
            new_list[key.room_name] = []
            for item in value:
                new_list[key.room_name].append(item.name)
        return new_list
