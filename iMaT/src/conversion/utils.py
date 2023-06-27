import os
import tkinter as tk
from tkinter import filedialog

from openpyxl import load_workbook

from src.cli.menu_constructors import display_menu_print_results, display_menu_print_textblock, \
    display_menu_request_selection
from src.utils.error_handling import handle_error


def get_parsable_files_in_folder(folder_path):
    """
    Lists all parsable music files in a given folder.

    Parameters
    ----------
    folder_path : str
        Path to the folder to be searched.

    Returns
    -------
    list
        List of parsable music file names.
    """
    try:
        parsable_extensions = ['.abc', '.capx', '.gex', '.humdrum', '.krn', '.mei', '.midi', '.mid', '.musedata',
                               '.musicxml', '.mxl', '.noteworthy', '.nwc', '.romanText', '.rntxt', '.scala',
                               '.tinynotation', '.volpiano']
        parsable_files = [f for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in parsable_extensions]
        return parsable_files

    except Exception as e:
        handle_error(e)


def display_parseable_files_in_folder(folder_path):
    try:
        while True:

            parsable_files = get_parsable_files_in_folder(folder_path)
            parsable_files_display = parsable_files[:30]  # Only take the first 30 files for display
            if len(parsable_files) > 30:  # If there are more than 30 files, add an indicator at the end
                parsable_files_display.append("... (more files not shown)")

            music_files_dict = {
                "menu_displayed_text":
                    ["File Conversion: Found music files",
                     f"In Folder: '{folder_path}'  ({len(parsable_files)} files found)",
                     "<To continue, please press Enter (enter 'r' to refresh)> ",
                     ["File Path"]],
                "menu_entries_results":
                    [[file] for file in parsable_files_display]
            }

            refresh_choice = display_menu_print_results(music_files_dict)
            if refresh_choice.lower() != 'r':
                break
        return parsable_files

    except Exception as e:
        handle_error(e)


def display_success_rate(files_status, num_converted, num_files):
    try:
        # Create text_dict with both conversion success rate and failed files
        text_dict = {
            "menu_displayed_text": [
                "File Conversion: Conversion Summary",
                f"Conversion Success Rate {num_converted}/{num_files} ({(num_converted / num_files) * 100:.2f}%)",
                "<To continue, please press Enter>",
                ["File name", "Details"]
            ],
            "menu_entries_results": [
                [str(file), f"'{str(status)}'"] for file, status in files_status]
        }
        display_menu_print_results(text_dict)

    except Exception as e:
        handle_error(e)


def select_folder():
    """
    User interface for folder selection. The user can input the path to the desired folder.
    If the path does not exist or does not lead to a directory, an error message is displayed.

    Returns
    -------
    str
        Path to the selected folder.
    """
    parsable_extensions = ['.abc', '.capx', '.gex', '.humdrum', '.krn', '.mei', '.midi', '.mid', '.musedata',
                           '.musicxml', '.mxl', '.noteworthy', '.nwc', '.romanText', '.rntxt', '.scala',
                           '.tinynotation', '.volpiano']

    try:
        while True:
            textblock_dict = {
                "menu_displayed_text": [
                    "-- Folder Selection --",
                    "Please read the following information:",
                    "<To continue and select a folder, please press Enter>",
                    ["", "Information"],
                ],
                "menu_entries_text": [
                    ["Parsable Music File Types",
                     ", ".join(parsable_extensions)],
                    ["Folder Requirements",
                     "The folder must contain at least one parsable music file of the above types to be processed by this tool."],
                    ["Return to Main Menu",
                     "If you do not have a suitable folder with valid files at the moment, press enter and close the selection display that will be displayed right after.\n"
                     "You will then be returned to the Main Menu."]
                ]
            }

            display_menu_print_textblock(textblock_dict)

            root = tk.Tk()
            # root.withdraw()  # Hide the root window

            # Open a file dialog and get the selected file path
            folder_path = filedialog.askdirectory()

            root.destroy()  # Destroy the root window

            if folder_path == "":  # If the user canceled the dialog
                return None

            parsable_files = get_parsable_files_in_folder(folder_path)
            if len(parsable_files) == 0:
                error_message_dict = {
                    "menu_displayed_text": [
                        "File Conversion: Folder Selection - Error",
                        "The selected directory contains no parsable music files:",
                        "<To continue, please press Enter>",
                        ["", "Troubleshooting assistance:"]
                    ],
                    "menu_entries_text": [
                        ["Parsable Music File Types",
                         ", ".join(parsable_extensions)],
                        ["Reason 1:", "There are no parsable music files in the selected directory."],
                        ["Reason 2:", "Ensure the directory you select contains the music files you want to convert."],
                        ["Return to Main Menu",
                         "If you do not have a suitable folder with valid files at the moment, press enter and close the "
                         "selection display that will be displayed right after.\n"
                         "You will then be returned to the Main Menu."]
                    ]
                }
                display_menu_print_textblock(error_message_dict)
                continue
            else:
                return folder_path

    except Exception as e:
        handle_error(e)


def select_conversion_format():
    """
    User interface for conversion format selection. The user can choose a conversion format from a list.
    The function loops until a valid choice is made.

    Returns
    -------
    str
        Chosen conversion format.
    """
    # Get all available formats.
    formats = [['.midi', '.mid', '.midi/.mid ok'],
               ['.mxl', '.mxl', 'ok'],
               ['.musicxml', '.musicxml', 'ok'],
               ['.noteworthy', '.noteworthy', 'Attention: a bytes-like object is required'],
               ['.nwc', '.nwc', 'Attention: a bytes-like object is required'],
               ['.scala', '.scala', 'ok'],
               ['.tinynotation', '.tinynotation', 'ok'],
               ['.abc', '.abc', 'ok'],
               ['.capx', '.capx', 'ok'],
               ['.gex', '.gex', 'conversion not supported'],
               ['.humdrum', '.humdrum', 'ok'],
               ['.krn', '.krn', 'ok'],
               ['.mei', '.mei', 'MEI export is not yet implemented.'],
               ['.musedata', '.musedata', 'ok'],
               ['.romanText', '.romanText', 'ok'],
               ['.rntxt', '.rntxt', 'ok'],
               ['.volpiano', '.volpiano', 'ok']]

    try:
        # Loop to allow re-selection in case of invalid choice.
        while True:
            # Construct data container for displaying the menu.
            imat_data_container = {
                "menu_displayed_text": [
                    "File Conversion: Conversion formats",
                    "Please select one of the following conversion formats by entering the corresponding index number:",
                    "Which format do you want to select? (<No. of menu item>): ",
                    ["Format"]
                ],
                "menu_entries": formats
            }

            # Display menu and return the user's choice.
            return display_menu_request_selection(imat_data_container)

    except Exception as e:
        handle_error(e)


def create_log_entry(list, list_path):
    """
    Appends a new entry to an existing .xlsx file. If the file does not exist, it is created.

    Parameters
    ----------
    list : list
        List of strings to be appended as a new row.
    list_path : str
        Path to the .xlsx file.

    Returns
    -------
    None
    """
    try:
        wb = load_workbook(list_path)
        ws = wb.active
        ws.append(list)
        wb.save(list_path)

    except Exception as e:
        handle_error(e)
