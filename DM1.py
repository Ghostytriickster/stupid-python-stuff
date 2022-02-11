#1
#a
un_mot = "camembert"
print(un_mot)
un_mot_inverse = un_mot[::-1] #HOW, no serieusement, comment c'est fait ???
print(un_mot_inverse)
#mmm trebmemac n'est pas un palindrome, comme c'est bizarre.... (non)
#b
n = 12345 # un entier
n_chaine = str(n)
n_chaine_inverse = n_chaine[::-1] # une chaîne de caractères
print(n_chaine_inverse)
m = 12321
m_chaine_inverse = str(m)[::-1] # une chaîne de caractères
print(m_chaine_inverse)
m == m_chaine_inverse # observer que ça ne fonctionne pas
str(m) == m_chaine_inverse # observer que ça fonctionne
#ben 12345 n'est pas un palindrome, mais 12321 en est un

#c (AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA)
def est_un_palindrome(z):
    z_chaine = str(z)
    z_chaine_inverse = z_chaine[::-1] # une chaîne de caractères
    if z_chaine_inverse == z_chaine :
        print (z,"est un palindrome")
    else :
        print(z,"n'est pas un palindrome") #rrr comment on est sensé renvoyer un booléen
#2
def toutlespalindromesde10000a99999(_):
    t=0
    for y in range(10000,100000) :
        y_chaine = str(y) 
        y_chaine_inverse = y_chaine[::-1] #euuuhhhhhh
        if y_chaine_inverse == y_chaine:
            print (y_chaine) #ok ça marche, mais faudra que je le transforme en liste, j'ai oublié comment on fait et on l'a pas vu en cour. en plus c'est même pas ce qui est demandé
            t=t+1
    print ("il y a", t,"palindromes a 5 chiffres")
#3 pain 2 : electric boogaloo
#ok donc ça c'est le machin qu'on a vu a la fin d'un cour
#doonc
def AAAAA(_) :
    for h in range (100,1000):
        for r in range (100,1000):
            a=h*r #j'ai changé + par * et maintenant ça marche plus.... AAAAAAAAAAAAAAAAAAAA
        a_chaine=str(a)
        a_chaine_inverse = a_chaine[::-1]
        if a_chaine_inverse==a_chaine :
            print (a_chaine)
#        I I I I,
#    |'-----'|
#       |       |
#     '-----'
#       I I I I
#       I I I I
#       I I I I
#       I I I I
#       I I I I  RBMK fuel rod yay
#       I I I I
#       I I I I
#   |'-----'|
#       |       |
#    '-----'
#      I I I I

   