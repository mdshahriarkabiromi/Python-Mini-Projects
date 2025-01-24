import logo
print(logo.treasure_logo)
print("🌲 Welcome to the Python Adventure Game! 🌲")
print('''You find yourself in a dark, mysterious forest.
There are three paths in front of you, each leading to unknown adventures.''')

choice1 = int(input('''Do you want to:
1. Take the left path 🌿
2. Take the middle path 🌲
3. Take the right path 🌳
Enter 1, 2, or 3: '''))

if choice1 == 1:
    print("You walk down the left path and encounter a wild animal 🐻.")
    choice1_1 = int(input('Do you want to:\n'
                          '1. Run away 🏃\n'
                          '2. Fight the animal 🗡️\n'
                          '3. Try to tame the animal 🐾\n'
                          'Enter 1, 2, or 3: '))
    if choice1_1 == 1:
        print("You decide to run away, but you trip over a root and the animal catches up to you."
              " You have lost the game. 😢")
    elif choice1_1 == 2:
        print("You decide to fight the animal, but it overpowers you."
              " You have lost the game. 😢")
    else:
        print("You try to tame the animal, and surprisingly, it works!"
              " The animal becomes your loyal companion and helps you find a hidden treasure in the forest."
              " You have won the game! 🎉")

elif choice1 == 2:
    print("You take the middle path and find a mysterious cave 🕳️.")
    choice2_1 = int(input('Do you want to:\n'
                          '1. Enter the cave 🏞️\n'
                          '2. Walk past the cave 🚶\n'
                          '3. Set up camp outside the cave ⛺\n'
                          'Enter 1, 2, or 3: '))
    if choice2_1 == 1:
        print("You enter the cave and discover that it's the home of a dragon 🐉. The dragon kills you!"
              " You have lost the game. 😢")
    elif choice2_1 == 2:
        print("You decide to walk past the cave. As you continue down the path,"
              " you find a beautiful clearing with a hidden waterfall 💧."
              " You decide to rest here and enjoy the serene environment."
              " You have found a peaceful spot and won the game! 🌸")
    else:
        print("You set up camp outside the cave. During the night, you hear strange noises coming from inside.")
        choice2_2 = int(input('Do you want to:\n'
                              '1. Investigate the noises 🔍\n'
                              '2. Stay in your camp 🏕️\n'
                              'Enter 1 or 2: '))
        if choice2_2 == 1:
            print("You decide to investigate the noises and find out that it was a wolf 🐺."
                  " The wolf eats you and you lose the game. 😢")
        else:
            print("You stayed in your camp. In the morning, you are found by local people."
                  " They help you return home."
                  " You finally come back home and win the game! 🏡")

else:
    print("You take the right path and come across a river 🌊.")
    choice3_1 = int(input('Do you want to:\n'
                          '1. Swim across the river 🏊\n'
                          '2. Build a raft 🛶\n'
                          '3. Follow the river downstream 🚣\n'
                          'Enter 1, 2, or 3: '))
    if choice3_1 == 1:
        print("You decide to swim across the river, but the current is too strong and you get swept away."
              " You have lost the game. 😢")
    elif choice3_1 == 2:
        print("You decide to build a raft. After some effort,"
              " you successfully cross the river and find a hidden treasure chest on the other side."
              " You have won the game! 🎉")
    else:
        print("You follow the river downstream and find a village 🏘️."
              " The villagers welcome you and you decide to stay."
              " You have found a new home and won the game! 🏡")
