import pygame
import random
import time


pygame.init()
clock=pygame.time.Clock()
##############################################################################################################################
#make screens and surfaces here
#screen frame 
screen=pygame.display.set_mode((800,500))
pygame.display.set_caption("space invaders")
#icon
icon=pygame.image.load("/home/siddharth/programming/projects/space_invaders/icon.png")
pygame.display.set_icon(icon)
#font
main_font = pygame.font.SysFont("comicsans",30) 

####################################################################################################################################
menu_button=pygame.image.load("/home/siddharth/programming/projects/space_invaders/menu.png")
menu_button_rect=menu_button.get_rect(center=(450,250))

pause_button=pygame.image.load("/home/siddharth/programming/projects/space_invaders/pause-button.png")
pause_button_rect=pause_button.get_rect(center=(20,58))

continue_button=pygame.image.load("/home/siddharth/programming/projects/space_invaders/continue.png")
continue_button_rect=continue_button.get_rect(center=(350,250))

pause_screen=pygame.Rect((0,0),(800,500))
pause_screen_color=(173, 216, 230)

shop_health=pygame.image.load("/home/siddharth/programming/projects/space_invaders/shop_health.png")
shop_health_rect=shop_health.get_rect(center=(400,400))
#####################################################################################################################################
#background surface
background=pygame.image.load("/home/siddharth/programming/projects/space_invaders/background.png")


#player surface
playerX=400
playerY=400
player=pygame.image.load("/home/siddharth/programming/projects/space_invaders/player.png")
player_rect=player.get_rect(center=(playerX,playerY))
playerXchange=0


player_health=3
healthImg=[]
health_rect=[]
healthX=[]
healthY=[]
health_position=784
for health in range(player_health):
    healthX.append(health_position)
    health_position-=16
    healthY.append(484)
    healthImg.append(pygame.image.load("/home/siddharth/programming/projects/space_invaders/love.png"))
    health_rect.append(healthImg[health].get_rect(center=(healthX[health],healthY[health])))


#bullet1 surface
bullet=pygame.image.load("/home/siddharth/programming/projects/space_invaders/bullet2.png")
bullet_rect=bullet.get_rect(center=(playerX,playerY))
bulletXchange=0
bulletYchange=0
bullet_rect.x=player_rect.x+16
bullet_rect.y=player_rect.y+7
fireposition=bullet_rect.x


#bullet2 surface
powerup=pygame.image.load("/home/siddharth/programming/projects/space_invaders/bullet.png")
powerup_rect=powerup.get_rect(center=(playerX,playerY))
powerupXchange=0
powerupYchange=0
powerup_rect.x=player_rect.x+16
powerup_rect.y=player_rect.y+7
powerup_fireposition=powerup_rect.x


#enemies surface
enemyImg=[]
enemy_rect=[]
enemyX=[]
enemyY=[]
enemyXchange=[]
enemyYchange=1

enemy_speed_increaser=0

num_of_enemies=5
for i in range(num_of_enemies):
    enemyX.append(random.randint(200,600))
    enemyY.append(random.randint(-200,0))
    enemyImg.append(pygame.image.load("/home/siddharth/programming/projects/space_invaders/enemy.png"))
    enemy_rect.append(enemyImg[i].get_rect(center=(enemyX[i],enemyY[i])))
    enemyXchange.append(0)


#asteroid surface
asteroidImg=[]
asteroid_rect=[]
asteroidX=[]
asteroidY=[]
asteroidXchange=[]
asteroidYchange=1 

num_of_asteroids=3
for i in range(num_of_asteroids):
    asteroidX.append(random.randint(200,600))
    asteroidY.append(random.randint(-200,0))
    asteroidImg.append(pygame.image.load("/home/siddharth/programming/projects/space_invaders/asteroid.png"))
    asteroid_rect.append(asteroidImg[i].get_rect(center=(asteroidX[i],asteroidY[i])))
    asteroidXchange.append(0)


#####################################################################################################################################################
#user defined constants not associated with objects directly
ammunition="bullet"
collision_occurred = False
collision_occurred_asteroid=False
game_active=True
level=1
kill_count=0
score=0
menu_clicked=True
pause_active=False
###########################################################################################################################################
#make user-defined functions here
def bulletState(string,bulletxchange):
    bullet=bulletxchange
    if string=="fire":
        bullet_rect.x=fireposition
        powerup_rect.x=powerup_fireposition
        bullet=0
    if string=="ready":
        bullet_rect.x=player_rect.x+16
        powerup_rect.x=player_rect.x+16
    return bullet

def get_bulletState(bulletY,playerY):
    if bulletY==playerY+7:
        #print("ready")
        return "ready"
    else:
        #print("fire")
        return "fire"


def level_kill_counter(level_,kill_count,enemy_speed_increaser_):
    global level
    level=level_
    global enemy_speed_increaser
    enemy_speed_increaser=enemy_speed_increaser_
    if kill_count==20:
        level+=1
        enemy_speed_increaser+=0.1
    elif kill_count==50:
        level+=1
        enemy_speed_increaser+=0.1
    elif kill_count==80:
        level+=1
        enemy_speed_increaser+=0.1
    elif kill_count==110:
        level+=1
        enemy_speed_increaser+=0.3
    print("kill count=",kill_count)
    print("level=",level)


###############################################################################################################################################
running=True
while running:
    mouse_input=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
##########################################################
        if not pause_active:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_d:
                    playerXchange=6
                    bulletXchange=6 
                    powerupXchange=6
                if event.key==pygame.K_a:
                    playerXchange=-6
                    bulletXchange=-6
                    powerupXchange=-6
            
#########################################################
                if event.key==pygame.K_1:
                    ammunition="bullet"   
                if event.key==pygame.K_2:
                    ammunition="powerup"
                if event.key==pygame.K_SPACE:
                    if ammunition=="bullet":
                        bulletYchange=-15
                        bullet_rect.y += bulletYchange
                    elif ammunition=="powerup":
                        powerupYchange=-15
                        powerup_rect.y += powerupYchange
####################################################
                           
            if event.type ==pygame.KEYUP:
                if event.key==pygame.K_d or event.key==pygame.K_a:
                    playerXchange=0
                    bulletXchange=0
                    powerupXchange=0


##########################################################################
            if event.type==pygame.MOUSEBUTTONDOWN:
                print(mouse_input)
                if pause_button_rect.collidepoint(mouse_input):
                    print("pause collision")
                    game_active=False
                    pause_active=True
                
 #####################################################################           


        if pause_active:
            if event.type==pygame.MOUSEBUTTONDOWN:
                print(mouse_input)
                if menu_button_rect.collidepoint(mouse_input):
                    print("menu collision")
                pygame.draw.rect(screen,pause_screen_color,pause_screen)
                screen.blit(continue_button,continue_button_rect)
                shop_label=main_font.render(f"buy health",1,(0,0,0))  
                screen.blit(shop_label,(350,365))         
                screen.blit(menu_button,menu_button_rect)
                screen.blit(shop_health,shop_health_rect)
                if shop_health_rect.collidepoint(mouse_input):
                    print("buy health")
                    if score>=50:
                        player_health+=1
                        score-=50
                    else:
                        print("you cannot buy u poor fk")
                    healthImg=[]
                    healthX = []
                    healthY=[]
                    health_rect = []
                    health_position = 784
                    for i in range(player_health):
                        healthX.append(health_position)
                        health_position -= 16
                        healthY.append(484)
                        healthImg.append(pygame.image.load("/home/siddharth/programming/projects/space_invaders/love.png"))
                        health_rect.append(healthImg[i].get_rect(center=(healthX[i], healthY[i])))
                else:
                    print("u fked")
                if continue_button_rect.collidepoint(mouse_input):
                    print("continue collision")
                    game_active=True
                    pause_active=False

                    



        if player_health<=0:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_active=True
                    player_health=3 
                    playerXchange=0
                    score=0
                    enemy_speed_increaser=0
                    for i in range(num_of_enemies):
                        enemy_rect[i].y=-100
                    for i in range(num_of_asteroids):
                        asteroid_rect[i].y=-200
                    
    if game_active:      
###############################################################################################################################33333333333   
    #displaying screen
        screen.blit(background,(0,0))

        score_label=main_font.render(f"Money : {score}",1,(255,255,255))
        screen.blit(score_label,(16,469))

        level_label=main_font.render(f"Level: {level}",1,(255,255,255))
        screen.blit(level_label,(0,10))

        screen.blit(pause_button,pause_button_rect)
        
########################################################################################################################################3   
     
    #displaying bullet and bullet mechanics
        if ammunition=="bullet":
            screen.blit(bullet,bullet_rect)
            bullet_rect.x+=bulletXchange
            bullet_rect.y+=bulletYchange
            if bullet_rect.top<=0:
                bullet_rect.x=player_rect.x+16
                bullet_rect.y=player_rect.y+7
                bulletYchange=0
            fireposition=bullet_rect.x
            state=get_bulletState(bullet_rect.y,player_rect.y)
            bulletXchange=bulletState(state,bulletXchange)

    #displaying powerup and powerup mechanics       
        if ammunition=="powerup":
            screen.blit(powerup,powerup_rect)
            powerup_rect.x+=powerupXchange
            powerup_rect.y+=powerupYchange
            if powerup_rect.top<=0:
                powerup_rect.x=player_rect.x+16
                powerup_rect.y=player_rect.y+7
                powerupYchange=0
            powerup_fireposition=powerup_rect.x
            state2=get_bulletState(powerup_rect.y,player_rect.y)
            powerupXchange=bulletState(state2,powerupXchange)


#####################################################################################################################################    
    #displaying player and player mechanics
        screen.blit(player,player_rect)
        player_rect.x+=playerXchange
        if player_rect.right>=800:
            player_rect.right=800
        if player_rect.left<=0:
            player_rect.left=0
############################################################################################################################################ 
    #displaying player health mechanics   
        if player_health<=0:
            game_active=False
            kill_count=0
            level=1
            game_over_label=main_font.render(f"Game Over! Press spacebar to restart",1,(255,255,255))
            screen.blit(game_over_label,(250,250))

        for health in range(player_health):
            screen.blit(healthImg[health],health_rect[health])
##########################################################################################################################################







    #displaying enemy and enemy mechanics
        for i in range(num_of_enemies):
            screen.blit(enemyImg[i],enemy_rect[i])
            enemy_rect[i].y+=enemyYchange+enemy_speed_increaser

            #if enemies move off screen
            if enemy_rect[i].y>500:
                enemy_rect[i].top=-100
                enemy_rect[i].x=random.randint(100,700)
                if score<=0:
                    score=0
                else:
                    score-=20


        #checking collision with enemy and player
            if player_rect.colliderect(enemy_rect[i]):
                if not collision_occurred:
                    print("Collided!")
                    collision_occurred = True
                    player_health-=1

        #checking collision with enemy and bullet
            if (bullet_rect.colliderect(enemy_rect[i]) or powerup_rect.colliderect(enemy_rect[i])):
                enemy_rect[i].y=-100
                enemy_rect[i].x=random.randint(100,700)
                if (collision_occurred):
                   score+=0
                   print("no update")
                    
                else:
                   score+=5
                   print("update")

                bulletYchange=0 #stop bullet from moving
                powerupYchange=0
                bullet_rect.y=player_rect.y+7 # reset bullet y coordinate
                powerup_rect.y=player_rect.y+7
                kill_count+=1

                #levels and kill counter
                level_kill_counter(level,kill_count,enemy_speed_increaser)
   
        if not any(player_rect.colliderect(enemy) for enemy in enemy_rect):
            collision_occurred = False   

        



    #displaying asteroid and asteroid mechanics
        if level>=3:
            for i in range(num_of_asteroids):
                screen.blit(asteroidImg[i],asteroid_rect[i])
                asteroid_rect[i].y+=asteroidYchange

                if asteroid_rect[i].y>500:
                    asteroid_rect[i].top=-100
                    asteroid_rect[i].x=random.randint(100,700)
                    if score<=0:
                        score=0
                    else:
                        score-=50
                    
                if player_rect.colliderect(asteroid_rect[i]):
                    if not collision_occurred_asteroid:
                        print("Collided!")
                        collision_occurred_asteroid = True
                        player_health-=3


                if (powerup_rect.colliderect(asteroid_rect[i])):
                    asteroid_rect[i].y=-100
                    asteroid_rect[i].x=random.randint(100,700)
                    if collision_occurred:
                        score+=0
                        print("player collision with asteroid")
                    else:
                        score+=10
                        print("bullet collision with asteroid")
                    powerupYchange=0
                    powerup_rect.y=player_rect.y+7
                    kill_count+=1
                    level_kill_counter(level,kill_count,enemy_speed_increaser)

            if not any(player_rect.colliderect(asteroid) for asteroid in asteroid_rect):
                collision_occurred_asteroid = False 
    

#################################################################################################################################################
    pygame.display.update()
    clock.tick(120)

