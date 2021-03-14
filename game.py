import pygame, random, pygame_menu

from typing import Union
from pygame.locals import *

pygame.init()
FONT = pygame.font.Font(None, 42)

DIFFICULTY_GAME_TEXT = [('Fácil', 0), ('Normal', 1), ('Difícil', 2)]
DIFFICULTY_GAME_WEIGHTS = [[50, 50], [60, 40], [70, 30]]
DIFFICULTY_GAME = DIFFICULTY_GAME_WEIGHTS[0]
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

ERROS = 0
NUM_FALTANTES = 81
NUM_PREENCHIDOS = 0
# GRID = [
#     [8, 7, 9, 6, 5, 1, 3, 2, 4],
#     [5, 2, 3, 7, 4, 9, 1, 8, 6],
#     [1, 6, 4, 2, 3, 8, 7, 9, 5],
    
#     [6, 9, 5, 1, 2, 7, 8, 4, 3],
#     [3, 1, 7, 8, 9, 4, 6, 5, 2],
#     [2, 4, 8, 5, 6, 3, 9, 1, 7],
    
#     [4, 3, 1, 9, 7, 5, 2, 6, 8],
#     [9, 5, 6, 3, 8, 2, 4, 7, 1],
#     [7, 8, 2, 4, 1, 6, 5, 3, 9]
# ]

        

class Grid:

    def __init__(self):
        self.grid = []
    
    def initialize(self):

        list_int = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(list_int)

        col = 2
        row = 3
        for i, item in enumerate(list_int):
            
            if i % 3 == 0 and i != 0:
                row += 1
                col = 2
            col += 1

            self.grid.append({
                "text": item,
                "row": row,
                "column": col,
                "quadrante": 4,
                "preeenchido": False,
                "error": False,
            })

        for num_atual in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            for index_quadrante in range(0, 9, 1):
                
                # PULA QUADRANTE DO MEIO
                if index_quadrante == 4:
                    continue
                
                # BUCA ANALISA DO GRID
                self.analyze_grid(num_atual)
                
                # BUSCA CELULAS DO QUADRANTE QUE ESTÃO DISPONIVEIS
                list_cells_available = self.result_analyze_grid["celulas"]["quadrantes"][index_quadrante]

                delete_rows, delete_cols = self.cels_priority(num_atual, index_quadrante)
                print('Linhas que devem ser deletada: ', delete_rows)
                print('Colunas que devem ser deletada: ', delete_cols)
                
                if delete_rows:
                    filter_rows_delete = lambda x: x[0] not in delete_rows
                    if list(filter(filter_rows_delete, list_cells_available)):
                        list_cells_available = list(filter(filter_rows_delete, list_cells_available))
                if delete_cols:
                    filter_cols_delete = lambda x: x[1] not in delete_cols
                    if list(filter(filter_cols_delete, list_cells_available)):
                        list_cells_available = list(filter(filter_cols_delete, list_cells_available))

                #############################################################
                cell_selected = random.choices(list_cells_available)[0]

                self.grid.append({
                    "text": num_atual,
                    "row": cell_selected[0],
                    "column": cell_selected[1],
                    "quadrante": index_quadrante,
                    "preeenchido": False,
                    "error": False,
                })

                self.order_grid()
                self.print_grid()
                print('List Available:', list_cells_available)
                print('Numero:', num_atual, '--> Row:', cell_selected[0], 'Column:', cell_selected[1], 'Quadrante:', index_quadrante)
                print("")
                print("")
                print("")

        return self.grid
    
    def analyze_grid(self, num:int) -> dict:
        
        self.result_analyze_grid = {
            "numeros": {
                "quadrantes": {
                    0: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    1: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    2: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    3: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    4: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    5: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    6: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    7: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    8: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                },
                "colunas": {
                    0: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    1: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    2: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    3: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    4: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    5: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    6: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    7: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    8: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                },
                "linhas": {
                    0: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    1: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    2: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    3: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    4: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    5: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    6: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    7: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                    8: {
                        "numeros_faltantes": [],
                        "numeros_preenchidos": [],
                    },
                },
            },
            "celulas": {
                "quadrantes": {
                    0: [],
                    1: [],
                    2: [],
                    3: [],
                    4: [],
                    5: [],
                    6: [],
                    7: [],
                    8: [],
                },
            },
        }

        for index in range(0, 9, 1):
            # BUSCA NUMEROS DO QUADRANTE
            temp = self.get_nums_qdr(index)
            self.result_analyze_grid['numeros']['quadrantes'][index]['numeros_preenchidos'] = temp
            self.result_analyze_grid['numeros']['quadrantes'][index]['numeros_faltantes'] = list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(temp))

            temp = self.get_nums_col(index)
            self.result_analyze_grid['numeros']['colunas'][index]['numeros_preenchidos'] = temp
            self.result_analyze_grid['numeros']['colunas'][index]['numeros_faltantes'] = list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(temp))

            temp = self.get_nums_row(index)
            self.result_analyze_grid['numeros']['linhas'][index]['numeros_preenchidos'] = temp
            self.result_analyze_grid['numeros']['linhas'][index]['numeros_faltantes'] = list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(temp))
        
        for index in range(0, 9, 1):
            self.result_analyze_grid['celulas']['quadrantes'][index] = self.analyze_quadrant(index, num)

    def search_rows_cols_available(self, qdr:int, num:int=None) -> Union[list, list]:
        
        # DESCOBRE LINHAS E COLUNAS QUE SERAO ANALISADAS
        rows_available = []
        cols_available = []
        if qdr in [0, 1, 2]:
            rows_available = [0, 1, 2]
        elif qdr in [3, 4, 5]:
            rows_available = [3, 4, 5]
        else:
            rows_available = [6, 7, 8]
        
        if qdr % 3 == 0:
            cols_available = [0, 1, 2]
        elif qdr in [1, 4, 7]:
            cols_available = [3, 4, 5]
        else:
            cols_available = [6, 7, 8]
        
        # VERIFICA SE DEVE EXCLUIR ALGUM NUMERO
        if num:
            # VERIFICA SE JA POSSUI O NUMERO NO QUADRANTE
            if num in self.result_analyze_grid["numeros"]["quadrantes"][qdr]["numeros_preenchidos"]:
                return [], []

            # DESCOBRE LINHAS VALIDAS
            temp = []
            for i in rows_available:
                if num not in self.result_analyze_grid["numeros"]["linhas"][i]["numeros_preenchidos"]:
                    temp.append(i)
            rows_available = temp
            
            # DESCOBRE COLUNAS VALIDAS
            temp = []
            for i in cols_available:
                if num not in self.result_analyze_grid["numeros"]["colunas"][i]["numeros_preenchidos"]:
                    temp.append(i)
            cols_available = temp

        return rows_available, cols_available
    
    def analyze_quadrant(self, qdr:int, num:int) -> list:
        
        # DESCOBRE LINHAS E COLUNAS QUE SERAO ANALISADAS
        rows_available, cols_available = self.search_rows_cols_available(qdr, num)

        # BUSCA NUMEROS QUE JA FORAM PREENCHIDOS NO QUADRANTE ATUAL
        nums_in_qdr = self.get_nums_qdr(qdr, False)
        list_cels = self.get_col_row(nums_in_qdr) # RETONA ROW X COLUMN

        # DESCOBRE INDEX COL/ROW QUE INICIA O QUADRANTE
        index_row = 0
        index_col = 0
        list_available = []
        index_beging_col = (qdr % 3) * 3
        index_beging_row = int(qdr / 3) * 3

        # ANALISA TODAS AS CELULAS DO QUADRANTE
        for i in range(0, 9, 1):
            if i % 3 == 0 and i != 0:
                index_row += 1
                index_col = 0
            elif i != 0:
                index_col += 1
            
            # CELULA ROW X COLUMN
            check_cell = [index_beging_row + index_col, index_beging_col + index_row]

            # VERIFICA SE JA POSSUI NUMERO NO QUADRANTE
            if not list_cels:
                # VALIDA SE CELULA É VALIDA
                if check_cell[0] in rows_available and check_cell[1] in cols_available:
                    list_available.append(check_cell)
            
            else:

                # VERIFICA SE CELULA JA POSSUI CONTEUDO
                empty = True
                for cell in list_cels:
                    if cell[0] == check_cell[0] and cell[1] == check_cell[1]:
                        empty = False
                        break
                if not empty:
                    continue

                # POSSUI NUMEROS NO QUADRANTE
                # VALIDA SE A CELULA ATUAL É VALIDA
                if check_cell[0] in rows_available and check_cell[1] in cols_available:
                    
                    # CELULA ESTA DENTRO DE LINHA E COLUNA VALIDA
                    list_available.append(check_cell)
                
                else:
                    # LINHA OU COLUNA NÃO É VALIDA
                    
                    # VERIFICA SE A CELULA ESTA DENTRO DA LINHA E COLUNA VALIDA
                    if check_cell[0] in rows_available and check_cell[1] in cols_available:
                        print('check_cell:', check_cell, ' rows_available: ', rows_available)
                        list_available.append(check_cell)


        list_available = [list(x) for x in set(tuple(x) for x in list_available)]
        list_available = sorted(list_available, key=lambda x: [x[0], x[1]])
        return list_available
    
    def cels_priority(self, num:int, qdr:int) -> Union[list, list]:
        """ 
        # Cenario 1
        O num. 4 no quadrante 5 pode ser nas celulas com (*).
        No quadrante 3, obrigatoriamente tem que dar prioridade no num. 4 nas celulas [5, 1] ou [5, 2]
        ----------------------
        | | | |-|3|1|2|-| |4| |
        |4|1|2|-| | | |-| | |3|
        | |3| |-|4| | |-|1|2| |
        ----------------------
        | | |1|-|2|3|5|-|*| |*|
        | |2|3|-|6|9|4|-| |1| |
        | | | |-|8|7|1|-|3| |2|
        ----------------------
        |2| | |-| | | |-| |3|1|
        |1| | |-| | |3|-|2| | |
        |3| | |-|1|2| |-| | | |
        ----------------------
        """
        
        # ANALISA OS PROXIMOS QUADRANTES SE POSSUI UM QUADRANTE
        # COM SOMENTE UMA POSSIBILIDADE PARA O NUMERO ATUAL
        # E EXCLUI A LINHA OU COLUNA DESTA UNICA CELULA
        find_row = lambda x: x[0]
        find_cols = lambda x: x[1]

        delete_rows = []
        delete_cols = []
        
        if qdr == 8:
            return delete_rows, delete_cols
        
        for i in range(qdr + 1, 9, 1):
            
            # ANALISA SOMENTE QUANDO POSSUI DUAS CELULAS DISPONIVEIS PARA O VALOR
            cells_available = self.result_analyze_grid["celulas"]["quadrantes"][i]
            if len(cells_available) == 2:
                print('Numero:', num, 'Quadrante: ', i)
                tmp_rows = list(map(find_row, cells_available))
                tmp_cols = list(map(find_cols, cells_available))
                
                # AS DUAS CELULAS DISPONIVEIS ESTAO NA MESMA LINHA 
                # ENTAO DEVE EXCLUIR AS COLUNAS
                if tmp_rows[0] == tmp_rows[1]:
                    delete_cols = tmp_cols
                
                # AS DUAS CELULAS DISPONIVEIS ESTAO NA MESMA COLUNA 
                # ENTAO DEVE EXCLUIR AS LINHAS
                elif tmp_cols[0] == tmp_cols[1]:
                    delete_rows = tmp_rows

        return delete_rows, delete_cols

    def get_nums_col(self, col:int, row_ignore:int=None) -> list:
        filter_col = lambda x: x['column'] == col
        filter_col_ignore_row = lambda x: x['column'] == col and  x['row'] != row_ignore
        get_text = lambda x: x['text']

        if row_ignore is not None:
            list_nums_in_col = list(filter(filter_col, self.grid))
        else: 
            list_nums_in_col = list(filter(filter_col_ignore_row, self.grid))
        
        return list(map(get_text, list_nums_in_col))

    def get_nums_row(self, row:int, col_ignore:int=None) -> list:
        filter_row = lambda x: x['row'] == row
        filter_row_ignore_col = lambda x: x['row'] == row
        get_text = lambda x: x['text']
        
        if col_ignore is not None:
            list_nums_in_row = list(filter(filter_row, self.grid))
        else:
            list_nums_in_row = list(filter(filter_row_ignore_col, self.grid))
        
        return list(map(get_text, list_nums_in_row))

    def get_nums_qdr(self, qdr:int, text:bool=True) -> list:
        filter_qdr = lambda x: x['quadrante'] == qdr
        get_text = lambda x: x['text']
        
        list_nums_in_qdr = list(filter(filter_qdr, self.grid))
        if text:
            return list(map(get_text, list_nums_in_qdr))
        return list_nums_in_qdr

    def get_col_row(self, list_search:list) -> list:
        get_col_row = lambda x: [x['row'], x['column']]
        return list(map(get_col_row, list_search))

    def get_num_col_row(self, row:int, col:int) -> str:
        filter_num = lambda x: x['column'] == col and x['row'] == row
        get_text = lambda x: x['text']
        
        num = list(filter(filter_num, self.grid))
        return list(map(get_text, num))

    def order_grid(self):
        self.grid = sorted(self.grid, key=lambda x: (x["row"], x["column"]))

    def print_grid(self):
    
        self.order_grid()
        allGrid = []
        find_elem = lambda x: x['row'] == row and x['column'] == col
        get_text = lambda x: x["text"]

        for row in range(0, 9, 1):
            rowGrid = []
            if row % 3 == 0:
                allGrid.append(" ----------------------")

            for col in range(0, 9, 1):
                
                if col == 0:
                    rowGrid.append("|")

                dict_num = list(filter(find_elem, self.grid))
                if dict_num:
                    number = str(list(map(get_text, dict_num))[0])
                else:
                    number = " "
                
                if col % 3 == 0 and col != 0:
                    rowGrid.append("-|")
                rowGrid.append(number)
                
                rowGrid.append("|")
            allGrid.append(rowGrid)
        
        allGrid.append(" ----------------------")
        for i in allGrid:
            print("".join(i))


class InputBox:

    def __init__(self, x:float, y:float, w:float, h:float, position:list, text:str=''):
        global DIFFICULTY_GAME, NUM_FALTANTES, NUM_PREENCHIDOS, ERROS
        
        if text == "":
            if random.choices([0, 1], weights=DIFFICULTY_GAME, k=1)[0] == 1:
                text = str(GRID[position[0]][position[1]])
                NUM_FALTANTES -= 1
        
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
                if self.text == "" or self.error:
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
        global NUM_FALTANTES, NUM_PREENCHIDOS, ERROS
        if str(GRID[self.position[0]][self.position[1]]) != self.text:
            ERROS += 1
            self.color = COLOR_RED
            self.error = True
        else:
            NUM_FALTANTES -= 1
            NUM_PREENCHIDOS += 1
            self.color = COLOR_ACTIVE
            self.error = False

    def analyze(self, screen):
        if self.active:
            height = SCREEN_GAME_HEIGHT + 20

            num_row = GRID[self.position[0]]
            num_col = []
            num_qdr = []
            for row in GRID:
                for index, col in enumerate(row):
                    if index == self.position[1]:
                        num_col.append(col)
            
            if self.position[0] <= 2:
                if self.position[1] <= 2:
                    num_qdr.append(GRID[0][0])
                    num_qdr.append(GRID[0][1])
                    num_qdr.append(GRID[0][2])
                    num_qdr.append(GRID[1][0])
                    num_qdr.append(GRID[1][1])
                    num_qdr.append(GRID[1][2])
                    num_qdr.append(GRID[2][0])
                    num_qdr.append(GRID[2][1])
                    num_qdr.append(GRID[2][2])
                elif self.position[1] > 2 and self.position[1] <= 5:
                    num_qdr.append(GRID[1][3])
                    num_qdr.append(GRID[0][4])
                    num_qdr.append(GRID[0][5])
                    num_qdr.append(GRID[2][3])
                    num_qdr.append(GRID[1][4])
                    num_qdr.append(GRID[1][5])
                    num_qdr.append(GRID[3][3])
                    num_qdr.append(GRID[2][4])
                    num_qdr.append(GRID[2][5])
                else:
                    num_qdr.append(GRID[1][6])
                    num_qdr.append(GRID[0][7])
                    num_qdr.append(GRID[0][8])
                    num_qdr.append(GRID[2][6])
                    num_qdr.append(GRID[1][7])
                    num_qdr.append(GRID[1][8])
                    num_qdr.append(GRID[3][6])
                    num_qdr.append(GRID[2][7])
                    num_qdr.append(GRID[2][8])
            elif self.position[0] > 2 and self.position[0] <= 5:
                if self.position[1] <= 2:
                    num_qdr.append(GRID[3][0])
                    num_qdr.append(GRID[3][1])
                    num_qdr.append(GRID[3][2])
                    num_qdr.append(GRID[4][0])
                    num_qdr.append(GRID[4][1])
                    num_qdr.append(GRID[4][2])
                    num_qdr.append(GRID[5][0])
                    num_qdr.append(GRID[5][1])
                    num_qdr.append(GRID[5][2])
                elif self.position[1] > 2 and self.position[1] <= 5:
                    num_qdr.append(GRID[3][3])
                    num_qdr.append(GRID[3][4])
                    num_qdr.append(GRID[3][5])
                    num_qdr.append(GRID[4][3])
                    num_qdr.append(GRID[4][4])
                    num_qdr.append(GRID[4][5])
                    num_qdr.append(GRID[5][3])
                    num_qdr.append(GRID[5][4])
                    num_qdr.append(GRID[5][5])
                else:
                    num_qdr.append(GRID[3][6])
                    num_qdr.append(GRID[3][7])
                    num_qdr.append(GRID[3][8])
                    num_qdr.append(GRID[4][6])
                    num_qdr.append(GRID[4][7])
                    num_qdr.append(GRID[4][8])
                    num_qdr.append(GRID[5][6])
                    num_qdr.append(GRID[5][7])
                    num_qdr.append(GRID[5][8])
            else:
                if self.position[1] <= 2:
                    num_qdr.append(GRID[6][0])
                    num_qdr.append(GRID[6][1])
                    num_qdr.append(GRID[6][2])
                    num_qdr.append(GRID[7][0])
                    num_qdr.append(GRID[7][1])
                    num_qdr.append(GRID[7][2])
                    num_qdr.append(GRID[8][0])
                    num_qdr.append(GRID[8][1])
                    num_qdr.append(GRID[8][2])
                elif self.position[1] > 2 and self.position[1] <= 5:
                    num_qdr.append(GRID[6][3])
                    num_qdr.append(GRID[6][4])
                    num_qdr.append(GRID[6][5])
                    num_qdr.append(GRID[7][3])
                    num_qdr.append(GRID[7][4])
                    num_qdr.append(GRID[7][5])
                    num_qdr.append(GRID[8][3])
                    num_qdr.append(GRID[8][4])
                    num_qdr.append(GRID[8][5])
                else:
                    num_qdr.append(GRID[6][6])
                    num_qdr.append(GRID[6][7])
                    num_qdr.append(GRID[6][8])
                    num_qdr.append(GRID[7][6])
                    num_qdr.append(GRID[7][7])
                    num_qdr.append(GRID[7][8])
                    num_qdr.append(GRID[8][6])
                    num_qdr.append(GRID[8][7])
                    num_qdr.append(GRID[8][8])

            probabilidade = [1,2,3,4,5,6,7,8,9]
            screen.blit(FONT.render(f'1: {probabilidade[0]}', True, COLOR_BLACK), (height, 110))
            screen.blit(FONT.render(f'2: {probabilidade[1]}', True, COLOR_BLACK), (height, 140))
            screen.blit(FONT.render(f'3: {probabilidade[2]}', True, COLOR_BLACK), (height, 170))
            screen.blit(FONT.render(f'4: {probabilidade[3]}', True, COLOR_BLACK), (height, 200))
            screen.blit(FONT.render(f'5: {probabilidade[4]}', True, COLOR_BLACK), (height, 230))
            screen.blit(FONT.render(f'6: {probabilidade[5]}', True, COLOR_BLACK), (height, 260))
            screen.blit(FONT.render(f'7: {probabilidade[6]}', True, COLOR_BLACK), (height, 290))
            screen.blit(FONT.render(f'8: {probabilidade[7]}', True, COLOR_BLACK), (height, 320))
            screen.blit(FONT.render(f'9: {probabilidade[8]}', True, COLOR_BLACK), (height, 350))


# DIFICULDADE DO JOGO
def set_difficulty(value, difficulty):
    global DIFFICULTY_GAME
    DIFFICULTY_GAME = DIFFICULTY_GAME_WEIGHTS[difficulty]
    print('Dificuldade: ', DIFFICULTY_GAME_TEXT[difficulty][0])


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


def update_info():
    global ERROS, NUM_FALTANTES, NUM_PREENCHIDOS

    height = SCREEN_GAME_HEIGHT + 20
    screen.blit(FONT.render(f'Num faltantes: {NUM_FALTANTES}', True, COLOR_BLACK), (height, 20))
    screen.blit(FONT.render(f'Num preenchidos: {NUM_PREENCHIDOS}', True, COLOR_BLACK), (height, 50))
    screen.blit(FONT.render(f'Erros: {ERROS}', True, COLOR_BLACK), (height, 80))


# GAME
def start_the_game():
    
    global NUM_FALTANTES, GRID
    
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
        # TODO VALIDAR SE ESTA: ROW X COLUMN
        inputBoxSelect["text"] = GRID.get_num_col_row(inputBoxSelect["position"][0], inputBoxSelect["position"][1])
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
            box.analyze(screen)

        pygame.display.flip()
        
        # ATUALIZA INFO
        update_info()

        # ATUALIZA DA TELA
        pygame.display.update()

        if NUM_FALTANTES == 0:
            break


GRID = Grid()
GRID.initialize()

# PROPIEDADES SCREEN
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# MENU
menu = pygame_menu.Menu(SCREEN_HEIGHT, SCREEN_WIDTH, 'Bem Vindo(a)!', theme=pygame_menu.themes.THEME_GREEN)
menu.add_selector('Dificuldade :', DIFFICULTY_GAME_TEXT, onchange=set_difficulty)
menu.add_button('Jogar', start_the_game)
menu.add_button('Sair', pygame_menu.events.EXIT)
menu.mainloop(screen)
