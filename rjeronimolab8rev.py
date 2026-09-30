#Rogelio Jeronimo
#CTC-389-151
#September 16, 2026

#Lab 8 - Adventure Game

play_again = "yes"

while play_again == "yes":
    print ("Welcome adventure seeker")
    name = input ("What is your name? ")
    print ()

    print ("Hello", name)
    print ("You wake up on a mysterious island after your boat was")
    print ("caught in a terrible storm.")
    print ("You do not know where you are, but you must find a way")
    print ("off the island before nightfall.")
    print ()

    print ("You see three possible paths.")
    print ()
    print ("1. Walk into the jungle")
    print ("2. Follow the beach")
    print ("3. Climb a rocky hill")
    print ()

    choice1 = input ("Which path would you like to choose? ")

    if choice1 == "1":
        print ()
        print (name, "walks into the thick jungle.")
        print ("After walking for several minutes, you discover an old temple.")

    elif choice1 == "2":
        print ()
        print (name, "Follows the beach.")
        print ("After walking for serveral minutes, you discover an old temple.")

    else:
        print ()
        print (name, "climbs the rocky hill.")
        print ("from the top, you see an old temple and decide to investigate.")

    print ()
    print ("When you arrive at the temple, you see three entrances.")
    print ()
    print ("1. Enter throught the large wooden door")
    print ("2. Crawl through a small opening")
    print ("3. Climb through a broken window")
    print ()

    choice2 = input ("How would you like to enter the temple? ")

    if choice2 == "1":
        print ()
        print ("You push open the wooden door.")
        print ("It makes a loud creaking sound, but you safely enter.")

    elif choice2 == "2":
        print ()
        print ("You crawl through the small opening.")
        print ("It is dark and dusty, but you safely enter.")

    else:
        print ()
        print ("You carefully climb through the broken window.")
        print ("You enter a large room inside the temple.")

    print ()
    print ("Inside the temple you find three objects on a table.")
    print ()
    print ("1. A golden key")
    print ("2. A silver sword")
    print ("3. a strange glowing stone")
    print ()

    choice3 = input ("Which object will you choose? ")

    if choice3 == "1":
        item = "golden key"
        print ()
        print ("You have chosen the golden key and placed it in your pocket.")

    elif choice3 == "2":
        item = "silver sword"
        print ()
        print ("You have chosen the silver sword.")
        print ("You are hoping it will protect you.")

    else:
        item = "glowing stone"
        print ()
        print ("You have chosen the strange glowing stone.")
        print ("The stone suddenly begins to shine brightly.")

    print ()
    print ("Suddenly, you hear a loud growling sound behind you.")
    print ("A ginat tiger enters the room.")
    print ("You have to react quickly.")
    print ()
    print ("1. Run away")
    print ("2. Hide behind a large statue")
    print ("3. Stand your ground")
    print ()

    choice4 = input ("What will you do? ")

    alive = True

    if choice4 == "1":
        print ()
        print ("You run as fast as you can.")
        print ("Luckily, you escape throught another doorway.")

    elif choice4 =="2":
        print ()
        print ("You hide behind a large statue.")
        print ("The tiger walks past you without seeing you.")
        print ("You quietly escape through another doorway.")

    else:
        if item == "silver sword":
            print ()
            print ("You raise the siler sword.")
            print ("The tiger sees the sword and backs away.")
            print ("You safely escape from the room.")
        else:
            print ()
            print ("You try to stand your ground, but you have no weapon.")
            print ("The giant tiger attacks you.")
            print ()
            print (name, ", you have perished.")
            alive = False

    if alive == True:

        print ()
        print ("You leave the temple and discover a river.")
        print ("You must cross the river to reach the other side.")
        print ()
        print ("1. Swim across the river")
        print ("2. Use an old wooden bridge")
        print ("3. build a small raft")
        print ()

        choice5 = input ("How will you choose to cross the river? ")

        if choice5 == "1":
            print ()
            print ("You jump into the river and begin swimming.")
            print ("Suddenly, you see several crocodiles swimming toward you.")
            print ()
            print (name, ", you have been eaten by croodiles.")
            alive = False

        elif choice5 == "2":
            print ()
            print ("You carefully walk across the old bridge.")
            print ("Several boards break, but you make it safely across.")

        else:
            print ()
            print ("You use branches and vines to build a small raft.")
            print ("The raft slowly carries you safely across the river.")

    if alive == True:

        print ()
        print ("On the other side of the river you find an abandoned village.")
        print ("You see three buildings.")
        print ()
        print ("1. Search the large house")
        print ("2. Search the small hut")
        print ("3. Search the old storage building")

        choice6 = input ("Which building will you choose to search? ")

        if choice6 == "1":
            print ()
            print ("Inside the house you find food and fresh water.")
            print ("You take the supplies with you.")

        elif choice6 == "2":
            print ()
            print ("Inside the hut you find a map of the island.")
            print ("The map shows a boat located on the northern beach.")

        else:
            print ()
            print ("Inside the old storage building you find a flashlight.")
            print ("You take the flashlight with you.")

    if alive == True:

        print ()
        print ("As the sun begins to set, you reach the northern beach.")
        print ("You see three possible ways to escape the island.")
        print ()
        print ("1. Use an old motorboat")
        print ("2. Build a signal fire")
        print ("3. Swim into the ocean")
        print ()

        choice7 = input ("What will you chose to do? ")

        if choice7 == "1":
            print ()
            print ("You climb into the motoboat.")
            print ("Luckily, the engine starts.")
            print ("You drive away from the mysterious island.")
            print ()
            print ("Congratulations", name)
            print ("You escaped the island and Won the Game.")

        elif choice7 == "2":
            print ()
            print ("You build a large signal fire on the beach.")
            print ("Several hours later, a rescue helicopter sees your fire.")
            print ("The helicopter lands and rescues you.")
            print ()
            print ("Congratulations", name)
            print ("You escaped the island and Won the Game.")

        else:
            print ()
            print ("You decide to swim into the ocean.")
            print ("After swimming for several minutes, you become exhausted.")
            print ("You are unable to make it back to the island.")
            print ()
            print (name, ", you have perished.")

    print ()
    play_again = input ("Would you like to play again? ")

    play_again = play_again

    print ()

print ("Thank you for playing")


