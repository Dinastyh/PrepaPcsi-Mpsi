
import Stack

#Basic arithmetique

def power(elm, n):
    """
    Renvoie la puissance elm puissance n sans utiliser de boucle ni de recussivité
    """
    pass


def modulo(elm, n):
    """
    Renvoie le modulo de elm par n sans utiliser de boucle 
    """
    pass


#Basic List

def switch(i, n, l):
    """
    Tu dois echanger les elements ieme et nieme de la liste
    Renvoie True si l'operation est effectuée avec succes
    False si c'est impossible
    Interdiction de passer par une variable intermediaire
    """
    pass


def getI(l, i):
    """
    Tu dois ici renvoyer le ieme element de la liste i
    On ne testera pas ici un cas où i est hors de la liste
    """
    pass


def checkIn(elm, l):
    """
    Tu dois ici faire une fonction qui verifie si l'element elm
    est dans la list -> conseil regarde l'utilisation du mot clef in
    Si il est présent renvoit True
    Si il est absent renvoit False
    """
    pass


def addEnd(elm, l):
    """
    Tu dois ici faire une fonction qui ajoute en fin de la liste
    l'element elm
    """
    pass


def addI(elm, l, i):
    """
    Tu dois faire ici une fonction qui ajoute a la place i de la liste
    l'element elm
    Si c'est impossible renvoie False
    Si c'est possible renvoie True
    Conseil -> regarde la fonction insert
    """
    pass


def findElm(elm, l):
    """
    Tu dois trouver l'index de l'element elm dans la liste
    Si il y est tu renvoies l'index
    Sinon tu renvoies -1
    """
    pass


def fusion(l1, l2):
    """
    Tu dois fusionner les deux listes dans l1
    """
    pass


#Basic pile

#Pour creer une pile: s = Stack.Stack()
#Pour ajouter: s.push()
#Pour retourner le premier element de la pile sans retirer le premier element: s.peek()
#Pour retourner le premier element de la pile en le retirant de la pile: s.pop()
#Pour verifier si la pile est vide: s.isEmpty()

def reverse(l):
    """
    Retourne une nouvelle liste inverse de l en utilisant une pile
    """
    pass


def buildString(s):
    """
    Retourne un string composé de tous les elements de la pile espacé d'espace
    """
    pass


#Bonus

def power2(n):
    """
    Renvoie la puissance n de 2 sans utiliser les operateurs de puissance
    ni les boucles
    Conseil -> Regarder Bitwise python (Fonction non obligatoire)
    """
    pass
