import json
from datetime import datetime
import shutil


def demander_texte(message):
    while True:
        texte = input(message).strip()

        if texte:
            return texte

        print("Ce champ ne peut pas être vide.")


def choisir_statut():
    print("1. A faire")
    print("2. En cours")
    print("3. Terminée")

    choix_statut = demander_texte("Choisir le statut : ")

    if choix_statut == "1":
        return "A faire"

    elif choix_statut == "2":
        return "En cours"

    elif choix_statut == "3":
        return "Terminée"

    else:
        print("Choix invalide")
        return None


def lire_notes():
    try:
        with open("notes.json", "r") as fichier:
            return json.load(fichier)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Erreur : le fichier notes.json est invalide.")
        return []


def sauvegarder_notes(notes):

    try:
        shutil.copy2("notes.json", "notes_backup.json")

    except FileNotFoundError:
        pass

    with open("notes.json", "w") as fichier:
        json.dump(notes, fichier, indent=4)


def ajouter_note():
    notes = lire_notes()

    titre = demander_texte("Titre : ")

    contenu = demander_texte("Contenu : ")

    categorie = demander_texte("Catégorie : ")

    statut = choisir_statut()

    if statut is None:
        return

    if notes:
        nouvel_id = max(note["id"] for note in notes) + 1
    else:
        nouvel_id = 1

    nouvelle_note = {
        "id": nouvel_id,
        "titre": titre,
        "contenu": contenu,
        "categorie": categorie,
        "statut": statut,
        "date_creation": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    notes.append(nouvelle_note)
    sauvegarder_notes(notes)

    print("Note ajoutée !")


def afficher_notes():
    notes = lire_notes()

    if not notes:
        print("Aucune note.")
        return

    print("\n=== MES NOTES ===")

    for note in notes:
        categorie = note.get("categorie", "Sans catégorie")
        statut = note.get("statut", "Statut inconnu")
        date_creation = note.get("date_creation", "Date inconnue")
        date_modification = note.get("date_modification")

        print(f'\n {note["id"]}. {note.get("titre", "Sans titre")}')
        print(f'    Catégorie : {categorie}')
        print(f'    Statut : {statut}')
        print(f'    {note["contenu"]}')
        print(f'    Créée le : {date_creation}')

        if date_modification:
  
            print(f'    Modifiée le : {date_modification}')


def rechercher_note():
    notes = lire_notes()

    if not notes:
        print("Aucune note.")
        return

    recherche = input("Rechercher: ").strip().lower()

    if not recherche:
        print("La recherche n'est pas valide.")
        return

    trouve = False

    for note in notes:
        if recherche in note.get("titre", "").lower() or recherche in note.get("categorie", "").lower() or recherche in note["contenu"].lower():
            print(f'\n {note["id"]}. {note.get("titre", "Sans titre")}')
            print(f'    Catégorie : {note.get("categorie", "Sans Catégorie")}')
            print(f'    Statut : {note.get("statut", "Statut inconnu")}')
            print(f'    {note["contenu"]}')
            trouve = True

    if not trouve:
        print("Aucune note trouvée.")


def modifier_note():
    notes = lire_notes()

    if not notes:
        print("Aucune note à modifier.")
        return

    afficher_notes()

    try:
        id_note = int(input("\nID de la note à modifier : "))

        for note in notes:
            if note["id"] == id_note:

                nouveau_titre = demander_texte("Nouveau titre : ")

                nouvelle_categorie = demander_texte("Nouvelle catégorie : ")

                statut = choisir_statut()

                if statut is None:
                    return
        
                nouveau_contenu = demander_texte("Nouveau Contenu : ")

                note["titre"] = nouveau_titre
                note["categorie"] = nouvelle_categorie
                note["statut"] = statut
                note["contenu"] = nouveau_contenu
                note["date_modification"] = datetime.now().strftime("%d/%m/%Y %H:%M")

                sauvegarder_notes(notes)

                print("Note modifiée !")
                return

        print("Aucune note avec cet ID.")
        return

    except ValueError:
        print("Veuillez entrer un nombre.")


def supprimer_note():
    notes = lire_notes()

    if not notes:
        print("Aucune note à supprimer.")
        return

    afficher_notes()

    try:
        id_note = int(input("\nID de la note à supprimer : "))

        for note in notes:
            if note["id"] == id_note:
                notes.remove(note)
                sauvegarder_notes(notes)
                print("Note supprimée !")
                return

        print("Aucune note avec cet ID.")

    except ValueError:
        print("Veuillez entrer un nombre.")