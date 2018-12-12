import pygame

#inititalizes the pygame module
pygame.init()



def light(toggleList):
#MODIFY CODE BELOW
#TOGGLELIST HAS ONLY 3 VALUES, ACCESS EACH ONE WITH toggleList[0],toggleList[1], or toggleList[2],
    if toggleList[0]:
        lightOn()#MAKES IT TURN THE LIGHT ON WHEN BUTTON 1 IS ON
    elif toggleList[1] and toggleList[2]:
        lightOn()
    else:
        lightOff()


#MODIFY CODE ABOVE





#Turns the light off
def lightOff():
    gameDisplay.fill(black)
    gameDisplay.blit(lightOffImg,(0.28*640,.04*640))

#Turn the light on
def lightOn():
    gameDisplay.fill(white)
    gameDisplay.blit(lightOnImg,(0.28*640,.04*640))

#handle text objects
def text_objects(text, font):
    textSurface=font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#handles the buttons drawing and toggle
def button(boundingX, boundingY, w, h, num, toggleList, click):
    mouse=pygame.mouse.get_pos()

    if (boundingX+w >mouse[0] > boundingX and boundingY+h > mouse[1] > boundingY) and click:
            toggleList[num]= not toggleList[num]
            pygame.time.wait(100)
    if toggleList[num]:
        color=green
        text="ON"
    else:
        color=red
        text="OFF"
    #draw the buttons with the colors
    pygame.draw.rect(gameDisplay,color,(boundingX,boundingY,w,h))
    #draw the tex above the button
    textFont=pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(text,textFont)
    textRect.center = ((boundingX+(w/2)),(boundingY+(h/2)))
    gameDisplay.blit(textSurf,textRect)


width=640
height=640
#set screen size and title
click=False


gameDisplay=pygame.display.set_mode((width,height))
pygame.display.set_caption('Lightswitches')

clock=pygame.time.Clock()

#colors
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)

#load images for use
lightOnImg= pygame.image.load('lightbulb_ON.png')
lightOffImg= pygame.image.load('lightbulb_OFF.png')
exited= False
#buttons Toggle List
buttonList=[False,False,False]


lightOff();

#this loop runs the game
while not exited:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exited=True
        elif event.type==pygame.MOUSEBUTTONDOWN:
            click= True
            pygame.time.wait(100)
        elif event.type==pygame.MOUSEBUTTONUP:
            click= False
            pygame.time.wait(100)
    light(buttonList)
    button(100,450,100,50,0,buttonList,click)
    button(270,450,100,50,1,buttonList,click)
    button(440,450,100,50,2,buttonList,click)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
