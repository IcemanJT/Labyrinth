import pygame
from Labyrinth import Maze


maze = Maze(10)

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
