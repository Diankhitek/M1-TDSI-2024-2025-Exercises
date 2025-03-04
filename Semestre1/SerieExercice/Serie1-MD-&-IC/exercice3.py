"""
Dictionnaires : Création et Modification
Crée un dictionnaire contenant ces informations :
personne = {"nom": "Alice", "âge": 25, "ville": "Paris"}
Affiche l'âge de la personne.
Modifie l’âge d’Alice pour 26 ans.
Ajoute une nouvelle clé "profession" avec la valeur "Ingénieur".
Supprime la clé "ville".
Affiche le dictionnaire mis à jour.
Crée un dictionnaire contenant ces informations :
Affiche toutes les clés du dictionnaire.
Affiche toutes les valeurs du dictionnaire.
"""

personne = {"nom": "Alice", "age": 25, "ville": "Paris"}
print(f"Age de la personne : {personne['age']}")
personne["age"] = 26
print(f"Age de la personne modif.: {personne['age']}")
personne["profession"] = "Ingénieur"
print(f"Profession de la personne : {personne['profession']}")
del personne["ville"]
# print(f"Ville de la personne : {personne['ville']}")
print(f"Dictionnaire contenant ces informations : {personne}")

print(personne.keys())
print("Méthode 1 :")
for i in personne:
    print(f"{i} : {personne[i]}")

print("méthode 2 :")
for key,value in personne.items():
    print(f"{key} : {value}")


