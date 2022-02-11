#imports
import time
#are you coding son 
def diviseur(x):
    o=1
    n=0
    for i in range(x):
        if x%o==0:
            print(o)
            n=n+1
        o=o+1
    print("nombre de diviseurs:",n)
    if n==2:
        print(x,"est premier!")

###################################################################################################
def premier(x):
    o=1
    n=0
    for i in range(x):
        if x%o==0:
            n=n+1
        o=o+1
    if n==2:
        print(x,"est premier!")
    else:
        print(x,"n'est pas premier")
###################################################################################################
#def fermat(x):
####    x=2**2**x+1
#   premier(x) don't work and is totally useless, its not even used in the exercises
###################################################################################################
def timer(seconds): #we don't talk about that
    print("début chrono",seconds,"s")
    for i in range(seconds):
        time.sleep(1)
        seconds -=1
    if seconds ==0:
        print("fin") #dumb piece of trash made for fun
####################################@###############################################################################
