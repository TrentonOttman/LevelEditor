import pygame
from colors import *
from drawings import *

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Editor")
clock = pygame.time.Clock() 
screen_width, screen_height = screen.get_size()

# Set how big each grid box will be (in pixels)
GRID_SIZE = 50
grid = []

visibility = {"Grid" : True, "Task Bar" : True, "Minimize" : True}
DRAWING_MODE = False
ERASING_MODE = False
mouse_held_down = False

print(screen_width, screen_height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_held_down = False
            if buttons[0][1].collidepoint(event.pos) and visibility["Task Bar"] == True:
                visibility["Grid"] = not visibility["Grid"]
            if buttons[1][1].collidepoint(event.pos) and visibility["Task Bar"] == True:
                ERASING_MODE = False
                DRAWING_MODE = not DRAWING_MODE
                if DRAWING_MODE:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if minimize.collidepoint(event.pos):
                visibility["Task Bar"] = not visibility["Task Bar"]
        elif (event.type == pygame.MOUSEBUTTONDOWN or mouse_held_down) and DRAWING_MODE == True:
            mouse_held_down = True
            for item in grid:
                if item[1].collidepoint(event.pos):
                    item[0] = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    screen.fill(BLACK)
    if visibility["Grid"]:
        grid = draw_grid(GRID_SIZE, GRAY, screen_width, screen_height, screen, grid)
    if visibility["Task Bar"]:
        taskbar, buttons = draw_taskbar(screen_width, screen_height, screen)
        minimize = draw_minimize(screen_width, screen_height, RED, screen)
    else:
        minimize = draw_minimize(screen_width, screen_height, GREEN, screen)
    for item in grid:
        if item[0] == True:
            pygame.draw.rect(screen, WHITE, item[1])

    pygame.display.update()
    clock.tick(60)

pygame.quit()
