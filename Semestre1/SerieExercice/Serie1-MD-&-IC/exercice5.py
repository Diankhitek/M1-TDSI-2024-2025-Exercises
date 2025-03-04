"""
Boucles et Conditions
Demande à l’utilisateur d’entrer un nombre entier n.
Calcule et affiche la somme des nombres pairs de 1 à n.
Génère un nombre aléatoire entre 1 et 20. (Utilise random.randint(1, 20))
Demande à l’utilisateur de deviner ce nombre.
Affiche "Trop grand" ou "Trop petit" jusqu'à ce qu'il trouve la bonne réponse.
"""
import random

nombre = int(input("Entrer un nombre entier: "))
compt = 0
for i in range(nombre+1):
    if i % 2 == 0:
        compt += i
print(f"La somme des nombres pairs de 1 à {nombre} = {compt}")

nombre_aleatoire = random.randint(1, 20)
nombre_deviner = int(input("Essayer de deviner le nombre: "))
while nombre_deviner != nombre_aleatoire:
    if nombre_deviner < nombre_aleatoire:
        print("Trop petit")
    else :
        print("Trop grand")
    nombre_deviner = int(input("Essayer de deviner le nombre: "))
print("Trouvé !!!!")
