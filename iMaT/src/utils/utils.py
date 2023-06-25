from src.cli.cli_menu_structure import display_menu_print_results
from src.routines.routines_name_parts import select_and_name_parts, selected_score_part_names
from src.routines.routines_score_selection import score_selection


def select_new_score(selected_score, identifier):
    """
    Allows the user to select a new score.
    """
    score_selection()


def show_metadata():
    """
    Displays the metadata of the selected score.
    """
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


def show_part_names():
    """
    Displays the names of the individual parts/voices in the selected score.
    """
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


def change_part_names():
    """
    Allows the user to rename the individual parts/voices in the selected score.
    """
    selected_score = selected_score_part_names.get('Full Score', None)

    if selected_score is None:

        print("\nNo score has yet been selected. Please select a new score first.\n")
        input("<To continue, please press Enter>")

        return

    else:

        select_and_name_parts(selected_score)