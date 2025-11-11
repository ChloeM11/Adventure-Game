import random

inventory = []
health = 5

def menu():
    print("\n=== PARANORMAL CLUB ===")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Quit")
    choice = input("> ")
    while choice not in ["1", "2", "3"]:
        choice = input("Pick 1, 2, or 3: ")
    return choice

def instructions():
    print("\nYou explore a haunted school building.")
    print("Make simple choices and try not to lose all your health.")
    input("Press ENTER to go back.")

def move_player(steps, health_value):
    print(f"\nYou walk {steps} steps down the hallway...")
    health_value -= 1
    print("Health:", health_value)
    return health_value

def random_event():
    events = ["cold breeze", "weird shadow", "nothing"]
    event = random.choice(events)
    print("\nA random event happens:", event)

    global health
    if event == "cold breeze":
        health -= 1
        print("You lose 1 health.")
    elif event == "weird shadow":
        inventory.append("strange note")
        print("You found a strange note!")

def start_game():
    global health
    print("\nYou join the paranormal club.")
    print("Your team enters an old haunted classroom.")

    playing = True

    while playing:
        print("\nWhere do you want to go?")
        print("A: Check the desk")
        print("B: Leave the room")
        choice = input("> ").lower()

        while choice not in ["a", "b"]:
            choice = input("Pick A or B: ").lower()

        if choice == "b":
            print("\nYou leave without investigating.")
            print("You never learn the truth... the dream continues.")
            print("ENDING: Unaware")
            break

        if choice == "a":
            health = move_player(5, health)
            random_event()

            print("\nYou see a glowing message on the desk.")
            answer = input("It asks: 'What has keys but can't open doors?' ").lower()

            if answer == "piano":
                print("\nThe room fades away...")
                print("You realize this whole world is someone's dream.")
                print("ENDING: Dream Awakened")
                break
            else:
                print("\nThe message disappears. You feel dizzy.")
                health -= 1
                if health <= 0:
                    print("You pass out and vanish as the dream collapses.")
                    print("ENDING: Lost")
                    break


# MAIN LOOP
running = True
while running:
    choice = menu()

    if choice == "1":
        start_game()
    elif choice == "2":
        instructions()
    else:
        print("Goodbye!")
        running = False
