"""
Module: visualizations.main.py
==============================

This module, part of the `visualizations` package, provides workflow management for the display and playback of musical
scores. It includes functions that manage score selection and handle user interaction post-analysis.

Functions
---------
- `generic_display_workflow(display_func)`: Manages the workflow for displaying or playing back a musical score.
- `get_user_option_post_display()`: Presents post-analysis options to the user and retrieves their selection.

This module interacts with several other packages including `src.cli.menu_constructors`, `src.score_selection.main`,
`src.score_selection.name_parts`, and `src.score_selection.select_parts_and_measures`.

Examples
--------
Please see the docstrings of individual functions for specific examples of their use.
"""
from iMaT.src.cli.menu_constructors import display_menu_request_selection
from iMaT.src.score_selection.main import score_selection
from iMaT.src.score_selection.name_parts import selected_score_part_names
from iMaT.src.score_selection.select_parts_and_measures import select_parts_and_measures


def generic_display_workflow(display_func: callable):
    """
    Handles the display/playback function workflow for a musical score.

    The workflow includes score selection, application of the display function,
    and the post-display options.

    Parameters
    ----------
    display_func : callable
        Function to display or playback the musical score.
    """
    # a. Call the select_parts_and_measures() function, if no score has yet been selected, start the score selection
    # workflow by calling the score_selection() function.

    if selected_score_part_names == {}:
        score_selection()

    selected_score, given_name_selected_score, measures_chosen = select_parts_and_measures()

    # b. Perform the display/playback function
    display_func(selected_score)

    # c. Present the user with post-display options
    while True:
        option = get_user_option_post_display()

        # d. Depending on the user's choice ("repeat" or "back")
        if option == "repeat":
            generic_display_workflow(display_func)
            break
        else:
            break


def get_user_option_post_display():
    """
    Presents the user with post-analysis options and retrieves their selection.

    The post-analysis options include "repeat", "export", "display_results", or "back".

    Returns
    -------
    str
        User's selected option as a string.
    """
    imat_data_container = {
        "menu_displayed_text": [
            "Post-Analysis Menu",
            "Please select one of the following options by entering the corresponding index number:",
            "Which option do you want to select? (<No. of option>): ",
            ["Option", "<Explanation>"],
        ],
        "menu_entries": [
            ["REPT: Repeat function", 'repeat', "<Repeat the chosen function with a different score selection>"],
            ["BACK: Return to the Last Menu", 'back', "<Returns to the main menu>"],
        ],
    }

    return display_menu_request_selection(imat_data_container)

