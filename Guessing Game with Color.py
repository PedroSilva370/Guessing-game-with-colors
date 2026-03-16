import random

def game():
    # thinking...
    print("\n \033[1;30;47mI'M THINKING OF A NUMBER FROM 0 TO 5, TRY TO GUESS...\033[m")
    print('-==' * 20)

    # Choose the number
    escolhido = int(input("\033[1;30;47mGUESS THE NUMBER I'M THINKING OF: \033[m"))

    # randomness system
    list = [0, 1, 2, 3, 4, 5]
    random1 = random.choice(list)

    # condition system
    if escolhido == random1:
        print('\033[1;32mYou guessed the number I was thinking of!\033[m')
    else:
        print(f'I was thinking of the number {random1},\033[1;31m you missed it. ):\033[m')

# calling the function
game()

# game replay function
def repetition():
    again = int(input(('\nDo you want to try again?\n \033[1;32m1)Yes\033[m\n \033[1;31m2)No\033[m\n Note: only enter the number of the option.:  ')))
    if again == 1:
        game()
        while again == 1:
            repetition()
    elif again == 2:
        print(("\033[1;31m-=" * 20) +'GAME ENDED' + ("=-" * 20))
        exit()

# calling the function
repetition()

