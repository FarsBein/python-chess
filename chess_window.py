import pygame
import sys
from node_class import Node 

pygame.init() # initialize all imported pygame modules. No exceptions will be raised if a module fails

WIDTH = 800; HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Online")
clock = pygame.time.Clock()

# colors
BLUE = (0, 150, 255)
PINK = (255,13,255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 87, 51)
CLAY = (63,176,172)

GREEN = (118,150,86)
PALE = 	(238,238,210)

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
    color = node.get_piece_color()
    row, col = node.get_row_col()
    possible_moves = []
    
    movements = [
        (row-1,col+1),
        (row-1,col-1),
        (row-1,col),
        (row,col+1),
        (row,col-1),
        (row+1,col+1),
        (row+1,col-1),
        (row+1,col),
    ]

    for dx,dy in movements:
        if ((0 <= dx <= 7) and (0 <= dy <= 7)) and (grid[dx][dy].empty() or grid[dx][dy].get_piece_color() != color):
            possible_moves.append((dx,dy))
    
    print('king possible_moves:', possible_moves)
    return possible_moves

def queen_moves(node, grid):
    
    possible_moves = []
    
    possible_moves += bishop_moves(node, grid)
    possible_moves += castle_moves(node, grid)
    
    print('queen possible_moves:', possible_moves)
    return possible_moves

def horse_moves(node, grid):
    color = node.get_piece_color()
    row, col = node.get_row_col()
    possible_moves = []
    
    movements = [
        (row-2,col+1),
        (row-2,col-1),
        (row-1,col+2),
        (row-1,col-2),
        (row+2,col+1),
        (row+2,col-1),
        (row+1,col+2),
        (row+1,col-2),
    ]

    for dx,dy in movements:
        if ((0 <= dx <= 7) and (0 <= dy <= 7)) and (grid[dx][dy].empty() or grid[dx][dy].get_piece_color() != color):
            possible_moves.append((dx,dy))
    
    print('horse possible_moves:', possible_moves)
    return possible_moves
   
def bishop_moves(node, grid):
    color = node.get_piece_color()
    row, col = node.get_row_col()
    possible_moves = []
    
    dx,dy = row, col
    # top right
    while in_range_7(dx-1,dy+1) and (grid[dx-1][dy+1].empty() or grid[dx-1][dy+1].get_piece_color() != color):
        possible_moves.append((dx-1,dy+1))
        if grid[dx-1][dy+1].is_opposite(color):
            break
        dx,dy = dx-1,dy+1

    dx,dy = row, col
    # top left
    while in_range_7(dx-1,dy-1) and (grid[dx-1][dy-1].empty() or grid[dx-1][dy-1].get_piece_color() != color):
        possible_moves.append((dx-1,dy-1))
        if grid[dx-1][dy-1].is_opposite(color):
            break
        dx,dy = dx-1,dy-1

    dx,dy = row, col    
    # bottom right
    while in_range_7(dx+1,dy+1) and (grid[dx+1][dy+1].empty() or grid[dx+1][dy+1].get_piece_color() != color):
        possible_moves.append((dx+1,dy+1))
        if grid[dx+1][dy+1].is_opposite(color):
            break
        dx,dy = dx+1,dy+1

    dx,dy = row, col
    # bottom left
    while in_range_7(dx+1,dy-1) and (grid[dx+1][dy-1].empty() or grid[dx+1][dy-1].get_piece_color() != color):
        possible_moves.append((dx+1,dy-1))
        if grid[dx+1][dy-1].is_opposite(color):
            break
        dx,dy = dx+1,dy-1
       
    print('bishop possible_moves:', possible_moves)
    return possible_moves

def castle_moves(node, grid):
    color = node.get_piece_color()
    row, col = node.get_row_col()
    possible_moves = []
    
    dx,dy = row, col
    # top 
    while in_range_7(dy+1) and (grid[dx][dy+1].empty() or grid[dx][dy+1].get_piece_color() != color):
        possible_moves.append((dx,dy+1))
        if grid[dx][dy+1].is_opposite(color):
            break
        dx,dy = dx,dy+1

    dx,dy = row, col
    # bottom
    while in_range_7(dy-1) and (grid[dx][dy-1].empty() or grid[dx][dy-1].get_piece_color() != color):
        possible_moves.append((dx,dy-1))
        if grid[dx][dy-1].is_opposite(color):
            break
        dx,dy = dx,dy-1

    dx,dy = row, col    
    # right
    while in_range_7(dx+1) and (grid[dx+1][dy].empty() or grid[dx+1][dy].get_piece_color() != color):
        possible_moves.append((dx+1,dy))
        if grid[dx+1][dy].is_opposite(color):
            break
        dx,dy = dx+1,dy

    dx,dy = row, col
    # left
    while in_range_7(dx-1) and (grid[dx-1][dy].empty() or grid[dx-1][dy].get_piece_color() != color):
        possible_moves.append((dx-1,dy))
        if grid[dx-1][dy].is_opposite(color):
            break
        dx,dy = dx-1,dy
    
    print('castle possible_moves:', possible_moves)
    return possible_moves

def pawn_moves(node, grid):
    color = node.get_piece_color()
    row, col = node.get_row_col()
    possible_moves = []
    if color == 'b':
        if row == 6 and grid[row-2][col].empty(): # using 6 instead of ROWS
            possible_moves.append((row-2,col))
        if in_range_7(row-1) and grid[row-1][col].empty():
            possible_moves.append((row-1,col))
        if in_range_7(row-1,col-1) and node.get_piece_color() != grid[row-1][col-1].get_piece_color() != None:
            possible_moves.append((row-1,col-1))
        if in_range_7(row-1,col+1) and node.get_piece_color() != grid[row-1][col+1].get_piece_color() != None:
            possible_moves.append((row-1,col+1))
    else:
        if row == 1 and grid[row+2][col].empty():
            possible_moves.append((row+2,col))
        if in_range_7(row+1,col) and grid[row+1][col].empty():
            possible_moves.append((row+1,col))
        if in_range_7(row+1,col-1) and node.get_piece_color() != grid[row+1][col-1].get_piece_color() != None:
            possible_moves.append((row+1,col-1))
        if in_range_7(row+1,col+1) and node.get_piece_color() != grid[row+1][col+1].get_piece_color() != None:
            possible_moves.append((row+1,col+1))
            
    print('pawn possible_moves:', possible_moves)
    
    return possible_moves

def in_range_7(dx,dy=None):
    if dy:
        return ((0 <= dx <= 7) and (0 <= dy <= 7))
    else:
        return (0 <= dx <= 7)

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
    elif piece == 'c':
        possible_moves = castle_moves(start, grid)
        if end.get_row_col() in possible_moves:
            return True
        else:
            return False    
    elif piece == 'b':
        possible_moves = bishop_moves(start, grid)
        if end.get_row_col() in possible_moves:
            return True
        else:
            return False
    elif piece == 'h':
        possible_moves = horse_moves(start, grid)
        if end.get_row_col() in possible_moves:
            return True
        else:
            return False
    elif piece == 'k':
        possible_moves = king_moves(start, grid)
        if end.get_row_col() in possible_moves:
            return True
        else:
            return False
    elif piece == 'q':
        possible_moves = queen_moves(start, grid)
        if end.get_row_col() in possible_moves:
            return True
        else:
            return False

def main():
    rows = 8
    grid = make_grid(rows, WIDTH)
    
    picked = None
    
    clock.tick(20)
    
    prev_piece = 'b'
    
    white_win = False
    black_win = False

    while (not white_win and not black_win):
        draw(grid,lambda:draw_grid(rows, WIDTH))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if pygame.mouse.get_pressed()[0]: # left click
                node = get_node(event.pos, grid, rows, WIDTH)
                print('LEFT: ',node,'picked:', picked, 'empty:',node.empty())

                if not picked:
                    if not node.empty() and (node.get_piece_color() != prev_piece):
                        picked = node
                        node.selected()
                else:
                    if validate_move(picked, node, grid):
                        temp_color = node.get_piece_color()
                        temp_name = node.get_piece_name()[1] if node.get_piece_name() else None
                        node.set_piece(picked.make_empty())
                        prev_piece = node.get_piece_color()
                        
                        if temp_name == 'k':
                            if temp_color == 'w':
                                black_win = True
                            else:
                                white_win = True
                            break
                    picked.unselected()
                    picked = None
                    
            if pygame.mouse.get_pressed()[2]: # right click
                node = get_node(event.pos, grid, rows, WIDTH)
                print('RIGHT: ',node,'picked:', picked, 'empty:',node.empty())
                if picked:
                    picked.unselected()
                    picked = None
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    grid = make_grid(rows, WIDTH)
                    picked = None
                    prev_piece = 'b'
                    white_win = False
                    black_win = False
                    
    print("GAME OVER")
    while True: 
        SCREEN.fill(WHITE)
        font = pygame.font.SysFont(None, 100)
        img = font.render('BLACK WON!!!', True, BLACK) if black_win else font.render('WHITE WON!!!', True, BLACK)
        SCREEN.blit(img, (150, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    pygame.display.update()


main()