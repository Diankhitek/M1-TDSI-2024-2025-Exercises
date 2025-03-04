"""Tuples : Immutabilité et Manipulation
Crée un tuple contenant les nombres de 1 à 5.
Affiche le premier et le dernier élément du tuple.
Essaie de modifier un élément du tuple et observe l'erreur.
Convertis le tuple en liste, modifie un élément, puis reconvertis-le en tuple."""

tuple_nbre = (1,2,3,4,5)
print("Premier Nombre : ", tuple_nbre[0])
print("Dernier Nombre : ", tuple_nbre[-1])

"""Le dernier élément du tuple ne peut pas etre modifier car un tuple est immuable"""
tuple_to_list = list(tuple_nbre) # conversion du tuple en liste
print("Liste initial  :", tuple_to_list) #affcihage de la liste avant modfication
tuple_to_list[1] = 6 # modification de la valeur à la position 1 en 6
print("Liste modifiée :", tuple_to_list) # affichage de la liste aprés modification
list_to_tuple = tuple(tuple_to_list)
print("Tuple aprés modif:", list_to_tuple) # affichage du tuple
