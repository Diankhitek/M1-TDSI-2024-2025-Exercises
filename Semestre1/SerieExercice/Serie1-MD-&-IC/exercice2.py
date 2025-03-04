"""Listes : Manipulation et Parcours
Crée une liste avec ces éléments : ["pomme", "banane", "orange", "kiwi"].
Ajoute "fraise" à la fin de la liste.
Supprime "orange".
Trie la liste par ordre alphabétique. (Ne pas utiliser sort (), sorted ())
Affiche la liste modifiée."""

liste_fruit = ["pomme", "banane", "orange", "kiwi"]
liste_fruit[len(liste_fruit):] = ["fraise"]
print("Affichage de la liste aprés ajout : "+str(liste_fruit))
liste_fruit.remove("orange")
print("Liste aprés supp. 'orange': "+str(liste_fruit))

for i in range(len(liste_fruit)):
    for j in range(i,len(liste_fruit)):
        if liste_fruit[i] >  liste_fruit[j]:
            liste_fruit[i],liste_fruit[j] = liste_fruit[j],liste_fruit[i]
print("Liste aprés tri : "+str(liste_fruit))

dictionnaire_alphabet = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D',
                         'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H',
                         'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L',
                         'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P',
                         'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
                         'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X',
                         'y': 'Y', 'z': 'Z'}

for i in range(len(liste_fruit)):
    fruit = liste_fruit[i]
    fruit_maj = ""
    for letter in fruit:
        if letter in dictionnaire_alphabet:
             fruit_maj+= dictionnaire_alphabet[letter]
        else:
            fruit_maj+= letter
    liste_fruit[i] = fruit_maj
print("La liste maj. : "+str(liste_fruit))


