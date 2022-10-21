import pygame
import random
import time

WIN_HEIGHT = 196
WIN_WIDTH = 392
ROWS = 7
COLUMNS = 14

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)

AGENT = (0, 255, 0)
OBJECTIVE = (255, 0, 0)


class Spot():
    def __init__(self, row, column, width, total_rows):
        self.row = row
        self.column = column
        self.x = width * row
        self.y = width * column
        self.state = False
        self.spot_width = width
        self.total_rows = total_rows
        self.color = self.get_color()
    
    def get_color(self):
        if self.state:
            color = OBJECTIVE
        else:
            color = BLACK
        return color

    def get_pos(self):
        return (self.row, self.column)
        
    def draw(self, win):
        pygame.draw.rect(win, self.get_color(), (self.x/2, self.y/2, self.spot_width/2, self.spot_width/2))
        
def make_grid(rows, columns, width):
    grid = []
    gap = width // rows
    for i in range(columns):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid

def draw_grid(win, rows, columns, width, height):
    r_gap =  height // rows
    c_gap = width // columns
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * r_gap), (width, i * r_gap))
        for j in range(columns):
            pygame.draw.line(win, GREY, (j* c_gap, 0), (j * c_gap, height))

def draw(win, grid, rows, columns, width, height):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)
            
    draw_grid(win, rows, columns, width, height)
    pygame.display.update()

#to create a function that randomly assign states to different spot objects in the grid
def random_spot_chooser(grid):
    x = random.randint(0, len(grid)-1)
    y = random.randint(0, len(grid[x])-1)

    return x, y
    
def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    while True:
        grid = make_grid(ROWS, COLUMNS, WIN_WIDTH)
        time.sleep(1)
        x, y =random_spot_chooser(grid)
        grid[7][0].state = True
        draw(SCREEN, grid, ROWS, COLUMNS, WIN_WIDTH, WIN_HEIGHT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()

main()
