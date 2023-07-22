import pygame
import random as r
pygame.init()
#def
def crash(player):
    if player.top <= 0 or player.bottom >= 500 or player.left <= 0 or player.right >= 700:
        return True
    return False
def point(player,food):
    global score
    global eaten
    global food_x
    global food_y
    if player.colliderect(food) and eaten == False:
        score += 1
        eaten = True
        food_x = r.randint(0,550)
        food_y = r.randint(0,350)
    else:
        eaten = False
    return score
window = pygame.display.set_mode((700,500))
pygame.display.set_caption("Hunter Game")
#variables
white = (255,255,255)
black = (0,0,0)
bg = (42,189,44)
fps = 60
clock = pygame.time.Clock()
move_x = 300
move_y = 300
velocity = 3
is_pressed = False
up = True
down = False
left = False
right = False
eaten = False
food_x = r.randint(0,700)
food_y = r.randint(0,500)
drawed = False
game_started = False
losed = False
score = 0
old_score = 0
chosed = False
high_score = 0

font = pygame.font.Font('04B_19.TTF',28)
#main
running = True
while running:
    clock.tick(fps)
    window.fill(bg)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not(crash(pygame.draw.rect(window, (0,0,0), (move_x,move_y,40,40)))):
            if event.key == pygame.K_SPACE:
                game_started = True
                losed = False
            if event.key == pygame.K_1 and game_started and not(losed):
                velocity = 3
                chosed = True
            elif event.key == pygame.K_2 and game_started and not(losed):
                velocity = 5
                chosed = True
            elif event.key == pygame.K_3 and game_started and not(losed):
                velocity = 7
                chosed = True
            if event.key == pygame.K_s and game_started and not(losed):
                up = False
                down = True
                left = False
                right = False
            elif event.key == pygame.K_w and game_started and not(losed):
                up = True
                down = False
                left = False
                right = False
            elif event.key == pygame.K_a and game_started and not(losed):
                up = False
                down = False
                left = True
                right = False
            elif event.key == pygame.K_d and game_started and not(losed):
                up = False
                down = False
                left = False
                right = True
    if not(game_started) and not(losed):
        title1 = font.render("Hunter Game",True,white,black)
        title2 = font.render("Press Spacebar to play", True,black)
        title1Rect = title1.get_rect()
        title2Rect = title2.get_rect()
        title1Rect.center = (700 // 2, 500 // 2)
        title2Rect.center = (700 // 2, 300)
        window.blit(title1, title1Rect)
        window.blit(title2, title2Rect)
    elif losed:
        over = font.render("Game Over!", True, white,black)
        result = font.render("Your Score: "+str(old_score),True,white,black)
        high_sc = font.render("High Score: "+str(high_score),True,white,black)
        overRect = over.get_rect()
        resultRect = result.get_rect()
        high_scRect = high_sc.get_rect()
        overRect.center = (700 // 2, 200)
        resultRect.center = (700 // 2, 300)
        high_scRect.center = (700 // 2, 500 // 2)
        window.blit(over, overRect)
        window.blit(result, resultRect)
        window.blit(high_sc, high_scRect)
    elif game_started and not(losed):
        if not(chosed):
            normal = font.render("Normal Mode - Press 2", True, white,black)
            normalRect = normal.get_rect()
            normalRect.center = (700 // 2, 500 // 2)
            window.blit(normal, normalRect)
            hard = font.render("Hard Mode - Press 3", True, white,black)
            hardRect = hard.get_rect()
            hardRect.center = (700 // 2, 300)
            window.blit(hard, hardRect)
            easy = font.render("Easy Mode - Press 1", True, white,black)
            easyRect = easy.get_rect()
            easyRect.center = (700 // 2, 200)
            window.blit(easy, easyRect)
        if chosed:
            if not(crash(pygame.draw.rect(window, (0,0,0), (move_x,move_y,40,40)))):
                if eaten:
                    pygame.draw.rect(window,(255,0,0), (food_x,food_y,20,20))
                    drawed = True
                if not(drawed):
                    pygame.draw.rect(window,(255,0,0), (food_x,food_y,20,20))
                pygame.draw.rect(window, (0,0,0), (move_x,move_y,40,40))
                text = font.render("Score: "+str(point(pygame.draw.rect(window, (0,0,0), (move_x,move_y,40,40)),pygame.draw.rect(window,(255,0,0), (food_x,food_y,20,20)))), True, white,black)
                textRect = text.get_rect()
                textRect.topleft = (0,0)
                window.blit(text, textRect)
                if up:
                    move_y -= velocity
                elif down: 
                    move_y += velocity
                elif right:
                    move_x += velocity
                elif left:
                    move_x -= velocity
                point(pygame.draw.rect(window, (0,0,0), (move_x,move_y,40,40)),pygame.draw.rect(window,(255,0,0), (food_x,food_y,20,20)))
            elif crash(pygame.draw.rect(window, (0,0,0), (move_x,move_y,40,40))) and game_started: 
                losed = True
                game_started = False
                if high_score <= score:
                    high_score = score
                old_score = score
                score = 0
                move_x = 300
                move_y = 300
                up = True
                down = False
                left = False
                right = False
                chosed = False

    pygame.display.update()
    pygame.display.flip()
pygame.quit()