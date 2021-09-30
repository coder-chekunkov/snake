import random
import pygame
import sys


# Класс получения координат змейки:
class snakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Проверка выхода за границы:
    def is_inside(self):
        return 0 <= self.x < COUNT_BLOCKS and 0 <= self.y < COUNT_BLOCKS

    # Проверка "укуса" змейки себя:
    def is_snake(self):
        for i in range(0, len(SNAKE_BLOCK) - 1):
            if SNAKE_BLOCK[-1].x == SNAKE_BLOCK[i].x and SNAKE_BLOCK[-1].y == SNAKE_BLOCK[i].y:
                print("GAME OVER")
                makeStatistic()
                pygame.quit()
                sys.exit()

    def __eq__(self, other):
        return isinstance(other, snakeBlock) and self.x == other.x and self.y == other.y


pygame.font.init()
# Основные переменные (цвета, размер одной ячейки,
# количество полей и т.д.):
WHITE = (255, 255, 255)
APPLE_COLOR = (224, 0, 0)
BACK_COLOR = (74, 117, 44)
FRAME_COLOR = (87, 138, 52)
FIRST_COLOR_FIELD = (170, 215, 81)
SECOND_COLOR_FIELD = (162, 209, 73)
SNAKE_COLOR = (80, 118, 249)
SNAKE_HEAD_COLOR = (39, 66, 204)
SIZE_BLOCK = 35
COUNT_BLOCKS = 19
SNAKE_BLOCK = [snakeBlock(8, 9), snakeBlock(9, 9), snakeBlock(10, 9)]
POINTS = 0
font = pygame.font.SysFont('comicsansms', 33)
d_row = 0
d_col = 1


# Создание игрового поля:
def drawField(COLOR, raw, column):
    pygame.draw.rect(screen, COLOR, (18 + raw * SIZE_BLOCK, 90 + column * SIZE_BLOCK, SIZE_BLOCK, SIZE_BLOCK))


def drawApple(PIC, raw, column):
    screen.blit(PIC, (18 + raw * SIZE_BLOCK, 90 + column * SIZE_BLOCK, SIZE_BLOCK, SIZE_BLOCK))


# Генерация координат яблока:
def getApple():
    x = random.randint(0, COUNT_BLOCKS - 1)
    y = random.randint(0, COUNT_BLOCKS - 1)
    empty_block = snakeBlock(x, y)
    while empty_block in SNAKE_BLOCK:
        empty_block.x = random.randint(0, COUNT_BLOCKS - 1)
        empty_block.y = random.randint(0, COUNT_BLOCKS - 1)
    return empty_block


def makeStatistic():
    if BEST_SCORE < POINTS:
        my_file_write = open("statistic_file.txt", "w+")
        my_file_write.write(str(POINTS))
        my_file_write.close()


pygame.init()
# Создание и настройка игрового окна:
size_screen = [700, 770]
screen = pygame.display.set_mode(size_screen)
# Дополнительные перемнные:
icon = pygame.image.load("pic/icon.png")
apple_top_png = pygame.image.load("pic/apple_top.png")
apple_game_png = pygame.image.load("pic/apple_game.png")
highest_level = pygame.image.load("pic/highest_level.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Игра \"Змейка\"")
timer = pygame.time.Clock()
apple = getApple()
my_file = open("statistic_file.txt")
BEST_SCORE = int(my_file.read())
my_file.close()

# Работа с игровым окном:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_w or event.key == pygame.K_UP) and d_col != 0:
                d_row = -1
                d_col = 0
            elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and d_col != 0:
                d_row = 1
                d_col = 0
            elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and d_row != 0:
                d_row = 0
                d_col = -1
            elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and d_row != 0:
                d_row = 0
                d_col = 1

    # Задний фон и основные элементы:
    screen.fill(FRAME_COLOR)

    text_points = font.render(str(POINTS), True, WHITE)
    text_hight_score = font.render(str(BEST_SCORE), True, WHITE)
    pygame.draw.rect(screen, BACK_COLOR, (0, 0, 700, 75))
    screen.blit(apple_top_png, (25, 10))
    screen.blit(text_hight_score, (210, 18))
    screen.blit(text_points, (80, 18))
    screen.blit(highest_level, (150, 10))

    # Отросиовка поля:
    for i in range(COUNT_BLOCKS):
        for j in range(COUNT_BLOCKS):
            if (i + j) % 2 == 0:
                COLOR = FIRST_COLOR_FIELD
            else:
                COLOR = SECOND_COLOR_FIELD
            drawField(COLOR, i, j)

    # Проверка выхода за границы:
    snake_head = SNAKE_BLOCK[-1]
    if not snakeBlock.is_inside(snake_head):
        print("GAME OVER")
        makeStatistic()
        pygame.quit()
        sys.exit()

    # Проверка "укуса" змейки самой себя:
    snakeBlock.is_snake(SNAKE_BLOCK)

    # Генерация и отрисовка яблока:
    drawApple(apple_game_png, apple.x, apple.y)
    # Отрисовка змейки:
    for block in SNAKE_BLOCK:
        if block == SNAKE_BLOCK[-1]:
            drawField(SNAKE_HEAD_COLOR, block.x, block.y)
        else:
            drawField(SNAKE_COLOR, block.x, block.y)

    # Яблоко съедено, длина змейки увеличилась, количество очков увеличлось:
    if apple == snake_head:
        POINTS += 1
        SNAKE_BLOCK.append(apple)
        apple = getApple()

    # Движение змейки:
    new_snake_head = snakeBlock(snake_head.x + d_col, snake_head.y + d_row)
    SNAKE_BLOCK.append(new_snake_head)
    SNAKE_BLOCK.pop(0)

    pygame.display.flip()
    # Скорость движения:
    timer.tick(5)
