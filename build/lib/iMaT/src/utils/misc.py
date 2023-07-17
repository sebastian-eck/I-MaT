"""
utils.misc.py
=============

This module, part of the `utils` package, provides various utilities for manipulating, displaying and exporting
musical score metadata, part names, and analysis results. It uses the `music21` library for handling music data
and the pandas library for managing and exporting analysis results as a CSV file.

Functions
---------
- `show_metadata()`: Displays the metadata of the selected musical score.
- `show_part_names()`: Lists the names of the individual parts in the selected score.
- `change_part_names()`: Provides an interface for the user to rename the individual parts in the selected score.
- `export_results_to_csv_auto(previous_results, identifier, function_name)`: Exports the results of the
   previous analysis to a CSV file. The file name is automatically generated based on the analysis function name, a modified
   identifier (selected scores + selected measures), and the current timestamp.
"""
import datetime
import os

from music21 import environment

from iMaT.src.cli.menu_constructors import display_menu_print_results
from iMaT.src.score_selection.name_parts import select_and_name_parts, selected_score_part_names
from iMaT.src.utils.error_handling import handle_error


def show_metadata():
    """
    Display metadata of the selected score.

    This function extracts and displays the metadata of the selected musical score.
    If no score has been selected, it prompts the user to select a score first.

    Raises
    ------
    Exception
        If there is an error during metadata extraction or displaying.
    """
    try:
        selected_score = selected_score_part_names.get('Full Score', None)

        if selected_score is None:

            print("\nNo score has yet been selected. Please select a new score first.\n")
            input("<To continue, please press Enter>")

            return

        else:

            metadata = selected_score.metadata.all()
            metadata_entries = [list(item) for item in metadata]
            num_entries = len(metadata_entries)

            if num_entries == 0:
                metadata_entries = [["None", "No metadata available."]]
                num_entries = 1

            results_dict = {
                "menu_displayed_text": [
                    "Metadata for the selected score",
                    f"There are {num_entries} metadata entries available:",
                    "<To continue, please press Enter>",
                    ["Metadata", "Value"],
                ],
                "menu_entries_results": metadata_entries,
            }

            display_menu_print_results(results_dict)

    except Exception as e:
        handle_error(e)


def show_part_names():
    """
    Display the names of individual parts in the selected score.

    This function extracts and displays the names of the individual parts/voices
    in the selected musical score. If no score has been selected, it prompts the
    user to select a score first.

    Raises
    ------
    Exception
        If there is an error during part names extraction or displaying.
    """
    try:
        selected_score = selected_score_part_names.get('Full Score', None)

        if selected_score is None:

            print("\nNo score has yet been selected. Please select a new score first.\n")
            input("<To continue, please press Enter>")

            return

        else:

            part_names = [name for name in selected_score_part_names.keys() if name != 'Full Score']
            num_entries = len(part_names)

            # Structure the part names for display
            part_names_for_display = [[name] for name in part_names]

            results_dict = {
                "menu_displayed_text": [
                    f"Part names given dsignated within the selected scores",
                    f"There are {num_entries} parts and corresponding names available:",
                    "<To continue, please press Enter>",
                    ["Part Name"],
                ],
                "menu_entries_results": part_names_for_display,
            }

            display_menu_print_results(results_dict)

    except Exception as e:
        handle_error(e)


def change_part_names():
    """
    Modify the names of individual parts in the selected score.

    This function allows the user to rename the individual parts/voices in the selected
    musical score. If no score has been selected, it prompts the user to select a score first.

    Raises
    ------
    Exception
        If there is an error during part names modification.
    """
    try:
        selected_score = selected_score_part_names.get('Full Score', None)

        if selected_score is None:

            print("\nNo score has yet been selected. Please select a new score first.\n")
            input("<To continue, please press Enter>")

            return

        else:

            select_and_name_parts(selected_score)

    except Exception as e:
        handle_error(e)


def export_results_to_csv_auto(previous_results, identifier, function_name):
    """
    Export previous analysis results to a CSV file.

    This function automatically exports the results of the previous analysis to a CSV file with a unique name.
    The file name is based on the function_name, a modified identifier (selected scores + selected measures),
    and the current time. The file is saved in the music21's scratch directory.

    Parameters
    ----------
    previous_results : pandas.DataFrame
        The DataFrame containing the results of the previous analysis.

    identifier : str
        The identifier of the selected scores and measures.

    function_name : str
        The name of the function that performed the analysis.

    Raises
    ------
    Exception
        If there is an error during CSV file generation or saving.
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
