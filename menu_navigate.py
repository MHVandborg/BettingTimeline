# Contains all menus and menu selecting function

def menu_select(menu_current):
    # Function for getting number to navigate menus

    menu_selected = 0       # Variable to exit when menu is selected

    # Get correct input to a menu
    while 1 == 1:
        try:
            # Get input
            menu_selected = int(input("Type number to navigate menu: "))

            # Make menu range check
            if menu_current == "Main menu":
                if 0 < menu_selected < 6:
                    break
                else:
                    print("\nPlease enter a number to navigate the menu.\n")
            if menu_current == "Plot menu":
                if 0 < menu_selected < 3:
                    break
                else:
                    print("\nPlease enter a number to navigate the menu.\n")

        # Get new user input if current is not legit
        except ValueError:
            print("\nPlease enter a number to navigate the menu.\n")

    return menu_selected


def main_menu(menu):
    # Function for main menu

    # Text for main menu
    print("\nMain menu:")
    print("   1 - Plot betting timeline.")
    print("   2 - Add new bet.")
    print("   3 - Confirm win/loss for previous bet.")
    print("   4 - Betting history table.")
    print("   5 - Exit program.")

    # Get user input
    menu_selected = menu_select(menu)

    # Go to selected menu
    if menu_selected == 1:
        return "Plot"
    elif menu_selected == 2:
        return "Add bet"
    elif menu_selected == 3:
        return "Confirm WL"
    elif menu_selected == 4:
        return "Table history"
    elif menu_selected == 5:
        return "Exit"


def menu_navigator(menu):
    # Function to navigate menus

    if menu == "Main menu":
        return main_menu(menu)
    elif menu == "Plot":
        return "Main menu"
    elif menu == "Add bet":
        return "Main menu"
    elif menu == "Confirm WL":
        return "Main menu"
    elif menu == "Table history":
        return "Main menu"
    elif menu == "Exit":
        return 0


