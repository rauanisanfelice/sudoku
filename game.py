import pygame, random, pygame_menu

from pygame.locals import *

pygame.init()
FONT = pygame.font.Font(None, 42)

DIFFICULTY_GAME = [('Fácil', 0), ('Normal', 1), ('Difícil', 2)]
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 596

SCREEN_GAME_WIDTH = 596
SCREEN_GAME_HEIGHT = 596

SIZE_DIVISION_BIG_SQUARE = 5
SIZE_DIVISION_SMALL_SQUARE = 2
SIZE_SQUARE = 60

COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_LITE_GRAY = (100, 100, 100)
COLOR_STRONG_GRAY = (128, 128, 128)
COLOR_INACTIVE = COLOR_STRONG_GRAY
COLOR_ACTIVE = (255, 255, 255)

SMALL_SQUARE_SIZE = SIZE_SQUARE + (SIZE_DIVISION_SMALL_SQUARE * 2)
BIG_SQUARE_SIZE = (SMALL_SQUARE_SIZE * 3) + SIZE_DIVISION_BIG_SQUARE

GRID =[ 
    [8, 7, 9, 6, 5, 1, 3, 2, 4],
    [5, 2, 3, 7, 4, 9, 1, 8, 6],
    [1, 6, 4, 2, 3, 8, 7, 9, 5],
    
    [6, 9, 5, 1, 2, 7, 8, 4, 3],
    [3, 1, 7, 8, 9, 4, 6, 5, 2],
    [2, 4, 8, 5, 6, 3, 9, 1, 7],
    
    [4, 3, 1, 9, 7, 5, 2, 6, 8],
    [9, 5, 6, 3, 8, 2, 4, 7, 1],
    [7, 8, 2, 4, 1, 6, 5, 3, 9]
] 

class InputBox:

    def __init__(self, x:float, y:float, w:float, h:float, position:list, text:str=''):
        
        if text == "":
            if random.choices([0, 1], weights = [10, 90], k=1)[0] == 1:
                text = str(GRID[position[0]][position[1]])
        
        self.rect = pygame.Rect(x, y, w, h)
        self.position = position
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.error = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_ESCAPE:
                    self.active = False
                    self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
                
                else:
                    if self.text == "" or self.error == True:
                        self.text = event.unicode
                        self.check()

                        # Re-render the text
                        self.txt_surface = FONT.render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 25, self.rect.y + 20))
        pygame.draw.rect(screen, self.color, self.rect, SIZE_DIVISION_SMALL_SQUARE)
    
    def check(self):
        if str(GRID[self.position[0]][self.position[1]]) != self.text:
            self.color = COLOR_RED
            self.error = True
        else:
            self.color = COLOR_ACTIVE
            self.error = False



# DIFICULDADE DO JOGO
def set_difficulty(value, difficulty):
    print('Dificuldade: ', DIFFICULTY_GAME[difficulty][0])


def draw_scenario():

    screen.fill(COLOR_LITE_GRAY)

    # DIVISOES QUADRANTES MAIORES
    # VERTICAL
    pygame.draw.rect(screen, COLOR_BLACK, (BIG_SQUARE_SIZE, 0, SIZE_DIVISION_BIG_SQUARE, SCREEN_GAME_HEIGHT))
    pygame.draw.rect(screen, COLOR_BLACK, (BIG_SQUARE_SIZE * 2, 0, SIZE_DIVISION_BIG_SQUARE, SCREEN_GAME_HEIGHT))
    # HORIZONTAL
    pygame.draw.rect(screen, COLOR_BLACK, (0, BIG_SQUARE_SIZE, SCREEN_GAME_WIDTH, SIZE_DIVISION_BIG_SQUARE))
    pygame.draw.rect(screen, COLOR_BLACK, (0, BIG_SQUARE_SIZE * 2, SCREEN_GAME_WIDTH, SIZE_DIVISION_BIG_SQUARE))

    # BORDAS
    # VERTICAL
    pygame.draw.rect(screen, COLOR_BLACK, (0, 0, SCREEN_GAME_WIDTH, SIZE_DIVISION_BIG_SQUARE))
    pygame.draw.rect(screen, COLOR_BLACK, (0, 0, SIZE_DIVISION_BIG_SQUARE, SCREEN_GAME_HEIGHT))
    # HORIZONTAL
    pygame.draw.rect(screen, COLOR_BLACK, (SCREEN_GAME_WIDTH - SIZE_DIVISION_BIG_SQUARE, 0, SIZE_DIVISION_BIG_SQUARE, SCREEN_GAME_HEIGHT))
    pygame.draw.rect(screen, COLOR_BLACK, (0, SCREEN_GAME_HEIGHT - SIZE_DIVISION_BIG_SQUARE, SCREEN_GAME_HEIGHT, SIZE_DIVISION_BIG_SQUARE))


# GAME
def start_the_game():

    # FPS
    clock = pygame.time.Clock()
    draw_scenario()

    # DIVISOES QUADRANTES MENORES
    inputBoxs = [
        # QUADRANTE 01
        {"x": SIZE_DIVISION_BIG_SQUARE,                                                     "y": SIZE_DIVISION_BIG_SQUARE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [0, 0]},
        {"x": SIZE_DIVISION_BIG_SQUARE + SMALL_SQUARE_SIZE,                                 "y": SIZE_DIVISION_BIG_SQUARE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [0, 1]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (SMALL_SQUARE_SIZE * 2),                           "y": SIZE_DIVISION_BIG_SQUARE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [0, 2]},
        {"x": SIZE_DIVISION_BIG_SQUARE,                                                     "y": SIZE_DIVISION_BIG_SQUARE + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [1, 0]},
        {"x": SIZE_DIVISION_BIG_SQUARE + SMALL_SQUARE_SIZE,                                 "y": SIZE_DIVISION_BIG_SQUARE + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [1, 1]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (SMALL_SQUARE_SIZE * 2),                           "y": SIZE_DIVISION_BIG_SQUARE + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [1, 2]},
        {"x": SIZE_DIVISION_BIG_SQUARE,                                                     "y": SIZE_DIVISION_BIG_SQUARE + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [2, 0]},
        {"x": SIZE_DIVISION_BIG_SQUARE + SMALL_SQUARE_SIZE,                                 "y": SIZE_DIVISION_BIG_SQUARE + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [2, 1]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (SMALL_SQUARE_SIZE * 2),                           "y": SIZE_DIVISION_BIG_SQUARE + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [2, 2]},
        # QUADRANTE 02
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE,                                   "y": SIZE_DIVISION_BIG_SQUARE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [0, 3]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + SMALL_SQUARE_SIZE,               "y": SIZE_DIVISION_BIG_SQUARE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [0, 4]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + (SMALL_SQUARE_SIZE * 2),         "y": SIZE_DIVISION_BIG_SQUARE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [0, 5]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE,                                   "y": SIZE_DIVISION_BIG_SQUARE + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [1, 3]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + SMALL_SQUARE_SIZE,               "y": SIZE_DIVISION_BIG_SQUARE + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [1, 4]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + (SMALL_SQUARE_SIZE * 2),         "y": SIZE_DIVISION_BIG_SQUARE + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [1, 5]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE,                                   "y": SIZE_DIVISION_BIG_SQUARE + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [2, 3]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + SMALL_SQUARE_SIZE,               "y": SIZE_DIVISION_BIG_SQUARE + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [2, 4]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + (SMALL_SQUARE_SIZE * 2),         "y": SIZE_DIVISION_BIG_SQUARE + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [2, 5]},
        # QUADRANTE 03
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2),                             "y": SIZE_DIVISION_BIG_SQUARE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [0, 6]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + SMALL_SQUARE_SIZE,         "y": SIZE_DIVISION_BIG_SQUARE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [0, 7]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + (SMALL_SQUARE_SIZE * 2),   "y": SIZE_DIVISION_BIG_SQUARE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [0, 8]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2),                             "y": SIZE_DIVISION_BIG_SQUARE + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [1, 6]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + SMALL_SQUARE_SIZE,         "y": SIZE_DIVISION_BIG_SQUARE + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [1, 7]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + (SMALL_SQUARE_SIZE * 2),   "y": SIZE_DIVISION_BIG_SQUARE + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [1, 8]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2),                             "y": SIZE_DIVISION_BIG_SQUARE + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [2, 6]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + SMALL_SQUARE_SIZE,         "y": SIZE_DIVISION_BIG_SQUARE + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [2, 7]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + (SMALL_SQUARE_SIZE * 2),   "y": SIZE_DIVISION_BIG_SQUARE + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [2, 8]},
        # QUADRANTE 04
        {"x": SIZE_DIVISION_BIG_SQUARE,                                                     "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [3, 0]},
        {"x": SIZE_DIVISION_BIG_SQUARE + SMALL_SQUARE_SIZE,                                 "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [3, 1]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (SMALL_SQUARE_SIZE * 2),                           "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [3, 2]},
        {"x": SIZE_DIVISION_BIG_SQUARE,                                                     "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [4, 0]},
        {"x": SIZE_DIVISION_BIG_SQUARE + SMALL_SQUARE_SIZE,                                 "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [4, 1]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (SMALL_SQUARE_SIZE * 2),                           "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [4, 2]},
        {"x": SIZE_DIVISION_BIG_SQUARE,                                                     "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [5, 0]},
        {"x": SIZE_DIVISION_BIG_SQUARE + SMALL_SQUARE_SIZE,                                 "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [5, 1]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (SMALL_SQUARE_SIZE * 2),                           "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [5, 2]},
        # QUADRANTE 05
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE,                                   "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [3, 3]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + SMALL_SQUARE_SIZE,               "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [3, 4]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + (SMALL_SQUARE_SIZE * 2),         "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [3, 5]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE,                                   "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [4, 3]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + SMALL_SQUARE_SIZE,               "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [4, 4]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + (SMALL_SQUARE_SIZE * 2),         "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [4, 5]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE,                                   "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [5, 3]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + SMALL_SQUARE_SIZE,               "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [5, 4]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + (SMALL_SQUARE_SIZE * 2),         "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [5, 5]},
        # QUADRANTE 06
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2),                             "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [3, 6]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + SMALL_SQUARE_SIZE,         "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [3, 7]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + (SMALL_SQUARE_SIZE * 2),   "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [3, 8]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2),                             "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [4, 6]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + SMALL_SQUARE_SIZE,         "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [4, 7]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + (SMALL_SQUARE_SIZE * 2),   "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [4, 8]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2),                             "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [5, 6]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + SMALL_SQUARE_SIZE,         "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [5, 7]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + (SMALL_SQUARE_SIZE * 2),   "y": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [5, 8]},
        # QUADRANTE 07
        {"x": SIZE_DIVISION_BIG_SQUARE,                                                     "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [6, 0]},
        {"x": SIZE_DIVISION_BIG_SQUARE + SMALL_SQUARE_SIZE,                                 "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [6, 1]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (SMALL_SQUARE_SIZE * 2),                           "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [6, 2]},
        {"x": SIZE_DIVISION_BIG_SQUARE,                                                     "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [7, 0]},
        {"x": SIZE_DIVISION_BIG_SQUARE + SMALL_SQUARE_SIZE,                                 "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [7, 1]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (SMALL_SQUARE_SIZE * 2),                           "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [7, 2]},
        {"x": SIZE_DIVISION_BIG_SQUARE,                                                     "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [8, 0]},
        {"x": SIZE_DIVISION_BIG_SQUARE + SMALL_SQUARE_SIZE,                                 "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [8, 1]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (SMALL_SQUARE_SIZE * 2),                           "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [8, 2]},
        # QUADRANTE 08
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE,                                   "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [6, 3]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + SMALL_SQUARE_SIZE,               "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [6, 4]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + (SMALL_SQUARE_SIZE * 2),         "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [6, 5]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE,                                   "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [7, 3]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + SMALL_SQUARE_SIZE,               "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [7, 4]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + (SMALL_SQUARE_SIZE * 2),         "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [7, 5]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE,                                   "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [8, 3]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + SMALL_SQUARE_SIZE,               "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [8, 4]},
        {"x": SIZE_DIVISION_BIG_SQUARE + BIG_SQUARE_SIZE + (SMALL_SQUARE_SIZE * 2),         "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [8, 5]},
        # QUADRANTE 09
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2),                             "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [6, 6]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + SMALL_SQUARE_SIZE,         "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [6, 7]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + (SMALL_SQUARE_SIZE * 2),   "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [6, 8]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2),                             "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [7, 6]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + SMALL_SQUARE_SIZE,         "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [7, 7]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + (SMALL_SQUARE_SIZE * 2),   "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + SMALL_SQUARE_SIZE, "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [7, 8]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2),                             "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [8, 6]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + SMALL_SQUARE_SIZE,         "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [8, 7]},
        {"x": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + (SMALL_SQUARE_SIZE * 2),   "y": SIZE_DIVISION_BIG_SQUARE + (BIG_SQUARE_SIZE * 2) + (SMALL_SQUARE_SIZE * 2), "w": SMALL_SQUARE_SIZE, "h": SMALL_SQUARE_SIZE, "position": [8, 8]},
    ]

    input_boxes = []
    for inputBoxSelect in inputBoxs:
        input_boxes.append(InputBox(**inputBoxSelect))

    while True:
        
        # FPS  
        clock.tick(30)
        
        # VERIFICA EVENTOS
        for event in pygame.event.get():
            # SAIR
            if event.type == QUIT:
                pygame.quit()
            
            # VERIFICA SE BOX ESTA SELECIONADA
            for box in input_boxes:
                box.handle_event(event)

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        pygame.display.flip()
        
        # ATUALIZA DA TELA
        pygame.display.update()

# PROPIEDADES SCREEN
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# MENU
menu = pygame_menu.Menu(SCREEN_HEIGHT, SCREEN_WIDTH, 'Bem Vindo(a)!', theme=pygame_menu.themes.THEME_GREEN)
menu.add_selector('Dificuldade :', DIFFICULTY_GAME, onchange=set_difficulty)
menu.add_button('Jogar', start_the_game)
menu.add_button('Sair', pygame_menu.events.EXIT)
menu.mainloop(screen)
