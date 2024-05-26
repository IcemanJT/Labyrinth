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
    root.title("Maze dimensions")
    tk.Label(root, text="Maze width:").grid(row=0)
    tk.Label(root, text="Maze height:").grid(row=1)

    width_entry = tk.Entry(root)
    height_entry = tk.Entry(root)

    width_entry = tk.Entry(root)
    width_entry.insert(0, "10")

    height_entry = tk.Entry(root)
    height_entry.insert(0, "10")

    width_entry.grid(row=0, column=1)
    height_entry.grid(row=1, column=1)

    tk.Button(root, text='Submit', command=submit).grid(row=3, column=0, sticky=tk.W, pady=4)

    tk.mainloop()

    if dimensions['width'] < 2:
        dimensions['width'] = 5
    if dimensions['height'] < 2:
        dimensions['height'] = 5

    return dimensions['width'], dimensions['height']


def refresh_maze(labyrinth):
    labyrinth.fill_black()
    labyrinth.refresh_walls()
    labyrinth.display_with_pygame()


width, height = get_maze_dimensions()
maze = Maze(width, height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                refresh_maze(maze)
                maze.generate_maze_dfs()
            if event.key == pygame.K_p:
                refresh_maze(maze)
                maze.generate_maze_prim()
            if event.key == pygame.K_k:
                refresh_maze(maze)
                maze.generate_maze_kruskal()
            if event.key == pygame.K_a:
                refresh_maze(maze)
                maze.generate_maze_aldous_broder()
            if event.key == pygame.K_q:
                pygame.quit()
            if event.key == pygame.K_r:
                refresh_maze(maze)
                maze.display_with_pygame()

        maze.display_with_pygame()

    pygame.display.flip()

pygame.quit()
