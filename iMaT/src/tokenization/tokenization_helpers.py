import os
import tkinter as tk
from datetime import datetime
from tkinter import filedialog

from src.cli.cli_menu_structures import display_menu_print_textblock


def save_data_to_new_csv_file(df, file_name):
    """
    This function saves the refined DataFrame into a new CSV file in a directory named 'enhanced_csv_[current date
    and time]'.

    Parameters:
    df (DataFrame): The pandas DataFrame to be saved.
    file_name (str): The original file name used to generate the new file name.

    Returns:
    str: The path to the new CSV file.
    """
    folder_path = os.path.dirname(file_name)  # Get the directory path of the file
    cleaned_csv_dir = os.path.join(folder_path, "enhanced_csv_" + datetime.now().strftime("%Y%m%d_%H%M%S"))

    # Create new directory if it does not exist
    if not os.path.exists(cleaned_csv_dir):
        os.makedirs(cleaned_csv_dir)

    # Step 6: save the new file in the new directory
    new_file_path = os.path.join(cleaned_csv_dir, 'enhanced_' + os.path.basename(file_name))
    df.to_csv(new_file_path, index=False)

    return new_file_path


def select_csv_file_2d_token_representation():
    """
    This function opens a file dialog to allow the user to select a CSV file.

    Parameters: None

    Returns:
    str: The path to the selected file, if a file was selected.
    None: None, if the user canceled the dialog.
    """
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
