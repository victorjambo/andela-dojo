import random
from termcolor import cprint
from terminaltables import AsciiTable
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
            cprint("An {} called {} has been successfully created!"
                   .format(new_room.__class__.__name__, new_room.room_name),
                   'green')

    def add_person(self, args):
        """Adds a person to the system and allocates the person to a random room
        """
        person_name = args["<first_name>"] + " " + args["<last_name>"]
        map_people = {'staff': Staff, 'fellow': Fellow}
        designation = args["<designation>"].lower()
        wants_accomodation = args["-w"]
        person_id = len(self.all_people) + 1000
        new_person = map_people[designation](person_id, person_name)
        self.all_people.append(new_person)
        cprint("{} {} Staff ID {} has been successfully added."
               .format(new_person.__class__.__name__,
                       new_person.name,
                       new_person.person_id), 'green')
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
        secure_random = random.SystemRandom()
        selected_room = {}
        len_available_room = len(available_room)
        if len_available_room:
            selected_room[room] = secure_random.choice(available_room)
            room_with_occupants[selected_room[room]].append(new_person)
            cprint("{} has been allocated the office {}."
                   .format(new_person.name, selected_room[room].room_name),
                   'blue')
        else:
            cprint('No {} available'.format(room), 'yellow')
            Dojo().unallocated_people.append(new_person)

    @staticmethod
    def available_room(rooms, rooms_with_occupants):
        """returns all available rooms
        Used in:
            allocate_random_room
        """
        available_rooms = []
        for room in rooms:
            len_rooms_with_occupants = len(rooms_with_occupants[room])
            if room.room_capacity > len_rooms_with_occupants:
                available_rooms.append(room)
        return available_rooms

    def print_room(self, room_name):
        """Prints the names of all the people in room_name.
        """
        members = self.room_name_map[room_name]
        table_members = [["Members in room: ", room_name]]
        for member in members:
            table_members.append([member])
        table_members = AsciiTable(table_members)
        cprint(table_members.table, 'blue')

    def print_allocations(self):
        """Prints a list of allocations onto the screen.
        Specifying the optional -o option here outputs the
        registered allocations to a txt file"""
        for room in self.room_name_map:
            self.print_room(room)

    def print_unallocated(self):
        """Prints a list of unallocated people to the screen.
        Specifying the -o option outputs the info to the txt file provided
        """
        table_data = [['id', 'Name', 'Designation', 'Missing']]
        for person in self.unallocated_people:
            room = 'Office'\
                   if table_data[-1][0] != person.person_id\
                   else 'LivingSpace'
            table_data.append(
                [person.person_id,
                 person.name,
                 person.__class__.__name__,
                 room])
        table = AsciiTable(table_data)
        cprint(table.table, 'blue')

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
        for key, value in self.office_with_occupants.items():
            new_list[key.room_name] = []
            for item in value:
                new_list[key.room_name].append(item.name)
        return new_list

    def reallocate_person(self, args):
        """Relocate person
        """
        new_room_name = args['<new_room_name>']
        person_identifier = int(args['<person_identifier>'])
        person = self.get_person_by_id(person_identifier)
        if not person:
            cprint("Person with ID '{}' doesn't exist "
                   .format(person_identifier), 'yellow')
            return
        current_room = self.assigned_room(person)
        if not current_room:
            cprint("Room doesn't exist", "red")
            return
        if current_room.room_name == new_room_name:
            cprint("You are trying to move within same room", "red")
            cprint("Would you live to create room?Y/n", "red")
            return
        if self.is_within_room_type(new_room_name, current_room):
            self.relocate_to_new_room(new_room_name, person, current_room)
        else:
            cprint("Can't move accross different room types. "
                   "Or room could also be full",
                   "red")

    def is_within_room_type(self, new_room_name, current_room):
        """Since we can't move person from living to office
        or vice-verse, therefore we make sure we are moving within
        same room types
        Also checks if room is full
        """
        room_with_occupants = [self.office_with_occupants,
                               self.livingspace_with_occupants]
        for room_with_occupant in room_with_occupants:
            for room in room_with_occupant.keys():
                len_room = len(room_with_occupant[room])
                if new_room_name == room.room_name:
                    if room.room_capacity > len_room:
                        return True
            return False

    def assigned_room(self, person):
        """Returns room name that user is currently in
        otherwise return false
        tuple
        """
        room_with_occupants = [self.office_with_occupants,
                               self.livingspace_with_occupants]
        for room_with_occupant in room_with_occupants:
            for key, rooms in room_with_occupant.items():
                for room in rooms:
                    if person in room_with_occupant[key]:
                        return key
            return False

    def get_person_by_id(self, uid):
        """Gets name of the person whose id is provided
        If person is not will return False
        """
        for person in self.all_people:
            if person.person_id == uid:
                return person
        return False

    def relocate_to_new_room(self, new_room_name, person, current_room):
        """Handle appending person to the new room
        And removing person from old room
        """
        room_with_occupants = [self.office_with_occupants,
                               self.livingspace_with_occupants]
        for room_with_occupant in room_with_occupants:
            for room, people in room_with_occupant.items():
                if room.room_name == new_room_name:
                    room_with_occupant[room].append(person)
                    room_with_occupant[current_room].remove(person)
                    cprint("Successfully moved {} to room {}"
                           .format(person.name, new_room_name), "green")
                    return
            return False

    def load_people(self):
        """Function to add people to dojo from list of people in file
        """
        file = open("people.txt", "r")
        for line in file:
            arg = {}
            line = line.split()
            for index, item in enumerate(line):
                len_line = len(line)
                arg["<first_name>"] = line[0]
                arg["<last_name>"] = line[1]
                arg["<designation>"] = line[2]
                arg["-w"] = True if len_line == 4 else False
            self.add_person(arg)

    def print_people(self):
        """Returns list of all people in dojo
        """
        people = [['ID', 'Name', 'Designation']]
        for person in self.all_people:
            people.append([person.person_id,
                           person.name,
                           person.__class__.__name__])
        people = AsciiTable(people)
        cprint(people.table, 'yellow')

    def print_rooms(self):
        """Returns list of all rooms in dojo
        """
        rooms = [['Room Name', 'Type', 'Max occupants']]
        for room in self.all_rooms:
            rooms.append([room.room_name,
                          room.__class__.__name__,
                          room.room_capacity])
        rooms = AsciiTable(rooms)
        cprint(rooms.table, 'yellow')
