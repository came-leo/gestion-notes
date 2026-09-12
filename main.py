import notes

def menu():
    while True:
        print("\n=== GESTION DES NOTES ===")
        print("1. Ajouter une note")
        print("2. Afficher les notes")
        print("3. Rechercher une note")
        print("4. Modifier une note")
        print("5. Supprimer une note")
        print("6. Quitter")

        choix = input("\nVotre choix : ")

        if choix == "1":
            notes.ajouter_note()

        elif choix == "2":
            notes.afficher_notes()

        elif choix == "3":
            notes.rechercher_note()

        elif choix == "4":
            notes.modifier_note()

        elif choix == "5":
            notes.supprimer_note()

        elif choix == "6":
            print("Au revoir !")
            break

        else:
            print("Choix invalide.")

if __name__ == "__main__":
  menu()
