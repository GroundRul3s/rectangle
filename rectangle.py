import pygame
pygame.init()

WIDTH = 600
HEIGHT = 600 

screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("sky blue")


#def __init__ is a constructer
#used to initialise varibles!

class Rect:
    def __init__(self,x,y,w,h,color):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.color=color
        self.dim=(self.x,self.y,self.w,self.h)
        self.screen=screen

    def draw(self):
        self.rect_draw=pygame.draw.rect(self.screen,self.color,self.dim)

red = Rect(0,75,100,200,"red")

orang = Rect(50,150,100,200,"orange")

yelow = Rect(100,225,100,200,"yellow")

gren = Rect(150,300,100,200,"green")

blu = Rect(200,375,100,200,"blue")





while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    red.draw()
    orang.draw()
    yelow.draw()
    gren.draw()
    blu.draw()

    pygame.display.update()         


