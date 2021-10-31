import pygame
import os
pygame.font.init()




WIDTH = 900
HEIGHT = 500
spaceship_width  = 55
spaceship_height= 40
BORDER = pygame.Rect(WIDTH/2 - 5 , 0 , 10 , HEIGHT)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
MAX_BULLET = 5
YELLOW_HIT = pygame.USEREVENT+ 1
RED_HIT = pygame.USEREVENT+ 2

health_font = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('ASSETS','SPACE_BG.jpg')) , (WIDTH,HEIGHT))

VEL = 5
bullets_vel = 7 

WIN = pygame.display.set_mode((WIDTH,HEIGHT))#This is a statement which tells the python about the width and height of the window also tells about to create a window
pygame.display.set_caption("SpaceZO")
white = (255,240,200)
FPS = 60 #ITS THE FRAME PER SECOND
SPACESHIP_1 = pygame.image.load(os.path.join('ASSETS','spaceship_yellow.png'))#this variable  defined the images NOW WE HAVE RESIZE THE IMAGE SO
SPACESHIP_YELLOW = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_1,(spaceship_width,spaceship_height)),90)


SPACESHIP_2 = pygame.image.load(os.path.join('ASSETS','spaceship_red.png'))
SPACESHIP_RED = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_2,(spaceship_width,spaceship_height)),270)


#here i had created an function that handles all the drawing  function on the game
def draw_win(red,yellow,red_bullets,yellow_bullet,RED_HEALTH,YELLOW_HEALTH):
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN, BLACK , BORDER)

    red_health_text = health_font.render('HEALT: ' + str(RED_HEALTH) , 1 , white)
    yellow_health_text = health_font.render('HEALT: ' + str(YELLOW_HEALTH) , 1 , white)
    WIN.blit(red_health_text,(WIDTH - red_health_text.get_width()-10 , 10))
    WIN.blit(yellow_health_text,(10,10))


    WIN.blit(SPACESHIP_YELLOW,(yellow.x,yellow.y))#HERE I CALLED THE IMAGE AND GAVE ITS DIMENSIONS
    WIN.blit(SPACESHIP_RED,(red.x,red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED , bullet)
    
    for bullet in yellow_bullet:
        pygame.draw.rect(WIN, YELLOW , bullet)


    pygame.display.update()

def handle_bullets(yellow_bullet,red_bullets,red,yellow):


    for bullet in yellow_bullet:
        bullet.x += bullets_vel

        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))

            yellow_bullet.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullet.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= bullets_vel

        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))

            red_bullets.remove(bullet)
        elif bullet.x < 0 :
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text , 1 , white)




def main():#now this is the main function under with the whole games event will run

    red = pygame.Rect(700,300,spaceship_height,spaceship_width)#this creates an rectangle for the spaceship to move
    yellow = pygame.Rect(100,300,spaceship_height,spaceship_width)


    red_bullets = []
    yellow_bullet = []
    RED_HEALTH = 10
    YELLOW_HEALTH = 10


    clock = pygame.time.Clock()
    run = True # if the run variable is true then
    while run:# a while loop will run
        clock.tick(FPS)#THIS TELLS THE NO. OF TIMES THE WHILE LOOP WORKS PER SECOND
        for event in pygame.event.get():# here if in pygame  type event occurs
            if event.type == pygame.QUIT:
                run = False #then run becomes false

        


            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_LCTRL and len(yellow_bullet)<MAX_BULLET:
                    bullet = pygame.Rect(yellow.x + yellow.width , yellow.y + yellow.height//2 - 2 , 10 , 5)
                    yellow_bullet.append(bullet)
                
                if event.key == pygame.K_RCTRL and len(red_bullets)<MAX_BULLET:
                    bullet = pygame.Rect(red.x  ,red.y + red.height//2 - 2 , 10 , 5)
                    red_bullets.append(bullet)

            print(yellow_bullet,red_bullets)


            
            if event.type == RED_HIT:
                RED_HEALTH -= 1

            if event.type == YELLOW_HIT:
                YELLOW_HEALTH -= 1
            
            
            
            





            


        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and yellow.x - VEL > 0 :#for left movement
            yellow.x -= VEL
        if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x  :
            yellow.x += VEL
        if keys_pressed[pygame.K_w] and yellow.y - VEL > 0 :
            yellow.y -= VEL
        if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT :
            yellow.y += VEL
        
        if keys_pressed[pygame.K_UP] and red.y - VEL > 0 :
            red.y -= VEL
        if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT :
            red.y += VEL
        if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:
            red.x += VEL
        if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:
            red.x -= VEL



        handle_bullets(yellow_bullet,red_bullets,red,yellow)

        draw_win(red,yellow,red_bullets,yellow_bullet,RED_HEALTH,YELLOW_HEALTH)  

            
        

    pygame.quit() #thus  pygame quits automatically

if __name__ == "__main__":#this function tells pyhton to run this code in this file only
    main()