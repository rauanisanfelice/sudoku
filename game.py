import pygame, random, pygame_menu

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
        
        sequencia = [
            { "col": None, "row": 0},
            { "col": 8, "row": None},
            { "col": None, "row": 8},
            { "col": 0, "row": None},
            { "col": None, "row": 1},
            { "col": 7, "row": None},
            { "col": None, "row": 7},
            { "col": 1, "row": None},
            { "col": None, "row": 2},
            { "col": 6, "row": None},
            { "col": None, "row": 6},
        ]

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

        get_text = lambda x: x['text']
        get_column = lambda x: x['column']
        filter_row = lambda x: x['row'] == row
        filter_col = lambda x: x['column'] == col
        
        row_qdr = 0
        firts = True
        
        for item in sequencia:
            
            # CENARIO DE COLUNA
            if item['col'] is not None:
                
                # REMOVE NUMEROS QUE JA POSSUI NA COLUNA
                col = item['col']
                list_nums_in_col = list(filter(filter_col, self.grid))
                nums_in_col = list(map(get_text, list_nums_in_col))
                nums_faltantes = list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(nums_in_col))
                total_nums_faltantes = len(nums_faltantes)

                for i in range(0, total_nums_faltantes, 1):

                    # ATUALIZA E REMOVE NUMEROS QUE JA POSSUI NA COLUNA
                    list_nums_in_col = list(filter(filter_col, self.grid))
                    nums_in_col = list(map(get_text, list_nums_in_col))
                    nums_faltantes = list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(nums_in_col))

                    # row = max(list_nums_in_col, key=lambda x: x["row"])["row"] + 1
                    row = self.get_index_row_empty(col)
                    
                    # REMOVE NUMEROS QUE JA POSSUI NA LINHA
                    list_nums_in_row = list(filter(filter_row, self.grid))
                    nums_in_row = list(map(get_text, list_nums_in_row))
                    nums_faltantes = list(set(nums_faltantes) - set(nums_in_row))
                    
                    # DESCOBRE QUADRANTE
                    row_qdr  = int(row / 3)
                    qdr  = int(col / 3) + (row_qdr * 3)

                    # REMOVE NUMEROS QUE JA POSSUI NO QUADRANTE
                    nums_in_qdr = self.get_nums_qdr(qdr)
                    nums_faltantes = list(set(nums_faltantes) - set(nums_in_qdr))
                    
                    #############################################################
                    list_nums_priority = self.nums_priority(col, row, qdr)
                    if list_nums_priority:
                        if list(set(nums_faltantes).intersection(list_nums_priority)):
                            nums_faltantes_priority = list(set(nums_faltantes).intersection(list_nums_priority))
                            nums_faltantes = nums_faltantes_priority

                    #############################################################
                    self.grid.append({
                        "text": random.choices(nums_faltantes)[0],
                        "row": row,
                        "column": col,
                        "quadrante": qdr,
                        "preeenchido": False,
                        "error": False,
                    })

                    print("")
                    print("")
                    print("")
                    self.order_grid()
                    self.print_grid()
                    
            elif item['row'] is not None:
                
                # REMOVE NUMEROS QUE JA POSSUI NA LINHA
                row = item['row']
                list_nums_in_row = list(filter(filter_row, self.grid))
                nums_in_row = list(map(get_text, list_nums_in_row))
                nums_faltantes = list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(nums_in_row))
                total_nums_faltantes = len(nums_faltantes)

                for i in range(0, total_nums_faltantes, 1):
                    
                    list_nums_in_row = list(filter(filter_row, self.grid))
                    nums_in_row = list(map(get_text, list_nums_in_row))
                    nums_faltantes = list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(nums_in_row))

                    col = self.get_index_col_empty(row)

                    # REMOVE NUMEROS QUE JA POSSUI NA COLUNA
                    list_nums_in_col = list(filter(filter_col, self.grid))
                    nums_in_col = list(map(get_text, list_nums_in_col))
                    nums_faltantes = list(set(nums_faltantes) - set(nums_in_col))

                    # DESCOBRE QUADRANTE
                    row_qdr = int(row / 3)
                    qdr = int(col / 3) + (row_qdr * 3)

                    # REMOVE NUMEROS QUE JA POSSUI NO QUADRANTE
                    nums_in_qdr = self.get_nums_qdr(qdr)
                    nums_faltantes = list(set(nums_faltantes) - set(nums_in_qdr))

                    #############################################################
                    list_nums_priority = self.nums_priority(col, row, qdr, False)
                    if list_nums_priority:
                        if list(set(nums_faltantes).intersection(list_nums_priority)):
                            nums_faltantes_priority = list(set(nums_faltantes).intersection(list_nums_priority))
                            nums_faltantes = nums_faltantes_priority

                    #############################################################
                    self.grid.append({
                        "text": random.choices(nums_faltantes)[0],
                        "row": row,
                        "column": col,
                        "quadrante": qdr,
                        "preeenchido": False,
                        "error": False,
                    })
                    
                    print("")
                    print("")
                    print("")
                    self.order_grid()
                    self.print_grid()


            print("")
            print("")
            print("")
            self.order_grid()
            self.print_grid()

        return self.grid
    
    def nums_priority(self, col:int, row:int, qdr:int, is_col:bool=True) -> list:
        
        print("")
        print("")
        print("")
        self.print_grid()

        nums_priority_qdrs = []
        nums_priority_cols = []
        nums_priority_rows = []
        nums_in_col_01 = []
        nums_in_col_02 = []

        #############################################################
        # DA PRIORIDADE NOS NUMEROS DOS PROXIMOS QUADRANTES
        if is_col:
            if qdr in [0, 1, 2]:
                nums_in_qdr_01 = self.get_nums_qdr(qdr + 3, col=col)
                nums_in_qdr_02 = self.get_nums_qdr(qdr + 6, col=col)
            
            elif qdr in [3, 4, 5]:
                nums_in_qdr_01 = self.get_nums_qdr(qdr - 3, col=col)
                nums_in_qdr_02 = self.get_nums_qdr(qdr + 3, col=col)
            
            else:
                nums_in_qdr_01 = self.get_nums_qdr(qdr - 3, col=col)
                nums_in_qdr_02 = self.get_nums_qdr(qdr - 6, col=col)

        else:

            if qdr % 3 == 0:
                nums_in_qdr_01 = self.get_nums_qdr(qdr + 1, row=row)
                nums_in_qdr_02 = self.get_nums_qdr(qdr + 2, row=row)

            elif qdr in [1, 4, 7]:
                nums_in_qdr_01 = self.get_nums_qdr(qdr - 1, row=row)
                nums_in_qdr_02 = self.get_nums_qdr(qdr + 1, row=row)
        
            elif qdr in [2, 5, 8]:
                nums_in_qdr_01 = self.get_nums_qdr(qdr - 1, row=row)
                nums_in_qdr_02 = self.get_nums_qdr(qdr - 2, row=row)

        nums_priority_qdrs = list(set(nums_in_qdr_01).intersection(nums_in_qdr_02))
        
        # REMOVE NUMEROS JA UTILIZADOS
        nums_priority_qdrs = self.remove_nums_used(nums_priority_qdrs, qdr, col, row)
        nums_in_qdr_01 = self.remove_nums_used(nums_in_qdr_01, qdr, col, row)
        nums_in_qdr_02 = self.remove_nums_used(nums_in_qdr_02, qdr, col, row)

        #############################################################
        # DA PRIORIDADE NOS NUMEROS DAS PROXIMAS COLUNAS
        if col % 3 == 0:
            nums_in_col_01 = self.get_nums_col(col + 1, row)
            nums_in_col_02 = self.get_nums_col(col + 2, row)
            
            if nums_in_col_01 or nums_in_col_02:
                nums_priority_cols = list(set(nums_in_col_01).intersection(nums_in_col_02))

        elif col in [1, 4, 7]:
            
            nums_priority_cols = self.get_nums_col(col + 1, row)

        elif col in [2, 5, 8]:
            
            nums_in_col_01 = self.get_nums_col(col - 1, row)
            nums_in_col_02 = self.get_nums_col(col - 2, row)
            
            if nums_in_col_01 or nums_in_col_02:
                nums_priority_cols = list(set(nums_in_col_01).intersection(nums_in_col_02))
        
        # REMOVE NUMEROS JA UTILIZADOS
        nums_priority_cols = self.remove_nums_used(nums_priority_cols, qdr, col, row)
        nums_in_col_01 = self.remove_nums_used(nums_in_col_01, qdr, col, row)
        nums_in_col_02 = self.remove_nums_used(nums_in_col_02, qdr, col, row)


        #############################################################
        # DA PRIORIDADE NOS NUMEROS DAS PROXIMAS LINHAS
        if row % 3 == 0:
            nums_in_row_01 = self.get_nums_row(col, row + 1)
            nums_in_row_02 = self.get_nums_row(col, row + 2)
            
            if nums_in_row_01 or nums_in_row_02:
                nums_priority_rows = list(set(nums_in_row_01).intersection(nums_in_row_02))

        elif row in [1, 4, 7]:
            
            nums_priority_rows = self.get_nums_row(col, row + 1)

        elif row in [2, 5, 8]:
            
            nums_in_row_01 = self.get_nums_row(col, row - 1)
            nums_in_row_02 = self.get_nums_row(col, row - 2)
            
            if nums_in_row_01 or nums_in_row_02:
                nums_priority_rows = list(set(nums_in_row_01).intersection(nums_in_row_02))
        
        # REMOVE NUMEROS JA UTILIZADOS
        nums_priority_rows = self.remove_nums_used(nums_priority_rows, qdr, col, row)

        # ANALISA O CENARIO
        return_nums_priority = []
        if list(set(nums_priority_qdrs).intersection(nums_priority_cols).intersection(nums_priority_rows)):
            print("00")
            return_nums_priority = list(set(nums_priority_qdrs).intersection(nums_priority_cols).intersection(nums_priority_rows))
        
        else:
            if nums_priority_cols:
                if list(set(nums_priority_cols).intersection(nums_in_qdr_02)):
                    print("01")
                    return_nums_priority = list(set(nums_priority_cols).intersection(nums_in_qdr_02))
                else:
                    print("02")
                    return_nums_priority = nums_priority_cols
            elif list(set(nums_in_qdr_01).intersection(nums_in_qdr_02)):
                print("03")
                return_nums_priority = list(set(nums_in_qdr_01).intersection(nums_in_qdr_02))
            elif list(set(nums_in_qdr_02).intersection(nums_priority_cols)):
                print("04")
                return_nums_priority = list(set(nums_in_qdr_02).intersection(nums_priority_cols))
            elif list(set(nums_in_qdr_01).intersection(nums_priority_cols)):
                print("05")
                return_nums_priority = list(set(nums_in_qdr_01).intersection(nums_priority_cols))
            elif nums_in_qdr_02:
                print("06")
                return_nums_priority = nums_in_qdr_02
        
        return return_nums_priority
    
    def remove_nums_used(self, list_search:list, qdr:int, col:int, row:int) -> list:
        
        list_return = []
        nums_in_col = self.get_nums_col(col, 9)
        nums_in_row = self.get_nums_row(9, row)
        nums_in_qdr = self.get_nums_qdr(qdr, 9)
        
        for item in list_search:
            if item not in nums_in_col and item not in nums_in_row and item not in nums_in_qdr:
                list_return.append(item)
        
        return list_return

    def get_nums_col(self, col:int, row:int) -> list:
        filter_col = lambda x: x['column'] == col and x['row'] != row
        get_text = lambda x: x['text']

        list_nums_in_col = list(filter(filter_col, self.grid))
        return list(map(get_text, list_nums_in_col))

    def get_nums_row(self, col:int, row:int) -> list:
        filter_row = lambda x: x['row'] == row and x['column'] != col
        get_text = lambda x: x['text']

        list_nums_in_row = list(filter(filter_row, self.grid))
        return list(map(get_text, list_nums_in_row))

    def get_nums_qdr(self, qdr:int, col:int=None, row:int=None) -> list:
        filter_qdr_col = lambda x: x['quadrante'] == qdr and x['column'] != col
        filter_qdr_row = lambda x: x['quadrante'] == qdr and x['row'] != row
        get_text = lambda x: x['text']
        
        if col is not None:
            list_nums_in_qdr = list(filter(filter_qdr_col, self.grid))
        else:
            list_nums_in_qdr = list(filter(filter_qdr_row, self.grid))

        return list(map(get_text, list_nums_in_qdr))
    
    def get_index_row_empty(self, col:int) -> int:
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        nums_find = []
        for item in self.grid:
            if item["column"] == col:
                nums_find.append(item["row"])
        result = list(set(nums) - set(nums_find))
        result = sorted(result)
        return result[0]
    
    def get_index_col_empty(self, row:int) -> int:
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        nums_find = []
        for item in self.grid:
            if item["row"] == row:
                nums_find.append(item["column"])
        result = list(set(nums) - set(nums_find))
        result = sorted(result)
        return result[0]

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
    
    global NUM_FALTANTES
    
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
            box.analyze(screen)

        pygame.display.flip()
        
        # ATUALIZA INFO
        update_info()

        # ATUALIZA DA TELA
        pygame.display.update()

        if NUM_FALTANTES == 0:
            break


GRID = Grid().initialize()

# PROPIEDADES SCREEN
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# MENU
menu = pygame_menu.Menu(SCREEN_HEIGHT, SCREEN_WIDTH, 'Bem Vindo(a)!', theme=pygame_menu.themes.THEME_GREEN)
menu.add_selector('Dificuldade :', DIFFICULTY_GAME_TEXT, onchange=set_difficulty)
menu.add_button('Jogar', start_the_game)
menu.add_button('Sair', pygame_menu.events.EXIT)
menu.mainloop(screen)
