# Fichier fait par Francois Dufour Martel (2330346)

from util import lire_historique_utilisateur, enregistrer_partie, lire_dictionnaires_mots
from outils import *
import time


effacerConsole()

nom_utilisateur = choisirNom()

while True:
    print("Menu principal:\n1. Commencer une partie\n2. Afficher l'historique\n3. Quitter\n") 
    choix_menu_principal = input("Entrez votre choix: ")   

    if choix_menu_principal == "1":
        effacerConsole()
        print("Choississez une difficulte: \n1. Facile\n2. Intermediaire\n3. Difficile")
        
        niveau_choisi = False

        while not niveau_choisi:
            choix_niveau = input("Entrez votre choix: ")

            if choix_niveau in {"1", "2", "3"}:
                niveau_choisi = True
                game(choix_niveau,nom_utilisateur)
                
            else:
                print("Choix invalide, veuillez reessayer.")
                continue

    elif choix_menu_principal == "2":
        afficherHistorique(nom_utilisateur)

    elif choix_menu_principal == "3":
        print("Merci d'avoir joue, " + nom_utilisateur + "!")
        time.sleep(2)
        quit()
        
    else:
        print("Choix invalide, veuillez reessayer.")
        effacerConsole()
        continue
        

