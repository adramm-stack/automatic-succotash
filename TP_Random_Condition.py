#TP1 Python Openclassroom

import os
from random import randrange
from math import ceil


argent = 1000 
continuer = True 

print(argent, "€.")

# Choisir un nombre
while continuer : 
    nombre_mise = -1
    while nombre_mise < 0 or nombre_mise > 49:
        nombre_mise = input("Tapez le nombre sur lequel vous voulez miser (entre 0 et 49) : ")
        try:
            nombre_mise = int(nombre_mise)

# Erreur possible lors de la saisie du nombre
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            nombre_mise = -1
            continue
        if nombre_mise < 0:
            print("Nombre négatif")
        if nombre_mise > 49:
            print("Nombre supérieur à 49")

# Sélection de la somme à miser
    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Montant de la mise : ")
        try:
            mise = int(mise)
        except ValueError:
            print("Aucun nombre saisi")
            mise = -1
            continue
        if mise <= 0:
            print("La mise est négative ou nulle.")
        if mise > argent:
            print("Vous n'avez pas assez d'argent")

#Random
    numero_gagnant = randrange(50)
    print("La roulette s'arrête sur le numéro", numero_gagnant)

# Gain
    if numero_gagnant == nombre_mise:
        print("Vous obtenez", mise * 2, "€ !")
        argent += mise * 2
# Sinon si même couleur
    elif numero_gagnant % 2 == nombre_mise % 2: 
        mise = ceil(mise * 0.5)
        print("Bonne couleur. Vous obtenez", mise, "€ !")
        argent += mise
# Sinon
    else:
        print("Vous perdez votre mise. :(")
        argent -= mise

# Si argent inférieur ou égal à 0
    if argent <= 0:
        print("Game Over")
        continuer = False

# Afficher argent  
    else:
        print("Vous avez à présent", argent, "$")
        quitter = input("Quitter la partie ? (o/n)")
        if quitter == "o":
            continuer = False

# Pause du système
os.system("pause")