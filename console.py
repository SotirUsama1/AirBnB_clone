import cmd

class HBNBCommand(cmd.Cmd):
    """
        This is the console for airbnb clone project
    """


    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()