import os
from copy import deepcopy

import matplotlib.cm as cm
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from music21 import environment, note

from src.cli.cli_menu_structures import display_menu_print_results, display_menu_request_selection, \
    util_convert_pd_dataframe_to_imat_datacont
from src.pattern_search.pattern_search_utils import pattern_selection_notes_and_rhythm, \
    pattern_selection_notes_only, pattern_selection_rhythm_only
from src.score_selection.score_selection_name_parts import selected_score_part_names
from src.score_selection.score_selection_main import score_selection
from src.score_selection.score_selection_select_parts_and_measures import select_parts_and_measures


def map_analysis_function_to_display_function(pattern_search_func: callable):
    """
    Returns the corresponding pattern selection function for a provided pattern search function.

    Parameters
    ----------
    analysis_func : callable
        The pattern search function for which the corresponding pattern selection function is to be returned.

    Returns
    -------
    function
        The corresponding pattern selection function.

    """
    function_mapping = {

        'pattern_search_without_transposition_without_rhythm': pattern_selection_notes_only,
        'pattern_search_with_transposition_without_rhythm': pattern_selection_notes_only,
        'pattern_search_without_transposition_with_rhythm': pattern_selection_notes_and_rhythm,
        'pattern_search_with_transposition_with_rhythm': pattern_selection_notes_and_rhythm,
        'pattern_search_only_rhythm': pattern_selection_rhythm_only,
    }

    function_name = pattern_search_func.__name__

    pattern_selection_function = function_mapping[function_name]

    return pattern_selection_function


def generic_analysis_pattern_search(pattern_search_func: callable):
    # a. Call the select_parts_and_measures() function, if no score has yet been selected, start the score selection
    # workflow by calling the select_score() function.

    if selected_score_part_names == {}:
        score_selection()

    selected_score, given_name_selected_score, measures_chosen = select_parts_and_measures()

    # Reverse the selected_score_part_names dictionary to map music21 objects to part names or the full score
    identifier = f"{given_name_selected_score}, measures {measures_chosen[0]}-{measures_chosen[1]}"

    selected_score_deepcopy = deepcopy(selected_score.stripTies())

    selected_score_deepcopy = helper_ignore_rests(selected_score_deepcopy)

    search_pattern, search_pattern_clear_names = map_analysis_function_to_display_function(pattern_search_func)()

    # b. Perform the pattern search function
    pattern_search_results = pattern_search_func(identifier, selected_score_deepcopy, search_pattern,
                                                 search_pattern_clear_names)

    # c. Display the results
    results_dict = util_convert_pd_dataframe_to_imat_datacont(pattern_search_results)
    display_menu_print_results(results_dict)

    # d. Present the user with post-analysis options
    while True:
        option = get_user_option_post_analysis()

        # e. Depending on the user's choice ("repeat", "export", "display_results", or "back")
        if option == "repeat":
            generic_analysis_pattern_search(pattern_search_func)
            break
        elif option == "export":
            export_results_to_csv_auto(pattern_search_results, identifier, pattern_search_func.__name__)
        elif option == "display_results":
            # Get the function to display the results from the mapping:
            display_results_func(pattern_search_results, identifier, pattern_search_func.__name__)
        else:
            break


def display_results_func(pattern_search_results: pd.DataFrame, identifier: str, function_name: str):
    # Check if the pattern_search_results is a pandas DataFrame
    if not isinstance(pattern_search_results, pd.DataFrame):
        print("\nThe input should be a pandas DataFrame\n")
        input("<To continue, please press Enter>")
        return

    # Check if there are no pattern matches
    if "- No Matches Found -" in pattern_search_results.values:
        print("\nNo patterns were found in the selected score.\n")
        input("<To continue, please press Enter>")
        return

    # Get parts in the order they first appear in the DataFrame
    parts = pattern_search_results['Part/Voice'].drop_duplicates().tolist()

    # Map part names to the numerical order they appear in the DataFrame
    part_to_num = {part: i for i, part in enumerate(parts)}
    pattern_search_results['Part/Voice'] = pattern_search_results['Part/Voice'].map(part_to_num)

    # Convert pitch classes to MIDI numbers
    pattern_search_results['Pattern Starting Pitch'] = pattern_search_results['Pattern Starting Pitch'].apply(
        lambda x: note.Note(x).pitch.midi)

    # Convert search pattern to color
    unique_patterns = pattern_search_results['Search Pattern'].unique()
    colors = cm.rainbow(np.linspace(0, 1, len(unique_patterns)))
    pattern_to_color = dict(zip(unique_patterns, colors))
    pattern_search_results['Color'] = pattern_search_results['Search Pattern'].map(pattern_to_color)

    # Create the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(pattern_search_results['Measure'], pattern_search_results['Part/Voice'],
                c=pattern_search_results['Color'])
    plt.xlabel('Measure')
    plt.ylabel('Part/Voice')
    plt.title(f'Pattern Occurrences in Score: {identifier}\nAnalysis Function: {function_name}')
    plt.yticks(range(len(parts)), parts)  # Display original part names on y-axis

    # Create a custom legend to map colors to search patterns
    custom_lines = [Line2D([0], [0], color=color, lw=4) for color in pattern_to_color.values()]
    plt.legend(custom_lines, pattern_to_color.keys(), title='Search Patterns')

    plt.gca().invert_yaxis()  # Invert y-axis to reflect the order from top to bottom
    plt.show()


def helper_ignore_rests(selected_score_deepcopy):
    menu_text = {
        "menu_displayed_text": [
            "Pattern Search Menu",
            "Do you want to search patterns across rests?",
            "Which option do you want to select? (<No. of option>): ",
            ["Option", "Explanation"],
        ],
        "menu_entries": [
            ["YES: Search patterns across notes and rests", "yes", "<Search patterns across notes and rests>"],
            ["NO: Search patterns across notes only", "no", "<Search patterns across notes only>"],
        ],
    }
    ignore_rests = display_menu_request_selection(menu_text)
    if ignore_rests == "yes":
        return selected_score_deepcopy.recurse().notes
    else:
        return selected_score_deepcopy.recurse().notesAndRests


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
            ["Option", "Explanation"],
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
