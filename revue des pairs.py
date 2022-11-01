#Créer une calculatrice pour fractions incluant les opérations suivantes: 
 #Addition (a/b + d/c)
 #Soustraction (a/b - d/c)
 #Multiplication (a/b * d/c)
 #Divisions (a/b / d/c)
def calculatrice(n1, n2, n3, n4):
    Addition = (n1 / n2) + (n3 / n4)
    Soustraction = (n1 / n2) - (n3 / n4)
    Multiplication = (n1 / n2) * (n3 / n4)
    Division = (n1 / n2) / (n3 / n4)
    return Addition, Soustraction, Multiplication, Division

# Exercice 1, Partie 2:

#Écrivez vos fonctions de sorte qu'ils ne prennent que deux termes. Ex: fct(fraction1, fraction2).

def termes(fraction1, fraction2):
    Addition = fraction1 + fraction2    
    Soustraction = fraction1 - fraction2
    Multiplication = fraction1 * fraction2
    Division = fraction1 / fraction2
    return Addition, Soustraction, Multiplication, Division 

# Exercice 1, Partie 3:

#Affichez vos résultats sous forme de fraction et sous forme d'un float.
