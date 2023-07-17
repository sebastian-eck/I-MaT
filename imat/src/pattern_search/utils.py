"""
Module: pattern_search.utils.py
===============================

Provides utility functions for selecting musical patterns based on notes, rhythm,
or a combination of both in the pattern_search package. Each function prompts the
user to make selections and constructs musical patterns accordingly.

Functions
---------
- 'pattern_selection_notes_only': Allows the user to select a pattern based on notes only.
- 'pattern_selection_rhythm_only': Allows the user to select a pattern based on rhythm only.
- 'pattern_selection_notes_and_rhythm': Allows the user to select a pattern based on both notes and rhythm.

Each function returns a tuple containing the list of music21.note.Note objects
and a list of clear names, and handles errors using the `handle_error` function from the `src.utils.error_handling` module.

Notes
-----
This module uses the `music21` library, a toolkit for computer-aided musicology.
`music21`'s note.Note objects are used to represent individual notes in a musical pattern.

This module also uses the `src.cli.menu_constructors.display_menu_request_selection`
function to interactively display menus and handle user input.

Example
-------
>>> from pattern_search import utils
>>> utils.pattern_selection_notes_and_rhythm()
([<music21.note.Note C quarterLength=0.5>], [['C', '0.5']])

See Also
--------
music21.note.Note
src.cli.menu_constructors.display_menu_request_selection
src.utils.error_handling.handle_error

"""
from music21 import note

from iMaT.src.cli.menu_constructors import display_menu_request_selection
from iMaT.src.constants import NOTES_LIST, RHYTHMIC_VALUES_LIST
from iMaT.src.utils.error_handling import handle_error


def pattern_selection_notes_only():
    """
    Allows the user to select a pattern based on notes only.

    The user can add notes to the pattern, remove the last added note,
    or complete the pattern selection.

    Returns
    -------
    tuple
        Tuple containing the list of note.Note objects and a list of clear names.

    Raises
    ------
    Exception
        Any exception that occurs is caught and handled using `handle_error`.

    See Also
    --------
    src.cli.menu_constructors.display_menu_request_selection
    music21.note.Note
    src.utils.error_handling.handle_error

    Examples
    --------
    >>> pattern_selection_notes_only()
    ([<music21.note.Note C>], ['C'])
    """
    try:
        search_pattern_clear_names = []
        search_pattern = []

        while True:

            enter_notes_dict = {
                "menu_displayed_text": [
                    f"Pattern Search: Select Note Pattern - Pattern entered: {search_pattern_clear_names}",
                    "Please select one note by selecting the corresponding index number:",
                    "Which menu item do you want to select? (<No. of menu item>): ",
                    ["Menu item title", "<Short Explanation>"],
                ],
                "menu_entries": NOTES_LIST
            }

            selection = display_menu_request_selection(enter_notes_dict)

            if selection == "remove":

                if len(search_pattern) > 0:
                    search_pattern.pop()

            elif selection == "complete":

                return search_pattern, search_pattern_clear_names

            else:

                search_pattern_clear_names.append(selection)
                search_pattern.append(note.Note(selection))

    except Exception as e:
        handle_error(e)


def pattern_selection_rhythm_only():
    """
    Allows the user to select a pattern based on rhythm only.

    The user can add rhythms to the pattern, remove the last added rhythm,
    or complete the rhythm selection. The rhythm values are converted to
    quarterLength attribute of note.Note objects.

    Returns
    -------
    tuple
        Tuple containing the list of note.Note objects with specified quarterLength
        and a list of clear names.

    Raises
    ------
    Exception
        Any exception that occurs is caught and handled using `handle_error`.

    See Also
    --------
    src.cli.menu_constructors.display_menu_request_selection
    music21.note.Note
    src.utils.error_handling.handle_error

    Examples
    --------
    >>> pattern_selection_rhythm_only()
    ([<music21.note.Note C quarterLength=0.5>], ['0.5'])
    """
    try:
        search_pattern_clear_names = []
        search_pattern = []

        while True:

            enter_notes_dict = {
                "menu_displayed_text": [
                    f"Pattern Search: Select Note Pattern - Pattern entered: {search_pattern_clear_names}",
                    "Please select one note by selecting the corresponding index number:",
                    "Which menu item do you want to select? (<No. of menu item>): ",
                    ["Menu item title", "<Short Explanation>"],
                ],
                "menu_entries": RHYTHMIC_VALUES_LIST
            }

            selection = display_menu_request_selection(enter_notes_dict)

            if selection == "remove":

                if len(search_pattern) > 0:
                    search_pattern.pop()


            elif selection == "complete":

                prepared_search_pattern = []

                for rhythm in search_pattern:

                    if "/" in str(rhythm):

                        numerator, denominator = map(float, rhythm.split("/"))

                        prepared_search_pattern.append(note.Note(quarterLength=float(numerator / denominator)))

                    else:

                        prepared_search_pattern.append(note.Note(quarterLength=rhythm))

                return prepared_search_pattern, search_pattern_clear_names

            else:

                search_pattern_clear_names.append(selection)
                search_pattern.append(selection)

    except Exception as e:
        handle_error(e)


def pattern_selection_notes_and_rhythm():
    """
        Allows the user to select a pattern based on both notes and rhythm.

        The user can add notes and rhythms to the pattern, remove the last added pair,
        or complete the pattern selection. The rhythm values are converted to
        quarterLength attribute of note.Note objects.

        Returns
        -------
        tuple
            Tuple containing the list of note.Note objects with specified quarterLength
            and a list of clear names.

        Raises
        ------
        Exception
            Any exception that occurs is caught and handled using `handle_error`.

        See Also
        --------
        src.cli.menu_constructors.display_menu_request_selection
        music21.note.Note
        src.utils.error_handling.handle_error

        Examples
        --------
        >>> pattern_selection_notes_and_rhythm()
        ([<music21.note.Note C quarterLength=0.5>], [['C', '0.5']])
        """
    try:
        search_pattern_clear_names = []
        search_pattern = []

        while True:

            enter_notes_dict = {
                "menu_displayed_text": [
                    f"Pattern Search: Select Note Pattern - Pattern entered: {search_pattern_clear_names}",
                    "Please select one note by selecting the corresponding index number:",
                    "Which menu item do you want to select? (<No. of menu item>): ",
                    ["Menu item title", "<Short Explanation>"],
                ],
                "menu_entries": NOTES_LIST
            }

            note_selection = display_menu_request_selection(enter_notes_dict)

            if note_selection == "remove":

                if len(search_pattern) > 0:
                    search_pattern.pop()

            elif note_selection == "complete":
                prepared_search_pattern = []
                for pitch_name, rhythm in search_pattern:

                    if "/" in str(rhythm):
                        numerator, denominator = map(float, rhythm.split("/"))
                        prepared_search_pattern.append(note.Note(pitch_name.name, quarterLength=float(numerator / denominator)))

                    else:
                        prepared_search_pattern.append(note.Note(pitch_name.name, quarterLength=rhythm))

                return prepared_search_pattern, search_pattern_clear_names

            else:

                enter_notes_dict = {
                    "menu_displayed_text": [
                        f"Pattern Search: Select Note Pattern - Pattern entered: {search_pattern_clear_names}",
                        "Please select one note by selecting the corresponding index number:",
                        "Which menu item do you want to select? (<No. of menu item>): ",
                        ["Menu item title", "<Short Explanation>"],
                    ],
                    "menu_entries": RHYTHMIC_VALUES_LIST
                }

                rhythm_selection = display_menu_request_selection(enter_notes_dict)

                if rhythm_selection == "remove":

                    if len(search_pattern) > 0:
                        search_pattern.pop()


                elif note_selection == "complete":

                    prepared_search_pattern = []

                    for pitch_name, rhythm in search_pattern:

                        if "/" in str(rhythm):

                            numerator, denominator = map(float, rhythm.split("/"))

                            prepared_search_pattern.append(note.Note(pitch_name.name, quarterLength=float(numerator / denominator)))


                        else:

                            prepared_search_pattern.append(note.Note(pitch_name.name, quarterLength=rhythm))

                    return prepared_search_pattern, search_pattern_clear_names

                else:

                    search_pattern_clear_names.append([note_selection, rhythm_selection])
                    search_pattern.append([note.Note(note_selection), rhythm_selection])

    except Exception as e:
        handle_error(e)
