from util import lire_historique_utilisateur, enregistrer_partie, lire_dictionnaires_mots
from outils import *
import time

nom_utilisateur = ""

effacerConsole()

# TODO Faire une fonction qui englobe toutes ces operations
# TODO Bouger le username dans outils.py
while True:
    username = input("Veuillez entrer votre nom d'utilisateur: ")
    effacerConsole()
    
    if validerNom(username):
        print("Bienvenue, " + username + "!\n\n")
        nom_utilisateur = username
        
        break
    else:
        print("Votre nom est invalide!")
        continue



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
        

