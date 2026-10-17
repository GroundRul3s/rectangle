import pygame
pygame.init()

WIDTH = 600
HEIGHT = 600 

screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("blue")




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

rr = Rect(100,200,100,200,"red")





while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    rr.draw()

    pygame.display.update()         


