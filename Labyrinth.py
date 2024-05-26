# Jeremi Torój 7.05.2024

from Cell import Cell
from random import choice
import pygame


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
        pygame.init()
        self.clock = pygame.time.Clock()
        self.cell_size = 20  # Default cell size
        self.window_width = self.width * self.cell_size
        self.window_height = self.height * self.cell_size
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Maze")
        self.fps = 60  # Default frames per second

    def set_cell_size(self, cell_size: int):
        """
        Sets the size of each cell in pixels
        :param cell_size: the size of each cell
        """
        self.cell_size = cell_size
        self.window_width = self.width * self.cell_size
        self.window_height = self.height * self.cell_size
        self.window = pygame.display.set_mode((self.window_width, self.window_height))

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

            if not self.handle_pygame_events():
                return

            if neighbors:
                next_cell = choice(neighbors)
                current.remove_wall(next_cell)
                next_cell.visited = True
                stack.append(next_cell)

                self.display_with_pygame()
                self.clock.tick(self.fps)
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
            for x in range(self.width):
                maze_str += '+'
                maze_str += '-' if self.cells[x][y].wall_up else ' '
            maze_str += '+\n'

            for x in range(self.width):
                maze_str += '|' if self.cells[x][y].wall_left else ' '
                if self.cells[x][y] == self.start_cell:
                    maze_str += 'S'
                elif self.cells[x][y] == self.end_cell:
                    maze_str += 'E'
                else:
                    maze_str += ' '
            maze_str += '|\n' if self.cells[-1][y].wall_right else '\n'

        for x in range(self.width):
            maze_str += '+'
            maze_str += '-' if self.cells[x][-1].wall_down else ' '
        maze_str += '+\n'

        return maze_str

    def refresh_walls(self):
        self.cells = [[Cell(x, y) for y in range(self.height)] for x in range(self.width)]

    def clear_window(self):
        black = (0, 0, 0)  # RGB for black
        self.window.fill(black)
        pygame.display.flip()

    def display_with_pygame(self):
        """
        Displays the current state of the maze using Pygame
        """

        white = (255, 255, 255)
        purple = (128, 0, 128)
        red = (255, 0, 0)
        black = (0, 0, 0)

        for y in range(self.height):
            for x in range(self.width):
                cell = self.cells[x][y]

                if cell == self.start_cell:
                    pygame.draw.rect(self.window, purple, (x * self.cell_size, y * self.cell_size,
                                                           self.cell_size, self.cell_size))
                if cell == self.end_cell:
                    pygame.draw.rect(self.window, red, (x * self.cell_size, y * self.cell_size,
                                                        self.cell_size, self.cell_size))

                top_left = (x * self.cell_size, y * self.cell_size)
                top_right = ((x + 1) * self.cell_size, y * self.cell_size)
                bottom_left = (x * self.cell_size, (y + 1) * self.cell_size)
                bottom_right = ((x + 1) * self.cell_size, (y + 1) * self.cell_size)

                # Draw over the old walls with the background color
                pygame.draw.line(self.window, black, top_left, top_right)
                pygame.draw.line(self.window, black, top_left, bottom_left)
                if x == self.width - 1:
                    pygame.draw.line(self.window, black, top_right, bottom_right)
                if y == self.height - 1:
                    pygame.draw.line(self.window, black, bottom_left, bottom_right)

                if cell.wall_up:
                    pygame.draw.line(self.window, white, top_left, top_right)
                if cell.wall_left:
                    pygame.draw.line(self.window, white, top_left, bottom_left)
                if x == self.width - 1 and cell.wall_right:
                    pygame.draw.line(self.window, white, top_right, bottom_right)
                if y == self.height - 1 and cell.wall_down:
                    pygame.draw.line(self.window, white, bottom_left, bottom_right)

        pygame.display.flip()

    def increase_fps(self):
        if self.fps < 100:
            self.fps += 10
        else:
            self.fps = 100

    def decrease_fps(self):
        if self.fps > 11:
            self.fps -= 10
        else:
            self.fps = 1

    def fill_black(self):
        black = (0, 0, 0)
        self.window.fill(black)

    def set_fps(self, fps: int):
        """
        Sets the frames per second
        :param fps: the frames per second
        """
        self.fps = fps

    def handle_pygame_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.increase_fps()
                if event.key == pygame.K_DOWN:
                    self.decrease_fps()
                if event.key == pygame.K_q:
                    pygame.quit()
                    return False
                if event.key == pygame.K_r:
                    self.fill_black()
                    self.refresh_walls()
                    self.display_with_pygame()
                    return False
                if event.key == pygame.K_s:
                    self.set_fps(0)
                if event.key == pygame.K_SPACE:
                    pause = True
                    while pause:
                        for ev in pygame.event.get():
                            if ev.type == pygame.KEYDOWN:
                                if ev.key == pygame.K_SPACE:
                                    pause = False
                                if ev.key == pygame.K_q:
                                    pygame.quit()
                                    return False
        return True
