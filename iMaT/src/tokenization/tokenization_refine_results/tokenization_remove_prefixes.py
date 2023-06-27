import re

import pandas as pd
from tqdm import tqdm

from src.cli.menu_constructors import display_menu_print_results, display_menu_print_textblock, \
    display_menu_request_selection, util_convert_pd_dataframe_to_imat_datacont
from src.tokenization.utils import save_data_to_new_csv_file, select_csv_file_2d_token_representation


def corpus_tokenization_remove_prefixes():
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


def remove_prefixes_function(df):
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
