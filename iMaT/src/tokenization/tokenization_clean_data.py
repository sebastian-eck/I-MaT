import datetime
import os
import re
from datetime import datetime

import pandas as pd
from tqdm import tqdm

from src.cli.cli_menu_structure import display_menu_print_results, display_menu_print_textblock, \
    display_menu_request_selection, \
    util_convert_pd_dataframe_to_imat_datacont
from src.tokenization.tokenization_helpers import select_csv_file_2d_token_representation


def corpus_tokenization_refine_data_remove_prefixes():
    """
    Refines the data from a previously tokenized csv file by removing unwanted prefixes from the data.
    The csv file should be named according to either of the two patterns:
    1) 00_combined_tokenizer_[tokenizer name]_tokens.csv
    2) [some individual file name string]_tokenizer_[tokenizer name]_tokens.csv
    where [tokenizer name] should be from the tokenizers_available_for_refining list.
    """
    while True:
        file_name = select_csv_file_2d_token_representation()

        if file_name is None:
            break

        df = pd.read_csv(file_name)

        df = refine_data_function(df)

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


def refine_data_function(df):
    """
    Refines the DataFrame by removing unwanted prefixes from the data.
    """

    # tqdm adds a progress bar
    print("Removing 'Ignore_' prefixes...")
    df.replace("Ignore_", "", regex=True, inplace=True)

    # Adding tqdm in for loop for progress bar
    print("Removing column title prefixes...")
    for col in tqdm(df.columns):
        df[col] = df[col].apply(lambda x: re.sub(f'{col}_', '', str(x)))

    return df


def save_data_to_new_csv_file(df, file_name):
    """
    Save the refined DataFrame to a new CSV file.
    """
    folder_path = os.path.dirname(file_name)  # Get the directory path of the file
    cleaned_csv_dir = os.path.join(folder_path, "cleaned_csv_" + datetime.now().strftime("%Y%m%d_%H%M%S"))

    # Create new directory if it does not exist
    if not os.path.exists(cleaned_csv_dir):
        os.makedirs(cleaned_csv_dir)

    # Step 6: save the new file in the new directory
    new_file_path = os.path.join(cleaned_csv_dir, 'cleaned_' + os.path.basename(file_name))
    df.to_csv(new_file_path, index=False)

    return new_file_path

#corpus_tokenization_refine_data_remove_prefixes()
