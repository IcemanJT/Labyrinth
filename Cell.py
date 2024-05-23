# Jeremi Torój 23.05.2024

class Cell:

    def __init__(self, x: int, y: int):
        """
        Constructor for the Cell class, initializes the x and y coordinates of the cell
        :param x: x coordinate of the cell
        :param y: y coordinate of the cell
        """
        self.x = x
        self.y = y
        self.wall_up = True
        self.wall_down = True
        self.wall_left = True
        self.wall_right = True
        self.visited = False

    def remove_wall(self, other_cell):
        """
        Removes the wall between two cells
        :param other_cell: the other cell
        """
        x = self.x - other_cell.x
        y = self.y - other_cell.y

        if x == 1:
            self.wall_left = False
            other_cell.wall_right = False
        elif x == -1:
            self.wall_right = False
            other_cell.wall_left = False
        elif y == 1:
            self.wall_up = False
            other_cell.wall_down = False
        elif y == -1:
            self.wall_down = False
            other_cell.wall_up = False
        else:
            raise ValueError("Cells are not adjacent")

