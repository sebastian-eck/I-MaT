"""
analysis.utils.py
=================

This module contains utility functions that are used within the analysis package, particularly
for displaying menus and handling user input post analysis. These functions are used to enhance
the interaction of the users with the Interactive Music Analysis Tool (I-MaT) system.

The primary function in this module is `display_user_options_post_analysis`, which provides
the user with a menu of options after a piece has been analyzed. This function allows for smooth
user interaction during the post-analysis phase, offering choices like repeating the analysis,
exporting results, displaying results, or going back to the main menu.

This module also interacts with other modules, for instance, `display_menu_request_selection` from
`menu_constructors` module and `handle_error` from `error_handling` module are used to handle menu
displays and error scenarios respectively.

Functions
---------
- `display_user_options_post_analysis`: Presents the user with a menu of options after the analysis of a piece. This includes options to repeat the analysis, export results, display results, or go back to the main menu.

The module interacts with other modules like `menu_constructors` for displaying menus and `error_handling` for managing errors.
"""
from src.cli.menu_constructors import display_menu_request_selection
from src.utils.error_handling import handle_error


def display_user_options_post_analysis():
    """
    Display a menu with post-analysis options and return the user's choice.

    This function presents the user with a list of options after a musical piece has been analyzed.
    The available options are: 'repeat', 'export', 'display_results', or 'back'. The user's selection
    is then returned as a string.

    Returns
    -------
    str
        User's chosen option from the post-analysis menu. Options include: 'repeat', 'export', 'display_results', 'back'.

    Raises
    ------
    Exception
        Handles any exceptions that arise during the menu display and option selection by passing them to handle_error(e).

    See Also
    --------
    display_menu_request_selection : function
        Constructs a menu and handles user selection based on a given data container.

    Examples
    --------
    >>> user_choice = display_user_options_post_analysis()
    >>> print(user_choice)
    'repeat'

    Notes
    -----
    The function constructs the menu options using a predefined data container which contains the necessary details for each option.
    """
    try:
        imat_data_container = {
            "menu_displayed_text": [
                "Post-Analysis Menu",
                "Please select one of the following options by entering the corresponding index number:",
                "Which option do you want to select? (<No. of option>): ",
                ["Option", "<Explanation>"],
            ],
            "menu_entries": [
                ["REPT: Repeat analysis function", 'repeat',
                 "<Repeat the chosen analysis function with a different score selection>"],
                ["EXPT: Export Results to CSV", 'export', "<Explanation>"],
                ["SHOW: Display Results", 'display_results', "<Explanation>"],
                ["BACK: Return to the Last Menu", 'back', "<Returns to the main menu>"],
            ],
        }

        return display_menu_request_selection(imat_data_container)

    except Exception as e:
        handle_error(e)
