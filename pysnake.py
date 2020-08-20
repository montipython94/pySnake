import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 192)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (75, 139, 190)

colorOfSnake = (white, yellow, red, blue)

dis_width = 300
dis_height = 200
dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 5
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 11)
score_font = pygame.font.SysFont("comicsansms", 15)

#Score
def score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

#Snake
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, random.choice(colorOfSnake), [x[0], x[1], snake_block, snake_block])

#Message
def message(msg, color):
    msg = font_style.render(msg, True, color)
    dis.blit(msg, [dis_width / 6, dis_height / 3])

#Game Loop
def game_loop():
    game_over = False
    game_close = False

    x_wid = dis_width / 2
    y_hei = dis_height / 2
    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    applex = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    appley = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    left = False
    right = False
    up = False
    down = False

    while not game_over:

        while game_close:
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and right != True:
                    x_change = -snake_block
                    y_change = 0
                    left = True
                    right = False
                    up = False
                    down = False
                elif event.key == pygame.K_d and left != True:
                    x_change = snake_block
                    y_change = 0
                    right = True
                    left = False
                    up = False
                    down = False
                elif event.key == pygame.K_w and down != True:
                    y_change = -snake_block
                    x_change = 0
                    right = False
                    left = False
                    up = True
                    down = False
                elif event.key == pygame.K_s and up != True:
                    y_change = snake_block
                    x_change = 0
                    right = False
                    left = False
                    up = False
                    down = True

        if x_wid >= dis_width or x_wid < 0 or y_hei >= dis_height or y_hei < 0:
            game_close = True
        x_wid += x_change
        y_hei += y_change
        dis.fill(black)
        pygame.draw.ellipse(dis, green, [applex, appley, snake_block, snake_block])
        snake_head = [x_wid, y_hei]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_block, snake_list)
        score(length_of_snake - 1)

        pygame.display.update()

        if x_wid == applex and y_hei == appley:
            applex = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            appley = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()
