"""
score_selection.name_parts.py
=============================

This module provides functionalities to interact with and manipulate music scores using the music21 library. It takes
into account predefined names for each part of the score within the files and assigns them to the corresponding
music21 stream parts when assigning generic names.

Functions
---------
- `select_and_name_parts`: Initializes the `selected_score_part_names` dictionary and engages with the user to name the parts of the score.
- `rename_parts`: Allows the user to rename the parts of the chosen score.
- `view_score`: Displays the selected score by using the `show` method of `music21`.

Notes
-----
This module uses the `music21` library and functions from `src.cli.menu_constructors` and `src.utils.error_handling`.
The global variable `selected_score_part_names` associates part names with their corresponding `music21 Score` or `Part` objects.

Module-level variable definitions
---------------------------------

The module also defines a global variable:

selected_score_part_names: dict This global dictionary associates part names to their corresponding music21 Score or
Part objects, enabling user interaction with named parts rather than abstract music21 objects. The key 'Full Score'
is reserved for the whole Score object. The structure of the dictionary is as follows:

    ```
    selected_score_part_names = {
        'Full Score': <music21.stream.Score 0x230ce950730>,
        'Part 1': <music21.stream.Part Soprano>,
        'Part 2': <music21.stream.Part Alto>,
        'Part 3': <music21.stream.Part Tenor>,
        'Part 4': <music21.stream.Part Bass>
    }
    ```
"""

import music21

from src.cli.menu_constructors import display_menu_print_results, display_menu_print_textblock, \
    display_menu_request_selection
from src.utils.error_handling import handle_error

selected_score_part_names = {}

def select_and_name_parts(selected_score: music21.stream.Score) -> None:
    """
    Interacts with the user to assign custom or generic names to the parts of a provided music21 Score object.

    This function first clears and then repopulates the `selected_score_part_names` global dictionary, associating
    names (keys) with the parts of the given Score (values). The 'Full Score' key represents the entire Score object.

    The function presents a menu to the user to choose between assigning individual names, using generic names,
    or viewing the selected score. Depending on the user's choice, it either calls the `rename_parts` function
    to assign individual names, prints the `selected_score_part_names` dictionary if the user chooses generic names,
    or calls `view_score` to display the music score.

    The function handles exceptions by passing them to the `handle_error` function.

    Args:
        selected_score (music21.stream.Score): The Score object for which parts are to be named.

    Raises:
        Any exceptions occurring during the execution are caught and passed to the `handle_error` function.

    Returns:
        None. This function modifies the global 'selected_score_part_names' dictionary and doesn't return a value.

    See Also:
        1. `rename_parts()`: To assign individual names based on user input.
        2. `view_score()`: To display the music score.
        3. `handle_error()`: For handling exceptions occurring during the execution of this function.
    """

    try:
        selected_score_part_names.clear()  # Clear the dictionary
        selected_score_part_names['Full Score'] = selected_score  # Modify the dictionary
        for i, part in enumerate(selected_score.parts):
            selected_score_part_names[f"Part {i + 1}"] = part

        while True:
            menu_text = {
                "menu_displayed_text": [
                    "Naming parts (custom/generic)",
                    "Please select an option:",
                    "Enter your choice (1-3): ",
                    ["Menu item", "<Explanation>"],
                ],
                "menu_entries": [
                    ["GNRC: Assign generic names to parts", "Use generic names",
                     "<Use generic names (Part 1, Part 2, etc.)>"],
                    ["INDV: Assign individual/custom names to parts", "Assign individual names",
                     "<Type in custom names for individual parts>"],
                    ["VIEW: View the selected sheet music", "View the score",
                     "<Open the score for viewing in the defined sheet music program>"],
                ]
            }

            choice = display_menu_request_selection(menu_text)

            if choice == "Assign individual names":
                rename_parts()  # Modify the dictionary directly
                break
            elif choice == "Use generic names":
                menu_text = {'menu_displayed_text':
                                 ['Selected Score Part Names',
                                  'These are the generated generic score part names:',
                                  '<To continue, please press Enter>',
                                  ['Part Names']],
                             'menu_entries_results':
                                 [[k] for k in selected_score_part_names.keys() if k != 'Full Score']}
                display_menu_print_results(menu_text)
                break
            elif choice == "View the score":
                view_score(selected_score)
    except Exception as e:
        handle_error(e)

def rename_parts() -> None:
    """
    Interactive function that allows the user to rename parts in a musical score.
    The function operates on a global dictionary `selected_score_part_names`, where
    keys are part names and values are part objects.

    Here is an example of how the `selected_score_part_names` dictionary may look before renaming:

    ```
    selected_score_part_names = {
        'Full Score': <music21.stream.Score 0x230ce950730>,
        'Part 1': <music21.stream.Part Soprano>,
        'Part 2': <music21.stream.Part Alto>,
        'Part 3': <music21.stream.Part Tenor>,
        'Part 4': <music21.stream.Part Bass>
    }

    This function displays a list of current part names and prompts the user to enter
    new names for each part, one at a time. If the user enters a new name that is not
    already used by another part, the new name will be accepted and used to update the part's name.
    If the user tries to enter a name that is already in use, they will be prompted to choose another name.

    Once the user has been given the chance to rename all parts, a list of the new (or unchanged)
    part names is displayed. The user is then asked to confirm whether the new names are correct.

    If the user confirms that the new names are correct, the global `selected_score_part_names` dictionary
    is updated with the new part names. If the user indicates that the new names are not correct,
    the renaming process starts over.

    The function continues to run until the user confirms that the part names are correct.

    The function does not return any value. It directly modifies the `selected_score_part_names` dictionary.

    Raises:
        Any exceptions raised by this function are passed to the `handle_error` function for error handling.

    See Also:
        1. `display_menu_print_results()`: For displaying a list of current part names and to present new/unchanged names.
        2. `display_menu_request_selection()`: For requesting the user to select between confirming or rejecting the new names.
        3. `handle_error()`: For handling exceptions that occur during the renaming process.
    """
    try:
        global selected_score_part_names

        # Operate on a local copy of the global dictionary
        local_copy = selected_score_part_names.copy()

        while True:
            # Convert the dictionary to a list of tuples
            selected_score_part_list = list(local_copy.items())

            for i, (part, value) in enumerate(selected_score_part_list):
                if part != 'Full Score':
                    # Create I-MaT data container
                    part_name_dict = {
                        "menu_displayed_text": [
                            "Current Part Names",
                            "Please review the current part names:",
                            f"Enter a new name for {part} (leave blank to keep the existing name): ",
                            ["Part Names"],
                        ],
                        "menu_entries_results": []
                    }
                    # Fill in the part names
                    for p in selected_score_part_names.keys():
                        if p != 'Full Score':
                            arrow = "  <-----" if p == part else ""
                            part_name_dict["menu_entries_results"].append([str(p + arrow)])
                    # Display the part names and get new name
                    while True:
                        new_name = display_menu_print_results(part_name_dict)
                        # Continue if no name entered
                        if not new_name:
                            break
                        # If the new name doesn't already exist, use it
                        elif new_name not in dict(selected_score_part_list).keys():
                            selected_score_part_list[i] = (new_name, value)  # update the key in the tuple
                            break
                        else:
                            print("\nThis name already exists. Please choose another name.\n")
                            input("<To continue, please press Enter>")

            # Create a new data container for displaying the new/unchanged names
            new_names_dict = {
                "menu_displayed_text": [
                    "New Part Names",
                    "These are the new or unchanged part names:",
                    "<To continue, please press Enter>",
                    ["Part Names"],
                ],
                "menu_entries_results": []
            }
            # Fill in the new part names
            for p, _ in selected_score_part_list:
                if p != 'Full Score':
                    new_names_dict["menu_entries_results"].append([p])
            # Display the new part names
            display_menu_print_results(new_names_dict)

            new_names_correct = {
                "menu_entries": [
                    ["CONF: Confirm", "Yes", "Confirm the names"],
                    ["DONT: Do not confirm", "No", "Reject the names and rename"]
                ],
                "menu_displayed_text": [
                    "Confirmation",
                    "Are these names correct?",
                    "Enter your choice (1-2): ",
                    ["Menu item", "<Explanation>"]
                ]}
            confirmation = display_menu_request_selection(new_names_correct)
            if confirmation == "Yes":
                # Update the global dictionary only after the user has confirmed the changes
                selected_score_part_names.clear()
                selected_score_part_names.update(dict(selected_score_part_list))
                break  # Break the while loop once all renaming operations are completed

    except Exception as e:
        handle_error(e)


def view_score(selected_score: music21.stream.Score) -> None:
    """
    Opens the specified music21 Score object in the default sheet music viewer program.

    The music21 library will attempt to open the Score object in the user's default sheet music
    viewing program. The specific program used can vary depending on the user's system configuration.

    Before the Score is opened, a notice is displayed to the user. The notice informs the user
    that the sheet music viewer program likely needs to be closed before they can continue using
    the tool. The user must press Enter to proceed after reading the notice.

    After the user presses Enter, the Score is opened in the sheet music viewer program.

    Once the Score is displayed, the user can view the sheet music as needed. When they are done,
    they need to close the sheet music viewer program and return to the tool.

    If any exceptions occur while attempting to display the Score or during user interaction,
    they are passed to the `handle_error()` function for error handling.

    Args:
        selected_score (music21.stream.Score): The Score object to be displayed.

    Raises:
        Any exceptions that occur during the execution of this function are caught and passed to
        the `handle_error()` function for error handling.

    Returns:
        None. This function only performs actions and does not return a value.

    See Also:
        1. `display_menu_print_textblock()`: For displaying the notice before the Score is opened.
        2. `handle_error()`: For handling exceptions that occur while attempting to display the Score or during user interaction.
    """

    try:
        message = {
            "menu_displayed_text": [
                "Notice",
                "Please read the following message:",
                "<To open the program, please press Enter>",
                ["", "Message"],
            ],
            "menu_entries_text": [
                ["Message 1", "The program used to view the sheet music probably needs to be closed in order to "
                              "continue"
                              "with the tool."]
            ]
        }
        display_menu_print_textblock(message)
        selected_score.show()

    except Exception as e:
        handle_error(e)
