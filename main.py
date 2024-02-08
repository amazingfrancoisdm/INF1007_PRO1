from util import lire_historique_utilisateur, enregistrer_partie, lire_dictionnaires_mots
from outils import *
import time
import os

nom_utilisateur = ""
erreurs = 0
lettres_trouvees = []
lettres_ratees = []


# Boucle qui gere le nom entre par
while True:
    username = input("Veuillez entrer votre nom d'utilisateur: ")
    
    if isNameValid(username):
        print("Bienvenue, " + username + "!\n\n")
        nom_utilisateur = username
        break
    else:
        print("Votre nom est invalide!")
        continue

print("Menu principal:\n1. Commencer une partie\n2. Afficher l'historique\n3. Quitter\n") 

while True:
    choix_menu_principal = input("Entrez votre choix: ")   

    if choix_menu_principal == "1":
        effacerConsole()
        print("Choississez une difficulte: \n1. Facile\n2. Intermediaire\n3. Difficile")
        mots = lire_dictionnaires_mots()

        niveau_choisi = False

        while not niveau_choisi:
            choix_niveau = input("Entrez votre choix: ")

            if choix_niveau == "1":
                effacerConsole()
                niveau_choisi = True
                mot = choisirMot(mots["facile"])


                mot_trouve = False

                while True:
                    afficherJeu(lettres_ratees, lettres_trouvees, mot)
                    #MOT AFFICHE FOR HELP
                    print(mot)
                    lettre_entree = input("Entrez une lettre: ")

                    lettre_contenue = mot.find(lettre_entree)

                    if lettre_contenue == -1:
                        lettres_ratees.append(lettre_entree)
                        print("Cette lettre n'est pas dans le mot.")
                    else:
                        if lettre_entree in lettres_trouvees:
                            print("Vous avez deja entre cette lettre.")
                        else:
                            lettres_trouvees.append(lettre_entree)
                            print("Bravo, tu as trouve une lettre")



            elif choix_niveau == "2":
                niveau_choisi = True
                choisirMot(mots["intermediaire"])
                
            elif choix_niveau == "3":
                niveau_choisi = True
                choisirMot(mots["difficile"])
                
            else:
                print("Choix invalide, veuillez reessayer.")
                continue

    elif choix_menu_principal == "2":
        ...
    elif choix_menu_principal == "3":
        print("Merci d'avoir joue, " + nom_utilisateur + "!")
        time.sleep(2)
        quit()
    else:
        print("Choix invalide, veuillez reessayer.")
        continue
        

