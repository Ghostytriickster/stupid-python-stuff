import pygame
pygame.init
size = (600,400)
window = pygame.display.set_mode(size)

#colors
black=(0,0,0)
white=(255,255,255)
gray=(128,128,128)
window.fill(white)
#script de couleur pour la fenêtre
x=1
for _ in range(10):
    x=x+30
    b=pygame.Rect (x,1,30,30)
    pygame.draw.rect(window ,black,b)                  
    pygame.display.updatelocknstuff

lock = True #verrou(?)
while lock:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            lock=False
pygame.quit()