"""
tokenization.refine_results.remove_prefixes.py
==============================================

This module, part of the `tokenization.refine_results` package, refines tokenized data in a CSV file by removing unwanted prefixes.

Functions
---------
- `corpus_tokenization_refine_data_remove_prefixes`: Handles a workflow for refining tokenized data by removing unwanted prefixes.

- `remove_prefixes_function`: Helper function used within `corpus_tokenization_refine_data_remove_prefixes` to refine a DataFrame.

Notes
-----
The module expects CSV files to have a specific structure, including a 'filename' column, and is designed to remove prefixes like 'Ignore_'.
Please refer to the individual function docstrings for more detailed descriptions and examples of usage.
"""
import re

import pandas as pd
from tqdm import tqdm

from src.cli.menu_constructors import display_menu_print_results, display_menu_print_textblock, \
    display_menu_request_selection, util_convert_pd_dataframe_to_imat_datacont
from src.tokenization.utils import save_data_to_new_csv_file, select_csv_file_2d_token_representation
from src.utils.error_handling import handle_error


def corpus_tokenization_refine_data_remove_prefixes():
    """
    Refines CSV data by removing unwanted prefixes from the data.

    This function guides the user to select a CSV file, performs data refining operations to remove unwanted
    prefixes (specifically "Ignore_" prefixes and any prefixes that match column names), and displays a
    table with the results. The user then has an option to save the refined data into a new CSV file.

    Parameters: None

    Returns: None

    See Also
    --------
    select_csv_file_2d_token_representation : Opens a file dialog allowing the user to select a CSV file.
    remove_prefixes_function : Refines the pandas DataFrame by removing unwanted prefixes.
    """
    try:
        while True:
            file_name = select_csv_file_2d_token_representation()

            if file_name is None:
                break

            df = pd.read_csv(file_name)

            df = remove_prefixes_function(df)

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
                new_file_path = save_data_to_new_csv_file(df, file_name, "no_prefixes_")

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


def remove_prefixes_function(df):
    """
    Refines a pandas DataFrame by removing unwanted prefixes from the data.

    This function removes "Ignore_" prefixes from all entries in the DataFrame. Then, it iterates over each
    column in the DataFrame and removes any prefixes that match the column name.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to refine.

    Returns
    -------
    pandas.DataFrame
        The DataFrame with removed unwanted prefixes.
    """
    try:
        # tqdm adds a progress bar
        print("Removing 'Ignore_' prefixes...")
        df.replace("Ignore_", "", regex=True, inplace=True)

        # Adding tqdm in for loop for progress bar
        print("Removing column title prefixes...")
        for col in tqdm(df.columns):
            df[col] = df[col].apply(lambda x: re.sub(f'{col}_', '', str(x)))

        return df

    except Exception as e:
        handle_error(e)
