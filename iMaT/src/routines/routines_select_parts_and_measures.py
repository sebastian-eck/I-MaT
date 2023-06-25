"""
This module provides a user interface to facilitate the selection of musical parts and measures from a given musical
score using music21, a toolkit for computer-aided musicology.

The main functionalities include:
- Selecting the full score or individual parts.
- Selecting all measures or a specific range of measures.
- Repeating the previous selection.

A global dictionary `selected_score_part_names` is used to map part names to music21.stream.Score or
music21.stream.Part objects.

Functions
---------
select_parts_and_measures():
    Facilitates the user's selection of musical parts and measures from a global score.
    Returns a tuple containing the selected score or part and the selected measure range as a tuple.

select_measure_range(score):
    Prompts the user to input a valid measure range in a given musical score.
    Returns a tuple containing the start and end measures of the selected range.

Examples
--------
Here is how to use the functions in this module:

>>> from music21 import *
>>> selected_part, selected_range = select_parts_and_measures()

>>> from music21 import corpus
>>> score = corpus.parse('bwv66.6')
>>> start, end = select_measure_range(score)
>>> print(f"Selected range: {start} to {end}")

Notes
-----
This module uses the music21 library, which must be installed and imported for the functions to work correctly.
This module also depends on other modules like `routines_name_parts` and `src.cli.cli_menu_structure`
for some of its operations.
"""
import music21
from music21 import stream

from src.cli.cli_menu_structure import display_menu_print_textblock, display_menu_request_selection
from src.routines.routines_name_parts import selected_score_part_names

previous_score_selection = ()


def select_parts_and_measures() -> (music21.stream.Score or music21.stream.Part, (int, int)):
    """
    Facilitates the user's selection of musical parts and measures from a global score.

    This function displays a selection menu to the user with several options related to the selection of musical
    parts and measures. The user is allowed to choose from the full score or individual parts, and either all
    measures or a specific range of measures. The function also provides an option to repeat the previous selection
    if one exists.

    The function works with a dictionary named `selected_score_part_names` that should be initialized before calling
    this function. The dictionary maps part names to `music21.stream.Score` or `music21.stream.Part` objects.  Here is
    an example of how the dictionary might look for the score 'bwv66.6':

    selected_score_part_names = {
        'Full Score': <music21.stream.Score 0x230ce950730>,
        'Part 1': <music21.stream.Part Soprano>,
        'Part 2': <music21.stream.Part Alto>,
        'Part 3': <music21.stream.Part Tenor>,
        'Part 4': <music21.stream.Part Bass>
    }

    Returns
    -------
    tuple
        A tuple containing:
        - music21.stream.Score or music21.stream.Part: The selected part of the score based on the user's choice.
          The part contains either all measures or a specific range of measures, depending on the user's choice.
        - str: The name of the selected part.
        - tuple: A tuple representing the start and end measures of the selected range.

    Examples
    --------
    Here is how to use `select_parts_and_measures`:

    >>> from music21 import *
    >>> selected_part, selected_part_name, selected_range = select_parts_and_measures()
    """
    global previous_score_selection

    imat_data_container = {
        "menu_displayed_text": [
            "Score Selection Menu",
            "Please select one of the following options by entering the corresponding index number:",
            "Which option do you want to select? (<No. of option>): ",
            ["Option", "Explanation"],
        ],
        "menu_entries": [
            ["PRVS: Previous Score Selection", "prev_selection", "Repeat the previous score selection"],
            ["SCOR: Full Score - All Measures", "full_all", "Select the full score and all measures"],
            ["SLCT: Full Score - Range of Measures", "full_range", "Select the full score and a range of measures"],
            ["PART: Part - All Measures", "part_all", "Select an individual part and all measures"],
            ["SLCT: Part - Range of Measures", "part_range", "Select an individual part and a range of measures"]
        ]
    }

    choice = display_menu_request_selection(imat_data_container)

    if choice == "prev_selection":  # Repeat previous selection
        if previous_score_selection is not ():
            return previous_score_selection
        else:
            print("\nThere is no previous selection. Please make a new selection.\n")
            input("<To continue, please press Enter>")
            return select_parts_and_measures()

    if choice == "full_all":  # Full score with all measures
        previous_score_selection = (selected_score_part_names['Full Score'], 'Full Score', (
            1, len(selected_score_part_names['Full Score'].parts[0].getElementsByClass(stream.Measure))))
        return previous_score_selection

    if choice == "full_range":  # Full score with a range of measures
        range_ = select_measure_range(selected_score_part_names['Full Score'])
        score_selected_measures = selected_score_part_names['Full Score'].measures(*range_)
        previous_score_selection = (score_selected_measures, 'Full Score', range_)
        return previous_score_selection

    if choice == "part_all" or choice == "part_range":  # Individual part with all measures or a range of measures
        part_menu = {
            "menu_displayed_text": [
                "Part Selection Menu",
                "Please select one of the following parts by entering the corresponding index number:",
                "Which part do you want to select? (<No. of part>): ",
                ["Part Names"],
            ],
            "menu_entries": [[part, part] for idx, part in
                             enumerate(selected_score_part_names) if part != 'Full Score']
        }
        selected_part_name = display_menu_request_selection(part_menu, 10)

        if choice == "part_all":  # Individual part with all measures
            previous_score_selection = (selected_score_part_names[selected_part_name], selected_part_name, (
                1, len(selected_score_part_names[selected_part_name].getElementsByClass(stream.Measure))))
            return previous_score_selection

        # Individual part with a range of measures
        range_ = select_measure_range(selected_score_part_names[selected_part_name])
        score_selected_measures = selected_score_part_names[selected_part_name].measures(*range_)
        previous_score_selection = (score_selected_measures, selected_part_name, range_)
        return previous_score_selection


def select_measure_range(score: music21.stream.Part or music21.stream.Score):
    """
    Prompts the user to input a valid measure range in a given musical score.

    This function displays a menu to guide the user through the process of selecting a range of measures in the given
    musical score. The range is inclusive and the measures are 1-indexed. The user first enters a start measure and
    then an end measure. Both measures should lie within the total number of measures in the score. The end measure
    should be equal to or larger than the start measure.

    The user input is validated according to the following rules:
    - The input must be a positive integer.
    - The input must not exceed the total number of measures in the score.
    - The end measure should be equal to or larger than the start measure.

    If the user enters an invalid range, the function will prompt the user again to enter a valid range.

    Parameters
    ----------
    score : music21.stream.Part or music21.stream.Score
        The musical score or part in which the user is selecting a measure range.

    Returns
    -------
    start, end : tuple of int
        The start and end measures of the selected range.

    Examples
    --------
    Here is how to use `select_measure_range`:

    >>> from music21 import corpus
    >>> score = corpus.parse('bwv66.6')
    >>> start, end = select_measure_range(score)
    >>> print(f"Selected range: {start} to {end}")
    """
    # Check if 'score' is a Score or Part and get total measures accordingly
    if isinstance(score, music21.stream.Score):
        total_measures = len(score.parts[0].getElementsByClass(stream.Measure))
    elif isinstance(score, music21.stream.Part):
        total_measures = len(score.getElementsByClass(stream.Measure))
    else:
        raise TypeError(f"Expected music21.stream.Score or music21.stream.Part, but got {type(score)}.")

    text_dict = {
        "menu_displayed_text": [
            "-- Measure Selection --",
            f"Please enter a measure range. The score has {total_measures} measures (choosing pickup measures is ("
            f"currently) not supported).",
            "Enter the start measure (starting from 1): ",
            ["Measure Range: ", f"Enter a range from 1 to {total_measures}"],
        ],
        "menu_entries_text": [
            ["Start Measure: ", "Enter the number of the starting measure (1 or above)."],
            ["End Measure: ", "After the starting measure is entered, enter the ending measure."],
            ["Rules for Measure Selection: ", f"Enter a starting measure and an ending measure, both inclusive. The "
                                              f"first measure "
                                              f"is '1'. The ending measure should be equal to or larger than the "
                                              f"starting measure,"
                                              f"but should not exceed {total_measures}."],
            ["Invalid Input: ", "If your input is invalid, you will be asked to enter the measure range again."]
        ]
    }

    while True:
        start = display_menu_print_textblock(text_dict)

        if start.isdigit() and 1 <= int(start) <= total_measures:
            start = int(start)
            break
        print("\nInvalid starting measure. Please enter a valid measure.\n")
        input("<To continue, please press Enter>")

    text_dict["menu_entries_text"][1][1] = f"Now, enter the ending measure (should not exceed {total_measures} and " \
                                           f"should be equal to or larger than the starting measure)."
    text_dict["menu_entries_text"][0][1] = f"You entered {start} as the starting measure."
    text_dict["menu_entries_text"][1][1] = f"Now, enter the ending measure (should not exceed {total_measures} and " \
                                           f"should be equal to or larger than the starting measure)."

    text_dict["menu_displayed_text"][2] = f"Enter the end measure (starting from {start}, ending at {total_measures}): "
    text_dict["menu_displayed_text"][3][1] = f"Enter a range from {start} to {total_measures}"

    while True:

        end = display_menu_print_textblock(text_dict)

        if end.isdigit() and start <= int(end) <= total_measures:
            end = int(end)
            break
        print("\nInvalid ending measure. Please enter a valid measure.\n")
        input("<To continue, please press Enter>")

    return start, end

# (for testing purposes)
#
# from music21 import corpus, stream
#
# score = corpus.parse('bwv66.6')
#
# selected_score_part_names = {'Full Score': score}
#
# for idx, part in enumerate(score.parts):
#     selected_score_part_names[f"Part {idx+1}"] = part
#
# # Check the dictionary
# for key, value in selected_score_part_names.items():
#     print(f"{key}: {value}")
#
# #select_parts_and_measures().show()
#
#
#
# # score = corpus.parse('bwv66.6')
# # start, end = select_measure_range(score)
# # print(f"Selected range: {start} to {end}")
