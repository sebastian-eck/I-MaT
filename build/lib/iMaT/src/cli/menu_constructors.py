"""
cli.menu_constructors.py
========================

This module is designed to create, manage, and navigate through a menu interface in a console environment.

This Python module is designed to create, manage, and navigate through a menu interface in a console environment.
The module contains functions for constructing and displaying various types of menus (directed and undirected),
handling user navigation, executing menu-associated functions, displaying structured text information, and presenting
analysis results in an organized, readable format.

Module-level variables:
----------------------
menu_stack : list
    A stack to keep track of the previous menus. This stack is used to enable backward and forward navigation in
    undirected menus.

Functions
---------
- display_menu_print_results
- display_menu_print_textblock
- display_menu_request_selection
- display_menu_undirected
- print_menu_entries
- print_textblock
- util_convert_imat_datacont_to_pd_dataframe
- util_convert_pd_dataframe_to_imat_datacont

These functions help in providing a smooth user interface for the command-line operation, ensuring a consistent user
experience, and reducing complexity in navigating the tool's functionalities. By using these functions,
the Interactive Music Analysis Tool (I-MaT) system provides an interactive and user-friendly command-line interface
for music analysis.
"""
import os
import textwrap

import pandas as pd

from iMaT.src.constants import TITLE_TEXT
from iMaT.src.utils.error_handling import handle_error

menu_stack = []  # Stack to keep track of the previous menus


def display_menu_undirected(menu_content_dict: callable, parent_menu_func: callable = None) -> None:
    """
    Display a menu allowing the user to navigate between different levels.

    This function prints an interactive, navigation-capable menu from a dictionary.
    The dictionary represents the current menu, including its title, guidelines, requested input, and menu entries.
    Each menu entry consists of a title, function or menu control keyword, and description.

    This function allows the user to navigate freely between the different menu levels. This includes both backward
    and forward navigation.

    If the user selects a function that returns a dictionary (i.e., a submenu), the function enters a sublevel menu.
    If a function is selected, the function is executed and after its execution, the user will find themselves back
    in the menu. The user can also return to the parent menu or the main menu by selecting the appropriate options.

    Parameters
    ----------
    menu_content_dict : function
        A function returning a dictionary that contains information about the menu entries and displayed texts.
    parent_menu_func : function, optional
        A function returning a dictionary representing the parent menu from which the current menu was accessed.

    Returns
    -------
    None

    Examples
    --------

    This is a usage example where we consider four types of entries in our menu:
    going to a submenu, executing a function, and returning to the main menu or a parent menu.

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
    ...         "Which menu item should be executed? (<No. of menu item>): ",
    ...         ["Menu item titel", "<Short Explanation>"],
    ...     ],
    ...     "menu_entries": [
    ...         ["ABBR: Option 1 titel", example_submenu_entries_dict, "<Goes to submenu>"],
    ...         ["ABBR: Option 2 titel", example_some_function, "<Executes some function>"],
    ...         ["ABBR: Option 3 titel", example_another_function, "<Executes another function>"],
    ...         ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
    ...     ]
    ... }
    ...
    >>> display_menu_undirected(example_menu_entries_dict)
    """
    try:
        while True:

            os.system("cls" if os.name == "nt" else "clear")
            # below: displays the menu

            print(TITLE_TEXT)

            #first_level_menu_entries = start_menu_entries

            menu_entries = menu_content_dict()["menu_entries"]

            menu_title = menu_content_dict()["menu_displayed_text"][0]
            menu_guideline = menu_content_dict()["menu_displayed_text"][1]
            menu_requested_input = menu_content_dict()["menu_displayed_text"][2]
            menu_columns_description = menu_content_dict()["menu_displayed_text"][3]

            print(menu_title)
            print("")

            print(menu_guideline)
            print("")

            print_menu_entries(menu_columns_description, menu_entries)

            userInput_menuSelection = input(menu_requested_input)
            print("")

            # below: handles the user input

            if str(userInput_menuSelection) != "" and str.isdigit(userInput_menuSelection):
                userInput_menuSelection_int = int(userInput_menuSelection) - 1

                if 0 <= userInput_menuSelection_int < len(menu_entries):

                    result = menu_entries[userInput_menuSelection_int][1]

                    if isinstance(result, tuple):
                        # If the result is a tuple, we consider it as (function, arguments)

                        function, args = result
                        function(args)

                    elif not callable(result):
                        if result == 'back' and menu_stack:
                            # Pop the previous menu from the stack and navigate to it
                            previous_menu = menu_stack.pop()
                            # Recursive call with the parent menu entries function and the parent of the parent menu
                            display_menu_undirected(previous_menu["menu_entries_func"], previous_menu["parent_menu_func"])
                            break

                    elif isinstance(result, tuple):
                        # If the result is a tuple, we consider it as (function, arguments)

                        function, args = result
                        function(args)
                    elif isinstance(result(), dict):
                        # if the result is a dict, call the function with the display_menu_undirected function with the
                        # result Push the current menu to the stack and navigate to the new menu
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

    except Exception as e:
        handle_error(e)


def display_menu_request_selection(imat_data_container: dict, min_column_width = 20) -> str:
    """
    Display menu items in a console in a formatted manner.

    This function receives a dictionary, which includes a description of the menu items and a
    list of menu entries. The function uses this information to print the content in a well-formatted manner.

    The menu items are displayed in the order they are present in the dictionary. After the menu items are displayed,
    the function requests user input to choose a menu item. The input is validated to make sure it is a valid choice
    from the menu items. The function then returns the corresponding "string to return" of the chosen menu item.

    Parameters
    ----------
    imat_data_container : dict
        A dictionary containing the menu items of an analysis.

    Returns
    -------
    str
        The "string to return" of the chosen menu item.

    Examples
    --------
    Here is how to use `display_menu_print_results`.
    In this example, we have a dictionary `imat_data_container` that represents the menu items.

    >>> imat_data_container = {
    ...     "menu_displayed_text": [
    ...         "Menu Title",
    ...         "Please select one of the following menu options by entering the corresponding index number:",
    ...         "Which menu item do you want to select? (<No. of menu item>): ",
    ...         ["Menu item title", "<Short Explanation>"],
    ...     ],
    ...     "menu_entries": [
    ...         ["ABBR: Option 1 title", "string to return 1", "<Returns option 1>"],
    ...         ["ABBR: Option 2 title", "string to return 2", "<Returns option 2>"],
    ...         ["ABBR: Option 3 title", "string to return 3", "<Returns option 3>"],
    ...     ]
    ... }

    >>> display_menu_request_selection(imat_data_container, min_column_width)

    Note: the actual output of `display_menu_print_results` depends on the dictionary `imat_data_container`.
    """
    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear")

            print(TITLE_TEXT)

            # below: displays the menu

            menu_entries = imat_data_container["menu_entries"]

            menu_title = imat_data_container["menu_displayed_text"][0]
            menu_guideline = imat_data_container["menu_displayed_text"][1]
            menu_requested_input = imat_data_container["menu_displayed_text"][2]
            menu_columns_description = imat_data_container["menu_displayed_text"][3]

            print(menu_title)
            print("")

            print(menu_guideline)
            print("")

            print_menu_entries(menu_columns_description, menu_entries, min_col_width=20)

            user_choice = input(menu_requested_input)

            # Validate the user's input
            if user_choice.isdigit() and 0 <= int(user_choice) - 1 < len(menu_entries):
                return menu_entries[int(user_choice) - 1][1]

            print("\nInvalid choice. Please choose a valid menu item.\n")
            input("<To continue, please press Enter>")

    except Exception as e:
        handle_error(e)


def display_menu_print_results(results_dict: dict) -> str:
    """
    Display analysis results in a console in a formatted manner.

    This function receives a dictionary, which includes a description of the results and a
    list of result entries. The function uses this information to print the content in a well-formatted manner.

    Note that if the results are stored in a pandas DataFrame, they need to be converted to an I-MaT data container
    using `util_convert_pd_dataframe_to_imat_datacont()` function before being passed to this function.

    The results are displayed in the order they are present in the dictionary. After the results are displayed,
    the function requests user input to continue. However, the input does not trigger any further actions within
    this function itself. Yet, when used in combination with the `display_menu_undirected()` function, this user input may serve as a pause before navigating to other parts of a broader workflow,
    such as exporting results or returning to the respective parent menu.

    Parameters
    ----------
    results_dict : dict
        A dictionary containing the results of an analysis. If the results are saved within a pandas DataFrame,
        they need to be converted to an I-MaT data container using `util_convert_pd_dataframe_to_imat_datacont()`.

    Returns
    -------
    str
        The user input collected after displaying the text block.

    See Also
    --------
    display_menu_undirected : For displaying menus with both backward and forward navigation.
    util_convert_pd_dataframe_to_imat_datacont : For converting pandas DataFrame to I-MaT data container
    before passing to this function.

    Examples
    --------
    Here is how to use `display_menu_print_results`.
    In this example, we have a pandas DataFrame `df` that needs to be converted to an I-MaT data container before being
    passed to the `display_menu_print_results` function.

    >>> df = pd.DataFrame({'col1': ['Result 1', 'Result 2', 'Result 3'],
    ...                    'col2': ["<Displays the 1st Column>", "<Displays the 1st Column>", "<Displays the 1st Column>"],
    ...                    'col3': ["<Displays the 2nd Column>", "<Displays the 2nd Column>", "<Displays the 2nd Column>"]})

    >>> results_dict = util_convert_pd_dataframe_to_imat_datacont(df)

    >>> display_menu_print_results(results_dict, print_all_columns=True)

    A I-MaT data container can directly be passed to the `display_menu_print_results` function:

    >>> imat_data_container = {
    ...    "menu_displayed_text": [
    ...        "Analysis Results",
    ...        "Please see the following analysis results:",
    ...        "<To continue, please press Enter>",
    ...        ["<Identifier>", "<Description>", "<Description>"],
    ...    ],
    ...    "menu_entries_results": [
    ...        ["Result 1", "<Displays the 1st Column>", "<Displays the 2nd Column >"],
    ...        ["Result 2", "<Displays the 1st Column>", "<Displays the 2nd Column >"],
    ...        ["Result 3", "<Displays the 1st Column>", "<Displays the 2nd Column >"],
    ...    ]
    ...}

    >>> display_menu_print_results(imat_data_container, print_all_columns=True)

    Note: the actual output of `display_menu_print_results` depends on the dictionary created by
    `util_convert_pd_dataframe_to_imat_datacont()` and would show three result lines in this case.
    """
    try:
        os.system("cls" if os.name == "nt" else "clear")

        if isinstance(results_dict, pd.DataFrame):
            results_dict = util_convert_pd_dataframe_to_imat_datacont(results_dict)

        print(TITLE_TEXT)

        # below: displays the menu

        menu_entries = results_dict["menu_entries_results"]

        menu_title = results_dict["menu_displayed_text"][0]
        menu_guideline = results_dict["menu_displayed_text"][1]
        menu_requested_input = results_dict["menu_displayed_text"][2]
        menu_columns_description = results_dict["menu_displayed_text"][3]

        print(menu_title)
        print("")

        print(menu_guideline)
        print("")

        print_menu_entries(menu_columns_description, menu_entries, 15, print_all_columns=True)

        return input(menu_requested_input)

    except Exception as e:
        handle_error(e)


def display_menu_print_textblock(text_dict: dict, textblock_sep_line=True) -> str:
    """
    Prints a formatted text block in the console based on a provided dictionary.

    This function takes a dictionary which includes a title, a request, column descriptions, and an input prompt,
    as well as a list of text entries to display. It uses this information to print the content in a formatted
    manner on the console.

    The text_dict should be a dictionary that contains two key-value pairs:
    1. "menu_displayed_text": A list containing the menu title, request, columns description, and input prompt.
    2. "menu_entries_text": A list containing pairs of title and corresponding text messages to be displayed.

    After displaying the text blocks, it requests a user input to continue. The input is not validated
    and does not trigger any further actions within this function itself.

    Parameters
    ----------
    text_dict : dict
        A dictionary containing custom text for display.
    textblock_sep_line : bool
        If True, a separator line is printed after each text block.

    Returns
    -------
    str
        The user input collected after displaying the text block.

    See Also
    --------
    print_textblock : function that prints out a block of text given in a list or a single string.
    example_text_dict : function that generates a dictionary representing text content.

    Examples
    --------
    Here is how to use `display_menu_print_textblock`:

    The function `example_text_dict` generates a dictionary that represents a text block to be displayed.
    This dictionary is then passed as a parameter to the `display_menu_print_textblock` function:

    >>>     example_text_dict {
    ...         "menu_displayed_text": [
    ...             "-- message to the user --",
    ...             "Please read the following message:",
    ...             "<To continue, please press Enter>",
    ...             ["", "Message"],
    ...         ],
    ...         "menu_entries_text": [
    ...             ["Message 1", "Textblock 1"],
    ...             ["Message 2", "Textblock 2"],
    ...             ["Message 3", "Textblock 3"],
    ...         ]
    ...     }
    >>> display_menu_print_textblock(example_text_dict)
    """
    try:
        os.system("cls" if os.name == "nt" else "clear")

        print(TITLE_TEXT)

        # below: displays the menu

        menu_title = text_dict["menu_displayed_text"][0]
        menu_guideline = text_dict["menu_displayed_text"][1]
        menu_requested_input = text_dict["menu_displayed_text"][2]
        menu_columns_description = text_dict["menu_displayed_text"][3]

        print(menu_title)
        print("")

        print(menu_guideline)
        print("")

        print_textblock(menu_columns_description, text_dict["menu_entries_text"], textblock_sep_line)

        return input(menu_requested_input)

    except Exception as e:
        handle_error(e)


def print_textblock(menu_columns_description: list, menu_entries: list[list], textblock_sep_line=True) -> None:
    """
    Prints a formatted text block in the console.

    This function takes in a description for menu columns, a list of menu entries, and a boolean indicating whether
    to separate text blocks with a line. It uses this information to print a formatted text block on the console.

    The function is used as a helper within `display_menu_print_textblock` which not only prints the text but also
    displays a full menu above the printed text. However, `print_textblock` can be independently used to print text
    without displaying a full menu.

    Parameters
    ----------
    menu_columns_description : list
        A list containing column descriptions. For instance, ["<Identifier>", "<Description>"].
    menu_entries : list
        A list of lists where each sublist contains the title and message for a text block.
    textblock_sep_line : bool, optional
        If True, a separator line is printed after each text block. By default, it is set to True.

    Returns
    -------
    None

    See Also
    --------

    display_menu_print_textblock : For displaying custom text blocks using the same structure as a menu.

    Examples
    --------
    Here is how to use `print_textblock`:

    >>> menu_columns_description = ["", "Message"]
    >>> menu_entries = [
    ...     ["Message 1", "Textblock 1"],
    ...     ["Message 2", "Textblock 2"],
    ...     ["Message 3", "Textblock 3"],
    ... ]
    >>> print_textblock(menu_columns_description, menu_entries)
    """
    try:
        first_col_width = max(max(len(entry[0]) for entry in menu_entries), len(menu_columns_description[0])) + 5
        # "+5": Or however wide you want the title column to be

        message_col_width = 80  # Or however wide you want the message column to be
        # Print each column name
        print(f"{menu_columns_description[0]}{'':{first_col_width-len(menu_columns_description[0])}} {menu_columns_description[1]}")
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

            if textblock_sep_line:
                print("")  # Empty line after each message

        if not textblock_sep_line:
            print("")

    except Exception as e:
        handle_error(e)


def print_menu_entries(menu_columns_description: list, menu_entries: list[list], min_col_width=45, print_all_columns=False) -> None:
    """
    Prints a formatted list of menu entries in the console.

    This function takes a list of menu entries and column descriptions, along with an optional minimum column width.
    It formats and prints the entries in a table-like structure. An additional optional parameter controls whether all
    columns or all but the second column are printed.

    This function is used as a helper within `display_menu_undirected` and `display_menu_print_results` for displaying menu options or analysis results. However, `print_menu_entries`
    can also be used independently to print a list of results or menu entries without displaying a full menu.

    Parameters
    ----------
    menu_columns_description : list
        A list containing column descriptions.
    menu_entries : list[list]
        A list of menu entries. Each entry is a list itself containing strings representing each column's data.
    min_col_width : int, optional
        Minimum width for each column. Default is 45.
    print_all_columns : bool, optional
        If True, all columns are printed. If False (default), all columns but the second one are printed.

    Returns
    -------
    None

    See Also
    --------
    display_menu_undirected : For displaying menus with both backward and forward navigation.
    display_menu_print_results : For displaying a list of analysis results.

    Examples
    --------
    Here is how to use `print_menu_entries`:

    >>> menu_columns_description = ["<Identifier>", "<Description>", "<Description>"]
    >>> menu_entries = [
    ...        ["Result 1", "<Displays the 1st Column>", "<Displays the 2nd Column>"],
    ...        ["Result 2", "<Displays the 1st Column>", "<Displays the 2nd Column>"],
    ...        ["Result 3", "<Displays the 1st Column>", "<Displays the 2nd Column>"],
    ...    ]
    >>> print_menu_entries(menu_columns_description, menu_entries, print_all_columns=True)
    """
    try:
        additional_col_width = 5

        if not print_all_columns:
            menu_entries = [entry[:1] + entry[2:] for entry in menu_entries]

        # Transpose menu_entries
        menu_entries_transposed = list(map(list, zip(*menu_entries)))

        # Create list of column widths
        col_widths = [max(min_col_width, max(len(str(item)) for item in col)) + additional_col_width
                      for col in menu_entries_transposed]

        # Add headers to col_widths calculation
        col_widths = [max(w, len(header)) for w, header in zip(col_widths, menu_columns_description)]

        # Print menu_columns_description in one line
        print("{:<8}".format("No."), end='  ')
        for header, width in zip(menu_columns_description, col_widths):
            print("{:<{}}".format(header, width), end='  ')
        print("\n")

        # Print menu_entries in multiple lines
        for index, item in enumerate(menu_entries, 1):
            print("{:<8}".format(index), end='  ')
            for i, (entry, width) in enumerate(zip(item, col_widths)):
                print("{:<{}}".format(entry, width), end='  ')
            print()
        print("")

    except Exception as e:
        handle_error(e)


def util_convert_pd_dataframe_to_imat_datacont(pd_dataframe: pd.DataFrame,
                                               menu_title: str = "Analysis Results",
                                               menu_guideline: str = "Please see the following analysis results:",
                                               menu_requested_input: str = "<To continue, please press Enter>",
                                               menu_columns_description: list[str] = None) -> dict:
    """
    Converts a pandas DataFrame to an I-MaT data container format.

    This function converts a pandas DataFrame into a data format compatible with I-MaT's display functions. It's
    particularly useful for preparing data to be displayed in the console via `display_menu_print_results()`.

    Parameters
    ----------
    pd_dataframe : pd.DataFrame
        DataFrame containing the data to be displayed.
    menu_title : str, optional
        Title for the data display. Defaults to "Analysis Results".
    menu_guideline : str, optional
        Instruction for the user. Defaults to "Please see the following analysis results:".
    menu_requested_input : str, optional
        Prompt for user input. Defaults to "<To continue, please press Enter>".
    menu_columns_description : List[str], optional
        Descriptions for data columns. If not provided, the DataFrame's column names will be used.

    Returns
    -------
    dict
        A dictionary in I-MaT data container format that can be used by the `display_menu_print_results()` function.

    See Also
    --------
    display_menu_print_results: Use this function to display the converted DataFrame in console.
    util_convert_imat_datacont_to_pd_dataframe: For the reverse operation - converting an I-MaT data container
    into a pandas DataFrame before processing.


    Examples
    --------
    >>> df = pd.DataFrame({
    ...     'col1': ['Result 1', 'Result 2', 'Result 3'],
    ...     'col2': ['<Displays the 1st Column>', '<Displays the 1st Column>', '<Displays the 1st Column>'],
    ...     'col3': ['<Displays the 2nd Column>', '<Displays the 2nd Column>', '<Displays the 2nd Column>']
    ... })

    >>> results_dict = util_convert_pd_dataframe_to_imat_datacont(df)
    >>> display_menu_print_results(results_dict)

    This will display a result set with 3 rows in the console. The actual output is determined by the dictionary
    returned from `util_convert_pd_dataframe_to_imat_datacont()`.

    An I-MaT data container created from a DataFrame would look like this:

    >>> def example_analysis_results_dict():
    ...     return {
    ...         "menu_displayed_text": [
    ...             "Analysis Results",
    ...             "Please see the following analysis results:",
    ...             "<To continue, please press Enter>",
    ...             ["<Identifier>", "<Description>", "<Description>"],
    ...         ],
    ...         "menu_entries_results": [
    ...             ["Result 1", "<Displays the 1st Column>", "<Displays the 2nd Column>"],
    ...             ["Result 2", "<Displays the 1st Column>", "<Displays the 2nd Column>"],
    ...             ["Result 3", "<Displays the 1st Column>", "<Displays the 2nd Column>"],
    ...         ]
    ...     }
    """
    try:
        if menu_columns_description is None:
            # if no menu_columns_description is provided, use the DataFrame's column names'
            menu_columns_description = list(pd_dataframe.columns)

        imat_datacont = {
            "menu_displayed_text": [
                menu_title,
                menu_guideline,
                menu_requested_input,
                menu_columns_description,
            ],
            "menu_entries_results": []
        }

        for _, row in pd_dataframe.iterrows():
            imat_datacont["menu_entries_results"].append(list(row))

        return imat_datacont

    except Exception as e:
        handle_error(e)


def util_convert_imat_datacont_to_pd_dataframe(imat_cont: dict) -> pd.DataFrame:
    """
    Converts an I-MaT data container to a pandas DataFrame format.

    This function takes an I-MaT data container and converts it into a pandas DataFrame. It's an excellent way to
    facilitate user-friendly, manual data entry, as the vertical orientation of the I-MaT data container is easier to
    read than a typical pandas DataFrame.

    Parameters
    ----------
    imat_cont : dict
        I-MaT data container dictionary containing the data to be converted into a DataFrame.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the data from the I-MaT data container.

    See Also
    --------
    display_menu_print_results: Use this function to display data from the I-MaT data container.
    util_convert_pd_dataframe_to_imat_datacont: For the reverse operation - converting a pandas DataFrame
    into an I-MaT data container.


    Examples
    --------

        >>> df = pd.DataFrame({
    ...     'col1': ['Result 1', 'Result 2', 'Result 3'],
    ...     'col2': ['<Displays the 1st Column>', '<Displays the 1st Column>', '<Displays the 1st Column>'],
    ...     'col3': ['<Displays the 2nd Column>', '<Displays the 2nd Column>', '<Displays the 2nd Column>']
    ... })

    >>> imat_cont = {
    ...     "menu_displayed_text": [
    ...         "Analysis Results",
    ...         "Please see the following analysis results:",
    ...         "<To continue, please press Enter>",
    ...         ["<Identifier>", "<Description>", "<Description>"],
    ...     ],
    ...     "menu_entries_results": [
    ...         ["Result 1", "<Displays the 1st Column>", "<Displays the 2nd Column>"],
    ...         ["Result 2", "<Displays the 1st Column>", "<Displays the 2nd Column>"],
    ...         ["Result 3", "<Displays the 1st Column>", "<Displays the 2nd Column>"],
    ...     ]
    ... }

    >>> df = util_convert_imat_datacont_to_pd_dataframe(imat_cont)

    This will convert the I-MaT data container to a DataFrame with 3 rows. The DataFrame can then be used for further
    data processing or analysis.
    """
    try:
        column_names = imat_cont['menu_displayed_text'][2]
        data = imat_cont['menu_entries_results']

        pd_dataframe = pd.DataFrame(data, columns=column_names)

        return pd_dataframe

    except Exception as e:
        handle_error(e)
