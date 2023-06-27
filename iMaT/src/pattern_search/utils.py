from music21 import note

from src.cli.menu_constructors import display_menu_request_selection
from src.constants import NOTES_LIST, RHYTHMIC_VALUES_LIST
from src.utils.error_handling import handle_error


def pattern_selection_notes_only():
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
