import pygame
import sys


# Класс получения координат змейки:
class snakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < COUNT_BLOCKS and 0 <= self.y < COUNT_BLOCKS


# Основные переменные (цвета, размер одной ячейки,
# количество полей и т.д.):
BACK_COLOR = (74, 117, 44)
FRAME_COLOR = (87, 138, 52)
FIRST_COLOR_FIELD = (170, 215, 81)
SECOND_COLOR_FIELD = (162, 209, 73)
SNAKE_COLOR = (80, 118, 249)
SNAKE_HEAD_COLOR = (39, 66, 204)
SIZE_BLOCK = 35
COUNT_BLOCKS = 19
SNAKE_BLOCK = [snakeBlock(8, 9), snakeBlock(9, 9), snakeBlock(10, 9)]

d_row = 0
d_col = 1


# Создание игрового поля:
def drawField(COLOR, raw, column):
    pygame.draw.rect(screen, COLOR, (18 + raw * SIZE_BLOCK, 90 + column * SIZE_BLOCK, SIZE_BLOCK, SIZE_BLOCK))


pygame.init()
# Создание и настройка игрового окна:
size_screen = [700, 770]
screen = pygame.display.set_mode(size_screen)
icon = pygame.image.load("pic/icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Игра \"Змейка\"")
timer = pygame.time.Clock()

# Работу с игровым окном:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col != 0:
                d_row = -1
                d_col = 0
            elif event.key == pygame.K_DOWN and d_col != 0:
                d_row = 1
                d_col = 0
            elif event.key == pygame.K_LEFT and d_row != 0:
                d_row = 0
                d_col = -1
            elif event.key == pygame.K_RIGHT and d_row != 0:
                d_row = 0
                d_col = 1

    # Задний фон и основные элементы:
    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, BACK_COLOR, (0, 0, 700, 75))

    # Отросиовка поля:
    for i in range(COUNT_BLOCKS):
        for j in range(COUNT_BLOCKS):
            if (i + j) % 2 == 0:
                COLOR = FIRST_COLOR_FIELD
            else:
                COLOR = SECOND_COLOR_FIELD
            drawField(COLOR, i, j)

    # Отрисовка змейки:
    snake_head = SNAKE_BLOCK[-1]
    if not snakeBlock.is_inside(snake_head):
        print("GAME OVER")
        pygame.quit()
        sys.exit()
    for block in SNAKE_BLOCK:
        if block == SNAKE_BLOCK[-1]:
            drawField(SNAKE_HEAD_COLOR, block.x, block.y)
        else:
            drawField(SNAKE_COLOR, block.x, block.y)

    # Движение змейки:
    new_snake_head = snakeBlock(snake_head.x + d_col, snake_head.y + d_row)
    SNAKE_BLOCK.append(new_snake_head)
    SNAKE_BLOCK.pop(0)

    pygame.display.flip()
    timer.tick(2)
