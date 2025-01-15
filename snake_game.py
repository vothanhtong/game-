import pygame
import time
import random

# Khởi tạo pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 800, 600

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Tạo màn hình trò chơi
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Tốc độ FPS
clock = pygame.time.Clock()
SNAKE_BLOCK = 20  # Kích thước của mỗi khối rắn
SNAKE_SPEED = 15
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value = score_font.render(f"Your Score: {score}", True, WHITE)
    screen.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.circle(screen, GREEN, (x[0] + snake_block // 2, x[1] + snake_block // 2), snake_block // 2)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def gameLoop():
    game_over = False
    game_close = False

    # Khởi tạo vị trí của rắn
    x1, y1 = WIDTH / 2, HEIGHT / 2
    x1_change, y1_change = 0, 0

    # Danh sách để lưu vị trí của rắn
    snake_list = []
    length_of_snake = 1

    # Vị trí thức ăn
    foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change, y1_change = -SNAKE_BLOCK, 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change, y1_change = SNAKE_BLOCK, 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    x1_change, y1_change = 0, -SNAKE_BLOCK
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    x1_change, y1_change = 0, SNAKE_BLOCK

        # Kiểm tra nếu rắn vượt quá giới hạn
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLUE)

        # Vẽ thức ăn
        pygame.draw.circle(screen, RED, (int(foodx) + SNAKE_BLOCK // 2, int(foody) + SNAKE_BLOCK // 2), SNAKE_BLOCK // 2)

        # Cập nhật vị trí của rắn
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(SNAKE_BLOCK, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # Kiểm tra nếu rắn ăn thức ăn
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            length_of_snake += 1

            # Tăng tốc độ trò chơi khi ăn thức ăn
            if length_of_snake % 5 == 0:  # Tăng tốc độ mỗi 5 lần ăn
                global SNAKE_SPEED
                SNAKE_SPEED += 2

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

if __name__ == "__main__":
    gameLoop()
