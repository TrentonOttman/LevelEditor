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

visibility = {"Grid" : True, "Task Bar" : True, "Minimize" : True, "Build Bar" : False}
DRAWING_MODE = False
SELECTING_MODE = False
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
            # Turn on/off grid
            if task_buttons[0][1].collidepoint(event.pos) and visibility["Task Bar"] == True:
                visibility["Build Bar"] = False
                visibility["Grid"] = not visibility["Grid"]
            
            # Turn on/off drawing mode
            if task_buttons[1][1].collidepoint(event.pos) and visibility["Task Bar"] == True:
                ERASING_MODE = False
                DRAWING_MODE = False
                SELECTING_MODE = not SELECTING_MODE
                visibility["Build Bar"] = False

            if SELECTING_MODE:
                visibility["Build Bar"] = True
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                buildbar, build_buttons = draw_buildbar(screen_width, screen_height, screen)
                if build_buttons[0][1].collidepoint(event.pos) and visibility["Task Bar"] == True and visibility["Build Bar"] == True:
                    SELECTING_MODE = False
                    DRAWING_MODE = True

            if DRAWING_MODE:
                visibility["Build Bar"] = False
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            # Turn on/off erasing mode
            if task_buttons[2][1].collidepoint(event.pos) and visibility["Task Bar"] == True:
                DRAWING_MODE = False
                SELECTING_MODE = False
                visibility["Build Bar"] = False
                ERASING_MODE = not ERASING_MODE
                if ERASING_MODE:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            # Minimize task bar
            if minimize.collidepoint(event.pos):
                visibility["Build Bar"] = False
                visibility["Task Bar"] = not visibility["Task Bar"]

        # Update grid during draw mode/erase mode
        elif (event.type == pygame.MOUSEBUTTONDOWN or mouse_held_down) and DRAWING_MODE == True:
            mouse_held_down = True
            visibility["Build Bar"] = False
            for item in grid:
                if item[1].collidepoint(event.pos):
                    item[0] = True
        elif (event.type == pygame.MOUSEBUTTONDOWN or mouse_held_down) and ERASING_MODE == True:
            mouse_held_down = True
            visibility["Build Bar"] = False
            for item in grid:
                if item[1].collidepoint(event.pos):
                    item[0] = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    screen.fill(BLACK)
    if visibility["Grid"]:
        grid = draw_grid(GRID_SIZE, GRAY, screen_width, screen_height, screen, grid)
    for item in grid:
        if item[0] == True:
            pygame.draw.rect(screen, WHITE, item[1])
    if visibility["Task Bar"]:
        taskbar, task_buttons = draw_taskbar(screen_width, screen_height, screen)
        minimize = draw_minimize(screen_width, screen_height, RED, screen)
    else:
        minimize = draw_minimize(screen_width, screen_height, GREEN, screen)
    if visibility["Build Bar"]:
        buildbar, build_buttons = draw_buildbar(screen_width, screen_height, screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
