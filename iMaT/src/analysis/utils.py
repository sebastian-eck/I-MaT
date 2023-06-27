from src.cli.menu_constructors import display_menu_request_selection
from src.utils.error_handling import handle_error


def display_user_options_post_analysis():
    """
    Presents the user with post-analysis options ("repeat", "export", "display_results", or "back") and gets their selection.
    Returns the user's selection as a string. Use the display_menu_request_selection() to display the possible options.
    """
    try:
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

    except Exception as e:
        handle_error(e)
