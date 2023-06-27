import glob
import os
import tkinter as tk
from datetime import datetime
from tkinter import filedialog

import pandas as pd
from openpyxl import load_workbook
from tqdm import tqdm

from src.cli.menu_constructors import display_menu_print_results, display_menu_print_textblock
from src.utils.error_handling import handle_error


def save_data_to_new_csv_file(df, file_name, identifier):
    """
    This function saves the refined DataFrame into a new CSV file in a directory named 'enhanced_csv_[current date
    and time]'.

    Parameters:
    df (DataFrame): The pandas DataFrame to be saved.
    file_name (str): The original file name used to generate the new file name.

    Returns:
    str: The path to the new CSV file.
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
    This function opens a file dialog to allow the user to select a CSV file.

    Parameters: None

    Returns:
    str: The path to the selected file, if a file was selected.
    None: None, if the user canceled the dialog.
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
    Lists all MIDI files in a given folder.

    Parameters
    ----------
    folder_path : str
        Path to the folder to be searched.

    Returns
    -------
    list
        List of MIDI file names.
    """
    try:
        tokenizable_extensions = ['.midi', '.mid']
        tokenizable_files = [f for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in tokenizable_extensions]
        return tokenizable_files

    except Exception as e:
        handle_error(e)


def display_success_rate(files_status, num_files_tokenized, num_tokenized):
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
    Combine all CSV files in a given directory into a single CSV file.

    Parameters
    ----------
    directory_path : str
        Path to the directory with the CSV files.
    output_file_name : str
        Name of the combined output CSV file.

    Returns
    -------
    None
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
    Appends a new entry to an existing .xlsx file.

    If the file does not exist, it is created.

    Parameters
    ----------
    log_list : list
        List of strings to be appended as a new row.
    log_list_path : str
        Path to the .xlsx file.

    Returns
    -------
    None
    """
    try:
        wb = load_workbook(log_list_path)
        ws = wb.active
        ws.append(log_list)
        wb.save(log_list_path)

    except Exception as e:
        handle_error(e)
