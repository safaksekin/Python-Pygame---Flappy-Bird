import pygame
import random
import sys


pygame.init()
clock = pygame.time.Clock()

gravity = 0.25

window = pygame.display.set_mode((480,735))
background=pygame.image.load("background.jpg")
background=pygame.transform.scale(background, (480,735))

bird=pygame.image.load("bird.png")
bird=pygame.transform.scale(bird, (75,60))
bird_y_change=0
bird_rect=bird.get_rect(center=(50,250))

floor=pygame.image.load("floor.png").convert_alpha()
floor=pygame.transform.scale(floor, (480, 200))
floor_x=0

space=pygame.image.load("space.png").convert_alpha()
space=pygame.transform.scale(space, (180, 75))
space_rect=space.get_rect(center = (238,300))

game_over=pygame.image.load("game_over.png").convert_alpha()
game_over=pygame.transform.scale(game_over, (480, 200))
game_over_rect=game_over.get_rect(center= (236,150))

high_score=pygame.image.load("HIGH-SCORE.png").convert_alpha()
high_score=pygame.transform.scale(high_score, (200, 100))
high_score_rect=high_score.get_rect(center= (236,400))


block_gen=50
block_yuk=random.randint(100,450)
block_colour=(112, 231, 140)
block_x_change=-4
block_x=500

score_image=pygame.image.load("score.png").convert_alpha()
score_image=pygame.transform.scale(score_image, (70,30))

score_image2=pygame.image.load("score.png").convert_alpha()
score_image2=pygame.transform.scale(score_image2, (140,60))

gold=0
score=0
font=pygame.font.Font("freesansbold.ttf", 30)
font2=pygame.font.SysFont("candara", 20)



def score_display(score):
    text=font.render(f"{score}", True, (0,0,0))
    window.blit(text, (75,2))


def floor_loop(floor_x):
    window.blit(floor, (floor_x, 590))
    window.blit(floor, (floor_x + 480, 590))

def collision_detect():
    if bird_rect.top <= -100 or bird_rect.bottom >= 590:
        return False
    return True

def create_block(block_yuk):
    pygame.draw.rect(window, block_colour, (block_x,0,block_gen,block_yuk))
    bottom_block_yuk=590-block_yuk-150
    pygame.draw.rect(window, block_colour, (block_x, block_yuk+150, block_gen, bottom_block_yuk))

def impact(block_x, block_yuk, bird_top_y, bird_rect_centery, bottom_block_yuk):
    if block_x >= 2 and block_x <= 77:
        if bird_top_y+12 <= block_yuk or bird_rect_centery+20 >= bottom_block_yuk:
            return True
    return False
score_list=[0]
def gameover():
    maximum = max(score_list)
    window.blit(game_over, game_over_rect)
    window.blit(high_score, high_score_rect)
    text2=font.render(f"{maximum}",True, (0,0,0))
    window.blit(text2, (350,387))
    if score > maximum:
        text3 = font.render(f"NEW HIGH SCORE!", True, (200,35,35))
        window.blit(text3, (400,300))

def start():
    label = font.render(f"PRESS SPACE BAR TO START", True, (200, 35, 35))
    label2=font2.render("made by Safak Sekin", True, (128, 0, 255))
    window.blit(label, (20, 300))
    window.blit(label2, (300,700))
    pygame.display.update()

go = False
st = True
waiting = True


while True:
    window.blit(background, (0, 0))
    impacting = impact(block_x, block_yuk, bird_rect.top, bird_rect.centery, block_yuk + 150)
    regularly = collision_detect()
    while waiting:
        if st:
            start()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False
        if go:
            maximum = max(score_list)
            window.blit(game_over, game_over_rect)
            window.blit(high_score, high_score_rect)
            text2 = font.render(f"{maximum}", True, (0, 0, 0))
            window.blit(text2, (350, 387))
            if score > maximum:
                text3 = font.render(f"NEW HIGH SCORE!", True, (200, 35, 35))
                window.blit(text3, (400, 300))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and regularly:
                bird_y_change = 0
                bird_y_change -= 6
            if event.key == pygame.K_SPACE and regularly == False:
                bird_rect.center = (50, 250)
                bird_y_change = 0
                regularly = True

    if regularly == False:
        score2 = score
        score_list.append(score)
        window.blit(score_image2, (165, 250))
        font1 = pygame.font.Font("freesansbold.ttf", 40)
        text = font1.render(f"{score2}", True, (0, 0, 0))
        window.blit(text, (320, 263))
        gameover()
        score = 0
    else:
        bird_y_change += gravity
        bird_rect.centery += bird_y_change
        window.blit(bird, bird_rect)

        block_x += block_x_change
        if block_x <= -50:
            block_x = 500
            block_yuk = random.randint(200, 400)
            score += 1
        create_block(block_yuk)


        

    window.blit(score_image, (0, 0))
    score_display(score)

    if impacting:
        pygame.quit()
        sys.exit()

    floor_x -= 2
    floor_loop(floor_x)
    if floor_x <= -480:
        floor_x = 0

    clock.tick(60)
    pygame.display.update()









