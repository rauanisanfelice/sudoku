import pygame, random, pygame_menu

from pygame.locals import *

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 620

SCREEN_GAME_WIDTH = 620
SCREEN_GAME_HEIGHT = 620
SIZE_DIVISION = 5

SPEED = 10
GAME_SPEED = 10

COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_LITE_GRAY = (100, 100, 100)
COLOR_STRONG_GRAY = (128, 128, 128)


# DIFICULDADE DO JOGO
def set_difficulty(value, difficulty):
    print(difficulty)


def draw_scenario():

    screen.fill(COLOR_LITE_GRAY)
    BIG_SQUARE_SIZE = (SCREEN_GAME_WIDTH - (SIZE_DIVISION * 4)) / 3
    SMALL_SQUARE_SIZE = BIG_SQUARE_SIZE / 3
    
    # DIVISOES QUADRANTES MENORES
    # VERTICAL
    pygame.draw.rect(screen, COLOR_STRONG_GRAY, (SMALL_SQUARE_SIZE, 0, SIZE_DIVISION / 2, SCREEN_GAME_HEIGHT))
    pygame.draw.rect(screen, COLOR_STRONG_GRAY, (SMALL_SQUARE_SIZE * 2, 0, SIZE_DIVISION / 2, SCREEN_GAME_HEIGHT))
    pygame.draw.rect(screen, COLOR_STRONG_GRAY, (SMALL_SQUARE_SIZE * 4, 0, SIZE_DIVISION / 2, SCREEN_GAME_HEIGHT))
    pygame.draw.rect(screen, COLOR_STRONG_GRAY, (SMALL_SQUARE_SIZE * 5, 0, SIZE_DIVISION / 2, SCREEN_GAME_HEIGHT))
    pygame.draw.rect(screen, COLOR_STRONG_GRAY, (SMALL_SQUARE_SIZE * 7, 0, SIZE_DIVISION / 2, SCREEN_GAME_HEIGHT))
    pygame.draw.rect(screen, COLOR_STRONG_GRAY, (SMALL_SQUARE_SIZE * 8, 0, SIZE_DIVISION / 2, SCREEN_GAME_HEIGHT))

    # HORIZONTAL
    pygame.draw.rect(screen, COLOR_STRONG_GRAY, (0, SMALL_SQUARE_SIZE, SCREEN_GAME_WIDTH, SIZE_DIVISION / 2))
    pygame.draw.rect(screen, COLOR_STRONG_GRAY, (0, SMALL_SQUARE_SIZE * 2, SCREEN_GAME_WIDTH, SIZE_DIVISION / 2))
    pygame.draw.rect(screen, COLOR_STRONG_GRAY, (0, SMALL_SQUARE_SIZE * 4, SCREEN_GAME_WIDTH, SIZE_DIVISION / 2))
    pygame.draw.rect(screen, COLOR_STRONG_GRAY, (0, SMALL_SQUARE_SIZE * 5, SCREEN_GAME_WIDTH, SIZE_DIVISION / 2))
    pygame.draw.rect(screen, COLOR_STRONG_GRAY, (0, SMALL_SQUARE_SIZE * 7, SCREEN_GAME_WIDTH, SIZE_DIVISION / 2))
    pygame.draw.rect(screen, COLOR_STRONG_GRAY, (0, SMALL_SQUARE_SIZE * 8, SCREEN_GAME_WIDTH, SIZE_DIVISION / 2))

    # DIVISOES QUADRANTES MAIORES
    # VERTICAL
    pygame.draw.rect(screen, COLOR_BLACK, (BIG_SQUARE_SIZE, 0, SIZE_DIVISION, SCREEN_GAME_HEIGHT))
    pygame.draw.rect(screen, COLOR_BLACK, (BIG_SQUARE_SIZE * 2, 0, SIZE_DIVISION, SCREEN_GAME_HEIGHT))
    # HORIZONTAL
    pygame.draw.rect(screen, COLOR_BLACK, (0, BIG_SQUARE_SIZE, SCREEN_GAME_WIDTH, SIZE_DIVISION))
    pygame.draw.rect(screen, COLOR_BLACK, (0, BIG_SQUARE_SIZE * 2, SCREEN_GAME_WIDTH, SIZE_DIVISION))

    # BORDAS
    # VERTICAL
    pygame.draw.rect(screen, COLOR_BLACK, (0, 0, SCREEN_GAME_WIDTH, SIZE_DIVISION))
    pygame.draw.rect(screen, COLOR_BLACK, (0, 0, SIZE_DIVISION, SCREEN_GAME_HEIGHT))
    # HORIZONTAL
    pygame.draw.rect(screen, COLOR_BLACK, (SCREEN_GAME_WIDTH - SIZE_DIVISION, 0, SIZE_DIVISION, SCREEN_GAME_HEIGHT))
    pygame.draw.rect(screen, COLOR_BLACK, (0, SCREEN_GAME_HEIGHT - SIZE_DIVISION, SCREEN_GAME_HEIGHT, SIZE_DIVISION))


# GAME
def start_the_game():

    # FPS
    clock = pygame.time.Clock()
    draw_scenario()

    while True:
        
        # FPS  
        clock.tick(30)
        
        # VERIFICA EVENTOS
        for event in pygame.event.get():
            # SAIR
            if event.type == QUIT:
                pygame.quit()
            
            # KEYDWON
            # if event.type == KEYDOWN:
            #     if event.key == K_SPACE:
            #         pass
        
        
        # ATUALIZA DA TELA
        pygame.display.update()


# INICIA JOGO COM SCREEN
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.font.Font(None, 32)

# MENU
menu = pygame_menu.Menu(SCREEN_HEIGHT, SCREEN_WIDTH, 'Bem Vindo(a)!', theme=pygame_menu.themes.THEME_GREEN)
menu.add_selector('Dificuldade :', [('Fácil', 0), ('Normal', 1), ('Difícil', 2)], onchange=set_difficulty)
menu.add_button('Jogar', start_the_game)
menu.add_button('Sair', pygame_menu.events.EXIT)
menu.mainloop(screen)
