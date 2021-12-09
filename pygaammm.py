import pygame
pygame.init

size = (600,400)
window = pygame.display.set_mode(size)
#couleurs
blue=(0,0,255)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
black=(0,0,0)
window.fill(white)

#le unfunny script
def funky(z,y,u):
    x=0
    r=0
    i=0
    if u==1 : 
        r=(0,0,0)
        i=(255,255,255)
    if u==2 :
        r=(255,255,255)
        i=(0,0,0)
    y=y*100 #why the fuck does it doesn't work anymore 
    
    for _ in range(6):
        bl=pygame.Rect (x,y,100,100)
        pygame.draw.rect(window,r,bl)
        x=x+100#like this should work, irght ?
        b=pygame.Rect (x,y,100,100)
        pygame.draw.rect(window,i,b)
        x=x+100

pygame.display.update()
funky(1,1,0)
#locknstuff
lock = True #verrou(?)
while lock:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            lock=False
pygame.quit()