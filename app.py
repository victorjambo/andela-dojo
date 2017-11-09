"""
Dojo App. pick a command below
Usage:
    create_room <room_type> <room_name> ...
    add_person <first_name> <last_name> <designation> [-w]
    print_room <room_name>
    print_allocations [-o]
    q
    (-i | --interactive)
    Options:
    -h --help Show this screen.
    -i --interactive Interactive mode.
    -v --version
"""
import cmd
from docopt import docopt, DocoptExit
from pyfiglet import figlet_format
from termcolor import cprint
from src.dojo import Dojo


def app_exec(func):
    """
    Decorator definition for the app.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            msg = "Invalid command! See help."
            print(msg)
            print(e)
            return

        except SystemExit:
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)

    return fn


def intro():
    cprint(figlet_format("Dojo", font="slant"), "blue")
    cprint(__doc__, "green")


class DojoCli(cmd.Cmd):
    intro()

    prompt = "Dojo ~> "
    file = None
    dojo = Dojo()

    @app_exec
    def do_create_room(self, arg):
        """Creates a new room
        Usage: create_room <room_type> <room_name> ...
        """
        try:
            self.dojo.create_room(arg)
        except KeyError:
            cprint("Invalid command '{}'!!! try office or livingspace"
                   .format(arg["<room_type>"]), "red")
            cprint(self.do_create_room.__doc__, "green")

    @app_exec
    def do_add_person(self, arg):
        """Creates a new room
        Usage:
            add_person <first_name> <last_name> <designation> [-w]
        """
        self.dojo.add_person(arg)

    @app_exec
    def do_print_room(self, arg):
        """Prints  the names of all the people in room_name
        Usage:
            print_room <room_name>
        """
        self.dojo.print_room(arg)

    @app_exec
    def do_my_rooms(self, arg):
        """
        Usage: my_rooms [p]
        """
        self.dojo.print_all_rooms(arg)

    @app_exec
    def do_print_allocations(self, arg):
        """Prints a list of allocations onto the screen
        Usage:
            print_allocations [-o]
        """
        self.dojo.print_allocations(arg)

    @app_exec
    def do_q(self, arg):
        """
        Exits the app.
        Usage: q
        """
        exit()


if __name__ == '__main__':
    DojoCli().cmdloop()
