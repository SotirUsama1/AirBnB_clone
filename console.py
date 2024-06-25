#!/usr/bin/python3
"""
The console v: 0.0.1
Contains the entry point of the command interpreter
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Custom console class
    """

    prompt = "(hbnb) "

    def handle_empty_line(self, line):
        """
        Eliminates empty lines
        """
        return False

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    do_quit = do_EOF


if __name__ == '__main__':
    HBNBCommand().cmdloop()