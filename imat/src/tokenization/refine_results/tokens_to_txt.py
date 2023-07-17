"""
Module: tokenization.refine_results.tokens_to_txt.py
====================================================

This module, a part of the `tokenization.refine_results` package, handles the conversion of tokenized data from a CSV file
to individual text files.

Functions
---------
- `tokenization_export_csv_columns_to_txt_file`: Exports a CSV file's contents to individual text files, with directories
  for each column.

- `save_txt_files_to_directory`: Saves data from a dictionary into text files, organizing the files into directories based on keys.

Notes
-----
The module expects CSV files to have a specific structure, including a 'filename' column.
Please refer to the individual function docstrings for more detailed descriptions and examples of usage.
"""
import os
from datetime import datetime

import pandas as pd
from tqdm import tqdm

from iMaT.src.tokenization.utils import select_csv_file_2d_token_representation
from iMaT.src.utils.error_handling import handle_error

tokenizers_available_for_refining = ['CPWord', 'Octuple', 'OctupleMono', 'MuMIDI']

def tokenization_export_csv_columns_to_txt_file():
    """
    Exports the columns of a CSV file to individual text files.

    This function asks the user to select a CSV file, and then groups the DataFrame by filename. For each group,
    it concatenates the values of each column into a string. Finally, it saves each column's concatenated string
    into individual text files in directories named after each column. These directories are then bundled into
    a single directory named 'extracted_data_[current date and time]'.

    Parameters: None

    Returns: None

    See Also
    --------
    select_csv_file_2d_token_representation : Opens a file dialog allowing the user to select a CSV file.
    save_txt_files_to_directory : Saves the refined data into text files in directories named after each column.
    """
    try:
        file_path = select_csv_file_2d_token_representation()

        if file_path is None:
            return

        df = pd.read_csv(file_path)

        # Initialize a dictionary to hold grouped column data
        grouped_data = {}

        # Check if the DataFrame contains the 'filename' column
        if 'filename' in df.columns:

            # Group the data by filename
            grouped = df.groupby('filename')

            # Loop through each group
            for name, group in tqdm(grouped, desc='Grouping data', unit='group'):
                column_data = {}

                # Loop over the remaining columns in the group and concatenate the values into a string
                for column in group.columns:
                    if column != 'filename':
                        column_data[column] = ' '.join(group[column].astype(str).values)

                # Save the column data for the current group in the grouped_data dictionary
                grouped_data[name] = column_data

            # Save the data to the new text files
            save_txt_files_to_directory(grouped_data, file_path)
        else:
            print("'filename' column does not exist in the DataFrame.")

    except Exception as e:
        handle_error(e)


def save_txt_files_to_directory(data, file_path):
    """
    Saves a dictionary of data into text files in directories named after each key.

    Each key-value pair in the data dictionary represents a filename and its associated data respectively.
    For each filename, the function creates a directory and within that directory, it creates a text file for
    each data column and writes the corresponding data into it. These directories are then bundled into a
    single directory named 'extracted_data_[current date and time]'.

    Parameters
    ----------
    data : dict
        The dictionary of data to be saved. Each key-value pair represents a filename and its associated data.
    file_path : str
        The original file path used to generate the new directory's name.

    Returns
    -------
    str
        The path to the newly created directory.

    See Also
    --------
    os.path.dirname : Returns the directory component of a pathname.
    os.makedirs : Recursively creates directories.
    """
    try:
        folder_path = os.path.dirname(file_path)  # Get the directory path of the file
        cleaned_csv_dir = os.path.join(folder_path, "extracted_data_" + datetime.now().strftime("%Y%m%d_%H%M%S"))

        # Create new directory if it does not exist
        os.makedirs(cleaned_csv_dir, exist_ok=True)

        # Loop over the data
        for filename, column_data in tqdm(data.items(), desc='Writing to file', unit='file'):

            # Loop over each column data
            for column_name, data in column_data.items():
                # Create a new directory for the column
                new_dir_path = os.path.join(cleaned_csv_dir, column_name)
                os.makedirs(new_dir_path, exist_ok=True)

                # Define the output file path
                output_file_path = os.path.join(new_dir_path, f"{filename}_{column_name}.txt")

                # Write the data to the output file
                with open(output_file_path, 'w') as output_file:
                    output_file.write(data)

        return cleaned_csv_dir

    except Exception as e:
        handle_error(e)
