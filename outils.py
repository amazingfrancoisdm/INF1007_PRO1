import random
import os

def isNameValid(name):  
    if len(name)>=3:
        for n in name:
            code = ord(n)
            if not (65 <= code <= 90 or 97 <= code <= 122):
                return False   
        return True
    else:
        return False


def choisirMot(mots):
    index = random.randrange(len(mots)-1)
    print(mots[index])
    return mots[index]

def effacerConsole():
    os.system("clear")


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
    print("   +---+")
    print("   |   |")

    if len(lettres_ratees)==1:
        print("   0   |")
        print("       |")
        print("       |")
    elif len(lettres_ratees)==2:
        print("   0   |")
        print("   |   |")
        print("       |")
    elif len(lettres_ratees)==3:
        print("   0   |")
        print("  /|   |")
        print("       |")
    elif len(lettres_ratees)==4:
        print("   0   |")
        print("  /|\  |")
        print("       |")  
    elif len(lettres_ratees)==5:
        print("   0   |")
        print("  /|\  |")
        print("  /    |")   
    elif len(lettres_ratees)==6:
        print("   0   |")
        print("  /|\  |")
        print("  / \  |")    
    else:
        print("       |")
        print("       |")
        print("       |")

    print("       |")
    print("==========")