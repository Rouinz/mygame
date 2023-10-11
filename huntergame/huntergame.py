import pygame
import random as r
import time

pygame.init()
#def
def game_over():
    global game_started, high_score, score, old_score, move_x, move_y, player_pos, food_x, food_y, food_pos, up, down, left ,right, chosed, losed, trap_spawn_rate, traps
    losed = True
    game_started = False
    if high_score <= score:
        high_score = score
    old_score = score
    score = 0
    move_x = 300
    move_y = 300
    player_pos = (300,300,40,40)
    food_x = r.randint(30,670)
    food_y = r.randint(30,470)
    food_pos = (food_x,food_y,20,20)
    up = True
    down = False
    left = False
    right = False
    chosed = False
    trap_spawn_rate = 0
    traps = True
def crash(player_pos):
    player_left = player_pos[0]
    player_top = player_pos[1]
    player_right = player_pos[0] + player_pos[2]
    player_bottom = player_pos[1] + player_pos[3]

    if player_top <= 0 or player_bottom >= 500 or player_left <= 0 or player_right >= 700:
        return True
    return False
def point(player,food):
    global score
    global eaten
    global food_x
    global food_y
    global food_pos
    global trap_spawn_rate
    if player.colliderect(food) and eaten == False:
        score += 1
        eaten = True
        food_x = r.randint(30,670)
        food_y = r.randint(30,470)
        food_pos = (food_x,food_y,20,20)
        trap_spawn_rate += r.randint(10,20)
    else:
        eaten = False
    return score
#class
class Trap:
    def __init__(self,x,y):
        self.x = 0
        self.y = 0
        self.width = 20
        self.height = 20
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    def draw(self, window):
        pygame.draw.rect(window, black, self.hitbox)
    def check_col(self,other_rect):
        return self.hitbox.colliderect(other_rect)
width = 700
height = 500
window = pygame.display.set_mode((700,500))
pygame.display.set_caption("Hunt or Get Hunted")
#variables
#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
bg = (42,189,44)
#fps
fps = 60
clock = pygame.time.Clock()
#movement
move_x = 300
move_y = 300
player_pos = (move_x,move_y,40,40)
velocity = 3
is_pressed = False
up = True
down = False
left = False
right = False
eaten = False
#food
food_x = r.randint(30,670)
food_y = r.randint(30,470)
food_pos = (food_x,food_y,20,20)
drawed = False
#trap
trap = None
traps = True
trap_x = r.randint(20,680)
trap_y = r.randint(20,480)
trap_display_time = None
trap_spawn_rate = 0
is_spawned = False
#score
game_started = False
losed = False
score = 0
old_score = 0
chosed = False
high_score = 0

font = pygame.font.Font('04B_19.TTF',35)
#main
running = True
while running:
    clock.tick(fps)
    window.fill(bg)
    #game event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_started = True
                losed = False
            if event.key == pygame.K_1 and game_started and not(losed):
                velocity = 4
                chosed = True
            elif event.key == pygame.K_2 and game_started and not(losed):
                velocity = 7
                chosed = True
            elif event.key == pygame.K_3 and game_started and not(losed):
                velocity = 9
                chosed = True
            if game_started and not(losed) and event.key == pygame.K_s:
                up = False
                down = True
                left = False
                right = False
            elif game_started and not(losed) and event.key == pygame.K_w:
                up = True
                down = False
                left = False
                right = False
            elif game_started and not(losed) and event.key == pygame.K_a:
                up = False
                down = False
                left = True
                right = False
            elif game_started and not(losed) and event.key == pygame.K_d:
                up = False
                down = False
                left = False
                right = True
    #starting
    if not(game_started) and not(losed):
        title1 = font.render("Hunt or Get Hunted",True,white,black)
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
        #mode choosing
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
        elif chosed:
            #playing
            if not(crash(player_pos)) and not(losed):
                if traps:
                    trap_spawn_rate = r.randint(1,50)
                    traps = False
                if trap_spawn_rate >= 100:
                    trap_x = r.randint(30,670)
                    trap_y = r.randint(30,470)
                    while (trap_x == move_x + 200 and trap_y == move_y + 200 and trap_x == move_x + 240 and trap_y == move_y + 240 and trap_x == food_x and trap_y == food_y):
                        trap_x = r.randint(30,670)
                        trap_y = r.randint(30,470)
                    if trap is None:
                        trap = Trap(trap_x,trap_y)
                    elif trap_display_time is None:
                        trap.x = trap_x
                        trap.y = trap_y
                        trap.hitbox.x = trap_x
                        trap.hitbox.y = trap_y
                        trap_display_time = time.time()
                    elif time.time() - trap_display_time >= 10:
                        trap_display_time = None
                        traps = True
                    if trap is not None:
                        trap.draw(window)
                        if trap.check_col(pygame.Rect(player_pos)):
                            game_over()
                
                player_pos = (move_x,move_y,40,40)
                pygame.draw.rect(window, black, player_pos)
                if eaten:
                    pygame.draw.rect(window,red, food_pos)
                    drawed = True
                if not(drawed):
                    pygame.draw.rect(window,red, food_pos)
                pygame.draw.rect(window, black, player_pos)
                text = font.render("Score: "+str(point(pygame.draw.rect(window, black, player_pos),pygame.draw.rect(window,red, food_pos))), True, white,black)
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
                point(pygame.draw.rect(window, black, player_pos),pygame.draw.rect(window,red, food_pos))
            elif (crash(pygame.draw.rect(window, black, player_pos)) and game_started) or (losed): 
                game_over()

    pygame.display.update()
    pygame.display.flip()
pygame.quit()