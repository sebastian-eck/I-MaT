"""
Module: tokenization.utils.py
=============================

This module provides various utility functions that assist in the tokenization of MIDI files and handling of data.

Functions
---------
- `save_data_to_new_csv_file`: Saves a DataFrame to a new CSV file in a timestamped directory.
- `select_csv_file_2d_token_representation`: Opens a dialog for the user to select a CSV file.
- `display_tokenizable_files_in_folder`: Prints all the tokenizable files in a specific folder.
- `get_tokenizable_files_in_folder`: Retrieves all tokenizable MIDI files in a specific folder.
- `display_success_rate`: Shows the success rate of the tokenization process and any errors.
- `combine_csv_files_in_directory`: Merges all CSV files in a specific directory into one CSV file.
- `create_log_entry`: Adds a new entry to an existing Excel file, or creates a new one if it doesn't exist.

Notes
-----
These functions are used throughout the package to facilitate the tokenization process for MIDI files and ensure correct data handling, saving, and logging.
Please refer to the individual function docstrings for more detailed descriptions and examples of usage.
"""
import glob
import os
import tkinter as tk
from datetime import datetime
from tkinter import filedialog

import pandas as pd
from openpyxl import load_workbook
from tqdm import tqdm

from iMaT.src.cli.menu_constructors import display_menu_print_results, display_menu_print_textblock
from iMaT.src.utils.error_handling import handle_error


def save_data_to_new_csv_file(df, file_name, identifier):
    """
    Saves the refined DataFrame to a new CSV file in a directory named 'enhanced_csv_[current date and time]'.

    This function extracts the directory path of the provided file, then creates a new directory in that path
    with the provided identifier and current timestamp. The DataFrame is then saved to this new directory
    with the identifier prepended to the original filename.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to be saved.
    file_name : str
        The original file name used to generate the new file name.
    identifier : str
        A string to be used as an identifier for the new directory and file name.

    Returns
    -------
    str
        The path to the new CSV file.

    Raises
    ------
    Exception
        If an error occurs during directory creation or file saving.
    """
    try:
        folder_path = os.path.dirname(file_name)  # Get the directory path of the file
        cleaned_csv_dir = os.path.join(folder_path, identifier + datetime.now().strftime("%Y%m%d_%H%M%S"))

        # Create new directory if it does not exist
        if not os.path.exists(cleaned_csv_dir):
            os.makedirs(cleaned_csv_dir)

        # Step 6: save the new file in the new directory
        new_file_path = os.path.join(cleaned_csv_dir, identifier + os.path.basename(file_name))
        df.to_csv(new_file_path, index=False)

        return new_file_path

    except Exception as e:
        handle_error(e)


def select_csv_file_2d_token_representation():
    """
    Opens a file dialog allowing the user to select a CSV file.

    This function guides the user to select a suitable CSV file for further processing.
    It makes use of a graphical file dialog and informs the user about the requirements
    for the file selection via terminal outputs.

    Returns
    -------
    str
        The path to the selected file if a file was selected.
    None
        None if the user canceled the dialog.

    Raises
    ------
    Exception
        If an error occurs during file selection.
    """
    try:
        while True:

            textblock_dict_tokenizer = {
                "menu_displayed_text": [
                    "-- Tokenized File Selection --",
                    "Please read the following information:",
                    "<To continue and select a file, please press Enter>",
                    ["", "Information"],
                ],
                "menu_entries_text": [
                    ["Valid Files",
                     "The selected file must be processed by any of the following tokenizers in order to be processed by this tool:"],
                    ["Tokenizers:", "CPWord, Octuple, OctupleMono, MuMIDI (Two-Dimensional Tokenizers)"],
                    ["File Requirements",
                     "The filename must contain one of these strings: 'CPWord', 'Octuple', 'OctupleMono', 'MuMIDI'.\n"
                     "Please select a file that matches this requirement."],
                    ["Return to Main Menu",
                     "If you do not have a suitable file at the moment, press enter and close the selection display that will be displayed right after.\n"
                     "You will then be returned to the Main Menu."]
                ]
            }

            display_menu_print_textblock(textblock_dict_tokenizer)

            root = tk.Tk()
            # root.withdraw()  # Hide the root window

            # Open a file dialog and get the selected file path
            file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

            root.destroy()  # Destroy the root window

            # Verifying the selected file name
            base_file_name = os.path.basename(file_path)  # Get the file name without the directory path

            textblock_dict_tokenizer = {
                "menu_displayed_text": [
                    "-- Tokenizer Warning --",
                    "Please read the following warning:",
                    "<To continue, please press Enter>",
                    ["", "Warning"],
                ],
                "menu_entries_text": [
                    ["Tokenizer Warning",
                     "The selected file does not contain the name of any of the valid tokenizers.\n"
                     "Please select a file that matches one of the required patterns and includes a valid tokenizer name."]
                ]
            }

            if file_path == "":  # If the user canceled the dialog
                return None

            tokenizers_available_for_refining = ['CPWord', 'Octuple', 'OctupleMono', 'MuMIDI']

            if not any(tokenizer in base_file_name for tokenizer in tokenizers_available_for_refining):
                display_menu_print_textblock(textblock_dict_tokenizer)
                continue

            if file_path:  # If a file was selected
                return file_path

    except Exception as e:
        handle_error(e)


def display_tokenizable_files_in_folder(folder_path):
    """
    Displays the tokenizable files in the provided directory.

    The function uses the 'get_tokenizable_files_in_folder' function to fetch all tokenizable files from
    the directory. Then, it displays the files to the user. If more than 30 files exist in the directory,
    only the first 30 are displayed, along with a note indicating more files are not shown.

    Parameters
    ----------
    folder_path : str
        The path of the directory to search for tokenizable files.

    Returns
    -------
    list
        A list of tokenizable file names.

    Raises
    ------
    Exception
        If an error occurs during the process.
    """
    try:
        while True:

            tokenizable_files = get_tokenizable_files_in_folder(folder_path)
            tokenizable_files_display = tokenizable_files[:30]  # Only take the first 30 files for display
            if len(tokenizable_files) > 30:  # If there are more than 30 files, add an indicator at the end
                tokenizable_files_display.append("... (more files not shown)")

            music_files_dict = {
                "menu_displayed_text":
                    [f"File Tokenization: Found MIDI files ({len(tokenizable_files)} files found)",
                     f"In Folder: '{folder_path}'",
                     "<To continue, please press Enter (enter 'r' to refresh)> ",
                     ["File Path"]],
                "menu_entries_results":
                    [[file] for file in tokenizable_files_display]
            }
            refresh_choice = display_menu_print_results(music_files_dict)
            if refresh_choice.lower() != 'r':
                break
        return tokenizable_files

    except Exception as e:
        handle_error(e)


def get_tokenizable_files_in_folder(folder_path):
    """
    Retrieves all tokenizable MIDI files in the given folder.

    This function inspects the given directory and identifies all files with the extensions '.midi' or '.mid',
    which are considered tokenizable.

    Parameters
    ----------
    folder_path : str
        The path of the folder to be searched.

    Returns
    -------
    list
        A list of filenames that can be tokenized.

    Raises
    ------
    Exception
        If an error occurs during the process.
    """
    try:
        tokenizable_extensions = ['.midi', '.mid']
        tokenizable_files = [f for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in tokenizable_extensions]
        return tokenizable_files

    except Exception as e:
        handle_error(e)


def display_success_rate(files_status, num_files_tokenized, num_tokenized):
    """
    Displays the tokenization success rate and details of failed tokenizations.

    This function calculates and displays the success rate of file tokenization. It also identifies
    and displays any failed tokenizations, including details of the associated tokenizer and file.

    Parameters
    ----------
    files_status : list
        A list of status messages from the file tokenization process.
    num_files_tokenized : int
        The total number of files that were attempted to be tokenized.
    num_tokenized : int
        The total number of files that were successfully tokenized.

    Returns
    -------
    None

    Raises
    ------
    Exception
        If an error occurs during the process.
    """
    try:
        # Create text_dict with both tokenization success rate and failed files
        failed_files_status = [status for status in files_status if "<successfully converted>" not in status]
        if failed_files_status:  # If there are failed tokenizations
            # Filter out only the failed tokenizations and create text_dict with failed files only
            text_dict = {
                "menu_displayed_text": [
                    "File Tokenization: Tokenization Summary",
                    f"Conversion Success Rate {num_tokenized}/{num_files_tokenized} ({(num_tokenized / num_files_tokenized) * 100:.2f}%)",
                    "<To continue, please press Enter>",
                    ["Tokenizer name", "File name", "Details"]
                ],
                "menu_entries_results": [
                    [str(tokenizer_name), str(file), f"'{str(status)}'"] for tokenizer_name, file, status in
                    failed_files_status]
            }
        else:  # If there are no failed tokenizations
            # Show the first 30 successful tokenizations, or all if less than 30
            num_successful_files = min(30, len(files_status))
            successful_files_status = files_status[:num_successful_files]
            successful_files_display = successful_files_status
            if len(files_status) > 30:  # If there are more than 30 files, add an indicator at the end
                successful_files_display.append(["...", "...", "<more files not shown>"])
            text_dict = {
                "menu_displayed_text": [
                    "File Tokenization: Tokenization Summary",
                    f"Conversion Success Rate {num_tokenized}/{num_files_tokenized} ({(num_tokenized / num_files_tokenized) * 100:.2f}%)",
                    "<To continue, please press Enter>",
                    ["Tokenizer name", "File name", "Details"]
                ],
                "menu_entries_results": [
                    [str(tokenizer_name), str(file), f"'{str(status)}'"] for tokenizer_name, file, status in
                    successful_files_display]
            }
        display_menu_print_results(text_dict)

    except Exception as e:
        handle_error(e)


def combine_csv_files_in_directory(directory_path, output_file_name):
    """
    Combines all CSV files in a given directory into a single CSV file.

    This function reads all CSV files in the provided directory, extracts the original filenames from these files,
    and adds these as a new column in the DataFrames. The DataFrames are then concatenated and saved as a new CSV file
    in the same directory.

    Parameters
    ----------
    directory_path : str
        The path to the directory containing the CSV files.
    output_file_name : str
        The name of the combined output CSV file.

    Returns
    -------
    None

    Raises
    ------
    Exception
        If an error occurs during the process.
    """
    try:
        # Get a list of all CSV files in the directory
        csv_files = glob.glob(os.path.join(directory_path, "*.csv"))

        # Initialize an empty list to hold DataFrames
        df_list = []
        # Loop through each CSV file
        for csv_file in tqdm(csv_files, ncols=70):  # Wrap csv_files with tqdm for progress bar
            # Read the CSV file into a DataFrame
            df = pd.read_csv(csv_file)

            # Extract the original file name from the CSV file name
            original_file_name = os.path.basename(csv_file).split('_tokenizer')[0]
            # Assuming file names are in the format "<original_name>_tokenizer_<tokenizer_name>_tokens.csv"

            # Insert it into a new column at the start of the DataFrame
            df.insert(0, 'filename', original_file_name)

            # Append the DataFrame to the list
            df_list.append(df)

        # Concatenate all DataFrames in the list
        combined_df = pd.concat(df_list, ignore_index=True)

        # Save the combined DataFrame to a CSV file
        combined_df.to_csv(os.path.join(directory_path, output_file_name), index=False)

    except Exception as e:
        handle_error(e)


def create_log_entry(log_list, log_list_path):
    """
    Appends a new entry to an existing .xlsx file or creates the file if it doesn't exist.

    The function uses the openpyxl library to open or create a .xlsx file at the provided path.
    It then appends the provided log_list as a new row to the first sheet of the workbook.

    Parameters
    ----------
    log_list : list
        A list of strings to be appended as a new row.
    log_list_path : str
        The path to the .xlsx file.

    Returns
    -------
    None

    Raises
    ------
    Exception
        If an error occurs during the process.
    """
    try:
        wb = load_workbook(log_list_path)
        ws = wb.active
        ws.append(log_list)
        wb.save(log_list_path)

    except Exception as e:
        handle_error(e)
