import pygame
from Labyrinth import Maze
import tkinter as tk


def get_maze_dimensions():
    dimensions = {'width': 0, 'height': 0}

    def submit():
        dimensions['width'] = int(width_entry.get())
        dimensions['height'] = int(height_entry.get())
        root.destroy()

    root = tk.Tk()
    tk.Label(root, text="Maze width:").grid(row=0)
    tk.Label(root, text="Maze height:").grid(row=1)

    width_entry = tk.Entry(root)
    height_entry = tk.Entry(root)

    width_entry.grid(row=0, column=1)
    height_entry.grid(row=1, column=1)

    tk.Button(root, text='Submit', command=submit).grid(row=3, column=0, sticky=tk.W, pady=4)

    tk.mainloop()

    return dimensions['width'], dimensions['height']


width, height = get_maze_dimensions()
maze = Maze(width, height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                maze.fill_black()
                maze.refresh_walls()
                maze.generate_maze_dfs()
            if event.key == pygame.K_q:
                pygame.quit()
            if event.key == pygame.K_r:
                maze.fill_black()
                maze.refresh_walls()
                maze.display_with_pygame()

        maze.display_with_pygame()

    pygame.display.flip()

pygame.quit()
