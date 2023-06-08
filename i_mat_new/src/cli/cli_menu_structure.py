from os import system

from i_mat_new.src.cli.cli_menu_entries import startmenu_entries
from i_mat_new.src.cli.cli_menu_static_text import text_general_title

##

def example_menu_entries():
    return {
        "menu_displayed_text": [
            "Submenu Header",
            "Please select:",
            ["No.", "Menu item", "<Explanation>"],
            "Which menu item should be executed? (<No. of menu item>): "
        ],
        "menu_entries": [
            ["Option 1", "submenu_entries_dict", "<Goes to submenu>"],
            ["Option 2", "some_function", "<Executes some function>"],
            ["Exit", 'main-menu', "<Returns to main menu>"],
        ]
    }

def example_analysis_results():
    return {
        "menu_displayed_text": [
            "Analysis Results",
            "Please select an analysis result:",
            ["No.", "<Identifier>", "<Description>", "<Description>"],
            "<To continue, please press Enter>"
        ],
        "results": [
            ["Result 1", "<Displays the 1st >", "<Displays the 1st >"],
            ["Result 2", "<Displays the 2nd >", "<Displays the 2nd >"],
            ["Result 3", "<Displays the 3rd >", "<Displays the 3rd >"],
        ]
    }


menu_stack = []  # Stack to keep track of the previous menus


# this function allows the user to return to navigate freely between
# the different menu levels (includes back and forward navigations)

def open_menu_undirected(menu_content_dict, parent_menu_func=None):
    while True:

        # below: displays the menu

        print(text_general_title())

        first_level_menu_entries = startmenu_entries

        menu_entries = menu_content_dict()["menu_entries"]
        system("cls")

        menu_titel = menu_content_dict()["menu_displayed_text"][0]
        menu_request = menu_content_dict()["menu_displayed_text"][1]
        menu_header = menu_content_dict()["menu_displayed_text"][2]
        menu_input_text = menu_content_dict()["menu_displayed_text"][3]

        print(menu_titel)
        print("")

        print(menu_request)
        print("")

        # Print menu_header in one line
        # the number of columns is adjusted automatically based on the amount elements in menu_header

        print("{:<4}".format(menu_header[0]), end='')
        for header in menu_header[1:]:
            print("{:<65}".format(header), end='')
        print("\n")

        # Print menu_entries in multiple lines
        # the number of columns is adjusted automatically based on the number of elements in menu_entries[n]

        for index, item in enumerate(menu_entries, 1):
            print("{:<4}".format(index), end='')
            for i, entry in enumerate(item[:-1]):
                if i != 1:  # Skip printing menu_entries[1]
                    print("{:<65}".format(entry), end='')
            print(item[-1])

        print("")

        userInput_menuSelection = input(menu_input_text)
        print("")

        system("cls")

        # below: handles the user input

        if str(userInput_menuSelection) != "" and str.isdigit(userInput_menuSelection):
            userInput_menuSelection_int = int(userInput_menuSelection) - 1

            if 0 <= userInput_menuSelection_int < len(menu_entries):
                system("cls")

                result = menu_entries[userInput_menuSelection_int][1]

                system("cls")

                if not callable(result):
                    if result == 'back' and menu_stack:
                        # Pop the previous menu from the stack and navigate to it
                        previous_menu = menu_stack.pop()
                        # Recursive call with the parent menu entries function and the parent of the parent menu
                        open_menu_undirected(previous_menu["menu_entries_func"], previous_menu["parent_menu_func"])
                        break
                    elif result == 'main-menu':
                        # Clear the menu stack and navigate to the main menu
                        menu_stack.clear()
                        # Recursive call with the main menu entries function
                        open_menu_undirected(first_level_menu_entries)
                        break
                elif isinstance(result(), dict):
                    # if the result is a list, call the function with the menu entries function
                    # Push the current menu to the stack and navigate to the new menu
                    menu_stack.append({
                        "menu_entries_func": menu_content_dict,
                        "parent_menu_func": parent_menu_func
                    })
                    # if the result is not a list, the function is executed by calling isinstance(result(), list)
                    open_menu_undirected(result, menu_content_dict)
                    break
                else:
                    dummy = None

            else:
                print("Please choose a value from the list")
                print("")

                input("<To continue, please press Enter>")
                print("")

        else:
            print("Please choose a value from the list")
            print("")

            input("<To continue, please press Enter>")
            print("")


# This function does not allow the user to return to the previous menu this function does not allow the user to
# return to navigate freely between the different menu levels (only forward navigation). This function is for linear
# menus, such as for analyzes that ask the user for input. Other than handling input differently, it is not different
# from the open_menu_undirected function

def open_menu_directed(menu_content_dict, parent_menu_func=None):
    while True:

        print(text_general_title())

        # below: displays the menu

        menu_entries = menu_content_dict()["menu_entries"]
        system("cls")

        menu_titel = menu_content_dict()["menu_displayed_text"][0]
        menu_request = menu_content_dict()["menu_displayed_text"][1]
        menu_header = menu_content_dict()["menu_displayed_text"][2]
        menu_input_text = menu_content_dict()["menu_displayed_text"][3]

        print(menu_titel)
        print("")

        print(menu_request)
        print("")

        # Print menu_header in one line
        # the number of columns is adjusted automatically based on the amount elements in menu_header

        print("{:<4}".format(menu_header[0]), end='')
        for header in menu_header[1:]:
            print("{:<65}".format(header), end='')
        print("\n")

        # Print menu_entries in multiple lines
        # the number of columns is adjusted automatically based on the number of elements in menu_entries[n]

        for index, item in enumerate(menu_entries, 1):
            print("{:<4}".format(index), end='')
            for i, entry in enumerate(item[:-1]):
                if i != 1:  # Skip printing menu_entries[1]
                    print("{:<65}".format(entry), end='')
            print(item[-1])

        print("")

        userInput_menuSelection = input(menu_input_text)
        print("")

        system("cls")

        # below: handles the user input

        if str(userInput_menuSelection) != "" and str.isdigit(userInput_menuSelection):
            userInput_menuSelection_int = int(userInput_menuSelection) - 1

            if 0 <= userInput_menuSelection_int < len(menu_entries):
                system("cls")

                result = menu_entries[userInput_menuSelection_int][1]

                system("cls")

                if isinstance(result(), dict):
                    # Push the current menu to the stack and navigate to the new menu
                    menu_stack.append({
                        "menu_entries_func": menu_content_dict,
                        "parent_menu_func": parent_menu_func
                    })
                    open_menu_directed(result, menu_content_dict)
                    break
                else:
                    dummy = None

            else:
                print("Please choose a value from the list")
                print("")

                input("<To continue, please press Enter>")
                print("")

        else:
            print("Please choose a value from the list")
            print("")

            input("<To continue, please press Enter>")
            print("")


# this function is only for displaying the contents of the given dictionary (headers and entries)
# this functions is used for displaying the results of the analysis or pattern searches

def open_menu_display_results(results_dict):

    print(text_general_title())

    # below: displays the menu

    menu_entries = results_dict()["results"]
    system("cls")

    menu_titel = results_dict()["menu_displayed_text"][0]
    menu_request = results_dict()["menu_displayed_text"][1]
    menu_header = results_dict()["menu_displayed_text"][2]
    menu_input_text = results_dict()["menu_displayed_text"][3]

    print(menu_titel)
    print("")

    print(menu_request)
    print("")

    # Extract the strings from the "menu_displayed_text" list for comparison
    text_list = [item for item in results_dict()["menu_displayed_text"][2] if isinstance(item, str)]

    # Include the longest length from the "menu_displayed_text" list in the comparison
    longest_length = max(len(item) for item in text_list)

    # Iterate through each sublist in the "results" list
    for sublist in results_dict()["results"]:
        # Iterate through each value in the sublist
        for value in sublist:
            # Check if the value is a string and if its length is longer than the current longest length
            if isinstance(value, str) and len(value) > longest_length:
                longest_length = len(value)

    minimum_length = 10
    longest_length += 5

    if longest_length < minimum_length:

        longest_length = minimum_length

    # Print menu_header in one line
    # the number of columns is adjusted automatically based on the amount elements in menu_header

    print("{:<4}".format(menu_header[0]), end='')
    for header in menu_header[1:]:
        print("{:<{}}".format(header, longest_length), end='')
    print("\n")

    # Print menu_entries in multiple lines the number of columns is adjusted automatically based on the number of
    # elements in menu_entries[n] this function does not, other than open_menu_undirected() and open_menu_directed(),
    # exlude the second column from being printed as its entries are assumed to be only text (and no functions).

    for index, item in enumerate(menu_entries, 1):
        print("{:<4}".format(index), end='')
        for i, entry in enumerate(item[:-1]):
            print("{:<{}}".format(entry, longest_length), end='')
        print(item[-1])

    print("")

    # below: mainly used for the user to press enter to continue to the next display. The function returns the user
    # input. The userinput is not checked whether the input is within the expected values. If the input is not within
    # the expected values, the function open_menu_display_results() can be called again with the same input.

    return input(menu_input_text)

open_menu_display_results(example_analysis_results)