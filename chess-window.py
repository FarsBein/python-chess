import pygame
import sys

pygame.init() # initialize all imported pygame modules. No exceptions will be raised if a module fails

WIDTH = 800; HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

# colors
BLUE = (0, 150, 255)
PINK = (255,13,255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 87, 51)
CLAY = (63,176,172)

GREEN = (118,150,86)
PALE = 	(238,238,210)

class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = width * row
        self.y = width * col
        self.width = width
        self.color = PALE if ((col+(row%2))%2 == 0) else GREEN

    def draw(self):
        pygame.draw.rect(SCREEN, self.color, [self.x,self.y, self.width, self.width])
        
    def __str__(self): 
        return '(row: ' + str(self.row) + ' ,col: ' + str(self.col) + ' ) ' + '(x: ' + str(self.x) + ' ,y: ' + str(self.x) + ' ) '

    def __lt__(self, other): # to avoid error when compared
        return False

def make_grid(rows, width_of_screen):
    grid = []
    node_width = width_of_screen // rows
    
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i,j,node_width)
            grid[i].append(node)
    
    return grid

def draw_grid(rows, width_of_screen):
    x = y = 0    
    node_width = width_of_screen // rows
    
    for i in range(rows):
        pygame.draw.line(SCREEN,BLACK, (0, i*node_width), (width_of_screen, i*node_width)) # start then end. (start/end, distance from the top)
    
    for j in range(rows):
        pygame.draw.line(SCREEN,BLACK, (j*node_width, 0), (j*node_width, width_of_screen)) # start then end. (distance from the left, start/end)
    
def draw(grid, lambda_draw_grid):
    SCREEN.fill(WHITE)
    
    # draw the nodes first before lines to see lines
    for row in grid:
        for node in row:
            node.draw()
    
    # draw lines. All the needed argument already passed before call
    lambda_draw_grid()
    
    pygame.display.update() # Called only once per frame.

def get_node(coordinate, grid, rows, width_of_screen):
    x, y = coordinate
    node_width = width_of_screen // rows
    
    x = x//node_width
    y = y//node_width
    
    return grid[x][y]

def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    
    rows  = 8
    grid = make_grid(rows, WIDTH)
    
    while True:
        
        draw(grid,lambda:draw_grid(rows, WIDTH))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if pygame.mouse.get_pressed()[0]: # left click
                node = get_node(event.pos, grid, rows, WIDTH)
                print('LEFT:  ',node)
                
    pygame.display.update()
    
main()