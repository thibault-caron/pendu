from .ajouter_mot import ajouter_mot

def menu(font, fichier_mots, choix_joueur):
    """
    Main function used to provide options to the user to exit or enter a new operation,
    with or without the previous result.
    :param: history: A dictionary of operations history.
    :param: index: The index of the last operation in operations history.
    :return: ∅
    """
    choix = choix_joueur

    match choix:
        case "1":  # Lancer une partie
            font.render("Placeholder lance partie")
            # Hangman().main()  

        case "2":  # ajouter un mot dans le dictionnaire
            fichier = fichier_mots
            nouveau_mot = input("Enter the new word to add: ").lower()
            ajouter_mot(fichier, nouveau_mot)
            menu()

        case "3":  # Change la difficulté
            # difficulte()
            menu()

        case "4":  # Affiche les scores
            font.render("Scores:")
            with open("scores.txt", "r") as myfile:
                scores = myfile.read().splitlines()
            for i, score in enumerate(scores, start=1):
                print(f"{i}. {score}")

        case "5":  # Exit the program.
            font.render("Goodbye.\n")
            exit()

        case "h":  # Display menu again.
            # affiche_menu()
            menu()

        case _:  # Case of a wrong input.
            font.render("Mauvaise saisie")
            menu()