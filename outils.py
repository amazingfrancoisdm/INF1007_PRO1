import random
import os
import time
from util import lire_historique_utilisateur, enregistrer_partie, lire_dictionnaires_mots

def validerNom(name):  
    if len(name)>=3:
        for n in name:
            if not (65 <= ord(n) <= 90 or 97 <= ord(n) <= 122):
                return False   
        return True
    else:
        return False

def choisirMot(mots):
    index = random.randrange(len(mots)-1)
    print(mots[index])
    return mots[index]

def effacerConsole():
    os.system('cls' if os.name == 'nt' else 'clear')


def afficherMot(lettres_trouvees, mot):
    txt = []
    for i in range(len(mot)):
        txt.append("_")

    for i in range(len(lettres_trouvees)):
        for j in range(len(mot)):
            if mot[j] == lettres_trouvees[i]:
                txt[j] = lettres_trouvees[i]
    
    print("Mot: " + " ".join(txt))


def afficherJeu(lettres_ratees, lettres_trouvees, mot):
    effacerConsole()
    afficherMot(lettres_trouvees, mot)
    print("Lettres trouvees: " + " ".join(lettres_trouvees))
    print("Lettres ratees: " + " ".join(lettres_ratees)+"\n") 

    parties = [
    ["   0   |", "       |", "       |"],
    ["   0   |", "   |   |", "       |"],
    ["   0   |", "  /|   |", "       |"],
    ["   0   |", "  /|\  |", "       |"],
    ["   0   |", "  /|\  |", "  /    |"],
    ["   0   |", "  /|\  |", "  / \  |"]
    ]

    partie_a_afficher = parties[len(lettres_ratees)-1] if len(lettres_ratees) > 0 else ["       |", "       |", "       |"]

    print("   +---+")
    print("   |   |")
    print("\n".join(partie_a_afficher))
    print("       |")
    print("==========")
    

def validerLettre(lettres_ratees, lettres_trouvees, mot):

    lettre = input("Entrez une lettre: ")

    if (len(lettre) != 1) or not (65 <= ord(lettre) <= 90 or 97 <= ord(lettre) <= 122):
        print("Vous devez entrer une lettre.")
    else:
        lettre_contenue = mot.find(lettre)

        if (lettre in lettres_ratees) or (lettre in lettres_trouvees):
            print("Cette lettre a déjà été essayée.")
        elif lettre_contenue == -1:
            lettres_ratees.append(lettre)
            afficherJeu(lettres_ratees, lettres_trouvees, mot)
        else:
            lettres_trouvees.append(lettre)
            afficherJeu(lettres_ratees, lettres_trouvees, mot)


def etatDeLaPartie(lettres_ratees, lettres_trouvees, mot, nom, temps_debut):
    temps = round(time.time()-temps_debut)

    if len(lettres_ratees) == 6:
        print(f"Dommage ! Le mot était {mot}.")
        input("Appuyez sur entrer pour continuer...")
        lettres_trouvees.clear()
        lettres_ratees.clear()
        enregistrer_partie(nom, mot, False, temps)
        effacerConsole()
        return True
    elif len(lettres_trouvees) == len(set(mot)):
        print(f"Félicitations {nom} ! Vous avez deviné le mot {mot} en {temps} secondes et {len(lettres_ratees)} tentatives échouées.")
        input("Appuyez sur entrer pour continuer...")
        lettres_trouvees.clear()
        lettres_ratees.clear()
        enregistrer_partie(nom, mot, True, temps)
        effacerConsole()
        return True
    else:
        return False
    

def game(lettres_ratees, lettres_trouvees, mot,nom):
    fin_de_partie = False

    afficherJeu(lettres_ratees, lettres_trouvees, mot)
    start = time.time()
    while not fin_de_partie:
        print(mot)
        validerLettre(lettres_ratees, lettres_trouvees, mot)
        fin_de_partie = etatDeLaPartie(lettres_ratees, lettres_trouvees, mot, nom, start)
        

def lecture(nom):
    effacerConsole()
    parties = lire_historique_utilisateur(nom)

    print("Historique des parties:")

    for i in range(len(parties)):
        victoire = "gagné" if parties[i]["resultat"] == True else "perdu"
        print("\t"+ parties[i]["mot"] + f" - {victoire} - " + str(parties[i]["duree"]) + " secondes")

    input("Appuyez pour continuer...")
    effacerConsole()