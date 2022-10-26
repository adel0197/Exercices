# Créer une fonction prenant en paramètre l'année de naissance d'une personne et lui retournant son l'âge qu'elle aura à sa fête en 2022.
def age(année_naissance ):
    calcul= 2022 - année_naissance
    return calcul

# Créer une fonction prenant 2 nombres en paramètre et retournant leur addition et soustraction.
def fonction(n1, n2):
    addition = n1 + n2
    soustraction = n1 - n2
    return addition, soustraction
    
# Créer une fonction prenant 1 ou 2 nombres et effectuer l'addition de leur carré. 
# Si un seul nombre est passé en paramètre, assumez que la valeur par défaut est 1.
def fonction(n1, n2= 1):
    calcul = (n1**2) + (n2**2)
    return calcul

# Créer une fonction prenant trois nombres et retournant la moyenne de leur carré + 1.

# Ensuite, ecrire une nouvelle fonction pour retourner la moyenne de leur cube + 2.

# Finalement retournant la moyenne de la fonction suivante: x^x + x + 3, pour les 3 nombres.
def carre(n):
    return n ** 2
def cube(n):
    return n ** 3
def fct(n):
    return n ** n + n + 3
def moy(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def resultats(n1, n2, n3):
    
    moy_carre = moy(carre(n1), carre(n2), carre(n3)) + 1
    moy_cube = moy(cube(n1), cube(n2), cube(n3)) + 2
    moy_fct = moy(fct(n1), fct(n2), fct(n3))
    return moy_carre, moy_cube, moy_fct 

# Créer une fonction prenant 4 paramètres et retournant la somme des deux premiers multipliés par le 3ième et divisé par le 4ème.
def fonction(n1, n2, n3, n4):
    calcul = ((n1 + n2) * n3) / n4 
    return calcul 
# Créer une fonction qui calcule la moyenne de 4 paramètre et qui retourne aussi la somme de ces 4 paramètres.
def fonction(n1, n2, n3, n4):
    somme = n1 + n2 + n3 + n4
    moy =  (n1 + n2 + n3 + n4) / 4
    return somme, moy 
# Créer une fonction qui permet de calculer la fonction suivante: (x + y) / z.
 #Essayer avec z = 0.    

def fonction(n1, n2, n3 = 0): 
    calcul = (n1 + n2) / n3 
    return calcul

# Créer une fonction prenant un seul paramètre retournant le modulo de deux nombres(a modulo b).

# Créer une fonction permettant de faire la puissance d'un nombre pour ensuite en faire la division. 
# Votre fonction doit prendre de 1 à 3 paramètres, le premier paramètre étant la base, le deuxième paramètre étant l'exposant et le troisième paramètre étant la division.
# Si aucun exposant n'est donné, faites le carré. Si aucun diviseur n'est donné, n'effectuez pas de division.

def fonction( n1, n2 = 1, n3 = 1):
    calcul = (n1**n2) / n3  
    return calcul 



