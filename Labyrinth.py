# Jeremi Torój 7.05.2024

from Cell import Cell
from random import choice


class Maze:

    def __init__(self, *args: int):
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

        self.cells = [[Cell(x, y) for y in range(self.height)] for x in range(self.width)]
        self.start_cell = None
        self.end_cell = None

    def generate_maze_dfs(self):
        """
        Generates the maze using the depth-first search algorithm
        """
        stack = []
        self.pick_maze_end()
        current = self.pick_maze_start()
        current.visited = True
        stack.append(current)

        while stack:
            current = stack[-1]
            neighbors = self.get_unvisited_neighbors(current)

            if neighbors:
                next_cell = choice(neighbors)
                current.remove_wall(next_cell)
                next_cell.visited = True
                stack.append(next_cell)
            else:
                stack.pop()

    def get_unvisited_neighbors(self, cell: Cell):
        """
        Returns unvisited neighbors of a cell
        :param cell: the cell
        :return: list of unvisited neighbors
        """
        neighbors = []
        x = cell.x
        y = cell.y

        if x > 0 and not self.cells[x - 1][y].visited:
            neighbors.append(self.cells[x - 1][y])
        if x < self.width - 1 and not self.cells[x + 1][y].visited:
            neighbors.append(self.cells[x + 1][y])
        if y > 0 and not self.cells[x][y - 1].visited:
            neighbors.append(self.cells[x][y - 1])
        if y < self.height - 1 and not self.cells[x][y + 1].visited:
            neighbors.append(self.cells[x][y + 1])

        return neighbors

    def pick_maze_start(self):
        """
        Picks a random cell as the start of the maze
        """
        self.start_cell = choice(self.cells[0])
        return self.start_cell

    def pick_maze_end(self):
        """
        Picks a random cell as the end of the maze
        """
        self.end_cell = choice(self.cells[-1])
        return self.end_cell

    def display(self):
        """
        Returns a string representation of the maze
        """
        maze_str = ""
        for y in range(self.height):
            # Add the upper walls and corners to the string
            for x in range(self.width):
                maze_str += '+'
                maze_str += '-' if self.cells[x][y].wall_up else ' '
            maze_str += '+\n'

            # Add the left walls and the cells to the string
            for x in range(self.width):
                maze_str += '|' if self.cells[x][y].wall_left else ' '
                if self.cells[x][y] == self.start_cell:
                    maze_str += 'S'
                elif self.cells[x][y] == self.end_cell:
                    maze_str += 'E'
                else:
                    maze_str += ' '
            maze_str += '|\n' if self.cells[-1][y].wall_right else '\n'

        # Add the lower walls and corners of the last row to the string
        for x in range(self.width):
            maze_str += '+'
            maze_str += '-' if self.cells[x][-1].wall_down else ' '
        maze_str += '+\n'

        return maze_str


