import pygame
from colors import *
from GridPoint import *

def draw_grid(grid_size, grid_color, screen_width, screen_height, screen, grid):
    # Vertical Lines
    x = (screen_width%grid_size)/2
    for i in range(1, screen_width//grid_size):
        x += grid_size
        pygame.draw.line(screen, grid_color, (x, grid_size+((screen_height%grid_size)/2)), (x, screen_height-(grid_size + (screen_height%grid_size)/2)))
    
    # Horizontal Lines
    y = (screen_height%grid_size)/2
    for i in range(1, screen_height//grid_size):
        y += grid_size
        pygame.draw.line(screen, grid_color, (grid_size+((screen_width%grid_size)/2), y), (screen_width-(grid_size + (screen_width%grid_size)/2), y))

    # Append all grid locations to grid list
    if len(grid) == 0:
        for i in range((screen_width//grid_size)-2):
            for j in range((screen_height//grid_size)-2):
                left = ((screen_width%grid_size)/2)+(grid_size * (i+1))
                top = ((screen_height%grid_size)/2)+(grid_size * (j+1))
                grid.append([False, pygame.Rect(left, top, grid_size, grid_size)])
        print("MADE NEW GRID")
    return grid

def draw_taskbar(screen_width, screen_height, screen):
    bar = pygame.Rect(screen_width*.10, screen_height*.95, screen_width*.80, screen_height*.05)
    pygame.draw.rect(screen, WHITE, bar, 0, 0, min(screen_height,screen_width)//50, min(screen_height,screen_width)//50)
    buttons = []
    buttons.append((1, pygame.Rect(screen_width*.10, screen_height*.95, screen_width*.08, screen_height*.05)))
    for i in range(1, 10):
        pygame.draw.line(screen, BLACK, (screen_width*.10 + ((screen_width*.80)/10)*i, screen_height*.95), (screen_width*.10 + ((screen_width*.80)/10)*i, screen_height), 5)
        buttons.append((i+1, pygame.Rect((screen_width*.10 + ((screen_width*.80)/10)*i), screen_height*.95, screen_width*.08, screen_height*.05)))
    
    for i in range(len(buttons)):
        font = pygame.font.Font(None, int(screen_width*.02))
        if i == 0:
            text_surface = font.render("Grid", True, BLACK)
        elif i == 1:
            text_surface = font.render("Build", True, BLACK)
        elif i == 2:
            text_surface = font.render("Erase", True, BLACK)
        else:
            text_surface = font.render(str(i+1), True, BLACK)
        text_rect = text_surface.get_rect(center=buttons[i][1].center)
        screen.blit(text_surface, text_rect)

    return bar, buttons

def draw_buildbar(screen_width, screen_height, screen):
    bar = pygame.Rect(screen_width*.10, screen_height*.88, screen_width*.24, screen_height*.05)
    pygame.draw.rect(screen, WHITE, bar, 0, min(screen_height,screen_width)//50)
    buttons = []
    buttons.append((1, pygame.Rect(screen_width*.10, screen_height*.88, screen_width*.03, screen_height*.05)))
    for i in range(1, 8):
        pygame.draw.line(screen, BLACK, (screen_width*.10 + ((screen_width*.24)/8)*i, screen_height*.88), (screen_width*.10 + ((screen_width*.24)/8)*i, screen_height*.93), 5)
        buttons.append((i+1, pygame.Rect((screen_width*.10 + ((screen_width*.24)/8)*i), screen_height*.88, screen_width*.03, screen_height*.05)))
    
    for i in range(len(buttons)):
        font = pygame.font.Font(None, int(screen_width*.02))
        text_surface = font.render(str(i+1), True, BLACK)
        text_rect = text_surface.get_rect(center=buttons[i][1].center)
        screen.blit(text_surface, text_rect)
    
    return bar, buttons

def draw_minimize(screen_width, screen_height, color, screen):
    box = pygame.Rect(screen_width*.05, screen_height*.975, screen_width*.05, screen_height*.025)
    pygame.draw.rect(screen, color, box, 0, 0, min(screen_height,screen_width)//50)
    return box