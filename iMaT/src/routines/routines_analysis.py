import os

from music21 import environment

from src.cli.cli_menu_structure import display_menu_print_results, display_menu_request_selection, \
    util_convert_pd_dataframe_to_imat_datacont
from src.routines.routines_name_parts import selected_score_part_names
from src.routines.routines_score_selection import score_selection
from src.routines.routines_select_parts_and_measures import select_parts_and_measures
from src.visualizations.visualizations_analysis_results import map_analysis_function_to_display_function


def generic_analysis_workflow_single(analysis_func: callable):

    # a. Call the select_parts_and_measures() function, if no score has yet been selected, start the score selection
    # workflow by calling the select_score() function.

    if selected_score_part_names == {}:
        score_selection()

    selected_score, given_name_selected_score, measures_chosen = select_parts_and_measures()

    # Reverse the selected_score_part_names dictionary to map music21 objects to part names or the full score
    identifier = f"{given_name_selected_score}, measures {measures_chosen[0]}-{measures_chosen[1]}"

    # b. Perform the analysis function
    analysis_results = analysis_func(selected_score, identifier)

    # c. Display the results

    results_dict = util_convert_pd_dataframe_to_imat_datacont(analysis_results)
    display_menu_print_results(results_dict)

    # d. Present the user with post-analysis options
    while True:
        option = get_user_option_post_analysis()

        # e. Depending on the user's choice ("repeat", "export", "display_results", or "back")
        if option == "repeat":
            generic_analysis_workflow_single(analysis_func)
            break
        elif option == "export":
            export_results_to_csv_auto(analysis_results, identifier, analysis_func.__name__)
        elif option == "display_results":
            # Get the function to display the results from the mapping:
            display_results_func = map_analysis_function_to_display_function(analysis_func)

            if display_results_func is not None:
                display_results_func(analysis_results, identifier)

        else:
            break


def get_user_option_post_analysis():
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
            ["REPT: Repeat analysis function", 'repeat', "<Repeat the chosen analysis function with a different score selection>"],
            ["EXPT: Export Results to CSV", 'export', "<Explanation>"],
            ["SHOW: Display Results", 'display_results', "<Explanation>"],
            ["BACK: Return to the Last Menu", 'back', "<Returns to the main menu>"],
        ],
    }

    return display_menu_request_selection(imat_data_container)


import datetime

def export_results_to_csv_auto(previous_results, identifier, function_name):
    """
    Automatically export the results of the previous analysis to a CSV file with a unique name.

    The file name is generated using the function_name, modified identifier (selected scores + selected measures),
    and the current time, and the contents of `previous_results` are written to a CSV file in music21's scratch
    directory.
    """
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




