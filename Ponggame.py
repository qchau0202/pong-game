from sys import exit

import pygame, random

pygame.init()
pygame.display.set_caption("Pong Game")
SIZE = (600, 600)
canvas = pygame.display.set_mode(SIZE)
BG_COLOR = (96, 96, 96)
clock = pygame.time.Clock()

# get images
paddle_image = pygame.image.load("/Users/Chou/Desktop/CS-01/NewGame/assets/paddle.png")
ball_image = pygame.image.load("/Users/Chou/Desktop/CS-01/NewGame/assets/ball.png")

# paddle 1
x1 = 0
y1 = 250
# paddle 2
x2 = 570
y2 = 250
# ball
ball_x = 285
ball_y = 300
# keys
w_pressed = False
s_pressed = False
up_pressed = False
down_pressed = False
# ball speed
ball_x_v = 2 
ball_y_v = 4
# score 
p1 = 0
p2 = 0
line = '|'
game_font = pygame.font.Font(None, 20)
# game loop
while True:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            exit()

        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                w_pressed = True
            elif e.key == pygame.K_s:
                s_pressed = True
            elif e.key == pygame.K_UP:
                up_pressed = True
            elif e.key == pygame.K_DOWN:
                down_pressed = True

        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                w_pressed = False
            elif e.key == pygame.K_s:
                s_pressed = False
            elif e.key == pygame.K_DOWN:
                down_pressed = False
            elif e.key == pygame.K_UP:
                up_pressed = False
    # update ball's velocity
    if y1 <= ball_y <= (y1 + 120) and ball_x <= (x1 + 30):
        ball_x_v = -ball_x_v
    if y2 <= ball_y <= (y2 + 120) and ball_x >= (x2 - 20):
        ball_x_v = - ball_x_v
    # scoring system
    if ball_x <= 0:
        ball_x = 270
        ball_y = 270
        ball_x_v *= random.choice((1,-1))
        ball_y_v *= random.choice((1,-1))
        p1 += 1
    if ball_x >= 580:
        ball_x = 270
        ball_y = 270
        ball_x_v *= random.choice((1,-1))
        ball_y_v *= random.choice((1,-1))
        p2 += 1
    # scoring system
    if ball_y <= 0 or ball_y >= 580:
        ball_y_v = -ball_y_v
    # move ball
    ball_x += ball_x_v
    ball_y += ball_y_v
    # paddle stops when hits walls
    if y1 <= 0:
        w_pressed = False
    if y2 <= 0:
        up_pressed = False
    if y1 >= 480:
        s_pressed = False
    if y2 >= 480:
        down_pressed = False
    # move paddle
    if w_pressed:
        y1 -= 5
    elif s_pressed:
        y1 += 5
    elif up_pressed:
        y2 -= 5
    elif down_pressed:
        y2 += 5
    
    # draw
    canvas.fill(BG_COLOR)
    canvas.blit(paddle_image, (x1, y1))
    canvas.blit(paddle_image, (x2, y2))
    canvas.blit(ball_image, (ball_x, ball_y))
    # display
    p1_text = game_font.render(f'{p1}', False, (255, 255, 255) )
    p2_text = game_font.render(f'{p2}', False, (255, 255, 255) )
    createLine = game_font.render(f'{line}', False, (255,255,255))
    canvas.blit(p1_text,(310,270))
    canvas.blit(createLine,(297,268))
    canvas.blit(p2_text,(280,270))
    clock.tick(60)
    pygame.display.flip()