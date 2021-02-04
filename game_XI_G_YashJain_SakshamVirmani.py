'''
Project Title: Ninja Run
Class-Section: XI-G
Developed by : Saksham Virmani & Yash Jain
'''

#importing random module
import random

#importing pygame module
import pygame
from pygame.locals import *

#initialize pygame module
pygame.init()


#screen height and width
screen = pygame.display.set_mode((600, 400))

#screen title
pygame.display.set_caption('Ninja Run')

#font
font = pygame.font.Font('freesansbold.ttf', 20)


#backgroung settions
bg = pygame.image.load('background.png')

#player sprites
player = pygame.image.load('dra1.png')
player = pygame.transform.scale(player, (70 ,70))
player1= pygame.image.load('dra2.png')
player1= pygame.transform.scale(player1, (70 ,70))
player2= pygame.image.load('dra3.png')
player2= pygame.transform.scale(player2, (70 ,70))
player3= pygame.image.load('dra4.png')
player3= pygame.transform.scale(player3, (70 ,70))
player4= pygame.image.load('dra5.png')
player4= pygame.transform.scale(player4, (70 ,70))

#list of sprites for player animation
walk = [player, player,player,player, player, player,player,player,player, player,player,player,player1, player1,player1,player1,player1, player1,player1,player1,player1, player1,player1,player1,player2, player2,player2,player2,player2, player2,player2,player2,player2, player2,player2,player2,player3,player3,player3,player3,player3,player3,player3,player3,player3,player3,player3,player3, player4, player4, player4, player4 ,player4, player4, player4, player4, player4, player4, player4, player4]


#obstacle sprites
obstacle = pygame.image.load('hurdle1.png')
obstacle = pygame.transform.scale(obstacle, (70, 70))
obstacle1 = pygame.image.load('hurdle2.png')
obstacle1 = pygame.transform.scale(obstacle1, (90, 90))
obstacle2 = pygame.image.load('hurdle3.png')
obstacle2 = pygame.transform.scale(obstacle2, (90, 90))
obstacle3 = pygame.image.load('hurdle5.png')
obstacle3 = pygame.transform.scale(obstacle3, (150, 150))
obstacle4 = pygame.image.load('hurdle4.png')
obstacle4 = pygame.transform.scale(obstacle4, (90, 90))

#high score counter
hscore = 0

#main loop
def gameloop():
    
    #game Variables
    bg_velocity = 0
    bg_x = 0
    bg_y = 0
    white = (255,255,255)
    black = (0, 0, 0)
    gravity = 4
    walkpoint = 0
    game = False
    jump = False
    gameover = False
    obstacle_y = 280
    obstacle_x = random.randint(650,700)
    obstacle1_x = random.randint(1050,1250)
    obstacle2_x = random.randint(1450,1650)
    obstacle3_x = random.randint(1850,2050)
    obstacle4_x = random.randint(2260,2450)
    player_x = 50
    player_y = 265
    score = 0
    global hscore

    #keyboard controls
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
              pygame.quit()
            if event.type == KEYDOWN:
               if event.key == K_SPACE or event.key == K_UP:
                   if player_y == 265:
                     jump = True
                     game = True
                     bg_velocity = 3
               if gameover == True:
                   if event.key == K_SPACE or event.key== K_UP:
                        gameloop()
            
        

        #infinite scrollong background
        if bg_x == -600:
            bg_x = 0

        bg_x -= bg_velocity

        #position of background
        screen.blit(bg, [bg_x, bg_y]) 
        screen.blit(bg, [bg_x + 600, bg_y])

        #obstacle scrolling
        obstacle_x -= bg_velocity
        obstacle1_x -= bg_velocity
        obstacle2_x -= 1.1*bg_velocity
        obstacle3_x -= bg_velocity
        obstacle4_x -= bg_velocity

        if obstacle_x < -2500:
            obstacle_x = random.randint(650,700)
        if obstacle1_x < -2500:
            obstacle1_x = random.randint(1050,1250)
        if obstacle2_x < -2500:
            obstacle2_x = random.randint(1450,1650)
        if obstacle3_x < -2500:
            obstacle3_x = random.randint(1850,2050)
        if obstacle4_x < -2500:
            obstacle4_x = random.randint(2250,2450)

    
        #jump function
        if  266 > player_y > 115:
            if jump == True:
                player_y -= gravity
        else:
            jump = False
        if player_y <265:
            if jump == False:
                player_y += gravity

    
        #collision
        if obstacle_x < player_x + 20 < obstacle_x + 25 and obstacle_y < player_y+50 < obstacle_y+50:
            bg_velocity = 0
            walkpoint = 0
            game = False
            gameover = True
        if obstacle1_x< player_x + 20 < obstacle1_x + 25 and obstacle_y < player_y+50 < obstacle_y+50:
            bg_velocity = 0
            walkpoint = 0
            game = False
            gameover = True
        if obstacle2_x < player_x + 20 < obstacle2_x + 25 and obstacle_y < player_y+50 < obstacle_y+50:
            bg_velocity = 0
            walkpoint = 0
            game = False
            gameover = True
        if obstacle3_x< player_x + 20 < obstacle3_x + 50 and obstacle_y < player_y+50 < obstacle_y+50:
            bg_velocity = 0
            walkpoint = 0
            game = False
            gameover = True
        if obstacle4_x < player_x + 20 < obstacle4_x + 25 and obstacle_y < player_y+50 < obstacle_y+50:
            bg_velocity = 0
            walkpoint = 0
            game = False
            gameover = True

            
        #score function
        if game == True:
            score+=1
        if gameover == True:
            if hscore<=score:
                hscore=score


        #game over text
        text  = font.render('SCORE : '+ str(score), True, black)
        text1 = font.render('Game Over !!', True, black)
        text2 = font.render('Press SPACE or UP key to Continue', True, black)
        text3 = font.render(' HIGH SCORE : ' + str(hscore),True, black)
        screen.blit(text3,[400,50])
        screen.blit(text, [460, 100])
        if gameover == True:
            screen.blit(text1, [243, 150])
            screen.blit(text2, [140, 180])
            

        #animation of player
        screen.blit(walk[walkpoint], [player_x, player_y]) #position of player
        walkpoint += 1
        if walkpoint > len(walk)-1:
            walkpoint = 0
    
        
        #obstacle repetition
        screen.blit(obstacle, [obstacle_x, obstacle_y-10])
        screen.blit(obstacle1,[obstacle1_x, obstacle_y-35])
        screen.blit(obstacle2,[obstacle2_x , obstacle_y-40 ])
        screen.blit(obstacle3,[obstacle3_x , obstacle_y -75])
        screen.blit(obstacle4,[obstacle4_x , obstacle_y-40 ])

        pygame.display.update()
        
gameloop()
