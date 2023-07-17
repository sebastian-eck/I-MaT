# from lorem_text import lorem
#
# from iMaT.src.analysis.analysis import example_analysis
# from iMaT.src.cli.cli_menu_structure import display_menu_directed, display_menu_print_results, display_menu_print_textblock
# from iMaT.src.routines.routines_analysis import analysis_workflow_single_musical_piece
#
#
# def example_mainmenu_entries_dict() -> dict:
#     """
#     Generate a representative dictionary for menu entries.
#
#     This function creates and returns a dictionary that simulates a menu.
#     This dictionary is structured to be used by the `display_menu_undirected()` function.
#     The dictionary includes the text displayed for the menu and a list of menu entries.
#
#     The "menu_displayed_text" field in the dictionary includes a title for the menu, an instruction for selection,
#     a representative entry layout, and a prompt for the user's choice.
#
#     The "menu_entries" field is a list of potential options available in the menu. Each entry is a list itself,
#     with the first element being a brief description of the entry, the second element being the function that will be
#     executed when this entry is selected, and the third element being a more detailed explanation of what the entry
#     does.
#
#     When the `display_menu_undirected()` function uses this dictionary, it behaves as follows:
#
#     1. **If a submenu is selected** (e.g., "ABBR: Option 1 titel"):
#        The corresponding function (e.g., `example_submenu_entries_dict()`) is expected to return another dictionary
#        that represents the submenu. The function will then recursively call itself with the new dictionary,
#        thus entering the submenu.
#
#     2. **If a regular function is selected** (e.g., "ABBR: Option 2 titel"):
#        The corresponding function (e.g., `example_some_function()`) is executed.
#
#     3. **If the 'back' option is selected**:
#        The `display_menu_undirected()` function will return, reverting to the previous menu.
#
#     4. **If the 'main-menu' option is selected**:
#        The `display_menu_undirected()` function will return all the way up to the main menu.
#
#     Each of these actions will be followed by a return to the corresponding menu.
#
#
#     Returns
#     -------
#     dict
#         A dictionary that simulates a menu. The dictionary includes the following keys:
#         "menu_displayed_text": A list including a title, instructions for selection, a sample entry layout,
#         and a prompt for user input.
#         "menu_entries": A list of possible selections. Each entry is itself a list, including a brief description,
#         the function to execute, and a more detailed explanation. The number of entries can be dynamic and
#         adjusted to meet specific requirements.
#
#     Example
#     -------
#     >>> def example_mainmenu_entries_dict():
#     ...return {
#     ...     "menu_displayed_text": [
#     ...         "Menu Titel",
#     ...         "Please select one of the following menu options by entering the corresponding index number:",
#     ...         "Which menu item should be executed? (<No. of menu item>): ",
#     ...         ["Menu item: Titel"],
#     ...     ],
#     ...     "menu_entries": [
#     ...         ["ABBR: Option 1 titel", example_submenu_entries_dict, "<Goes to submenu>"],
#     ...         ["ABBR: Option 2 titel", example_some_function, "<Executes some function>"],
#     ...         ["ABBR: Option 3 titel", example_another_function], "<Executes another function>",
#     ...         ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
#     ...         ["MAIN: Return to the main menu", 'main-menu'], 'main-menu', "<Returns to main menu>",
#     ...    ]
#     ...}
#     """
#     return {
#         "menu_displayed_text": [
#             "Menu Titel",
#             "Please select one of the following menu options by entering the corresponding index number:",
#             "Which menu item should be executed? (<No. of menu item>): ",
#             ["Menu item titel", "<Short Explanation>"],
#         ],
#         "menu_entries": [
#             ["ABBR: Option 1 titel", example_submenu_entries_dict, "<Goes to submenu>"],
#             ["ABBR: Option 2 titel", example_some_function, "<Executes some function>"],
#             ["ABBR: Option 3 titel", example_another_function, "<Executes another function>"],
#             ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
#             ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
#         ]
#     }
#
#
# def example_sub_submenu_entries_dict() -> None:
#     """
#     Generate a representative dictionary for sub-submenu entries.
#
#     This function creates and returns a dictionary that simulates a sub-submenu. This dictionary is structured to be
#     used by the `display_menu_undirected()` function. The dictionary includes the text displayed for the sub-submenu
#     and a list of sub-submenu entries.
#
#     Similar to the main menu and submenu dictionaries, it includes two main fields: "menu_displayed_text" and
#     "menu_entries", which provide the necessary information for the menu display and interaction in the console.
#
#     As with other menus, user options could include other sub-submenus, functions, or options to return to parent menus.
#
#     Returns
#     -------
#     None
#
#     Example
#     -------
#     >>> example_sub_submenu_entries_dict()
#     """
#     input("this would return a sample sub-submenu dictionary instead of this function.")
#
#
# def example_some_function() -> None:
#     """
#     Example function for menu entry.
#
#     This function is intended to represent the kind of function that could be called from a menu. In this case,
#     it simply requests input from the user as a placeholder action. In a more complex application, this could be any
#     function that carries out a specific action.
#
#     In the context of menu functions like `display_menu_undirected` and `display_menu_directed`, this function could
#     be executed when a user selects the corresponding menu item. It would be part of a menu dictionary,
#     with the dictionary key representing the menu option, and this function as the value. When that option is
#     selected, this function would be called and its actions carried out.
#
#     After the function is executed, if called from a menu function like `display_menu_undirected` or
#     `display_menu_directed`, the user would be returned to the menu that the function was selected from,
#     allowing further interaction with the menu options.
#
#     For example, if a menu option was ["ABBR: Option 2 title", example_some_function, "<Executes some function>"],
#     and the user selects "Option 2", `example_some_function` would be executed and then the user would return to the
#     initial menu.
#
#
#     Returns
#     -------
#     None
#
#     See Also
#     --------
#     display_menu_undirected : Function that displays a menu to the user, allows user selection
#     and calls the appropriate function
#     display_menu_directed : Function similar to `display_menu_undirected` but with different navigation options
#
#     Example
#     -------
#     >>> def example_some_function():
#     ...     input("this would excecute a function instead of this example text output.")
#     """
#     input("this would excecute a function instead of this example text output.")
#
#
# def example_another_function() -> None:
#     """
#     Another example function for menu entry.
#
#     This function is another example of a function that could be called from a menu. Similar to
#     `example_some_function()`, it merely asks for user input as a placeholder action. In a real application,
#     this could be any function that performs a specific task.
#
#     In the context of menu functions like `display_menu_undirected` and `display_menu_directed`, this function could
#     be executed when a user selects the corresponding menu item. It would be part of a menu dictionary,
#     with the dictionary key representing the menu option, and this function as the value. When that option is
#     selected, this function would be called and its actions carried out.
#
#     After the function is executed, if called from a menu function like `display_menu_undirected` or
#     `display_menu_directed`, the user would be returned to the menu that the function was selected from,
#     allowing further interaction with the menu options.
#
#     For example, if a menu option was ["ABBR: Option 3 title", example_another_function, "<Executes another
#     function>"], and the user selects "Option 3", `example_another_function` would be executed and then the user
#     would return to the initial menu.
#
#     Returns
#     -------
#     None
#
#     See Also
#     --------
#     display_menu_undirected : Function that displays a menu to the user, allows user selection,
#     and calls the appropriate function
#     display_menu_directed : Function similar to `display_menu_undirected` but with different navigation options
#
#     Example
#     -------
#     >>> example_another_function()
#     """
#     input("This is another sample function.\n")
#
#
# def demo_menu_structure_dict() -> dict:
#     """
#     Generate a dictionary representing a demo menu structure.
#
#     This function returns a dictionary that simulates a demo menu. The dictionary includes a title, an instruction
#     for selection, a representative entry layout, a prompt for the user's choice, and a list of potential options
#     available in the menu.
#
#     Each menu entry is a list itself, with the first element being a brief description of the entry, the second
#     element being the function that will be executed when this entry is selected, and the third element being a more
#     detailed explanation of what the entry does.
#
#     Returns
#     -------
#     dict
#         A dictionary representing a demo menu structure.
#
#     See Also
#     --------
#     example_submenu_entries_dict : A function that returns a dictionary representing a submenu.
#     demo_function_directed_menu : A function that demonstrates the navigation of a directed menu.
#     demo_function_print_text : A function that demonstrates the display of a text block.
#     demo_function_print_results : A function that demonstrates the display of an analysis result set.
#     """
#     return {
#         "menu_displayed_text": [
#             "Menu Titel",
#             "Please select one of the following menu options by entering the corresponding index number:",
#             "Which menu item should be executed? (<No. of menu item>): ",
#             ["Menu item titel", "<Short Explanation>"],
#         ],
#         "menu_entries": [
#             ["DEMO: Enter Submenu", example_submenu_entries_dict, "<Goes to submenu>"],
#             ["DEMO: Enter directed menu", demo_function_directed_menu, "<Enters directed menu structure>"],
#             ["DEMO: Display demo text", demo_function_print_text, "<Displays a text>"],
#             ["DEMO: Display demo results", demo_function_print_results, "<Displays a sample analysis result set>"],
#             ["DEMO: Display demo results", (analysis_workflow_single_musical_piece, example_analysis), "<Starts an example analysis workflow>"],
#             ["BACK: Return to the last menu", 'back', "<Returns to the parent menu>"],
#             ["MAIN: Return to the main menu", 'main-menu', "<Returns to main menu>"],
#         ]
#     }
#
#
# def demo_function_print_text() -> None:
#     """
#     A demo function that demonstrates the display of text to the user.
#
#     This function demonstrates the usage of the `display_menu_print_textblock` function. It displays a predefined text
#     block to the user, using the `example_text_dict` dictionary to generate the text block.
#
#     `example_text_dict` is a dictionary with lorem ipsum text as messages. This dictionary generates three lorem ipsum
#     text messages, with 60, 32, and 40 words respectively. These messages are used to form the "menu_entries_text"
#     field of the dictionary. The "menu_displayed_text" field of the dictionary contains generic text related to the menu.
#
#     This function does not take any arguments or return any value. Instead, it simply executes the
#     `display_menu_print_textblock` function with the `example_text_dict` dictionary as an argument.
#
#     Parameters
#     ----------
#     None
#
#     Returns
#     -------
#     None
#
#     See Also
#     --------
#     display_menu_print_textblock : Function that prints a text block to the console.
#     example_text_dict : A dictionary that represents a text block.
#     print_textblock : Function that prints out a block of text given in a list or a single string.
#
#     Examples
#     --------
#     >>> example_text_dict
#     {
#             "menu_displayed_text": [
#                 "-- message to the user --",
#                 "Please read the following message:",
#                 "<To continue, please press Enter>",
#                 ["", "Message"],
#             ],
#             "menu_entries_text": [
#                 ["Message 1", "Textblock 1"],
#                 ["Message 2", "Textblock 2"],
#                 ["Message 3", "Textblock 3"],
#             ]
#         }
#     """
#     words = 10
#     text_1 = lorem.words(60)
#     text_2 = lorem.words(32)
#     text_3 = lorem.words(40)
#
#     example_text_dict = {
#         "menu_displayed_text": [
#             "-- message to the user --",
#             "Please read the following message:",
#             "<To continue, please press Enter>",
#             ["", "Message"]
#         ],
#         "menu_entries_text": [
#             ["Message 1", text_1],
#             ["Message 2", text_2],
#             ["Message 3", text_3],
#         ]
#     }
#     display_menu_print_textblock(example_text_dict)
#
#
# def demo_function_print_results() -> None:
#     """
#     A demo function that demonstrates the display of analysis results.
#
#     This function demonstrates the usage of the `display_menu_print_results` function. It displays a predefined set of
#     analysis results to the user, using the `example_analysis_results_dict` dictionary to generate the results.
#
#     `example_analysis_results_dict` is a dictionary that represents analysis results. This dictionary can be passed as a
#     parameter to the `display_menu_print_results` function. It includes a description of the results and a list of
#     results entries. The "menu_displayed_text" field in the dictionary includes a title for the results, a description
#     of the results, a layout for the results' entries, and a prompt for user interaction. The "menu_entries_results"
#     field is a list of the actual analysis results, with each entry is a list itself, representing different aspects of
#     the result.
#
#     When this dictionary is used by the `display_menu_print_results` function, each line of the "menu_entries_results"
#     list will be displayed as a separate line in the console, and the user can interact with the prompt specified in the
#     "menu_displayed_text" field.
#
#     This function does not take any arguments or return any value. Instead, it simply executes the
#     `display_menu_print_results` function with the `example_analysis_results_dict` dictionary as an argument.
#
#     Parameters
#     ----------
#     None
#
#     Returns
#     -------
#     None
#
#     See Also
#     --------
#     display_menu_print_results : Function that prints an analysis result set to the console.
#     example_analysis_results_dict : A dictionary that represents an analysis result set.
#     """
#     example_analysis_results_dict = {
#         "menu_displayed_text": [
#             "Analysis Results",
#             "Please see the following analysis results:",
#             "<To continue, please press Enter>",
#             ["<Identifier>", "<Description>", "<Description>"],
#         ],
#         "menu_entries_results": [
#             ["Result 1", "<Displays the 1st Column>", "<Displays the 2nd Column >"],
#             ["Result 2", "<Displays the 1st Column>", "<Displays the 2nd Column >"],
#             ["Result 3", "<Displays the 1st Column>", "<Displays the 2nd Column >"],
#         ]
#     }
#
#     display_menu_print_results(example_analysis_results_dict)
