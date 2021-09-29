import pygame
import sys

# Основные переменные:
BACK_COLOR = (74, 117, 44)
FRAME_COLOR = (87, 138, 52)
FIRST_COLOR_FIELD = (170, 215, 81)
SECOND_COLOR_FIELD = (162, 209, 73)
SIZE_BLOCK = 35
COUNT_BLOCKS = 19

pygame.init()
# Создание и настройка игрового окна:
size_screen = [700, 770]
screen = pygame.display.set_mode(size_screen)
pygame.display.set_caption("Игра \"Змейка\"")

# Работу с игровым окном:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Задний фон и основные элементы:
    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, BACK_COLOR, (0, 0, 700, 75))

    # Создание игрового поля: 
    change_color = True
    for i in range(COUNT_BLOCKS):
        for j in range(COUNT_BLOCKS):
            if change_color is True:
                pygame.draw.rect(screen, FIRST_COLOR_FIELD, (18 + i * SIZE_BLOCK, 90 + j * SIZE_BLOCK, SIZE_BLOCK, SIZE_BLOCK))
                change_color = False
            else:
                pygame.draw.rect(screen, SECOND_COLOR_FIELD, (18 + i * SIZE_BLOCK, 90 + j * SIZE_BLOCK, SIZE_BLOCK, SIZE_BLOCK))
                change_color = True

    pygame.display.flip()
