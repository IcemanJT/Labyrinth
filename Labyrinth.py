class Mase:

    def __init__(self, *args):
        """
        Constructor for the Maze class, initializes the width and height of the maze
        :param args: width and height of the maze
        """
        if len(args) == 1:
            self.width = args[0]
            self.height = args[0]
        elif len(args) == 2:
            self.width = args[0]
            self.height = args[1]
        elif len(args) == 0:
            self.width = 10
            self.height = 10
        else:
            raise ValueError("Invalid number of arguments")

    def generate(self):
        """
        Generates the maze using the <fill> algorithm
        :return: maze as a 2D list
        """
        pass

    def display(self):
        pass
