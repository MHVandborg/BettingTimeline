# Program to plot timeline of betting bet

# Import functions
from open_program import start_program       # Function to open program
from menu_navigate import menu_navigator
from menu_action import menu_active

# Variables
run = 1
menu = "Main menu"

# Program start
start_program()

# Looping program
while run:
    menu = menu_navigator(menu)
    run = menu_active(menu)

print("\nProgram ends...")

