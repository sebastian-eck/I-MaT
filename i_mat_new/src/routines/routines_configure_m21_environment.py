import os
from pathlib import Path

from music21 import environment

from src.cli.cli_menu_structure import display_menu_print_textblock, display_menu_request_selection


def set_user_preferences():
    """
    Prompt user for settings and set preferences in music21.
    """
    # Create new environment file
    us = environment.UserSettings()



    if not os.path.exists(us.getSettingsPath()):
        us.create()

    environment_path = str(us.getSettingsPath())

    # Define a helper function to validate paths
    def validate_path(path):
        return Path(path).exists()

    # Define a helper function to collect a path from the user
    def collect_path(prompt, explanation):
        while True:
            text_dict = {
                "menu_displayed_text": [
                    "-- Path Entry --",
                    "Please enter the path to the desired location.",
                    prompt,
                    ["Hints", "Guidelines"],
                ],
                "menu_entries_text": [
                    ["New Music21 environment file: ", environment_path],
                    explanation,
                    ["Format",
                     "Please provide the full absolute path. E.g., 'C:/Users/<username>/Desktop/Folder'."],
                    ["Drag and Drop",
                     "For a secure and quick way to enter the path, you can navigate to the folder in your file explorer, "
                     "then click on the path at the top, copy it, and paste it here. "
                     "Or, you can drag and drop the folder into this terminal window."],
                ]
            }
            path = display_menu_print_textblock(text_dict)
            if validate_path(path):
                return path
            else:
                text_dict = {
                    "menu_displayed_text": [
                        "-- Invalid Path --",
                        "The path you entered does not exist or cannot be accessed.",
                        "Press Enter to continue.",
                        ["", ""],
                    ],
                    "menu_entries_text": [
                        ["Path entered: ", path],
                        ["Hints", "Guidelines"],
                        ["1. Path does not exist.",
                         "Ensure that the path you have entered is correct and try again."],
                        ["2. Typo in the path.",
                         "Make sure there are no spelling errors in your path."],
                        ["3. Path is not an absolute path.",
                         "Ensure that you provide the complete path to the location, including the drive letter on "
                         "Windows."],
                        ["4. Path includes invalid characters.",
                         "Ensure that your path does not contain any invalid characters."],
                        ["5. Application does not have permission to access the path.",
                         "Ensure that the application has the necessary permissions to access the path."]
                    ]
                }
                display_menu_print_textblock(text_dict)

    # Prompt user for directoryScratch
    directoryScratch_explanation = [
        "Scratch Directory",
        "The 'export folder' or 'scratch directory' is used by Music21 to save temporary files, such as MusicXML "
        "files when showing scores."
        "It is essential for the proper functioning of the system and should point to a directory where these files "
        "can be stored safely."
    ]
    directoryScratch = collect_path("Enter the path to the export folder: ", directoryScratch_explanation)
    us["directoryScratch"] = directoryScratch

    # Prompt user for musescoreDirectPNGPath and musicxmlPath
    musescore_path_explanation = [
        "MuseScore Path",
        "Music21 uses MuseScore to display and print MusicXML sheet music. "
        "For this, we need the path to the MuseScore application. "
        "Please provide the path to your MuseScore4.exe file."
    ]
    musescore_path = collect_path("Enter the path to MuseScore4.exe: ", musescore_path_explanation)
    us["musescoreDirectPNGPath"] = musescore_path
    us["musicxmlPath"] = musescore_path

    # Set autoDownload to "allow"
    us["autoDownload"] = "allow"


def check_environmentFile():
    """
    Check if the music21 environment file exists
    """
    us = environment.UserSettings()
    path_environment_file = us.getSettingsPath()

    text_dict = {
        "menu_displayed_text": [
            "-- Check music21 environment file --",
            "A music21 environment file does not (yet) exist. The file is necessary for the tool to function properly.",
            "Enter your choice (1 or 2): ",
            ["", "Message"]
        ],
        "menu_entries": [
            ["NEW:  Create a new environment file", "create", "A new environment file will be created."],
            ["CONT: Continue without creating a new environment file", "keep", "No environment file will be created"
                                                                               " (not recommended)."]
        ]
    }

    if not os.path.isfile(path_environment_file):
        user_choice = display_menu_request_selection(text_dict)

        # If the user chose to create a new environment file, call set_user_preferences
        if user_choice == "create":
            set_user_preferences()


# def display_and_edit_settings():
#     """
#     Display current settings from the music21 environment file and allow the user to modify them.
#     """
#
#     # Get current settings
#     us = environment.UserSettings()
#     settings = us.keys()
#
#     # Create dictionary for display_menu_request_selection
#     menu_entries = [["{0}".format(setting), "{0}".format(us[setting])]
#                     for setting in settings]
#     menu_entries.append(["Continue without making any changes", ""])
#
#     imat_data_container = {
#         "menu_displayed_text": [
#             "-- Current Settings --",
#             "Please select one of the following settings to modify by entering the corresponding index number:",
#             "Which setting do you want to modify? (<No. of setting>): ",
#             ["Setting", "Current Value"],
#         ],
#         "menu_entries": menu_entries
#     }
#
#     # Get user selection
#     user_choice = display_menu_request_selection(imat_data_container)
#
#     # If the user chose to modify a setting
#     if user_choice != "Continue without making any changes":
#         # Create a dictionary to pass to display_menu_print_textblock
#         text_dict = {
#             "menu_displayed_text": [
#                 "-- Change Setting --",
#                 "You have selected to modify the {0} setting.".format(user_choice),
#                 "Enter a new value for {0}: ".format(user_choice),
#                 ["Setting", "Message"],
#             ],
#             "menu_entries_text": [
#                 ["Current Value", "{0}".format(us[user_choice])],
#                 ["Valid Values", "Enter a valid value according to the type and constraints of the selected setting."],
#             ]
#         }
#
#         # Use display_menu_print_textblock to prompt user for new value
#         new_value = display_menu_print_textblock(text_dict)
#
#         # Set new value
#         us[user_choice] = new_value
#
#         # Inform user of update
#         print("\n{0} updated. Please press Enter to continue.".format(user_choice))
#         input()