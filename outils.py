import random
import os
import time
from util import lire_historique_utilisateur, enregistrer_partie, lire_dictionnaires_mots


# TODO Ajuster la verification du nom avec isAlpha
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

# TODO Condition pour ne pas refaire la meme loop a chaque fois
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

    parties_jouees = [
    ["   0   |", "       |", "       |"],
    ["   0   |", "   |   |", "       |"],
    ["   0   |", "  /|   |", "       |"],
    ["   0   |", "  /|\  |", "       |"],
    ["   0   |", "  /|\  |", "  /    |"],
    ["   0   |", "  /|\  |", "  / \  |"]
    ]

    partie_a_afficher = parties_jouees[len(lettres_ratees)-1] if len(lettres_ratees) > 0 else ["       |", "       |", "       |"]

    print("   +---+")
    print("   |   |")
    print("\n".join(partie_a_afficher))
    print("       |")
    print("==========")
    
# TODO Revisiter la fonction pour voir si on peut simplifier ca
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

    partie_terminee = False

    if len(lettres_ratees) == 6:
        print(f"Dommage ! Le mot était {mot}.")
        partie_terminee = True
        
    elif len(lettres_trouvees) == len(set(mot)):
        print(f"Félicitations {nom} ! Vous avez deviné le mot {mot} en {temps} secondes et {len(lettres_ratees)} tentatives échouées.")
        partie_terminee = True
    
    if partie_terminee:
        input("Appuyez sur entrer pour continuer...")
        enregistrer_partie(nom, mot, len(lettres_trouvees) == len(set(mot)), temps)
        effacerConsole()

    return partie_terminee
    

def game(choix,nom):

    lettres_trouvees = []
    lettres_ratees = []
    fin_de_partie = False
    mot = choisirMot(lire_dictionnaires_mots()[["facile", "intermediaire", "difficile"][int(choix)-1]])

    afficherJeu(lettres_ratees, lettres_trouvees, mot)
    start = time.time()
    while not fin_de_partie:
        print(mot)
        validerLettre(lettres_ratees, lettres_trouvees, mot)
        fin_de_partie = etatDeLaPartie(lettres_ratees, lettres_trouvees, mot, nom, start)
        

def afficherHistorique(nom):
    effacerConsole()
    parties_jouees = lire_historique_utilisateur(nom)

    print("Historique des parties_jouees:")

    for i in range(len(parties_jouees)):
        victoire = "gagné" if parties_jouees[i]["resultat"] == True else "perdu"
        print("\t"+ parties_jouees[i]["mot"] + f" - {victoire} - " + str(parties_jouees[i]["duree"]) + " secondes")

    input("Appuyez pour continuer...")
    effacerConsole()