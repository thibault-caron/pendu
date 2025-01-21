# from main import Hangman
# from ..main import main

def menu():
    """
    Main function used to provide options to the user to exit or enter a new operation,
    with or without the previous result.
    :param: history: A dictionary of operations history.
    :param: index: The index of the last operation in operations history.
    :return: ∅
    """
    choix_joueur = input("\nEnter your choice ('h' for help): ")

    match choix_joueur:
        case "1": 
            Hangman().main()  

        case "2":  # ajouter un mot dans le dictionnaire
            nouveau_mot = input("Enter the new word to add: ").lower()
            with open("mots.txt", "a") as myfile:
                myfile.write(nouveau_mot)
            menu()

        case "3":  # Change la difficulté
            difficulte()
            menu()

        case "4":  # Affiche les scores
            print("Scores:")
            with open("scores.txt", "r") as myfile:
                scores = myfile.read().splitlines()
            for i, score in enumerate(scores, start=1):
                print(f"{i}. {score}")

        case "5":  # Exit the program.
            print("Goodbye.\n")
            exit()

        case "h":  # Display menu again.
            affiche_menu()
            menu()

        case _:  # Case of a wrong input.
            print("Saisie pourrie")
            menu()
