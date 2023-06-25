import re

import pandas as pd
from tqdm import tqdm

from src.tokenization.tokenization_helpers import save_data_to_new_csv_file, select_csv_file_2d_token_representation

tqdm.pandas()

from src.cli.cli_menu_structure import display_menu_print_results, display_menu_print_textblock, \
    display_menu_request_selection, \
    util_convert_pd_dataframe_to_imat_datacont

tokenizers_available_for_refining = ['CPWord', 'Octuple', 'OctupleMono', 'MuMIDI']


def corpus_tokenization_refine_data_absolute_duration():
    """
    This function performs several operations to refine tokenized and cleaned CSV data by creating and replacing
    column entries.

    This function first lets the user choose a csv file with a predefined file naming pattern, it then performs data
    enhancing operations, and then displays a table with the results. The user then has an option to save the refined
    data into a new CSV file.

    Parameters: None

    Returns: None
    """
    while True:
        file_name = select_csv_file_2d_token_representation()

        if file_name == None:
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
            new_file_path = save_data_to_new_csv_file(df, file_name)

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


def convert_duration_to_numerical(duration):
    """
    This function converts a duration from a string format ("a.b.c") to a numerical value if the format matches. If
    not, it returns the input as is.

    Parameters:
    duration (str): The duration value to be converted, in "a.b.c" format.

    Returns:
    float: The converted duration as a numerical value, if the format matches.
    str: The original duration, if the format doesn't match.
    """
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


def refine_data_function_absolute_duration(df):
    """
    This function applies the convert_duration_to_numerical function to the 'Duration' column of a pandas DataFrame.

    Parameters:
    df (DataFrame): The input pandas DataFrame.

    Returns:
    DataFrame: The pandas DataFrame with converted 'Duration' column.
    """
    print("Converting 'duration' column to numerical format...")
    if 'Duration' in df.columns:
        df['Duration'] = df['Duration'].progress_apply(convert_duration_to_numerical)

    return df


