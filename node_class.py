import pygame
import sys

WIDTH = 800; HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
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
    
    def is_opposite(self, color):
        if self.get_piece_color():
            return self.get_piece_color() != color
        else:
            return False
    
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
