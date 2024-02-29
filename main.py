from util import lire_historique_utilisateur, enregistrer_partie, lire_dictionnaires_mots
from outils import *
import time

nom_utilisateur = ""
lettres_trouvees = []
lettres_ratees = []
historique = []

effacerConsole()

# Boucle qui gere le nom entre par
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
        mots = lire_dictionnaires_mots()

        niveau_choisi = False

        while not niveau_choisi:
            choix_niveau = input("Entrez votre choix: ")

            if choix_niveau == "1":
                niveau_choisi = True
                mot = choisirMot(mots["facile"])
                game(lettres_ratees, lettres_trouvees, choisirMot(mots["facile"]),nom_utilisateur)

            elif choix_niveau == "2":
                niveau_choisi = True
                choisirMot(mots["intermediaire"])
                game(lettres_ratees, lettres_trouvees, choisirMot(mots["intermediaire"]),nom_utilisateur)
                
            elif choix_niveau == "3":
                niveau_choisi = True
                choisirMot(mots["difficile"])
                game(lettres_ratees, lettres_trouvees, choisirMot(mots["difficile"]),nom_utilisateur)
                
            else:
                print("Choix invalide, veuillez reessayer.")
                continue

    elif choix_menu_principal == "2":
        lecture(nom_utilisateur)
    elif choix_menu_principal == "3":
        print("Merci d'avoir joue, " + nom_utilisateur + "!")
        time.sleep(2)
        quit()
    else:
        print("Choix invalide, veuillez reessayer.")
        effacerConsole()
        continue
        

