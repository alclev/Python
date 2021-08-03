import pygame #import library

pygame.init() #initialize game engine

size=[800,500] #width and height
screen=pygame.display.set_mode(size)  #creates screen

pygame.display.set_caption("Graphics Practice")
pygame.display.set_icon(pygame.image.load("pyicon.png").convert_alpha())

#Colors
blue=(188, 209, 242)
white=(255,255,255)
pink=(255, 94, 166)
violet=(175, 82, 242)


done=False

clock= pygame.time.Clock()
x=400
y=250
#r=input("Radius?")
#radius=int(r)
while done==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

    #Body
    screen.fill(white)
    pos=pygame.mouse.get_pos()
    x+=1
    pygame.draw.circle(screen,violet, (pos), 50,0)
    pygame.draw.circle(screen,blue,(x,y),50,0)
    
    
    pygame.display.update()
    clock.tick(500) #limits in frames per second
pygame.quit()
