from turtle import *
from math import pi
try:
    reset ()
except Terminator:
    pass
setup (500,500)
speed(-10)
#n=nombre de coté, c=longueur coté.
#on fait (360,((r*2*pi)/360)) et on a un cercle ! 
def polygone (n,c):
    for _ in range (n):
        fd(c)
        right(360/n)
#r=rayon
def cercle (r):
    fd(2*r)
    right(90)
    for _ in range (360):
        fd((r*2*pi)/360)
        right(360/360)
#espacement de visibilité
def rosace (n,c):
    for  _ in range (n):
        polygone (n,c)
        right (360/n)
#polygone (360,((100*2*pi)/360))
def losange (c,a):
    for _ in range (2):
        fd(c)
        left(a)
        fd(c)
        left(180-a)
def HT (c):
    for _ in range(12):
        a=15
        for _ in range (11):
            losange(c,a)
            left(a)
            fd(c)
            right(a)
            a=a+15
        for _ in range (11):
            right(15)
            fd(c)
        right(180)
        fd(c)
        left(15)
HT(32)
mainloop()