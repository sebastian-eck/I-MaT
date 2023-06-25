from music21 import note

from src.cli.cli_menu_structure import display_menu_request_selection

notes_list = [
    ["‾‾‾‾  -   C-flat", "C-"],
    ["C         C", "C"],
    ["____  ♯   C-sharp", "C#"],
    ["‾‾‾‾  -   D-flat", "D-"],
    ["D         D", "D"],
    ["____  ♯   D-sharp", "D#"],
    ["‾‾‾‾  -   E-flat", "E-"],
    ["E         E", "E"],
    ["____  ♯   E-sharp", "E#"],
    ["‾‾‾‾  -   F-flat", "F-"],
    ["F         F", "F"],
    ["____  ♯   F-sharp", "F#"],
    ["‾‾‾‾  -   G-flat", "G-"],
    ["G         G", "G"],
    ["____  ♯   G-sharp", "G#"],
    ["‾‾‾‾  -   A-flat", "A-"],
    ["A         A", "A"],
    ["____  ♯   A-sharp", "A#"],
    ["‾‾‾‾  -   B-flat", "B-"],
    ["B         B", "B"],
    ["____  ♯   B-sharp", "B#"],
    ["BACK: Remove the last note entered", "remove"],
    ["DONE: Finish input", "complete"],
]

rhythmic_values_list = [
    ["[0.125]   Thirty-second note", 0.125],
    ["[0.25]    Sixteenth note", 0.25],
    ["[0.375]   Sixteenth note (dotted)", 0.375],
    ["[1/3]     Eighth note triplet", "1/3"],
    ["[0.5]     Eighth note", 0.5],
    ["[0.75]    Eighth note (dotted)", 0.75],
    ["[2/3]     Quarter note triplet", "2/3"],
    ["[1.0]     Quarter note", 1.0],
    ["[1.5]     Quarter note (dotted)", 1.5],
    ["[4/3]     Half note triplet", "4/3"],
    ["[2.0]     Half note", 2.0],
    ["[3.0]     Half note (dotted)", 3.0],
    ["[8/3]     Whole note triplet", "8/3"],
    ["[4.0]     Whole note", 4.0],
    ["[6.0]     Whole note (dotted)", 6.0],
    ["[16/3]    Double whole triplet", "16/3"],
    ["[8.0]     Double whole note", 8.0],
    ["[12.0]    Double whole note (dotted)", 12.0],
    ["BACK:     Remove the last note entered", "remove"],
    ["DONE:     Finish input", "complete"]
]


def pattern_selection_notes_only():
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
            "menu_entries": notes_list
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


def pattern_selection_rhythm_only():
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
            "menu_entries": rhythmic_values_list
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


def pattern_selection_notes_and_rhythm():
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
            "menu_entries": notes_list
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
                "menu_entries": rhythmic_values_list
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