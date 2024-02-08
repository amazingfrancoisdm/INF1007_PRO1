import os
import json
from datetime import datetime

CHEMIN_WORKSPACE = os.path.dirname(os.path.abspath(__file__))
CHEMIN_HISTORIQUE = os.path.join(CHEMIN_WORKSPACE, "data", "historique.json")
CHEMIN_MOTS = os.path.join(CHEMIN_WORKSPACE, "data", "mots.json")


def lire_dictionnaires_mots():
    """
    Lit les dictionnaires de mots et les retourne.

    Raises:
        Exception: Si une erreur survient lors de la lecture.

    Returns:
        dict: Dictionnaire contenant les mots par difficulté.
    """
    try:
        with open(CHEMIN_MOTS, "r") as file:
            return json.load(file)
    except Exception as e:
        print("Erreur lors de la lecture des dictionnaires de mots.")
        raise e


def enregistrer_partie(nom_utilisateur: str, mot: str, a_gagne: bool, duree_s: int):
    """
    Enregistre une partie dans l'historique.

    Args:
        nom_utilisateur (str): Nom de l'utilisateur.
        mot (str): Mot joué.
        a_gagne (bool): True si l'utilisateur a gagné, False sinon.
        duree (int): Durée de la partie en secondes.

    Raises:
        ValueError: Si les paramètres sont invalides.
        Exception: Si une erreur survient lors de l'enregistrement.

    Returns:
        bool: True si l'enregistrement s'est bien déroulé.
    """

    nouvelle_partie = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "mot": mot,
        "resultat": a_gagne,
        "duree": duree_s
    }

    valider_partie(nouvelle_partie)

    try:
        historique = lire_historique()
        historique_utilisateur = historique.get(nom_utilisateur, [])
        historique_utilisateur.append(nouvelle_partie)
        historique[nom_utilisateur] = historique_utilisateur

        with open(CHEMIN_HISTORIQUE, "w") as file:
            json.dump(historique, file)

    except Exception as e:
        print("Erreur lors de l'enregistrement de la partie.")
        raise e


def lire_historique_utilisateur(nom_utilisateur: str):
    """
    Lit l'historique d'un utilisateur et le retourne.

    Args:
        nom_utilisateur (str): Nom de l'utilisateur.

    Raises:
        ValueError: Si le nom d'utilisateur est invalide.
        Exception: Si une erreur survient lors de la lecture.

    Returns:
        list: Liste des parties jouées par l'utilisateur.
    """
    if not isinstance(nom_utilisateur, str):
        raise ValueError(
            "Le nom d'utilisateur doit être une chaîne de caractères")

    historique = lire_historique()
    return historique.get(nom_utilisateur, [])


def lire_historique():
    with open(CHEMIN_HISTORIQUE, "r") as file:
        historique = json.load(file)

    valider_historique(historique)

    return historique


def valider_historique(historique: dict) -> bool:
    try:
        if not isinstance(historique, dict):
            raise ValueError("L'historique doit être un dictionnaire")

        if not all(isinstance(key, str) for key in historique.keys()):
            raise ValueError(
                "Les clés de l'historique doivent être des chaînes de caractères (noms d'utilisateurs)")

        for parties in historique.values():
            if not isinstance(parties, list):
                raise ValueError("Les parties doivent être une liste")

            for partie in parties:
                valider_partie(partie)
    except Exception as exception:
        print("Erreur lors de la validation de l'historique.")
        reinitialiser_historique()
        raise exception


def valider_partie(partie_dict: dict) -> bool:
    if not isinstance(partie_dict, dict):
        raise ValueError("La partie doit être un dictionnaire")

    expected_keys = {"mot", "resultat", "duree", "timestamp"}
    if set(partie_dict.keys()) != expected_keys:
        raise ValueError(f"La partie doit contenir les clés {expected_keys}")

    if not all(isinstance(partie_dict[key], expected_type) for key, expected_type in [("mot", str), ("resultat", bool), ("duree", int), ("timestamp", str)]):
        raise ValueError("Les clés du dictionnaire doivent être du bon type")

    if not partie_dict["mot"]:
        raise ValueError("Le mot ne doit pas être vide")

    if partie_dict["duree"] < 0:
        raise ValueError("La durée doit être positive")

    try:
        datetime.strptime(partie_dict["timestamp"], "%Y-%m-%d %H:%M")
    except ValueError:
        raise ValueError("Le format de la date est invalide")


def reinitialiser_historique():
    print("Réinitialisation de l'historique...")
    with open(CHEMIN_HISTORIQUE, "w") as file:
        json.dump({}, file)
    print("Historique réinitialisé avec succès.")


if __name__ == "__main__":
    print("Test des fonctions utilitaires\n")

    print("## Affichage de l'historique de tous les utilisateurs")
    print(lire_historique())

    print("\n## Ajout d'une partie jouée par John Doe")
    enregistrer_partie("John Doe", "test", True, 30)
    print("Partie ajoutée avec succès.")

    print("\n## Affichage de l'historique des parties de John Doe")
    print(lire_historique_utilisateur("John Doe"))

    print("\n## Affichage des mots par difficulté")
    mots = lire_dictionnaires_mots()
    for difficulte, liste_mots in mots.items():
        print(f"Difficulté {difficulte}: {len(liste_mots)} mots")
        print(f"{', '.join(liste_mots)}\n")
