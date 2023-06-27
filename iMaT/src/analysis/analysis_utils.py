import datetime
import os

from music21 import environment

from src.cli.cli_menu_structures import display_menu_request_selection
from src.utils.utils_error_handling import handle_error


def display_user_options_post_analysis():
    """
    Presents the user with post-analysis options ("repeat", "export", "display_results", or "back") and gets their selection.
    Returns the user's selection as a string. Use the display_menu_request_selection() to display the possible options.
    """
    imat_data_container = {
        "menu_displayed_text": [
            "Post-Analysis Menu",
            "Please select one of the following options by entering the corresponding index number:",
            "Which option do you want to select? (<No. of option>): ",
            ["Option", "<Explanation>"],
        ],
        "menu_entries": [
            ["REPT: Repeat analysis function", 'repeat',
             "<Repeat the chosen analysis function with a different score selection>"],
            ["EXPT: Export Results to CSV", 'export', "<Explanation>"],
            ["SHOW: Display Results", 'display_results', "<Explanation>"],
            ["BACK: Return to the Last Menu", 'back', "<Returns to the main menu>"],
        ],
    }

    return display_menu_request_selection(imat_data_container)


def export_results_to_csv_auto(previous_results, identifier, function_name):
    """
    Automatically export the results of the previous analysis to a CSV file with a unique name.

    The file name is generated using the function_name, modified identifier (selected scores + selected measures),
    and the current time, and the contents of `previous_results` are written to a CSV file in music21's scratch
    directory.
    """
    try:
        # Prepare the file name and directory
        dir_scratch = environment.UserSettings()["directoryScratch"]
        time_only = datetime.datetime.now().strftime("%H%M%S")
        modified_identifier = identifier.replace(", measures ", "_")  # replace ", measures " with "_"
        filename = f"{function_name}_{modified_identifier}_{time_only}"
        file_path = os.path.join(dir_scratch, f"{filename}.csv")

        # Save the DataFrame to a CSV file
        previous_results.to_csv(file_path, index=False)

        print(f"\nResults exported to {filename}.csv in the directory: {dir_scratch}\n")
        input("<To continue, please press Enter>")

    except Exception as e:
        handle_error(e)
