"""
Dojo App. pick a command below
Usage:
    create_room
    add_person
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
        Usage: create_room
        """
        pass

    @app_exec
    def do_quit(self, arg):
        """
        Exits the app.
        Usage: quit
        """
        exit()


if __name__ == '__main__':
    DojoCli().cmdloop()
