import pygame
from pygame.locals import *
import time
from time import sleep
import random

#Start pygame instance
pygame.init()


# Game Display
display_width = 1200
display_height = 800

# Setting up game display
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('MP7 - By Allen and Snehil')

# Different font sizes
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

# Clock/Frames per second element
clock = pygame.time.Clock()

# Some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0,128,0)
bright_green = (0,255,0)
red = (128,0,0)
bright_red=(255,0,0)

# Images for rocket animation
s1 = pygame.image.load('f1.png')
s2 = pygame.image.load('f2.png')
s3 = pygame.image.load('f3.png')
s4 = pygame.image.load('f4.png')

# Dimensions according to the image
imageW = 100
imageH = 100

# Images scaled for meteor animation
M1 = pygame.image.load('meteor0001.png')
M1 = pygame.transform.scale(M1, (80, 200))
M2 = pygame.image.load('meteor0002.png')
M2 = pygame.transform.scale(M2, (80, 200))
M3 = pygame.image.load('meteor0003.png')
M3 = pygame.transform.scale(M3, (80, 200))
M4 = pygame.image.load('meteor0004.png')
M4 = pygame.transform.scale(M4, (80, 200))
M5 = pygame.image.load('meteor0005.png')
M5 = pygame.transform.scale(M5, (80, 200))
M6 = pygame.image.load('meteor0006.png')
M6 = pygame.transform.scale(M6, (80, 200))
M7 = pygame.image.load('meteor0007.png')
M7 = pygame.transform.scale(M7, (80, 200))
M8 = pygame.image.load('meteor0008.png')
M8 = pygame.transform.scale(M8, (80, 200))
M9 = pygame.image.load('meteor0009.png')
M9 = pygame.transform.scale(M9, (80, 200))
M10 = pygame.image.load('meteor0010.png')
M10 = pygame.transform.scale(M10, (80, 200))
M11 = pygame.image.load('meteor0011.png')
M11 = pygame.transform.scale(M11, (80, 200))

title = pygame.image.load("title.png")

# Background transformed to fit game display
background = pygame.image.load("starfield.png")
background = pygame.transform.scale(background, (display_width, display_height))

# y position for background to move up


#Scoring system on the top left
def score(score):
    text = smallfont.render("Score: "+ str(score), True, white)
    gameDisplay.blit(text, [0,0])





# Meteor animation
def meteor(curM, x,y):
    if curM == 1:
        gameDisplay.blit(M1, (x,y))
        curM += 1
    elif curM == 2:
        gameDisplay.blit(M2, (x,y))
        curM += 1
    elif curM == 3:
        gameDisplay.blit(M3, (x,y))
        curM += 1
    elif curM == 4:
        gameDisplay.blit(M4, (x,y))
        curM += 1
    elif curM == 5:
        gameDisplay.blit(M5, (x,y))
        curM += 1
    elif curM == 6:
        gameDisplay.blit(M6, (x,y))
        curM += 1
    elif curM == 7:
        gameDisplay.blit(M7, (x,y))
        curM += 1
    elif curM == 8:
        gameDisplay.blit(M8, (x,y))
        curM += 1
    elif curM == 9:
        gameDisplay.blit(M9, (x,y))
        curM += 1
    elif curM == 10:
        gameDisplay.blit(M10, (x,y))
        curM += 1
    else:
        gameDisplay.blit(M11, (x,y))
        curM = 1
    return curM

# Method for rotating image
def spaceRotate(img, angle, x, y):
    gameDisplay.blit(pygame.transform.rotate(img, angle), (x,y))



# Method for animating rocket and the fire
def animation(curImage, angle, lead_x, lead_y):
    if curImage == 1:
        spaceRotate(s1, angle, lead_x, lead_y)
        curImage += 1

    elif curImage == 2:
        spaceRotate(s2, angle, lead_x, lead_y)
        curImage =1

    elif curImage == 3:
        spaceRotate(s3, angle, lead_x, lead_y)
        curImage += 1

    elif curImage == 4:
        spaceRotate(s4, angle, lead_x, lead_y)
        curImage = 1
    return curImage


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 50)
    textSurf, textRect = text_objects("BEGIN!", smallText)
    textRect.center = ((550 + (100 / 2)), (430 + (50 / 2)))
    gameDisplay.blit(textSurf, textRect)

    smallText = pygame.font.Font("freesansbold.ttf", 50)
    textSurf, textRect = text_objects("QUIT!", smallText)
    textRect.center = ((550 + (100 / 2)), (580 + (50 / 2)))
    gameDisplay.blit(textSurf, textRect)


def game_intro():
    intro = True
    y = 0
    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        rel_y = y + display_height
        y -= 1
        if (y == display_height * -1):
            y = 0
        gameDisplay.fill(black)
        gameDisplay.blit(background, (0, y))
        gameDisplay.blit(background, (0, rel_y))
        gameDisplay.blit(title, (300, 100))
        # gameDisplay.fill(white)

        button("GO!", 500, 400, 200, 100, green, bright_green, game_loop)
        button("Quit", 500, 550, 200, 100, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)



# quit game function
def quitgame():
    pygame.quit()
    quit()

# Starts the game
def game_loop():





    y=0


    # The image the animation is currently at
    curImage = 1



    # Starting position of rocket
    lead_x = display_width / 2 - imageW
    lead_y = display_height / 2 - imageH

    # Variables to account for movement
    lead_x_change = 0
    lead_y_change = 0

    # Moving
    move = 10

    # Current angle for movement
    angle = 0

    # Current animation and dropping position.
    curM1 = 1
    meteorSpd1 = 4
    mX1 = random.randrange(0, display_width)
    mY1 = 0 - pygame.Surface.get_width(M1) - 200

    meteorSpd2 = 5
    curM2 = 1
    mX2 = random.randrange(0, display_width)
    mY2 = 0 - pygame.Surface.get_width(M1) - 300

    meteorSpd3 = 6
    curM3 = 1
    mX3 = random.randrange(0, display_width)
    mY3 = 0 - pygame.Surface.get_width(M1) - 150

    meteorSpd4 = 7
    curM4 = 1
    mX4 = random.randrange(0, display_width)
    mY4 = 0 - pygame.Surface.get_width(M1) - 320

    meteorSpd5 = 8
    curM5 = 1
    mX5 = random.randrange(0, display_width)
    mY5 = 0 - pygame.Surface.get_width(M1) - 250

    meteorSpd6 = 9
    curM6 = 1
    mX6 = random.randrange(0, display_width)
    mY6 = 0 - pygame.Surface.get_width(M1) - 90

    meteorSpd7 = 10
    curM7 = 1
    mX7 = random.randrange(0, display_width)
    mY7 = 0 - pygame.Surface.get_width(M1) - 90

    meteorSpd8 = 3
    curM8 = 1
    mX8 = random.randrange(0, display_width)
    mY8 = 0 - pygame.Surface.get_width(M1) - 90

    # Records highscore by using time
    highscore = 0
    curTime = time.time()

    # Determine if game ends
    exit = False

    # Determines if dead
    dead = False

    # Determines if user wants to restart game
    restartGame = False

    # Starting events, while user has not exited.
    while not exit:
        # If user is dead and wants to restart game
        if restartGame:
            curM1 = 1
            meteorSpd1 = 4
            mX1 = random.randrange(0, display_width)
            mY1 = 0 - pygame.Surface.get_width(M1)

            meteorSpd2 = 5
            curM2 = 1
            mX2 = random.randrange(0, display_width)
            mY2 = 0 - pygame.Surface.get_width(M1) - 100

            meteorSpd3 = 6
            curM3 = 1
            mX3 = random.randrange(0, display_width)
            mY3 = 0 - pygame.Surface.get_width(M1) - 50

            meteorSpd4 = 7
            curM4 = 1
            mX4 = random.randrange(0, display_width)
            mY4 = 0 - pygame.Surface.get_width(M1) - 150

            meteorSpd5 = 8
            curM5 = 1
            mX5 = random.randrange(0, display_width)
            mY5 = 0 - pygame.Surface.get_width(M1) - 125

            meteorSpd6 = 9
            curM6 = 1
            mX6 = random.randrange(0, display_width)
            mY6 = 0 - pygame.Surface.get_width(M1) - 25

            meteorSpd7 = 10
            curM7 = 1
            mX7 = random.randrange(0, display_width)
            mY7 = 0 - pygame.Surface.get_width(M1) - 90

            meteorSpd8 = 3
            curM7 = 1
            mX8 = random.randrange(0, display_width)
            mY8 = 0 - pygame.Surface.get_width(M1) - 90

            lead_x = display_width / 2 - imageW / 2
            lead_y = display_height / 2 - imageH / 2

            # Variables to account for movement
            lead_x_change = 0
            lead_y_change = 0
            curTime = time.time()
            angle = 0
            restartGame = False

        pressed = 0
        # Tracks every event that occurs
        for event in pygame.event.get():
            # Determine of game should be exited
            if event.type == pygame.QUIT:
                exit = True
                pygame.quit()
                quit()

            # Get the keys that are pressed
            keys = pygame.key.get_pressed()

            # Number of arrow keys current pressed
            pressed = keys[K_LEFT] + keys[K_RIGHT] + keys[K_UP] + keys[K_DOWN]

            if (pressed != 3):
                # if only 1 key is pressed, then move in that direction only.
                if pressed == 1:
                    # Horizontal movement
                    if keys[K_LEFT]:
                        lead_x_change = move * -1
                        lead_y_change = 0
                    elif keys[K_RIGHT]:
                        lead_x_change = move
                        lead_y_change = 0

                    # Vertical Movement
                    elif keys[K_UP]:
                        lead_y_change = move * -1
                        lead_x_change = 0
                    elif keys[K_DOWN]:
                        lead_y_change = move
                        lead_x_change = 0

                # if 2 keys are pressed at the same time, give it a diagonal value
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        lead_x_change = move * -1

                    if event.key == pygame.K_RIGHT:
                        lead_x_change = move

                    if event.key == pygame.K_DOWN:
                        lead_y_change = move

                    if event.key == pygame.K_UP:
                        lead_y_change = move * -1

        # Store the changes so rocket can be displayed at that position
        lead_x += lead_x_change
        lead_y += lead_y_change

        # Wipe out previous position and display new position
        gameDisplay.fill(black)

        # Bounds to limit rocket inside game display
        if lead_x > 0 and lead_y > 0 and lead_y + imageH * 2 /3  <= display_height and lead_x + imageH*2/3 <= display_width:
            if(pressed==3):
                curImage = animation(curImage, angle, lead_x, lead_y)
            # Determines orientation of rocket
            elif(pressed >= 1):
                if keys[K_RIGHT] and pressed == 1:
                    curImage = animation(curImage, 0, lead_x, lead_y)
                    angle = 0
                elif keys[K_RIGHT] and  keys[K_UP] and pressed == 2:
                    curImage = animation(curImage, 45, lead_x, lead_y)
                    angle = 45
                elif keys[K_UP] and pressed == 1:
                    curImage = animation(curImage, 90, lead_x, lead_y)
                    angle = 90
                elif keys[K_UP] and keys[K_LEFT] and pressed == 2:
                    curImage = animation(curImage, 135, lead_x, lead_y)
                    angle = 135
                elif keys[K_LEFT] and pressed == 1:
                    curImage = animation(curImage, 180, lead_x, lead_y)
                    angle = 180
                elif keys[K_DOWN] and keys[K_LEFT] and pressed == 2:
                    curImage = animation(curImage, 225, lead_x, lead_y)
                    angle = 225
                elif keys[K_DOWN] and pressed == 1:
                    curImage = animation(curImage, 270, lead_x, lead_y)
                    angle = 270
                elif keys[K_DOWN] and keys[K_RIGHT] and pressed == 2:
                    curImage = animation(curImage, 315, lead_x, lead_y)
                    angle = 315
                elif pressed == 3:
                    curImage = animation(curImage, angle, lead_x, lead_y)
            else:
                curImage = animation(curImage, angle, lead_x, lead_y)

        # If nothing is pressed, follow the orientation of the previous angle
        else:
            lead_x -= lead_x_change
            lead_y -= lead_y_change
            if keys[K_DOWN]:
                angle = 270
            elif keys[K_RIGHT]:
                angle = 0
            elif keys[K_LEFT]:
                angle = 180
            elif keys[K_UP]:
                angle = 90
            curImage = animation(curImage, angle, lead_x, lead_y)

        # Dropping 6 meteors from random positions from the top
        # Meteor 1...6
        mY1 += meteorSpd1
        mX1 += random.randrange(-5, 5)
        if(mY1 > display_height):
            meteorSpd1 *= 1.05
            mY1 = 0 - pygame.Surface.get_width(M1)
            mX1 = random.randrange(0, display_width)
        curM1 = meteor(curM1, mX1, mY1)

        mY2 += meteorSpd2
        mX2 += random.randrange(-5, 5)
        if (mY2 > display_height):
            meteorSpd2 *= 1.05
            mY2 = 0 - pygame.Surface.get_width(M1)
            mX2 = random.randrange(0, display_width)
        curM2 = meteor(curM2, mX2, mY2)

        mY3 += meteorSpd3
        mX3 += random.randrange(-5, 5)
        if (mY3 > display_height):
            meteorSpd3 *= 1.05
            mY3 = 0 - pygame.Surface.get_width(M1)
            mX3 = random.randrange(0, display_width)
        curM3 = meteor(curM3, mX3, mY3)

        mY4 += meteorSpd4
        mX4 += random.randrange(-5, 5)
        if (mY4 > display_height):
            meteorSpd4 *= 1.05
            mY4 = 0 - pygame.Surface.get_width(M1)
            mX4 = random.randrange(0, display_width)
        curM4 = meteor(curM4, mX4, mY4)

        mY5 += meteorSpd5
        mX5 += random.randrange(-5, 5)
        if (mY5 > display_height):
            meteorSpd5 *= 1.05
            mY5 = 0 - pygame.Surface.get_width(M1)
            mX5 = random.randrange(0, display_width)
        curM5 = meteor(curM5, mX5, mY5)

        mY6 += meteorSpd6
        mX6 += random.randrange(-5, 5)
        if (mY6 > display_height):
            meteorSpd6 *= 1.05
            mY6 = 0 - pygame.Surface.get_width(M1)
            mX6 = random.randrange(0, display_width)
        curM6 = meteor(curM6, mX6, mY6)

        mY7 += meteorSpd7
        mX7 += random.randrange(-5, 5)
        if (mY7 > display_height):
            meteorSpd7 *= 1.05
            mY7 = 0 - pygame.Surface.get_width(M1)
            mX7 = random.randrange(0, display_width)
        curM7 = meteor(curM7, mX7, mY7)

        mY8 += meteorSpd8
        mX8 += random.randrange(-5, 5)
        if (mY8 > display_height):
            meteorSpd8 *= 1.1
            mY8 = 0 - pygame.Surface.get_width(M1)
            mX8 = random.randrange(0, display_width)
        curM8 = meteor(curM8, mX8, mY8)

        # Testing if meteor and rocket collides
        # If player collides, player is dead
        # Testing from meteor 1 - meteor 6
        meteors = pygame.Rect(mX1+10, mY1+20, pygame.Surface.get_width(M2)-10, pygame.Surface.get_height(M2)-20)
        rocket = pygame.Rect(lead_x, lead_y, pygame.Surface.get_width(s1), pygame.Surface.get_width(s1))
        if(rocket.colliderect(meteors)):
            dead = True

        meteors = pygame.Rect(mX2+10, mY2 + 20, pygame.Surface.get_width(M2)-10, pygame.Surface.get_height(M2)-20)
        rocket = pygame.Rect(lead_x, lead_y, pygame.Surface.get_width(s1), pygame.Surface.get_width(s1))
        if (rocket.colliderect(meteors)):
            dead = True

        meteors = pygame.Rect(mX3+10, mY3 + 20, pygame.Surface.get_width(M2)-10, pygame.Surface.get_height(M2)-20)
        rocket = pygame.Rect(lead_x, lead_y, pygame.Surface.get_width(s1), pygame.Surface.get_width(s1))
        if (rocket.colliderect(meteors)):
            dead = True

        meteors = pygame.Rect(mX6+10, mY6 + 20, pygame.Surface.get_width(M2)-10, pygame.Surface.get_height(M2)-20)
        rocket = pygame.Rect(lead_x, lead_y, pygame.Surface.get_width(s1), pygame.Surface.get_width(s1))
        if (rocket.colliderect(meteors)):
            dead = True

        meteors = pygame.Rect(mX4+10, mY4 + 20, pygame.Surface.get_width(M2)-10, pygame.Surface.get_height(M2)-20)
        rocket = pygame.Rect(lead_x, lead_y, pygame.Surface.get_width(s1), pygame.Surface.get_width(s1))
        if (rocket.colliderect(meteors)):
            dead = True

        meteors = pygame.Rect(mX5+10, mY5 + 20, pygame.Surface.get_width(M2)-10, pygame.Surface.get_height(M2)-20)
        rocket = pygame.Rect(lead_x, lead_y, pygame.Surface.get_width(s1), pygame.Surface.get_width(s1))
        if (rocket.colliderect(meteors)):
            dead = True

        meteors = pygame.Rect(mX7+10, mY7 + 20, pygame.Surface.get_width(M2)-10, pygame.Surface.get_height(M2)-20)
        rocket = pygame.Rect(lead_x, lead_y, pygame.Surface.get_width(s1), pygame.Surface.get_width(s1))
        if (rocket.colliderect(meteors)):
            dead = True

        meteors = pygame.Rect(mX8+10, mY8 + 20, pygame.Surface.get_width(M2)-10, pygame.Surface.get_height(M2) - 20)
        rocket = pygame.Rect(lead_x, lead_y, pygame.Surface.get_width(s1), pygame.Surface.get_width(s1))
        if (rocket.colliderect(meteors)):
            dead = True
        # If player is dead, record the instance of time to calculate score.
        if(dead):
            Cur = time.time() - curTime
            if(Cur > highscore):
                highscore = Cur
                # sleep(0.2)

        # Jumps to another screen while player is dead
        while(dead):
            # Keeps background moving
            rel_y = y + display_height
            y -= 1
            if (y == display_height * -1):
                y = 0
            gameDisplay.fill(black)
            gameDisplay.blit(background, (0, y))
            gameDisplay.blit(background, (0, rel_y))

            # Displays certain text
            crashed = largefont.render("YOU CRASHED!!!", True, white)
            gameDisplay.blit(crashed, [320, 200])

            restart = medfont.render("Press \"space\" to restart!", True, white)
            gameDisplay.blit(restart, [350, 600])

            high = medfont.render("You survived " + str(int(Cur)) + " second(s)", True, white)
            gameDisplay.blit(high, [350, 400])

            hscore = smallfont.render("Highscore: " + str(int(highscore)), True, white)
            gameDisplay.blit(hscore, [0, 0])

            # Be sure to update due to moving background
            pygame.display.update()

            # If player decides to restart and press y, break out of the "dead" loop
            keys = pygame.key.get_pressed()
            if(keys[K_SPACE]):
                dead = False
                restartGame = True
                break

            # If player quits the game by clicking x, ends the pygame instance.
            ev = pygame.event.poll()
            if(ev.type == pygame.QUIT):
                pygame.quit()
                quit()

        # Keeps the background moving
        # To make the background display in a loop
        rel_y = y + display_height
        y -= 1
        # Refresh backgroundy
        if(y==display_height*-1):
            y=0;

        # Display background
        gameDisplay.blit(background, (0, y))

        # Display followup background
        gameDisplay.blit(background, (0, rel_y))

        # Keeps track of score at top left
        score(int((time.time() - curTime) / 1))

        # Update game the game display
        pygame.display.update()

        # Determines FPS
        clock.tick(25)

game_intro()
