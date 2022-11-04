# Exercice 1:


# Créez un programme demandant à un utilisateur d'entrer un entier et retournez-lui le carré. 
# Si le nombre est positif, retournez-lui aussi la racine carrée.
def fonction_exercise1():
    user_input = int(input('Entrez un nombre entier à mettre au carré: '))
    if user_input > 0:
        return user_input ** 2, user_input ** 0.5
    else:
        return user_input ** 2
    
def calcul_valeur():
    valeur = int(input("Entrez votre nombre : "))
    if valeur > 0 : 
        return valeur * valeur, valeur ** 0.5
    return valeur * valeur

def calcul_valeur2():
    valeur = int(input("Entrez un nombre entier a mettre au valeur et racine: "))
    resultat = valeur ** 2
    if valeur > 0:
        resultat = valeur ** 2, valeur ** 0.5
    return resultat

# print(fonction_exercise1())
# print(calcul_valeur())
# print(calcul_valeur2())

# Exercice 2:

# Créez un programme demandant à l'utilisateur un animal, une couleur et un lieu et retournez-lui la phrase suivante: 
# J'ai trouvé un (nom de l'animal) de couleur (nom de la couleur) dans mon lieu préféré: (nom du lieu). 
# Implémentez la fonction de sorte qu'elle ne prenne qu'un seul paramètre pour représenter les trois mots de l'utilisateur.

def recupererinfosanimal():
    nom_animal = input("Entrer un nom d'animal: ")
    couleur_animal = input("Entrer une couleur: ")
    lieu_prefere = input("Entrer un lieu: ")
    infos_animal = nom_animal, couleur_animal, lieu_prefere
    return infos_animal
#;gt >
def formatageinfosanimal():
    nom, couleur, lieu = recupererinfosanimal()
    return f" J'ai trouvé un {nom} de couleur {couleur} dans mon lieu préféré: {lieu} "#.format()
    
# print(formatageinfosanimal())

def user_infos_animal():
    nom_animal = input("Entrer un nom d'animal: ")
    couleur_animal = input("Entrer une couleur: ")
    lieu_prefere = input("Entrer un lieu: ")
    infos_animal = nom_animal, couleur_animal, lieu_prefere
    return infos_animal

def formatage_infos_animal(infos):
    nom, couleur, lieu = infos
    return f" J'ai trouvé un {nom} de couleur {couleur} dans mon lieu préféré: {lieu} "#.format()
    
# infos = user_infos_animal()
# infos_f = formatage_infos_animal(infos)
# print(infos_f)

# print(formatage_infos_animal(user_infos_animal()))
# Exercice 3:

# Créez un programme demandant à un utilisateur d'entrer sa date de fête, si la date est le 31 octobre, 
# affichez un message souhaitant bonne fête à l'utilisateur, sinon affichez le message suivant: 
# Ce n'est pas ta fête aujourd'hui :(.

def date_de_fête():

    #Faire deux inputs (1 pour le jour, 1 pour le mois)
    date = input("Entrer votre date de fête(jour mois Ex: 13 avril): ")
    #31 octobre
    #09/31
    #09 - 31
    #October 31st
    if date == "31 octobre":
        return "bonne fête"
    else :
        return "ce n'est pas ta fête aujourd'hui"

#print(date_de_fête())

def fete():
    mois = int(input("Entrer votre mois de fête en nombre(avril=4): "))
    jour = int(input("Entrer votre jours de fête: "))

    jour_a = dt.datetime.today().day
    mois_a = dt.datetime.today().month

    
    if jour == jour_a and mois == mois_a:
        print("Bonne fête!")
    else:
        print("Ce n'est pas ta fête aujourd'hui! :(")  
        # Exercice 4:

# Créez un programme demandant à un utilisateur d'entrer sa date de fête et retournez-lui sa saison de naissance s'il 
# est né dans l'hémisphère Nord. (Vous pouvez assumer que les équinoxes et solstices ont lieu le 21 du mois.)

def saison_de_fete_detector():
    jour_user = int(input('Entrer votre jour de naissance (ex: 15): '))
    mois_user = int(input('Entrer votre mois de naissance (ex: avril = 4 ou 04): '))

    if 1 <= jour_user <= 31 and 1 <= mois_user <= 2:
        print('Vous etes née en hiver ! ')
    elif 22 <= jour_user <= 31 and mois_user == 12 :
        print('Vous etes née en hiver ! ')
    elif 1 <= jour_user <= 21 and  mois_user == 3:
        print('Vous etes née en hiver ! ')

    elif 22 <= jour_user <= 31 and mois_user == 3 :
        print('Vous etes née au printemps ! ')
    elif 1 <= jour_user <= 31 and 4 <= mois_user <= 5:
        print('Vous etes née au printemps ! ')
    elif 1 <= jour_user <= 21 and  mois_user == 6:
        print('Vous etes née au printemps ! ')

    elif 22 <= jour_user <= 31 and mois_user ==  6:
        print('Vous etes née en été ! ')
    elif 1 <= jour_user <= 31 and 7 <= mois_user <= 8:
        print('Vous etes née en été ! ')
    elif 1 <= jour_user <= 21 and  mois_user == 9:
        print('Vous etes née en été ! ')
    
    elif 22 <= jour_user <= 31 and mois_user == 9 :
        print('Vous etes née en automne ! ')
    elif 1 <= jour_user <= 31 and 10 <= mois_user <= 11 :
        print('Vous etes née en automne ! ')
    elif 1 <= jour_user <= 21 and  mois_user == 12 :
        print('Vous etes née en automne ! ')

    else :
        print('Erreur')

saison_de_fete_detector()
# Exercice 5:

# Créez une fonction demandant à un utilisateur un nombre pair et un nombre impair, une fonction 
# permettant de vérifier que les nombres ne sont pas les deux pairs ou impairs, et affichez la phrase 
# suivante: Votre nombre impair est le x, votre nombre pair est le y et le résultat de leur division est égal à z. 
# Vous ne devez qu'afficher 3 chiffres après le point.

def pairs_impairs():
    nombre_utilisateur_1 = int(input("Veuillez entrer un nombre impair: "))
    nombre_utilisateur_2 = int(input("Veuillez entrer un nombre pair: "))
    if nombre_utilisateur_1 % 2 == 0:
        if nombre_utilisateur_2 % 2 == 0:
            print("Vos 2 nombres sont pairs.")
            return
        else:
            print(f"Pair: {nombre_utilisateur_1}, Impair: {nombre_utilisateur_2} Resultat: {nombre_utilisateur_1/nombre_utilisateur_2}")
    elif nombre_utilisateur_2 % 2 == 0:
        print(f"Pair: {nombre_utilisateur_2}, Impair: {nombre_utilisateur_1} Resultat: {nombre_utilisateur_1/nombre_utilisateur_2}")
    else:
        print("Vos 2 nombres sont impairs.")

pairs_impairs()

# Exercice 6:

# En partant de l'exercice du système de géolocation, modifiez votre code pour que les
#  positions en DMS incluent la direction cardinale(N, S, E, W ou O) et retourne une position en DD pouvant être négative. 
# Modifiez ensuite votre code pour permettre à un utilisateur de manuellement rentrer sa position.

#import math
#import random

def dms_to_dd(dms):
    degres, minutes, secondes, direction = dms
    coefficient = 1
    if direction == "S" or direction == "W" or direction == "O":
        coefficient = -1
    return coefficient * (degres + minutes/60 + secondes/3600)

def distance_2_point(position1, position2):
    x1, y1 = position1
    x2, y2 = position2
    return ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5
    #math.sqrt()

def distance_pole_nord(position):
    POLENORD_LAT = 86.494
    POLENORD_LONG = 162.867
    POLE_NORD = POLENORD_LAT, POLENORD_LONG

    lat, long = position
    lat_dd = dms_to_dd(lat)
    long_dd = dms_to_dd(long)
    position_dd = lat_dd, long_dd

    return distance_2_point(position_dd, POLE_NORD)

longitude = 45, 30, 31.9968, "S"
latitude = 73, 33, 42.0048, "W"
position = longitude, latitude

dist = distance_pole_nord(position)
print(dist) 

  
   