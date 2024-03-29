"""
Module: tokenization.refine_results.calculate_pitch_intervals.py
================================================================

This module, part of the `tokenization.refine_results` package, refines tokenized MIDI data by calculating pitch intervals.

Functions
---------
- `tokenization_calculate_pitch_intervals`: Handles a workflow for refining tokenized MIDI data by calculating pitch intervals.

- `calculate_pitch_intervals_function`: Helper function used within `tokenization_calculate_pitch_intervals` to add a pitch interval column to a DataFrame.

Notes
-----
The module expects CSV files to have a specific structure, including a 'filename' column, and pitches should be represented as MIDI pitch values.
Please refer to the individual function docstrings for more detailed descriptions and examples of usage.
"""
import numpy as np
import pandas as pd
from tqdm import tqdm

from iMaT.src.cli.menu_constructors import display_menu_print_results, display_menu_print_textblock, \
    display_menu_request_selection, util_convert_pd_dataframe_to_imat_datacont
from iMaT.src.tokenization.utils import save_data_to_new_csv_file, select_csv_file_2d_token_representation
from iMaT.src.utils.error_handling import handle_error


def tokenization_calculate_pitch_intervals():
    """
    Executes a workflow for refining CSV data by calculating pitch intervals.

    This function guides the user to select a CSV file, performs data refining operations to calculate pitch
    differences between the current row and the next row (grouped by filename if available), and displays a
    table with the results. The user then has an option to save the refined data into a new CSV file.

    Parameters: None

    Returns: None

    See Also
    --------
    select_csv_file_2d_token_representation : Opens a file dialog allowing the user to select a CSV file.
    calculate_pitch_intervals_function : Refines a pandas DataFrame by calculating pitch differences
                                         between the current row and the next row, grouping by filename if available.
    """
    try:
        while True:
            file_name = select_csv_file_2d_token_representation()

            if file_name is None:
                break

            df = pd.read_csv(file_name)

            df = calculate_pitch_intervals_function(df)

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
                new_file_path = save_data_to_new_csv_file(df, file_name, "add_pitch_interval_")

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


def calculate_pitch_intervals_function(df):
    """
    Refines a pandas DataFrame by calculating pitch differences between the current row and the next row.

    This function first checks if the 'Pitch' column exists in the DataFrame. If so, it calculates the pitch
    differences between the current row and the next row. The operation is performed for each unique filename
    if a 'filename' column exists in the DataFrame. If the 'Pitch' column contained non-numeric entries
    (i.e., had a prefix), it adds the prefix to the calculated difference values.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to refine.

    Returns
    -------
    pandas.DataFrame
        The DataFrame with added 'PitchDifferenceToNextPitch' column.

    See Also
    --------
    pandas.DataFrame.diff : Calculates the difference of a DataFrame element compared with another
                            element in the DataFrame (default is the element in the same column of the previous row).
    pandas.DataFrame.shift : Shifts index by desired number of periods with an optional time freq.
    """
    try:
        if 'Pitch' not in df.columns:
            return df

        prefix = "Pitch_"
        df["PurePitch"] = df["Pitch"].apply(lambda x: float(x[len(prefix):]) if x.startswith(prefix) else float(x))

        # Check if "Pitch_" prefix is present
        has_prefix = df["Pitch"].str.startswith(prefix).any()

        # Initialize a new column for pitch differences with NaNs
        df['PitchDifferenceToNextPitch'] = np.nan

        # Calculate pitch differences, grouped by 'filename' if it exists
        if 'filename' in df.columns:
            filenames = df['filename'].unique()
            for filename in tqdm(filenames, desc='Calculating pitch differences'):
                filename_group = df[df['filename'] == filename].sort_index()
                notes_only = filename_group[~filename_group['PurePitch'].isna()]
                differences = notes_only['PurePitch'].diff().shift(-1)
                df.loc[differences.index, 'PitchDifferenceToNextPitch'] = differences
        else:
            notes_only = df[~df['PurePitch'].isna()]
            differences = notes_only['PurePitch'].diff().shift(-1)
            df.loc[differences.index, 'PitchDifferenceToNextPitch'] = differences

        # If 'Pitch' column had non-numeric entries (i.e., had a prefix), add prefix to the calculated difference values
        if has_prefix:
            df['PitchDifferenceToNextPitch'] = 'PitchDifferenceToNextPitch_' + df['PitchDifferenceToNextPitch'].astype(str)

        # Cleanup - remove PurePitch column
        df = df.drop(columns="PurePitch")

        return df

    except Exception as e:
        handle_error(e)





