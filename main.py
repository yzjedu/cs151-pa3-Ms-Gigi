# Programmer Name: Oreoluwa Adebusoye
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 11/07/2024
# Program Name: ASCII Art Program
# What program does (purpose):


import random

# Main Menu Function
# Purpose: Display a menu with options for the user to choose from (circle, lines, random design, or exit).
# Name: main_menu()
# Parameters: None.
# Return: None
def main_menu():
    print("\nHey There! Welcome to ASCII Art Creation!")
    print("This program allows you to choose between four options:")
    print("\t1. Output a Circle: See a simple approximation of a circle using ASCII art.")
    print("\t2. Output a Set of Lines: Create multiple lines with characters of your choice.")
    print("\t3. Output a Random Design: Let the program surprise you with a random pattern.")
    print("\t4. Exit: Exit the program.")
    print("\nLet's get started!\n")

# Display Circle Function
# Purpose: Display an ASCII art approximation of a circle.
# Name: display_circle()
# Parameters: None
# Return: None
def display_circle():
    print("You chose to display a circle!")
    print("Here is an approximation of a circle:\n")
    print("   ___  ")
    print(" /     \\")
    print("|       |")
    print(" \\ ___ /\n")

# Display Lines Function
# Purpose: Display a set of user-defined lines.
# Name: display_lines()
# Parameters: None
# Return: None
def display_line():
    print("You chose to display lines!")

    # Get user input for the number of lines
    num_lines = input("How many lines do you want to draw? ")
    while not num_lines.isdigit() or int(num_lines) <= 0:
        print("Please enter a valid positive number.")
        num_lines = input("How many lines do you want to draw? ")
    num_lines = int(num_lines)  # Convert to integer after validation

    # Get user input for the character to display
    character_displayed = input("What character do you want to use? ").strip()
    while character_displayed == "":
        print("Invalid input. The input cannot be empty.")
        character_displayed = input("What character do you want to use? ").strip()

    # Get user input for the number of repetitions
    repeat_num = input("How many times should the character(s) repeat? ")
    while not repeat_num.isdigit() or int(repeat_num) <= 0:
        print("Please enter a valid positive number.")
        repeat_num = input("How many times should the character(s) repeat? ")
    repeat_num = int(repeat_num)  # Convert to integer after validation

    # Output the lines
    print("\nHere are your lines:\n")
    for char in range(num_lines):
        print(character_displayed * repeat_num)
    print("\n")

# Random Design Function
# Purpose: Display a random design from three pre-defined designs.
# Name: display_random_design()
# Parameters: None.
# Return: None.
def display_random_design():
    print("\nYou selected: Output a Random Design!")
    print("Here is a randomly selected design:")
    design_to_display = random.randint(1,3)
    if design_to_display == 1:
        # Red Phoenix - Source:https://www.asciiart.eu/mythology/dragons
        print("\nDesign 1: ASCII Art (Dragon)")
        print("                _ ___                /^^\\ /^\\  /^^\\_")
        print("    _          _@)@) \\            ,,/ '` ~ `'~~ ', `\\.")
        print("  _/o\\_ _ _ _/~`.`...'~\\        ./~~..,'`','',.,' '  ~:")
        print(" / `,'.~,~.~  .   , . , ~|,   ,/ .,' , ,. .. ,,.   `,  ~\\_")
        print("( ' _' _ '_` _  '  .    , `\\_/ .' ..' '  `  `   `..  `,   \\_")
        print(" ~V~ V~ V~ V~ ~\\ `   ' .  '    , ' .,.,''`.,.''`.,.``. ',   \\_")
        print(" < ~ ~ '~`'~'`, .,  .   `_: ::: \\_ '      `_/ ::: \\_ `.,' . ',  \\_")
        print("  \\ ' `_  '`_    _    ',/ _::_::_ \\ _    _/ _::_::_ \\   `.,'.,`., \\-,-,-,_,_,")
        print("   `'~~ `'~~ `'~~ `'~~  \\(_)(_)(_)/  `~~' \\(_)(_)(_)/ ~'`\\_.._,._,'_;_;_;_;_;")
    elif design_to_display == 2:
        print("\nDesign 2: Birthday Cake")
        # Display candles
        print("        ()()()        ")
        print("        ||||||        ")
        for layer in range(4):
            print('*' * 22)  # Top border of the cake layer
            for i in range(3):  # Each layer is three lines high
                print('*' + ' ' * 20 + '*')
        print('*' * 22)
    elif design_to_display == 3:
        print("\nDesign 3: Cat on a mug")
        print("=" * 30)
        print("|" + " " * 29 + "|")
        print("|                             |_______")
        print("|                             |       |")
        print("|                             |       |")
        print("|          /\\_/\\              |_______|")
        print("|         ( o.o )             |")
        print("|          > ^ <              |")
        print("|    Have a purrrfect day!    |")
        for i in range(3):
            print("|" + " " * 29 + "|")

# Main Function
# Purpose: Control the flow of the program.
# Name: main()
# Parameters: None
# Return: None
def main():
    main_menu()

    # Get user input and validate
    choice = input("Please enter your choice (1-4): ").strip()
    options = [1, 2, 3, 4]

    # Loop until the user enters a valid choice
    while not choice.isdigit() or int(choice) not in options:
        print("Invalid choice. Please enter a number between 1 and 4.\n")
        choice = input("Please enter your choice (1-4): ").strip()

    # Convert the valid choice to an integer
    choice = int(choice)

    # Handle user choice
    if choice == 1:
        display_circle()
    elif choice == 2:
        display_line()
    elif choice == 3:
        display_random_design()
    elif choice == 4:
        print("\nThank you for using the ASCII Art Program. Goodbye!\n")

main()
