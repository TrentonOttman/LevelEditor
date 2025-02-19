import pygame
from colors import *
from drawings import *
from GridPoint import *

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
selected_type = None
START = False
END = False

print(screen_width, screen_height)

# Initialize
grid = draw_grid(GRID_SIZE, GRAY, screen_width, screen_height, screen, grid)
buildbar, build_buttons = draw_buildbar(screen_width, screen_height, screen)
taskbar, task_buttons = draw_taskbar(screen_width, screen_height, screen)
minimize = draw_minimize(screen_width, screen_height, RED, screen)

running = True
while running:
    for event in pygame.event.get():
        mouse_x, mouse_y = pygame.mouse.get_pos()
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
                if build_buttons[0][1].collidepoint(event.pos) and visibility["Task Bar"] == True and visibility["Build Bar"] == True:
                    selected_type = "Wall"
                elif build_buttons[1][1].collidepoint(event.pos) and visibility["Task Bar"] == True and visibility["Build Bar"] == True:
                    selected_type = "Spike"
                elif build_buttons[2][1].collidepoint(event.pos) and visibility["Task Bar"] == True and visibility["Build Bar"] == True:
                    selected_type = "Sand"
                elif build_buttons[3][1].collidepoint(event.pos) and visibility["Task Bar"] == True and visibility["Build Bar"] == True:
                    selected_type = "Trampoline"
                elif build_buttons[4][1].collidepoint(event.pos) and visibility["Task Bar"] == True and visibility["Build Bar"] == True and not START:
                    selected_type = "Start"
                elif build_buttons[5][1].collidepoint(event.pos) and visibility["Task Bar"] == True and visibility["Build Bar"] == True and not END:
                    selected_type = "End"
                if (build_buttons[0][1].collidepoint(event.pos) or build_buttons[1][1].collidepoint(event.pos) or build_buttons[2][1].collidepoint(event.pos) or build_buttons[3][1].collidepoint(event.pos) or build_buttons[4][1].collidepoint(event.pos) or build_buttons[5][1].collidepoint(event.pos)) and visibility["Task Bar"] == True and visibility["Build Bar"] == True:
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
                SELECTING_MODE = False
                visibility["Build Bar"] = False
                visibility["Task Bar"] = not visibility["Task Bar"]

        # Update grid during draw mode/erase mode
        elif (event.type == pygame.MOUSEBUTTONDOWN or mouse_held_down) and DRAWING_MODE == True:
            mouse_held_down = True
            visibility["Build Bar"] = False
            for item in grid:
                if item.type == "Start":
                    START = True
                else:
                    START = False
                if item.type == "End":
                    END = True
                else:
                    END = False
                if selected_type == "Start" and START:
                    DRAWING_MODE = False
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    break
                if selected_type == "End" and END:
                    DRAWING_MODE = False
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    break
                if item.rect.collidepoint(mouse_x, mouse_y):
                    item.set_type(selected_type)
        elif (event.type == pygame.MOUSEBUTTONDOWN or mouse_held_down) and ERASING_MODE == True:
            mouse_held_down = True
            visibility["Build Bar"] = False
            for item in grid:
                if item.rect.collidepoint(mouse_x, mouse_y):
                    item.clear()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    screen.fill(BLACK)
    if visibility["Grid"]:
        grid = draw_grid(GRID_SIZE, GRAY, screen_width, screen_height, screen, grid)
    for item in grid:
        item.draw(screen)
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
