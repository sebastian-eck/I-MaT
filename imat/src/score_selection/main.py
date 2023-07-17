"""
Module: score_selection.main.py
===============================

This module facilitates the selection and loading of a music score for further analysis or processing.

The primary function in this module, `score_selection`, coordinates the process of selecting a score. The user is
initially offered a choice between selecting from a list of pre-defined scores or providing their own score via
a local file or URL. Depending on their selection, a relevant helper function is invoked to assist the user
through the selection process.

Functions
---------
- `select_score_source`: Displays a menu that allows the user to choose the source of the score.
- `select_example_score`: Shows a menu that lets the user select a predefined score.
- `load_example_score`: Loads the selected example score and provides troubleshooting tips if needed.
- `select_own_score`: Provides instructions to the user for entering a path or URL to their score.
- `load_own_score`: Starts loading the user-provided score and offers troubleshooting advice if needed.

Each function handles user inputs and may return a music21 stream object
representing the selected score or guide the user through the score selection process.

In case of any exceptions during the process, they are caught and redirected to the `handle_error` function for
suitable management and resolution.

Example
-------
>>> from score_selection import main
>>> score = main.load_example_score("path/to/example/score.xml")

Notes
-----
This module heavily relies on the `music21` library, specifically the `music21.converter`
module to load musical scores from various sources and formats.

See Also
--------
music21.converter.parse
music21.stream.Stream
src.utils.error_handling.handle_error

"""

import os
from urllib.parse import urlparse

import requests
from music21 import converter

from iMaT.src.cli.menu_constructors import display_menu_print_textblock, display_menu_request_selection
from iMaT.src.constants import EXAMPLE_SCORES_DICT
from iMaT.src.score_selection.name_parts import select_and_name_parts
from iMaT.src.utils.error_handling import handle_error


def score_selection():
    """
    The main function that orchestrates the selection of music scores.

    This function guides the user through the process of selecting a music score. It first asks the user to choose a
    source for the music score - either from a predefined example or from their own local file or URL. The function
    then loads the selected score and calls the select_and_name_parts function to allow the user to name the parts of
    the score. If any exception occurs during this process, it is caught and passed to the handle_error function.

    See Also:
        select_score_source: Function to select a source of a music score.
        select_example_score: Function to select an example music score.
        select_own_score: Function to select a custom music score.
    """
    try:
        source = select_score_source()
        if source == "example":
            score_url = select_example_score()
            selected_score = load_example_score(score_url)
            select_and_name_parts(selected_score)
        elif source == "own":
            score_url = select_own_score()
            selected_score = load_own_score(score_url)
            select_and_name_parts(selected_score)
        else:
            print("\nInvalid input. Please try again.\n")
            input("<To continue, please press Enter>")
            score_selection()

    except Exception as e:
        handle_error(e)


def select_score_source():
    """
    Helper function to allow the user to select an example music score.

    This function presents the user with a menu of available example scores. The menu entries are constructed based on
    the entries in the example_scores_dict dictionary. The function uses the display_menu_request_selection function
    to present the menu and capture the user's choice. If any exception occurs during this process, it is caught and
    passed to the handle_error function.

    See Also:
        display_menu_request_selection: Function to display a menu and request a selection.
    """
    try:
        source_menu = {
            "menu_displayed_text": [
                "Select Score Source",
                "Please select a source of music scores:",
                "Enter your choice (1 or 2): ",
                ["Menu item", "<Explanation>"],
            ],
            "menu_entries": [
                ["EXMP: Example sheet music file", "example",
                 "<Choose one entry from a list of predefined sheet music files>"],
                ["CSTM: Custom sheet music file", "own",
                 "<Select your own sheet music file by entering a local path or an URL>"],
            ]
        }
        return display_menu_request_selection(source_menu)
    except Exception as e:
        handle_error(e)


def select_example_score():
    """
    Helper function to allow the user to select their own music score.

    This function presents the user with guidelines for inputting the path or URL to their own score. The function
    uses the display_menu_print_textblock function to present the guidelines and capture the user's input. If any
    exception occurs during this process, it is caught and passed to the handle_error function.

    See Also:
        display_menu_print_textblock: Function to display a text block and request user input.
    """
    try:
        score_menu = {
            "menu_displayed_text": [
                "Select Example Score",
                "Please select an example score:",
                "Enter your choice (1-" + str(len(EXAMPLE_SCORES_DICT)) + "): ",
                ["Score Name", "Source/Database"],
            ],
            "menu_entries": [
                [value[0], value[1], value[2]]
                for key, value in EXAMPLE_SCORES_DICT.items()
            ],
        }
        return display_menu_request_selection(score_menu)
    except Exception as e:
        handle_error(e)


def load_example_score(score_url):
    """
    Helper function to load an example music score.

    This function takes as input a URL to an example music score. It first attempts to access the URL, providing
    troubleshooting guidance to the user if this fails. If the URL is successfully accessed, the function then
    attempts to parse the score, again providing troubleshooting guidance if this fails. If the score is successfully
    parsed and contains at least one part, it is returned. Otherwise, the user is prompted to select another score.

    See Also:
        display_menu_print_textblock: Function to display a text block and request user input.
        score_selection: Main function to orchestrate the selection of music scores.
    """
    try:
        response = requests.get(score_url)
        response.raise_for_status()
    except (requests.RequestException, ValueError):
        text_dict = {
            "menu_displayed_text": [
                "Error",
                "The score could not be accessed.",
                "Press Enter to try again: ",
                ["", "Troubleshooting assistance:"]
            ],
            "menu_entries_text": [
                ["Possible reasons:",
                 "1. The URL provided may be incorrect.\n"
                 "2. Your Internet connection might be down.\n"
                 "3. The 'autoDownload' setting in the music21 environment file might be set to 'no', which prevents "
                 "music21 from accessing files from the web."],
                ["Suggestion:",
                 "1. Check the URL you've provided.\n"
                 "2. Check your Internet connection.\n"
                 "3. Change the 'autoDownload' setting in the music21 environment file to 'yes'."]
            ]
        }
        display_menu_print_textblock(text_dict)
        score_selection()
        return

    try:
        score = converter.parse(score_url)
        if len(score.parts) > 0:
            return score
        else:
            text_dict = {
                "menu_displayed_text": [
                    "Error",
                    "The score does not contain any parts.",
                    "Press Enter to try again: ",
                    ["", "Troubleshooting assistance:"]
                ],
                "menu_entries_text": [
                    ["Possible reasons:",
                     "The example score selected may not contain any identifiable parts."],
                    ["Suggestion:",
                     "Please try another example score. The scores should have been vetted for content, but there may "
                     "have been an error."]
                ]
            }
            display_menu_print_textblock(text_dict)
            score_selection()
    except:
        text_dict = {
            "menu_displayed_text": [
                "Error",
                "The score could not be parsed.",
                "Press Enter to try again: ",
                ["", "Troubleshooting assistance:"]
            ],
            "menu_entries_text": [
                ["Possible reasons:",
                 "There might be an issue with the format or content of the selected example score. It could be "
                 "corrupted or in an incompatible format."],
                ["Suggestion:",
                 "Please try selecting another example score. If the issue persists with multiple scores, there may "
                 "be a problem with the parser."]
            ]
        }
        display_menu_print_textblock(text_dict)
        score_selection()


# noinspection HttpUrlsUsage
def select_own_score():
    """
    Helper function to allow the user to select their own music score.

    This function presents the user with guidelines for inputting the path or URL to their own score. The function
    uses the display_menu_print_textblock function to present the guidelines and capture the user's input. If any
    exception occurs during this process, it is caught and passed to the handle_error function.

    See Also:
        display_menu_print_textblock: Function to display a text block and request user input.
    """
    try:
        text_dict = {
            "menu_displayed_text": [
                "Select Your Own Score",
                "Please provide the path to your own score or a URL. Here are some guidelines:",
                "Enter the path or URL: ",
                ["Hints", "Guidelines"],
            ],
            "menu_entries_text": [
                ["File format",
                 "Music21 can parse a variety of file formats including MIDI (.mid, .midi), MusicXML (.xml, .musicxml), "
                 "ABC (.abc), and more. Please make sure your file is in a supported format."],
                ["Path format",
                 "The path to your file should be a string. If the path includes spaces, make sure to surround it with "
                 "quotes. For example: '/Users/username/Documents/My Music/my_file.mid'"],
                ["URL",
                 "You can also provide a URL to a file. Ensure that the URL ends with the file extension, "
                 "like 'http://example.com/my_file.mid'. Not all websites allow direct access to files, so this method "
                 "may not always work."],
                ["Drag and drop",
                 "You can drag and drop the file into the console. The path will be automatically populated. Note: This "
                 "method does not work for URLs."]
            ]
        }
        path = display_menu_print_textblock(text_dict)
        return path

    except Exception as e:
        handle_error(e)


def load_own_score(filepath):
    """
    Helper function to load a user-provided music score.

    This function takes as input a path or URL to a music score. It first checks whether the input is a URL. If it is,
    the function attempts to access the URL, providing troubleshooting guidance to the user if this fails. If the input
    is not a URL, the function checks whether it corresponds to a valid local file path, again providing
    troubleshooting guidance if this fails. If the score file is successfully accessed, the function then attempts to
    parse the score, providing troubleshooting guidance if this fails. If the score is successfully parsed and contains
    at least one part, it is returned. Otherwise, the user is prompted to select another score.

    See Also:
        display_menu_print_textblock: Function to display a text block and request user input.
        score_selection: Main function to orchestrate the selection of music scores.
    """
    try:
        # Check if the given path is a URL
        parsed = urlparse(filepath)
        is_url = bool(parsed.netloc)

        if is_url:
            try:
                response = requests.get(filepath)
                response.raise_for_status()
            except (requests.RequestException, ValueError):
                text_dict = {
                    "menu_displayed_text": [
                        "Error",
                        "The score could not be accessed.",
                        "Press Enter to try again: ",
                        ["", "Troubleshooting assistance:"]
                    ],
                    "menu_entries_text": [
                        ["Possible reasons:",
                         "1. The URL provided may be incorrect.\n"
                         "2. Your Internet connection might be down.\n"
                         "3. The 'autoDownload' setting in the music21 environment file might be set to 'no', "
                         "which prevents music21 from accessing files from the web."],
                        ["Suggestion:",
                         "1. Check the URL you've provided.\n"
                         "2. Check your Internet connection.\n"
                         "3. Change the 'autoDownload' setting in the music21 environment file to 'yes'."]
                    ]
                }
                display_menu_print_textblock(text_dict)
                score_selection()
                return
        else:
            if not os.path.exists(filepath):
                text_dict = {
                    "menu_displayed_text": [
                        "Error",
                        "The file does not exist.",
                        "Press Enter to try again: ",
                        ["", "Troubleshooting assistance:"]
                    ],
                    "menu_entries_text": [
                        ["Possible reasons:",
                         "The file path or URL you've provided may not be valid, or the file may have been moved or "
                         "deleted."],
                        ["Suggestion:",
                         "Check that you've entered the file path or URL correctly. If you're using a file path, "
                         "it should be absolute (including the full path from the root directory) and correctly formatted "
                         "for your operating system. If you're using a URL, ensure it is accessible."]
                    ]
                }
                display_menu_print_textblock(text_dict)
                score_selection()
                return

        try:
            score = converter.parse(filepath)
            if len(score.parts) > 0:
                return score
            else:
                text_dict = {
                    "menu_displayed_text": [
                        "Error",
                        "The score does not contain any parts.",
                        "Press Enter to try again: ",
                        ["", "Troubleshooting assistance:"]
                    ],
                    "menu_entries_text": [
                        ["Possible reasons:",
                         "The file you're providing may not contain a musical score, or it does not contain any "
                         "identifiable parts."],
                        ["Suggestion:",
                         "Please ensure the file is a valid musical score with at least one part, such as a melody or "
                         "harmony line."]
                    ]
                }
                display_menu_print_textblock(text_dict)
                score_selection()
        except:
            text_dict = {
                "menu_displayed_text": [
                    "Error",
                    "The score could not be parsed.",
                    "Press Enter to continue: ",
                    ["", "Troubleshooting assistance:"]
                ],
                "menu_entries_text": [
                    ["Possible reasons:",
                     "There might be an issue with the file format or the content of the file. The file may not be in a "
                     "format that music21 can parse, or it could be corrupted."],
                    ["Suggestion:",
                     "Try using a different file or converting your file to a different format. The file formats "
                     "supported by music21 include MIDI (.mid), MusicXML (.xml), ABC (.abc), and others."]
                ]
            }
            display_menu_print_textblock(text_dict)
            score_selection()

    except Exception as e:
        handle_error(e)