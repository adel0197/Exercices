def operation(a, b, c=7):
    somme= a + b + c 
    soustraction= b - c
    produit= a * b
    return somme, soustraction, produit
print(operation(5,2,8))    
print(operation(5,2))
