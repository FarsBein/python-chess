import pygame
import sys

pygame.init() # initialize all imported pygame modules. No exceptions will be raised if a module fails

WIDTH = 800; HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Online")

# white pieces
wk = pygame.image.load(r"C:\Users\User\Desktop\dev\projects\python-chess\img\white-king.png").convert_alpha()
wk = pygame.transform.smoothscale(wk, (100, 100)) 
wq = pygame.image.load(r"C:\Users\User\Desktop\dev\projects\python-chess\img\white-queen.png").convert_alpha()
wq = pygame.transform.smoothscale(wq, (100, 100)) 
wc = pygame.image.load(r"C:\Users\User\Desktop\dev\projects\python-chess\img\white-castle.png").convert_alpha()
wc = pygame.transform.smoothscale(wc, (100, 100)) 
wh = pygame.image.load(r"C:\Users\User\Desktop\dev\projects\python-chess\img\white-horse.png").convert_alpha()
wh = pygame.transform.smoothscale(wh, (100, 100)) 
wb = pygame.image.load(r"C:\Users\User\Desktop\dev\projects\python-chess\img\white-bishop.png").convert_alpha()
wb = pygame.transform.smoothscale(wb, (100, 100)) 
wp = pygame.image.load(r"C:\Users\User\Desktop\dev\projects\python-chess\img\white-pawn.png").convert_alpha()
wp = pygame.transform.smoothscale(wp, (100, 100)) 
# black pieces
bk = pygame.image.load(r"C:\Users\User\Desktop\dev\projects\python-chess\img\black-king.png").convert_alpha()
bk = pygame.transform.smoothscale(bk, (100, 100)) 
bq = pygame.image.load(r"C:\Users\User\Desktop\dev\projects\python-chess\img\black-queen.png").convert_alpha()
bq = pygame.transform.smoothscale(bq, (100, 100)) 
bc = pygame.image.load(r"C:\Users\User\Desktop\dev\projects\python-chess\img\black-castle.png").convert_alpha()
bc = pygame.transform.smoothscale(bc, (100, 100)) 
bh = pygame.image.load(r"C:\Users\User\Desktop\dev\projects\python-chess\img\black-horse.png").convert_alpha()
bh = pygame.transform.smoothscale(bh, (100, 100)) 
bb = pygame.image.load(r"C:\Users\User\Desktop\dev\projects\python-chess\img\black-bishop.png").convert_alpha()
bb = pygame.transform.smoothscale(bb, (100, 100)) 
bp = pygame.image.load(r"C:\Users\User\Desktop\dev\projects\python-chess\img\black-pawn.png").convert_alpha()
bp = pygame.transform.smoothscale(bp, (100, 100)) 

pieces = {'wk':wk,'wq':wq,'wc':wc,'wh':wh,'wb':wb,'wp':wp,'bk':bk,'bq':bq,'bc':bc,'bh':bh,'bb':bb,'bp':bp}

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
        self.x = width * col
        self.y = width * row
        self.width = width
        self.color = PALE if ((col+(row%2))%2 == 0) else GREEN
        self.piece = None
        self.piece_name = None
        self.picked = False
    
    def get_row_col(self):
        return (self.row,self.col)
    
    def selected(self):
        self.picked = True    
    
    def unselected(self):
        self.picked = False  
    
    def empty(self):
        return self.piece == None
    
    def make_empty(self):
        temp = self.piece_name 
        self.piece = None
        self.piece_name = None
        return temp
    
    def get_piece_color(self):
        if self.piece_name:
            return self.piece_name[0]
        else:
            return None
    
    def get_piece_name(self):
        return self.piece_name
    
    def get_piece(self):
        return self.piece_name
    
    def set_piece(self, piece_name):
        if piece_name:
            self.piece_name = piece_name
            self.piece = pieces[piece_name]
    
    def draw(self):
        if self.picked:
            pygame.draw.rect(SCREEN, RED, [self.x,self.y, self.width, self.width])
        else:
            pygame.draw.rect(SCREEN, self.color, [self.x,self.y, self.width, self.width])
    
    def draw_piece(self):
        if self.piece:
            SCREEN.blit(self.piece, (self.x, self.y))
    
    def __str__(self): 
        return '(row: ' + str(self.row) + ' ,col: ' + str(self.col) + ' ) ' + '(x: ' + str(self.x) + ' ,y: ' + str(self.y) + ' ) ' + 'piece: ' + str(self.piece_name)

    def __lt__(self, other): # to avoid error when compared
        return False

def make_grid(rows, width_of_screen):
    grid = []
    node_width = width_of_screen // rows    
    for row in range(rows):
        grid.append([])
        for col in range(rows):
            node = Node(row,col,node_width)
            if row == 1: 
                node.set_piece('wp')
            elif row == 6: 
                node.set_piece('bp')
            elif row == 0 and (col == 0 or col == rows-1): 
                node.set_piece('wc')
            elif row == rows-1 and (col == 0 or col == rows-1): 
                node.set_piece('bc')
            elif row == 0 and (col == 1 or col == 6): 
                node.set_piece('wh')
            elif row == rows-1 and (col == 1 or col == 6): 
                node.set_piece('bh')
            elif row == 0 and (col == 2 or col == 5): 
                node.set_piece('wb')
            elif row == rows-1 and (col == 2 or col == 5): 
                node.set_piece('bb')
            elif row == 0 and col == 3:
                node.set_piece('wq')
            elif row == rows-1 and col == 3:
                node.set_piece('bq')
            elif row == 0 and col == 4:
                node.set_piece('wk')
            elif row == rows-1 and col == 4:
                node.set_piece('bk')
            
            grid[row].append(node)
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
            node.draw()        # draw box with color
            node.draw_piece()  # draw piece
            
    # draw lines. All the needed argument already passed before call
    lambda_draw_grid()
    
    
    pygame.display.update() # Called only once per frame.

def get_node(coordinate, grid, rows, width_of_screen):
    x, y = coordinate
    node_width = width_of_screen // rows
    
    x = x//node_width
    y = y//node_width
    
    return grid[y][x]

def king_moves(node, grid):
    pass

def queen_moves(node, grid):
    pass

def horse_moves(node, grid):
    pass

def bishop_moves(node, grid):
    pass

def castle_moves(node, grid):
    pass

def pawn_moves(node, grid):
    color = node.get_piece_color()
    row, col = node.get_row_col()
    possible_moves = []
    if color == 'b':
        if row == 6 and grid[row-2][col].empty(): # using 6 instead of ROWS
            possible_moves.append((row-2,col))
        if grid[row-1][col].empty():
            possible_moves.append((row-1,col))
        if node.get_piece_color() != grid[row-1][col-1].get_piece_color() != None:
            possible_moves.append((row-1,col-1))
        if node.get_piece_color() != grid[row-1][col+1].get_piece_color() != None:
            possible_moves.append((row-1,col+1))
    else:
        if row == 1 and grid[row+2][col].empty():
            possible_moves.append((row+2,col))
        if grid[row+1][col].empty():
            possible_moves.append((row+1,col))
        if node.get_piece_color() != grid[row+1][col-1].get_piece_color() != None:
            possible_moves.append((row+1,col-1))
        if node.get_piece_color() != grid[row+1][col+1].get_piece_color() != None:
            possible_moves.append((row+1,col+1))
            
    print('pawn possible_moves:', possible_moves)
    
    return possible_moves

def validate_move(start, end, grid):
    if start.get_piece_color() == end.get_piece_color():
        return False

    piece = start.get_piece_name()[1] # e.g. 'bp' -> 'p' which is queen
    
    if piece == 'p':
        possible_moves = pawn_moves(start, grid)
        if end.get_row_col() in possible_moves:
            return True
        else:
            return False

def main():
    rows = 8
    grid = make_grid(rows, WIDTH)
    
    picked = None
    
    while True:
        draw(grid,lambda:draw_grid(rows, WIDTH))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if pygame.mouse.get_pressed()[0]: # left click
                node = get_node(event.pos, grid, rows, WIDTH)
                print('LEFT: ',node,'picked:', picked, 'empty:',node.empty())
                if not picked:
                    if not node.empty():
                        picked = node
                        node.selected()
                else:
                    if validate_move(picked, node, grid):
                        node.set_piece(picked.make_empty())
                    picked.unselected()
                    picked = None
                    
            if pygame.mouse.get_pressed()[2]: # right click
                node = get_node(event.pos, grid, rows, WIDTH)
                print('RIGHT:  ',node.get_piece_name())
                if picked:
                    picked.unselected()
                    picked = None

    pygame.display.update()
    
main()