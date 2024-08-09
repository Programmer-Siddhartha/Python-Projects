def start_game():
    print("Welcome to 'Mystery of the Lost Treasure'!")
    print("You find yourself in a dense forest. There are paths to the north and east.")
    
    choice = input("Do you want to go north or east? ").lower()

    if choice == "north":
        north_path()
    elif choice == "east":
        east_path()
    else:

        print("Invalid choice. Please choose 'north' or 'east'.")
        start_game()

def north_path():
    print("You head north and encounter a mysterious old man.")
    print("He offers you a map in exchange for a gold coin.")

    choice = input("Do you want to give him a coin or refuse? ").lower()

    if choice == "give":
        print("The old man gives you the map. You follow it and find the treasure!")
        print("Congratulations, you won!")
    elif choice == "refuse":
        print("The old man disappears. You wander around and eventually get lost.")
        print("Game over!")
    else:

        print("Invalid choice. Please choose 'give' or 'refuse'.")
        north_path()

def east_path():

    print("You head east and come across a river.")
    print("There is a boat and a bridge crossing the river.")

    choice = input("Do you want to take the boat or cross the bridge? ").lower()


    if choice == "boat":
        print("The boat drifts downstream and you reach a hidden cave.")
        print("Inside, you find the treasure! Congratulations, you won!")
    elif choice == "bridge":
        print("The bridge collapses, and you fall into the river.")
        print("Game over!")
    else:

        print("Invalid choice. Please choose 'boat' or 'bridge'.")
        east_path()

start_game()
