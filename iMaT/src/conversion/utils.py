"""
Module: conversion.utils.py
===========================

A module to handle various utility tasks related to the music file conversion process.

This module provides functions for:

- Retrieving a list of parsable music files in a specified directory.
- Displaying a list of parsable music files in a specified directory.
- Displaying the success rate of file conversion.
- Interactively selecting a folder containing parsable music files through a GUI.
- Providing a user interface to select a music file conversion format.
- Adding a new entry to a .xlsx log file.

All of these functions are designed to be used in the conversion process, and exceptions raised during their
execution are handled and displayed to the user.

Functions
---------
- 'get_parsable_files_in_folder': Retrieve a list of parsable music files in a given directory.
- 'display_parseable_files_in_folder': Display a list of parsable music files in a given directory.
- 'display_success_rate': Display the success rate of file conversion.
- 'select_folder': Interactively select a folder containing parsable music files.
- 'select_conversion_format': Provide a user interface to select a music file conversion format.
- 'create_log_entry': Add a new entry to a .xlsx log file.

Raises
------
Exception:
    Any exception that occurs during the execution of the function is handled and displayed to the user.
"""
import os
import tkinter as tk
from tkinter import filedialog

from openpyxl import load_workbook

from iMaT.src.cli.menu_constructors import display_menu_print_results, display_menu_print_textblock, \
    display_menu_request_selection
from iMaT.src.utils.error_handling import handle_error


def get_parsable_files_in_folder(folder_path):
    """
    Retrieve a list of parsable music files in a given directory.

    This function checks a specified directory for files with parsable music file extensions.
    It lists all the files with these extensions.

    Parameters
    ----------
    folder_path : str
        The path of the directory to check.

    Returns
    -------
    list
        A list of filenames of parsable music files.

    Raises
    ------
    Exception
        Any exception that occurs during the execution of the function is handled and displayed to the user.
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
    """
    Displays a list of parsable music files in a given directory.

    This function first retrieves a list of parsable music files in the given directory.
    It then displays these files to the user.

    Parameters
    ----------
    folder_path : str
        The path of the directory to check.

    Returns
    -------
    list
        A list of filenames of parsable music files.

    Raises
    ------
    Exception
        Any exception that occurs during the execution of the function is handled and displayed to the user.
    """
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
    """
    Displays the success rate of file conversion.

    This function calculates the success rate of file conversion based on the total number of files and
    the number of successfully converted files. It then displays this information along with a list of file conversion statuses.

    Parameters
    ----------
    files_status : list
        A list of tuples where each tuple contains a file's name and its conversion status.
    num_converted : int
        The number of files that were successfully converted.
    num_files : int
        The total number of files that were attempted to be converted.

    Raises
    ------
    Exception
        Any exception that occurs during the execution of the function is handled and displayed to the user.
    """
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
    Interactively select a folder containing parsable music files.

    This function displays a GUI file dialog to the user to select a folder. It ensures that the selected folder
    contains at least one parsable music file of the supported types. The function loops until a valid folder is
    selected or the user cancels the operation. It also provides information to the user about the types of parsable
    music files and folder requirements.

    Returns
    -------
    str
        The path to the selected folder containing parsable music files. Returns None if the operation is cancelled.

    Raises
    ------
    Exception
        Any exception that occurs during the execution of the function is handled and displayed to the user.
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
    Provides a user interface to select a music file conversion format.

    This function displays a list of available music file conversion formats to the user and
    prompts them to select one. It continues to prompt the user until a valid selection is made.

    Returns
    -------
    str
        The file extension of the chosen conversion format.

    Raises
    ------
    Exception
        Any exception that occurs during the execution of the function is handled and displayed to the user.
    """
    # Get all available formats.
    formats = [
        ["MIDI: MIDI (.midi, .mid)", '.mid', "<Both .midi and .mid formats are supported without issues>"],
        ["MXML: MusicXML Compressed (.mxl)", '.mxl', "<The compressed MusicXML (.mxl) format is supported without issues>"],
        ["MXML: MusicXML (.musicxml)", '.musicxml', "<The .musicxml format is supported without issues>"],
        ["VOLP: Volpiano (.volpiano)", '.volpiano', "<The .volpiano format is supported without issues>"],
        ["NOTE: Noteworthy (.noteworthy)", '.noteworthy', "<Attention: a bytes-like object is required>"],
        ["NOTE: Noteworthy Compressed (.nwc)", '.nwc', "<Attention: a bytes-like object is required>"]
]

    try:
        # Loop to allow re-selection in case of invalid choice.
        while True:
            # Construct data container for displaying the menu.
            imat_data_container = {
                "menu_displayed_text": [
                    "File Conversion: Conversion formats",
                    "Please select one of the following conversion formats by entering the corresponding index number:",
                    "Which format do you want to select? (<No. of menu item>): ",
                    ["Format", "<Explanation>"]
                ],
                "menu_entries": formats
            }

            # Display menu and return the user's choice.
            return display_menu_request_selection(imat_data_container)

    except Exception as e:
        handle_error(e)


def create_log_entry(list, list_path):
    """
    Add a new entry to a .xlsx log file.

    This function appends a new row to a specified .xlsx file.
    If the file does not exist, it creates a new one.

    Parameters
    ----------
    list : list
        The new row to be added to the .xlsx file. Each element in the list represents a cell in the row.
    list_path : str
        The path of the .xlsx file.

    Returns
    -------
    None

    Raises
    ------
    Exception
        Any exception that occurs during the execution of the function is handled and displayed to the user.
    """
    try:
        wb = load_workbook(list_path)
        ws = wb.active
        ws.append(list)
        wb.save(list_path)

    except Exception as e:
        handle_error(e)
