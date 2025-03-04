"""
Demande à l’utilisateur d’entrer son nom.
Affiche le nom en majuscules et en minuscules. (Sans utiliser upper ni lower)
Affiche la longueur du nom.
"""

dictionnaire_alphabet = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D',
                         'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H',
                         'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L',
                         'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P',
                         'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
                         'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X',
                         'y': 'Y', 'z': 'Z'}

dictionnaire_alphabet2 = {'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e',
                          'F':'f', 'G':'g', 'H':'h', 'I':'i', 'J':'j',
                          'K':'k', 'L':'l', 'M':'m', 'N':'n',
                          'O':'o', 'P':'p', 'Q':'q', 'R':'r',
                          'S':'s', 'T':'t', 'U':'u', 'V':'v',
                          'W':'w', 'X':'x', 'Y':'y', 'Z':'z'}


print("Saisir votre nom :")
nom = input()
# prenom = input("Saisir votre prenom :")
# age = input("Saisir votre age :")
print("Nom initial:", nom)
# print("Prenom :", prenom)
# print("Age :", age)
# print(f"Age Année prochaine : {int(age)+1}")


nom_maj = ""
for letter in nom:
    if letter in dictionnaire_alphabet:
        nom_maj += dictionnaire_alphabet[letter]
    else:
        nom_maj += letter
nom = nom_maj
print("Nom en maj. : ", nom)


# ---- Méthode 1 ----
nom_minus = ""
for letter in nom:
    if letter in dictionnaire_alphabet2:
        nom_minus += dictionnaire_alphabet2[letter]
    else:
        nom_minus += letter
print("Nom en minus. :", nom_minus)

# ---- Methode 2 ----
nom_minus2 = ""
for letter in nom:
    nom_minus2 += dictionnaire_alphabet2.get(letter, letter)
print("Nom en minus2. :", nom_minus2)

"""
Étant donné la liste suivante :
nombres = [10, 23, 45, 66, 75, 90, 101]
Crée une nouvelle liste contenant uniquement les nombres pairs.
Affiche la liste filtrée."""


nombres = [10, 23, 45, 66, 75, 90, 101]
nombre_pair = []
for nombre in nombres:
    if nombre % 2 == 0:
        nombre_pair += [nombre]
print("la liste des nombres pairs :", nombre_pair)