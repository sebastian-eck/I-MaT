"""
tokenization.refine_results.asbolute_duration.py
================================================

This module, a part of the `tokenization.refine_results` package, refines MIDI data by converting string representations of duration to absolute numerical values.

Functions
---------
- `corpus_tokenization_refine_data_absolute_duration`: Handles a workflow for refining tokenized data by converting duration values to numerical format.

- `convert_duration_to_numerical`: Helper function that converts a duration string to a numerical format.

- `refine_data_function_absolute_duration`: Applies the `convert_duration_to_numerical` function to the 'Duration' column of a DataFrame.

Notes
-----
The module expects CSV files to have a specific structure, including a 'Duration' column.
Please refer to the individual function docstrings for more detailed descriptions and examples of usage.
"""
import re

import pandas as pd
from tqdm import tqdm

from iMaT.src.tokenization.utils import save_data_to_new_csv_file, select_csv_file_2d_token_representation
from iMaT.src.utils.error_handling import handle_error

tqdm.pandas()

from iMaT.src.cli.menu_constructors import display_menu_print_results, display_menu_print_textblock, \
    display_menu_request_selection, util_convert_pd_dataframe_to_imat_datacont

tokenizers_available_for_refining = ['CPWord', 'Octuple', 'OctupleMono', 'MuMIDI']


def corpus_tokenization_refine_data_absolute_duration():
    """
    Executes a workflow for refining tokenized and cleaned CSV data.

    This function guides the user to select a CSV file with a predefined naming pattern, performs data refining operations
    on the data within, and displays a table with the refined results. The user then has an option to save the refined data
    into a new CSV file.

    Parameters: None

    Returns: None

    See Also
    --------
    select_csv_file_2d_token_representation : Opens a file dialog allowing the user to select a CSV file.
    refine_data_function_absolute_duration : Applies the convert_duration_to_numerical function to the 'Duration'
                                             column of a pandas DataFrame.
    """
    try:
        while True:
            file_name = select_csv_file_2d_token_representation()

            if file_name is None:
                break

            df = pd.read_csv(file_name)

            df = refine_data_function_absolute_duration(df)

            # Step 4: show the user the first 30 rows after executing step 2 and 3
            results_dict = util_convert_pd_dataframe_to_imat_datacont(df.head(30))
            display_menu_print_results(results_dict)

            # Step 5: ask the user whether he wants to save the new file
            yes_no_menu = {
                "menu_displayed_text": [
                    "Save Refined Data",
                    "Do you want to save the refined data to a new CSV file?",
                    "Please select your choice (1-2): ",
                    ["Choice", "Description"],
                ],
                "menu_entries": [
                    ["CONT: Save the new file", "Yes", "Yes, save the refined data to a new CSV file"],
                    ["DONT: Do not save the new file", "No", "No, do not save the refined data"],
                ]
            }

            save_input = display_menu_request_selection(yes_no_menu)

            if save_input.lower() == 'yes':
                new_file_path = save_data_to_new_csv_file(df, file_name, "abs_duration_")

                textblock_dict_newfile = {
                    "menu_displayed_text": [
                        "-- New File Path --",
                        "Please read the following message:",
                        "<To continue, please press Enter>",
                        ["", "Message"],
                    ],
                    "menu_entries_text": [
                        ["New File Path", f"The refined data has been saved to a new CSV file: {new_file_path}"]
                    ]
                }

                display_menu_print_textblock(textblock_dict_newfile)
            break

    except Exception as e:
        handle_error(e)


def convert_duration_to_numerical(duration):
    """
    Converts a duration from a string format ("a.b.c") to a numerical value if the format matches.

    The function checks whether the duration starts with the prefix "Duration_", and if so, removes the prefix
    before performing the conversion. If the format of the duration doesn't match the expected format, the function
    returns the original duration.

    Parameters
    ----------
    duration : str
        The duration value to be converted, in "a.b.c" format.

    Returns
    -------
    float or str
        The converted duration as a numerical value, if the format matches.
        The original duration, if the format doesn't match.
    """
    try:
        prefix = ""
        entry_string = str(duration)

        # check if the input string starts with "Duration_"
        if entry_string.startswith("Duration_"):
            prefix = "Duration_"
            entry_string = entry_string[len(prefix):]  # strip off the prefix

        if re.match(r"\d+\.\d+\.\d+", entry_string):
            parts = list(map(float, entry_string.split('.')))
            if len(parts) == 3:
                a, b, c = parts
                return prefix + str(a + b / c)
            else:
                return duration
        else:
            return duration

    except Exception as e:
        handle_error(e)


def refine_data_function_absolute_duration(df):
    """
    Applies the convert_duration_to_numerical function to the 'Duration' column of a pandas DataFrame.

    This function first checks if the 'Duration' column exists in the DataFrame. If so, it applies the
    convert_duration_to_numerical function to each entry in the column, converting string representations of
    duration into numerical values where possible.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to refine.

    Returns
    -------
    pandas.DataFrame
        The DataFrame with converted 'Duration' column.

    See Also
    --------
    convert_duration_to_numerical : Converts a duration from a string format ("a.b.c") to a numerical value
                                    if the format matches.
    """
    try:
        print("Converting 'duration' column to numerical format...")
        if 'Duration' in df.columns:
            df['Duration'] = df['Duration'].progress_apply(convert_duration_to_numerical)

        return df

    except Exception as e:
        handle_error(e)


