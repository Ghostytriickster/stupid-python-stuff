## CORRECTION ## Les corrections suivantes sont précédées du commentaire ## CORRECTION ## pour vous permettre de les trouver plus facilement

#fichier python fait sur vim, vu que ni vscode ni thonny ne veut marcher sur mon installation windows pro....
##exercice 2
#print (2**53==2**53+1) #affiche false car 2^53 et 2^53+1 d้passent 52 mais ne sont pas compt้s en bits ## CORRECTION ## Comment ça comptés en bits ?
#print (2.**52==2.**52+1)#affiche false car 2. est flottant, or les valeurs sont comprise dans 52 bits
#print (2.**53==2.**53+1)#affiche true, car 2. est flottant, or 2.^53 et 2.^53+1 d้passent les 52 bits de la mantisse, et la valeur s'arrete au bout des 52 bits.

##exercice 4 #uhhhhh 
#def foo(n) :
#   if n%2==0 :
#    m = n/2
#   else :
#   m= 3*n+1
#   return m

#a = 5
#a = foo(a)
#print(a) 
#foo(a)
#print(a) 
#็a affiche 16.... et 16 ????? ah, c'est return qui fait ็a non ?## CORRECTION ## entre autre oui : le return donne une nouvelle valeur à a en ligne 18


##exercice 5
## CORRECTION ## ATTENTION : j'ai dû refaire toutes tes indentations auxquelles il manquait un espace à chaque fois
##bon je vais pas recopier le cod... si.## CORRECTION ## si parce qu'il va te servir ensuite !
def est_premier(n):
    d=2
    while d<n:
        if n%d==0:       
            return False
        d=d+1
        print("bong bong, ็a fait un tour")## CORRECTION ## c'est bien d'avoir laissé ça, ça fait office de compteur, c'est ce qu'il fallait faire ! Mais il fallait le
                                          ## CORRECTION ## mettre avant le return parce que sinon quand c'est False, ça ne compte pas le tour alors qu'il existe
    return True
#la boucle while tourne trois fois et ensuite renvoie False
## CORRECTION ## non ça fait 4 tours de boucle :(


##exercice 6 
##"no syntax highlighting, no proper formatting, truly what it felt like to write C in 1991" merci bob.
## CORRECTION ## Mais alors pourquoi tu as laissé le code en commentaire ?
#def aire_trapeze(a,b,h):
#   aire=((a+b)*h)/2
#   print(aire)
## CORRECTION ## un return est demandé :(


##exercice 7 

##ourf
#from math import sqrt ## CORRECTION ## à mettre en haut de préférence
#def aire_triangle(a,b,c):
#   p=(a+b+c)/2
#   A=sqrt(p*(p-a)*(p-b)*(p-c)
#   print(A)
## CORRECTION ## un return est demandé

##exercice 9... ENFIN
## CORRECTION ## Bravo pour les efforts que tu as faits pour cet exercice, tu as la bonne logique
## CORRECTION ## J'estime que tu as beaucoup progressé sur le fait d'organiser tes pensées, peu d'élèves ont bien fait cet exercice

## CORRECTION ## c'est bien d'avoir fait une fonction pour ça !
## CORRECTION ## tu aurais pu nommer la variable de retour autrement, ça prête à confusion
def f(n):
    n=n**2-n+41
    return (n)
def premierjusquax(x):
    n=0
    max=x## CORRECTION ## ça ne sert pas à grand chose, tu aurais pu appelé le paramètre max dans ce cas
    while n<max:
        print(est_premier(f(n))) #beurk
        ## CORRECTION ## ok mais regarde bien la correction stp !
        n=n+1
##donc en premier on fait 40, tout est "True"
##ensuite 100.... 14 nombres non premiers.

#thonny va suremement pas aimer l'encodage excusez moi.... ## CORRECTION ## en fait ce n'est paas "l'encodage" ! Il faut juste que
                                                           ## CORRECTION ## tu règles les tab de vim sur 4 espaces ou que tu fasses 4 espaces à chaque fois 
#mais vim devrais marcher...
#au moins cette fois il n'ya pas de "mega code bloaté de fou"... ## CORRECTION ## oui, c'est bien ça ! Mais n'écris pas bloat au bac hein :D

## CORRECTION ## Merci pour cet instant de poésie ¯\_(ツ)_/¯
## CORRECTION ## Effectivement je me suis retenur=e de raconter a en cours parce que ça n'intéresse pas beaucoup de monde
## CORRECTION ## Tu savais que GNU était un acronyme récursif ? Je te laisse avec ça.
        
#I'd just like to interject for a moment. 
#What you're referring to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux. 
#Linux is not an operating system unto itself, 
#but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, 
#shell utilities and vital system components comprising a full OS as defined by POSIX.
#Many computer users run a modified version of the GNU system every day, without realizing it. 
#Through a peculiar turn of events, the version of GNU which is widely used today is often called "Linux", 
#and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.
#There really is a Linux, and these people are using it, but it is just a part of the system they use. 
#Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. 
#the kernel is an essential part of an operating system, but useless by itself;
#it can only function in the context of a complete operating system.
#Linux is normally used in combination with the GNU operating system: 
#the whole system is basically GNU with Linux added, or GNU/Linux.
#All the so-called "Linux" distributions are really distributions of GNU/Linux.