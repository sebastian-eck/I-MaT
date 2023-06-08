"""
This module handles various types of menu displays and data presentations within a CLI.

This Python module is designed to create and manage a menu interface in a console environment. The module has functions
for displaying different types of menus, handling user navigation, and displaying results. It uses pandas for handling
and displaying data in a tabular format.

Module-level variables:
----------------------
menu_stack : list
    A stack to keep track of the previous menus. This stack is used to enable backward and forward navigation in
    undirected menus.

Functions:
----------
- display_menu_undirected(menu_content_dict: Dict, parent_menu_func: Optional[Callable] = None) -> None
- display_menu_directed(menu_content_dict: Dict) -> None
- display_menu_print_results(results_dict: Dict) -> None
- display_menu_print_textblock(text_dict: Dict) -> None
- print_textblock(menu_columns_description: list, menu_entries: [list, list, ...]) -> None
- save_data_in_pd_dataset(menu_entries: List[Tuple], menu_header: List[str]) -> pd.DataFrame
- print_pd_dataset_entries(dataset: pd.DataFrame) -> None
- print_menu_entries(menu_entries: List[Tuple], menu_header: List[str]) -> None
- example_menu_entries_dict() -> Dict
- example_analysis_results_dict() -> Dict
- example_text_dict() -> Dict
"""

import shutil
import textwrap
from os import system

import pandas as pd

from i_mat_new.src.cli.cli_menu_entries import startmenu_entries
from i_mat_new.src.cli.cli_menu_static_text import text_general_title

from lorem_text import lorem

menu_stack = []  # Stack to keep track of the previous menus


def display_menu_undirected(menu_content_dict, parent_menu_func=None):
    """
    Display a menu allowing the user to navigate between different levels.

    This function takes a dictionary that represents the current menu and an optional function that
    represents the parent menu. This function allows the user to navigate freely between the different menu levels.
    This includes both backward and forward navigation.

    Parameters
    ----------
    menu_content_dict : function
        A function returning a dictionary that contains information about the menu entries and displayed texts.
    parent_menu_func : function, optional
        A function returning a dictionary representing the parent menu from which the current menu was accessed.

    Returns
    -------
    None

    See Also
    --------
    display_menu_directed : For displaying menus with only forward navigation.

    Examples
    --------
    Here is an example of how to use `display_menu_undirected`.
    In this scenario, a variety of outcomes occur based on the user's selection:

    1. If a function that returns a dictionary (representing a new menu structure) is selected by the user,
       such as `submenu_entries_dict`, a sublevel menu is entered.
    2. If the user selects a function, such as `some_function`, the function is executed and after its execution,
       the user will find themselves back in the menu where the function was selected.
    3. If the user selects the "BACK: Return to the last menu" option, they are returned to the parent menu.
    4. If the user selects the "MAIN: Return to the main menu" option, they are returned to the main menu.

    >>> example_menu_entries_dict = {
    ...     "menu_displayed_text": [
    ...         "Menu Titel",
    ...         "Please select one of the following menu options by entering the corresponding index number:",
    ...         ["Menu item titel", "<Short Explanation>"],
    ...         "Which menu item should be executed? (<No. of menu item>): "
    ...     ],
    ...     "menu_entries": [
    ...         ["ABBR: Option 1 titel", example_submenu_entries_dict, "<Goes to submenu>"],
    ...         ["ABBR: Option 2 titel", example_some_function, "<Executes some function>"],
    ...         ["ABBR: Option 3 titel", example_another_function, "<Executes another function>"],
    ...         ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
    ...         ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
    ...     ]
    ... }
    ...
    >>> display_menu_undirected(example_menu_entries_dict)
    """
    while True:

        # below: displays the menu

        print(text_general_title())

        first_level_menu_entries = startmenu_entries

        menu_entries = menu_content_dict()["menu_entries"]
        system("cls")

        menu_titel = menu_content_dict()["menu_displayed_text"][0]
        menu_request = menu_content_dict()["menu_displayed_text"][1]
        menu_columns_description = menu_content_dict()["menu_displayed_text"][2]
        menu_input_text = menu_content_dict()["menu_displayed_text"][3]

        print(menu_titel)
        print("")

        print(menu_request)
        print("")

        print_menu_entries(menu_entries, menu_columns_description)

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
                        display_menu_undirected(previous_menu["menu_entries_func"], previous_menu["parent_menu_func"])
                        break
                    elif result == 'main-menu':
                        # Clear the menu stack and navigate to the main menu
                        menu_stack.clear()
                        # Recursive call with the main menu entries function
                        display_menu_undirected(first_level_menu_entries)
                        break
                elif isinstance(result(), dict):
                    # if the result is a dict, call the function with the display_menu_undirected function with the result
                    # Push the current menu to the stack and navigate to the new menu
                    menu_stack.append({
                        "menu_entries_func": menu_content_dict,
                        "parent_menu_func": parent_menu_func
                    })
                    # if the result is not a dict, the function is called by executing isinstance(result(), dict)
                    display_menu_undirected(result, menu_content_dict)
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
# from the display_menu_undirected function

def display_menu_directed(menu_content_dict):
    """
    Display a menu allowing the user to navigate only forward between different levels.

    This function takes a dictionary that represents the current menu. Unlike `display_menu_undirected`, this function
    does not allow the user to return to the previous menu, and is hence suitable for linear menus, such as analyses
    that require user input.

    Parameters
    ----------
    menu_content_dict : function
        A function returning a dictionary that contains information about the menu entries and displayed texts.

    Returns
    -------
    None

    See Also
    --------
    display_menu_undirected : For displaying menus with both backward and forward navigation.

    Examples
    --------
    Here is an example of how to use `display_menu_directed`:

    >>> example_linear_menu_entries_dict()
    ...{
    ...    "menu_displayed_text": [
    ...        "Submenu Header",
    ...        "Please select:",
    ...        ["Menu item", "<Explanation>"],
    ...        "Which menu item should be executed? (<No. of menu item>): "
    ...    ],
    ...    "menu_entries": [
    ...        ["Option 1", example_linear_submenu_entries_dict, "<Goes to submenu (one-directional)>"],
    ...        ["Option 2", example_some_function, "<Executes some function>"],
    ...        ["Option 3", example_another_function, "<Executes some function>"],
    ...    ]
    ...}
    ...
    >>> display_menu_directed(example_linear_menu_entries_dict)
    """
    while True:

        print(text_general_title())

        # below: displays the menu

        menu_entries = menu_content_dict()["menu_entries"]
        system("cls")

        menu_titel = menu_content_dict()["menu_displayed_text"][0]
        menu_request = menu_content_dict()["menu_displayed_text"][1]
        menu_columns_description = menu_content_dict()["menu_displayed_text"][2]
        menu_input_text = menu_content_dict()["menu_displayed_text"][3]

        print(menu_titel)
        print("")

        print(menu_request)
        print("")

        print("directed menu:")

        print_menu_entries(menu_entries, menu_columns_description)

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

                    print("The selected menu item is not valid for your current position.\n"
                          "One reason for this could be that the wrong menu structure was implemented for this menu.\n\n"
                          "Information for Developers:\n\n"
                          "Choose a nonlinear menu, i.e. display_menu_undirected(), instead for constructing this menu.")
                    print("")

                    input("<To continue, please press Enter>")
                    print("")

                elif isinstance(result(), dict):
                    # if the result is a dict, call the function with the display_menu_undirected function with the result
                    display_menu_directed(result)
                    break
                else:
                    # if the result is not a dict, the function is called by executing isinstance(result(), dict)
                    dummy = None
                    break

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


def display_menu_print_results(results_dict):
    """
    Display analysis results in the console.

    This function receives a function that returns a dictionary, which includes a description of the results and
    a list of results entries. The function uses this information to print the content in a formatted manner.

    If the menu entries are already in a pandas DataFrame, it will print them directly.
    Otherwise, it will convert the list of entries into a DataFrame before printing.

    After displaying the results, it requests a user input to continue. The input is not validated.
    The user input does not trigger any further actions within this function itself. However, in the broader context,
    it may be used in conjunction with the `display_menu_undirected()` or `display_menu_undirected()` functions
    to display for example the results of any prior analysis.

    Parameters
    ----------
    results_dict : function
        A function that returns a dictionary containing analysis results.

    Examples
    --------
    Here is how to use `display_menu_print_results`:

    The function `example_analysis_results_dict` generates a dictionary that represents analysis results.
    This dictionary is then passed as a parameter to the `display_menu_print_results` function:

    >>> example_analysis_results_dict = {
    ...     "menu_displayed_text": [
    ...         "Analysis Results",
    ...         "Please see the following analysis results:",
    ...         ["<Identifier>", "<Description>", "<Description>"],
    ...         "<To continue, please press Enter>"
    ...     ],
    ...     "menu_entries_results": [
    ...         ["Result 1", "<Displays the 1st Column>", "<Displays the 2nd Column >"],
    ...         ["Result 2", "<Displays the 1st Column>", "<Displays the 2nd Column >"],
    ...         ["Result 3", "<Displays the 1st Column>", "<Displays the 2nd Column >"],
    ...     ]
    ... }
    ...
    >>> display_menu_print_results(example_analysis_results_dict)
    """
    print(text_general_title())

    # below: displays the menu

    menu_entries = results_dict()["menu_entries_results"]
    system("cls")

    menu_titel = results_dict()["menu_displayed_text"][0]
    menu_request = results_dict()["menu_displayed_text"][1]
    menu_columns_description = results_dict()["menu_displayed_text"][2]
    menu_input_text = results_dict()["menu_displayed_text"][3]

    print(menu_titel)
    print("")

    print(menu_request)
    print("")

    if isinstance(menu_entries, pd.DataFrame):
        print_pd_dataset_entries(menu_entries)

    else:
        pd_dataset = save_data_in_pd_dataset(menu_entries, menu_columns_description)
        print_pd_dataset_entries(pd_dataset)

    input(menu_input_text)


def display_menu_print_textblock(text_dict):
    """
    This function prints a formatted text block based on a provided dictionary.

    The text_dict should be a dictionary that contains two key-value pairs:
    1. "menu_displayed_text": A list containing the menu title, request, columns description, and input prompt.
    2. "menu_entries_text": A list containing pairs of title and corresponding text messages to be displayed.

    After displaying the menu title, request, and each message in the text block,
    the function waits for user input before continuing.

    Parameters
    ----------
    text_dict : dict
        A dictionary containing menu-related texts.

    Examples
    --------
    >>> example_dict = example_text_dict()
    >>> display_menu_print_textblock(example_dict)

    The command above will display the following output in the console:

    I-MaT - Interactive Music Analysis Tool, Version 2.2, January 2022

    Project Title: "Computer-Assisted Music Analysis"

    Fellowship for Innovations in Digital University Teaching (University of Music Franz Liszt Weimar)

    ----------------------------------------------------------------------

                       -- message to the user --

    Please read the following message:

                   Message

    Message 1      incidunt quo id modi praesentium animi vero adipisci quaerat nam vel eum ex
                   accusantium totam consequatur error perferendis distinctio veniam corrupti
                   expedita dolorum eligendi magni voluptatum aut non officiis tenetur asperiores
                   neque sunt rerum quam voluptatem est aperiam obcaecati vitae aspernatur tempore
                   doloremque blanditiis iusto laborum unde debitis delectus dicta inventore libero
                   at odio dolor reprehenderit itaque nostrum voluptate quas

    Message 2      odit blanditiis illo quae asperiores quod facere omnis dolore distinctio atque
                   ratione delectus mollitia iste consequuntur ipsam provident explicabo sequi
                   consectetur nihil iusto impedit eveniet porro corporis tempora esse libero non
                   excepturi

    Message 3      quam mollitia sapiente sunt neque quo odit qui esse ducimus eum nobis minus
                   possimus tempora reprehenderit soluta sint perferendis illo optio accusantium
                   dolorum recusandae quae deserunt laboriosam impedit quidem maiores reiciendis
                   error in incidunt dicta ea nostrum a ipsam omnis

    <To continue, please press Enter>
    """
    print(text_general_title())

    # below: displays the menu

    menu_entries = text_dict()["menu_entries_text"]
    system("cls")

    menu_titel = text_dict()["menu_displayed_text"][0]
    menu_request = text_dict()["menu_displayed_text"][1]
    menu_columns_description = text_dict()["menu_displayed_text"][2]
    menu_input_text = text_dict()["menu_displayed_text"][3]

    print(menu_titel)
    print("")

    print(menu_request)
    print("")

    print_textblock(menu_columns_description, menu_entries)

    input(menu_input_text)


def print_textblock(menu_columns_description: list, menu_entries: [list, list, ...]):
    first_col_width = max(
        len(entry[0]) for entry in menu_entries) + 5  # Or however wide you want the title column to be
    message_col_width = 80  # Or however wide you want the message column to be
    # Print each column name
    print(f"{'':{first_col_width}} {menu_columns_description[1]}")
    print("")
    # Now print each menu item, wrapped if it exceeds 80 characters.
    for row in menu_entries:
        title, message = row
        wrapped_message = textwrap.fill(message, message_col_width)
        for i, second_col_line in enumerate(wrapped_message.split('\n')):
            if i == 0:
                print(f"{title:{first_col_width}} {second_col_line}")
            else:
                print(f"{'':{first_col_width}} {second_col_line}")
        print("")  # Empty line after each message


def print_pd_dataset_entries(dataset):
    # Set the index of the DataFrame to start from 1
    dataset.index = range(1, len(dataset) + 1)

    # Rename the index column as "No."
    dataset.index.name = "No."

    # Reset the DataFrame's index to become a regular column
    dataset.reset_index(inplace=True)

    # Set the display options for the DataFrame
    pd.set_option('display.max_colwidth', None)  # Set the maximum cell width to None for text wrapping
    pd.set_option('display.unicode.ambiguous_as_wide', True)  # Enable full-width characters
    pd.set_option('display.colheader_justify', 'left')  # Left-align column headers

    # Get the width of the command window dynamically
    terminal_width, _ = shutil.get_terminal_size()
    pd.set_option('display.width', terminal_width)

    # Print the DataFrame with left-aligned "No." index
    print(dataset.to_string(justify='left', col_space=10, index=False, formatters={'No.': lambda x: f'{x:<4}'}))
    print("")


def save_data_in_pd_dataset(menu_entries, menu_header):
    return pd.DataFrame(menu_entries, columns=menu_header)


def print_menu_entries(menu_entries, menu_header):
    # Print menu_header in one line
    # the number of columns is adjusted automatically based on the amount elements in menu_header
    print("{:<4}".format("No."), end='')
    for header in menu_header:
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


def example_mainmenu_entries_dict():
    """
    Generate a representative dictionary for menu entries.

    This function creates and returns a dictionary that simulates a menu.
    This dictionary is structured to be used by the `display_menu_undirected()` function.
    The dictionary includes the text displayed for the menu and a list of menu entries.

    The "menu_displayed_text" field in the dictionary includes a title for the menu, an instruction for selection,
    a representative entry layout, and a prompt for the user's choice.

    The "menu_entries" field is a list of potential options available in the menu. Each entry is a list itself,
    with the first element being a brief description of the entry, the second element being the function that will be
    executed when this entry is selected, and the third element being a more detailed explanation of what the entry does.

    When the `display_menu_undirected()` function uses this dictionary:
    - If a submenu is selected (e.g., "ABBR: Option 1 titel"), the corresponding function (e.g., `example_submenu_entries_dict()`)
    is expected to return another dictionary that represents the submenu. The function will then recursively call itself with
    the new dictionary, thus entering the submenu.
    - If a regular function is selected (e.g., "ABBR: Option 2 titel"), the corresponding function (e.g., `example_some_function()`) is executed.
    - If the 'back' option is selected, the `display_menu_undirected()` function will return, reverting to the previous menu.
    - If the 'main-menu' option is selected, the `display_menu_undirected()` function will return all the way up to the main menu.

    Returns
    -------
    dict
        A dictionary that simulates a menu. The dictionary includes the following keys:
        "menu_displayed_text": A list including a title, instructions for selection, a sample entry layout, and a prompt for user input.
        "menu_entries": A list of possible selections. Each entry is itself a list, including a brief description, the function to execute,
        and a more detailed explanation.

    Example
    -------
    >>> example_mainmenu_entries_dict()
    ...{
    ...    "menu_displayed_text": [
    ...        "Menu Titel",
    ...        "Please select one of the following menu options by entering the corresponding index number:",
    ...        ["Menu item titel", "<Short Explanation>"],
    ...         "Which menu item should be executed? (<No. of menu item>): "
    ...    ],
    ...     "menu_entries": [
    ...         ["ABBR: Option 1 titel", example_submenu_entries_dict, "<Goes to submenu>"],
    ...        ["ABBR: Option 2 titel", example_some_function, "<Executes some function>"],
    ...        ["ABBR: Option 3 titel", example_another_function, "<Executes another function>"],
    ...        ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
    ...        ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
    ...    ]
    ...}
    """
    return {
        "menu_displayed_text": [
            "Menu Titel",
            "Please select one of the following menu options by entering the corresponding index number:",
            ["Menu item titel", "<Short Explanation>"],
            "Which menu item should be executed? (<No. of menu item>): "
        ],
        "menu_entries": [
            ["ABBR: Option 1 titel", example_submenu_entries_dict, "<Goes to submenu>"],
            ["ABBR: Option 2 titel", example_some_function, "<Executes some function>"],
            ["ABBR: Option 3 titel", example_another_function, "<Executes another function>"],
            ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
            ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
        ]
    }


def example_submenu_entries_dict():
    """
    Generate a representative dictionary for submenu entries.

    This function creates and returns a dictionary that simulates a submenu. This dictionary is structured to be used by the
    `display_menu_undirected()` function. The dictionary includes the text displayed for the submenu and a list of submenu entries.

    The "menu_displayed_text" field in the dictionary includes a title for the submenu, an instruction for selection, a representative
    entry layout, and a prompt for the user's choice.

    The "menu_entries" field is a list of potential options available in the submenu. Each entry is a list itself, with the first element
    being a brief description of the entry, the second element being the function that will be executed when this entry is selected,
    and the third element being a more detailed explanation of what the entry does.

    When the `display_menu_undirected()` function uses this dictionary:
    - If another submenu is selected (e.g., "ABBR: Option 1 titel"), the corresponding function (e.g., `example_sub_submenu_entries_dict()`)
    is expected to return yet another dictionary that represents the sub-submenu. The function will then recursively call itself with
    the new dictionary, thus entering the sub-submenu.
    - If a regular function is selected (e.g., "ABBR: Option 2 titel"), the corresponding function (e.g., `example_some_function()`) is executed.
    - If the 'back' option is selected, the `display_menu_undirected()` function will return, reverting to the previous submenu or the main menu if it was a top-level submenu.
    - If the 'main-menu' option is selected, the `display_menu_undirected()` function will return all the way up to the main menu.

    Returns
    -------
    dict
        A dictionary that simulates a submenu. The dictionary includes the following keys:
        "menu_displayed_text": A list including a title, instructions for selection, a sample entry layout, and a prompt for user input.
        "menu_entries": A list of possible selections. Each entry is itself a list, including a brief description, the function to execute,
        and a more detailed explanation.

    Example
    -------
    >>> example_submenu_entries_dict()
    ...{
    ...    "menu_displayed_text": [
    ...        "Submenu Title",
    ...        "Please select one of the following submenu options by entering the corresponding index number:",
    ...        ["Submenu item title", "<Short Explanation>"],
    ...        "Which submenu item should be executed? (<No. of menu item>): "
    ...    ],
    ...    "menu_entries": [
    ...        ["ABBR: Sub-Option 1 title", example_sub_submenu_entries_dict, "<Goes to sub-submenu>"],
    ...        ["ABBR: Sub-Option 2 title", example_some_function, "<Executes some function>"],
    ...        ["ABBR: Sub-Option 3 title", example_another_function, "<Executes another function>"],
    ...        ["BACK: Return to the last menu", 'back', "<Returns to the parent submenu or main menu if no parent submenu>"],
    ...        ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
    ...    ]
    ...}
    """
    return {
        "menu_displayed_text": [
            "Menu Titel",
            "Please select one of the following menu options by entering the corresponding index number:",
            ["Menu item titel", "<Short Explanation>"],
            "Which menu item should be executed? (<No. of menu item>): "
        ],
        "menu_entries": [
            ["ABBR: Sub-Option 1 titel", example_sub_submenu_entries_dict, "<Goes to submenu>"],
            ["ABBR: Sub-Option 2 titel", example_some_function, "<Executes demo function>"],
            ["ABBR: Sub-Option 3 titel", example_another_function, "<Executes another function>"],
            ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
            ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
        ]
    }


def example_sub_submenu_entries_dict():
    """
    Generate a representative dictionary for sub-submenu entries.

    This function creates and returns a dictionary that simulates a sub-submenu. This dictionary is structured to be used by the
    `display_menu_undirected()` function. The dictionary includes the text displayed for the sub-submenu and a list of sub-submenu entries.

    Similar to the main menu and submenu dictionaries, it includes two main fields: "menu_displayed_text" and "menu_entries", which provide
    the necessary information for the menu display and interaction in the console.

    As with other menus, user options could include other sub-submenus, functions, or options to return to parent menus.

    Returns
    -------
    None

    Example
    -------
    >>> example_sub_submenu_entries_dict()
    """
    input("this would return a sample sub-submenu dictionary instead of this function.")


def example_analysis_results_dict():
    # todo: rewrite the docstring and include information about what happens when each menu line
    #  (in display_menu_print_results()) is being executed by the function display_menu_print_results()
    """
    Generate a representative dictionary for analysis results.

    This function creates and returns a dictionary that represents analysis results.
    This dictionary can be passed as a parameter to the `display_menu_print_results` function.

    The dictionary includes a description of the results and a list of results entries.
    The "menu_displayed_text" field in the dictionary includes a title for the results,
    a description of the results, a layout for the results' entries, and a prompt for user interaction.

    The "menu_entries_results" field is a list of the actual analysis results.
    Each entry is a list itself, with elements representing different aspects of the result.

    When this dictionary is used by the `display_menu_undirected()` function:
    - Each line of the "menu_entries_results" list will be displayed as a separate line in the console.
    - The user can interact with the prompt specified in the "menu_displayed_text" field.
    - User input does not cause any function calls or navigations within this dictionary, but in the broader context,
    it may be used in conjunction with the `display_menu_undirected()` or `display_menu_undirected()` functions
    to display for example the results of any prior analysis.

    Returns
    -------
    dict
        A dictionary representing analysis results.

    Example
    -------
    >>> example_analysis_results_dict()
    ...{
    ...    "menu_displayed_text": [
    ...        "Analysis Results",
    ...        "Please see the following analysis results:",
    ...        ["<Identifier>", "<Description>", "<Description>"],
    ...        "<To continue, please press Enter>"
    ...    ],
    ...    "menu_entries_results": [
    ...        ["Result 1", "<Displays the 1st Column>", "<Displays the 2nd Column >"],
    ...        ["Result 2", "<Displays the 1st Column>", "<Displays the 2nd Column >"],
    ...        ["Result 3", "<Displays the 1st Column>", "<Displays the 2nd Column >"],
    ...    ]
    ...}

    The command above will display the following output in the console:

    Analysis Results

    Please see the following analysis results:

    | <Identifier> | <Description>             | <Description>              |
    |--------------|---------------------------|----------------------------|
    | Result 1     | <Displays the 1st Column> | <Displays the 2nd Column > |
    | Result 2     | <Displays the 1st Column> | <Displays the 2nd Column > |
    | Result 3     | <Displays the 1st Column> | <Displays the 2nd Column > |

    <To continue, please press Enter>

    """
    return {
        "menu_displayed_text": [
            "Analysis Results",
            "Please see the following analysis results:",
            ["<Identifier>", "<Description>", "<Description>"],
            "<To continue, please press Enter>"
        ],
        "menu_entries_results": [
            ["Result 1", "<Displays the 1st Column>", "<Displays the 2nd Column >"],
            ["Result 2", "<Displays the 1st Column>", "<Displays the 2nd Column >"],
            ["Result 3", "<Displays the 1st Column>", "<Displays the 2nd Column >"],
        ]
    }


def example_text_dict():
    """
        This function generates a dictionary with lorem ipsum text as messages.

        The function generates three lorem ipsum text messages, with 60, 32, and 40 words respectively.
        These messages are used to form the "menu_entries_text" field of the dictionary. The "menu_displayed_text"
        field of the dictionary contains generic text related to the menu.

        Returns
        -------
        dict
            A dictionary with menu texts.

        Examples
        --------
        >>> example_text_dict()
        {
            "menu_displayed_text": [
                "-- message to the user --",
                "Please read the following message:",
                ["", "Message"],
                "<To continue, please press Enter>"
            ],
            "menu_entries_text": [
                ["Message 1", "<60 words lorem ipsum text>"],
                ["Message 2", "<32 words lorem ipsum text>"],
                ["Message 3", "<40 words lorem ipsum text>"],
            ]
        }
        """
    words = 10
    text_1 = lorem.words(60)
    text_2 = lorem.words(32)
    text_3 = lorem.words(40)

    return {
        "menu_displayed_text": [
            "                  -- message to the user --",
            "Please read the following message:",
            ["", "Message"],
            "<To continue, please press Enter>"
        ],
        "menu_entries_text": [
            ["Message 1", text_1],
            ["Message 2", text_2],
            ["Message 3", text_3],
        ]
    }


def example_some_function():
    """
    Example function for menu entry.

    This function is intended to represent the kind of function that could be called from a menu. In this case, it simply requests
    input from the user as a placeholder action. In a more complex application, this could be any function that carries out a specific action.

    Returns
    -------
    None

    Example
    -------
    >>> example_some_function()
    """
    input("This is a sample function.\n")


def example_another_function():
    """
    Another example function for menu entry.

    This function is another example of a function that could be called from a menu. Similar to `example_some_function()`, it merely asks for
    user input as a placeholder action. In a real application, this could be any function that performs a specific task.

    Returns
    -------
    None

    Example
    -------
    >>> example_another_function()
    """
    input("This is another sample function.\n")



def demo_function_1():
    # demonstrates that after executing a function in the directed menu, the directed menu instance will be ended

    display_menu_directed(example_mainmenu_entries_dict)


def demo_function_2():
    # demonstrates the display of text for the user

    display_menu_print_textblock(example_text_dict)


def demo_function_3():
    # demonstrates the display of analysis results

    display_menu_print_results(example_analysis_results_dict)


def demo_menu_structure_dict():
    return {
        "menu_displayed_text": [
            "Menu Titel",
            "Please select one of the following menu options by entering the corresponding index number:",
            ["Menu item titel", "<Short Explanation>"],
            "Which menu item should be executed? (<No. of menu item>): "
        ],
        "menu_entries": [
            ["DEMO: Enter Submenu", example_submenu_entries_dict, "<Goes to submenu>"],
            ["DEMO: Enter directed menu", demo_function_1, "<Enters directed menu structure>"],
            ["DEMO: Display demo text", demo_function_2, "<Displays a text>"],
            ["DEMO: Display demo results", demo_function_3, "<Displays a sample analysis result set>"],
            ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
            ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
        ]
    }


display_menu_undirected(demo_menu_structure_dict)
