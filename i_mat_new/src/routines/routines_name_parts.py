"""
This module includes three main functions related to the handling of music scores:

1. select_and_name_parts: A function to initialize the selected_score_part_names dictionary and present the user
with menu options for naming the parts of the score. The function allows the user to assign individual names to
parts, use generic names or view the selected sheet music. The function then calls the appropriate function
based on the user's choice.

2. rename_parts: A function to rename the parts of a selected score. This function first makes a local copy of
the selected_score_part_names dictionary and then iterates through it to present the user with current part
names. The user can choose to provide a new name for each part. If the new name is not already in use and the user
confirms the changes, the function then updates the global selected_score_part_names dictionary.

3. view_score: A function to display the selected music score using music21's show() method. Before displaying the
score, the function presents the user with a notice regarding the possible need to close the music score viewing
program to continue using the tool.


Module-level variable definitions
---------------------------------

selected_score_part_names: dict
    A global dictionary that holds mappings between the names assigned to parts of a selected music score
    and their corresponding music21 stream.Part objects. The key 'full' is reserved for the complete Score object.
"""

import music21

from src.cli.cli_menu_structure import display_menu_print_results, display_menu_print_textblock, \
    display_menu_request_selection
from src.utils.utils_errorhandling import handle_error


def select_and_name_parts(selected_score: music21.stream.Score) -> None:
    def select_and_name_parts(selected_score: music21.stream.Score) -> None:
        """
        Provides the user with the option to assign custom names or use generic names for parts of a music21 Score
        object.

        The function initially clears and refills the 'selected_score_part_names' dictionary, mapping names (keys) to
        parts of the provided Score object (values). The "full" key is used to represent the entire Score object.

        A while loop is initiated which presents the user with a menu to either assign individual names, use generic
        names, or view the selected score. This loop continues until the user makes a choice that breaks the loop.

        If the user chooses to assign individual names, the 'rename_parts()' function is called, which lets the user
        rename each part as desired. After renaming, the loop breaks.

        If the user chooses to use generic names, the current state of the 'selected_score_part_names' dictionary is
        printed and the loop breaks.

        If the user chooses to view the selected score, the 'view_score()' function is called, opening the score in the
        user's default sheet music viewer.

        Any exceptions that occur during execution are passed to the 'handle_error()' function for error handling.

        Args:
            selected_score (music21.stream.Score): The Score object for which parts are to be named.

        Raises:
            Any exceptions that occur during execution are caught and passed to the 'handle_error()' function.

        Returns:
            None. This function operates on the global 'selected_score_part_names' dictionary and does not return a value.
        """

    try:
        selected_score_part_names.clear()  # Clear the dictionary
        selected_score_part_names["full"] = selected_score  # Modify the dictionary
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
                    ["INDV: Assign individual/custom names to parts", "Assign individual names",
                     "<Type in custom names for individual parts>"],
                    ["GNRC: Assign generic names to parts", "Use generic names",
                     "<Use generic names (Part 1, Part 2, etc.)>"],
                    ["VIEW: View the selected sheet music", "View the score",
                     "<Open the score for viewing in the defined sheet music program>"],
                ]
            }

            choice = display_menu_request_selection(menu_text)

            if choice == "Assign individual names":
                rename_parts()  # Modify the dictionary directly
                break
            elif choice == "Use generic names":
                print(selected_score_part_names)
                break
            elif choice == "View the score":
                view_score(selected_score)
    except Exception as e:
        handle_error(e)




selected_score_part_names = {}


def rename_parts() -> None:
    """
    Interactive function that allows the user to rename parts in a musical score.
    The function operates on a global dictionary `selected_score_part_names`, where
    keys are part names and values are part objects.

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
    """
    try:
        global selected_score_part_names

        # Operate on a local copy of the global dictionary
        local_copy = selected_score_part_names.copy()

        while True:
            # Convert the dictionary to a list of tuples
            selected_score_part_list = list(local_copy.items())

            for i, (part, value) in enumerate(selected_score_part_list):
                if part != 'full':
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
                        if p != 'full':
                            arrow = "  <-----" if p == part else ""
                            part_name_dict["menu_entries_results"].append([str(p + arrow)])
                    # Display the part names and get new name
                    new_name = display_menu_print_results(part_name_dict)
                    # Continue if no name entered
                    if not new_name:
                        continue
                    # If the new name doesn't already exist, use it
                    elif new_name not in dict(selected_score_part_list).values():
                        selected_score_part_list[i] = (new_name, value)  # update the key in the tuple
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
                if p != 'full':
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
        selected_score.show()
        display_menu_print_textblock(message)
    except Exception as e:
        handle_error(e)
