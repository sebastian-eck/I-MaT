import os
from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilename

from music21 import environment

from src.cli.menu_constructors import display_menu_print_textblock, display_menu_request_selection
from src.utils.error_handling import handle_error


def set_user_preferences():
    """
    Prompt user for settings and set preferences in music21.
    """
    try:
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing

        # Create new environment file
        us = environment.UserSettings()

        if not os.path.exists(us.getSettingsPath()):
            us.create()

        environment_path = str(us.getSettingsPath())

        # Prompt user for directoryScratch
        directoryScratch_dict = {
            "menu_displayed_text": [
                "-- Directory Selection for Scratch Directory --",
                "In the next step, you will be prompted to select the export folder.",
                "<To continue, please press Enter>",
                ["", "Help"]
            ],
            "menu_entries_text": [
                ["New Music21 environment file: ", environment_path],
                ["Scratch Directory Explanation",
                 "The 'export folder' or 'scratch directory' is used by Music21 to save temporary files, "
                 "like MusicXML files when showing scores, as well as for exporting files. "
                 "It should point to a directory where these files can be stored safely and accessed easily."],
                ["Instructions",
                 "A new window will open after you press Enter. "
                 "In this window, navigate to the desired directory and select it."]
            ]
        }
        display_menu_print_textblock(directoryScratch_dict)
        directoryScratch = askdirectory()
        us["directoryScratch"] = directoryScratch
        us["graphicsPath"] = directoryScratch

        # Prompt user for musescoreDirectPNGPath and musicxmlPath
        musescore_path_dict = {
            "menu_displayed_text": [
                "-- File Selection for MuseScore --",
                "In the next step, you will be prompted to select the MuseScore4.exe/MuseScore4 file.",
                "<To continue, please press Enter>",
                ["", "Help"]
            ],
            "menu_entries_text": [
                ["New Music21 environment file: ", environment_path],
                ["MuseScore Path Explanation",
                 "Music21 uses MuseScore to display and print MusicXML sheet music. "
                 "Please provide the path to your MuseScore4.exe file."],
                ["Instructions",
                 "A new window will open after you press Enter. "
                 "In this window, navigate to the desired file and select it."],
                ["Finding MuseScore in Windows",
                 "In Windows, MuseScore is usually installed in the 'Program Files' directory. "
                 "Navigate to: This PC > Local Disk (C:) > Program Files or Program Files (x86) > MuseScore > MuseScore4.exe"],
                ["Finding MuseScore in Mac",
                 "In macOS, MuseScore is usually installed in the 'Applications' directory. "
                 "Navigate to: Applications > MuseScore > MuseScore4.app"]
            ]
        }

        display_menu_print_textblock(musescore_path_dict)
        musescore_path = askopenfilename(filetypes=[("Executable files", "*.exe")])
        us["musescoreDirectPNGPath"] = musescore_path

        # Set autoDownload to "allow"
        us["autoDownload"] = "allow"

    except Exception as e:
        handle_error(e)


def check_environmentFile():
    """
    Check if the music21 environment file exists
    """
    try:
        us = environment.UserSettings()
        path_environment_file = us.getSettingsPath()

        text_dict = {
            "menu_displayed_text": [
                "-- Check music21 environment file --",
                "A music21 environment file does not (yet) exist. The file is necessary for the tool to function properly.",
                "Enter your choice (1 or 2): ",
                ["Menu Item", "<Explanation>"]
            ],
            "menu_entries": [
                ["NEW:  Create a new environment file", "create", "<A new environment file will be created>"],
                ["CONT: Continue without creating a new environment file", "keep", "<No environment file will be created "
                                                                                   " (not recommended)>"]
            ]
        }

        if not os.path.isfile(path_environment_file):
            user_choice = display_menu_request_selection(text_dict)

            # If the user chose to create a new environment file, call set_user_preferences
            if user_choice == "create":
                set_user_preferences()

    except Exception as e:
        handle_error(e)


def display_environment_file():
    """
    Display the contents of the music21 environment file.
    """
    try:
        us = environment.UserSettings()
        path_environment_file = us.getSettingsPath()

        if not os.path.exists(path_environment_file):
            text_dict_no_file = {
                "menu_displayed_text": [
                    "-- music21 environment file --",
                    "There is no music21 environment file yet.",
                    "<To continue, please press Enter>",
                    ["", "Trouble Shooting"]
                ],
                "menu_entries_text": [
                    ["",
                     "You can create a new environment file by selecting 'CONF: Update Software Paths and "
                     "Preferences' in the previous menu and following the prompts to update or redefine paths to "
                     "essential software and user preferences."]
                ],
            }
            display_menu_print_textblock(text_dict_no_file)
            return

        text_dict = {
            "menu_displayed_text": [
                "-- music21 environment file --",
                f"Below are the key-value pairs from your music21 environment file: {path_environment_file}",
                "<To continue, please press Enter>",
                ["Key", "Value"]
            ],
            "menu_entries_text": [],
        }

        for key in sorted(us.keys()):
            value = us[key]
            # Handle None values
            if value is None:
                value = 'None'
            text_dict["menu_entries_text"].append([key, str(value)])

        display_menu_print_textblock(text_dict, textblock_sep_line=False)

    except Exception as e:
        handle_error(e)
