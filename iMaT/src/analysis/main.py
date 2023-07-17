"""
Module: analysis.main.py
========================

This module includes the main function for handling the workflow for analyzing a single musical piece within the Interactive Music Analysis Tool (I-MaT) tool.

This module includes the function `analysis_workflow_single_musical_piece`, which is a key function to handle
the workflow for analyzing a single musical piece in the Interactive Music Analysis Tool (I-MaT) tool.

It guides through the entire process of selecting a score, performing the analysis using a user-provided function,
displaying the results, and handling post-analysis user options.

An important part of this process involves making use of several helper functions from different modules such as
`score_selection`, `select_parts_and_measures`, `handle_error`, and more.

For a detailed workflow, refer to the docstring of `analysis_workflow_single_musical_piece` function.

This module is intended to be imported and used by the main entry point of the I-MaT system.

Functions
---------
- `analysis_workflow_single_musical_piece`: Manages the complete process of selecting a score, performing analysis using a user-specified function, displaying the results, and handling post-analysis user options.

The module utilizes several helper functions from different modules such as `score_selection`, `select_parts_and_measures`, `handle_error`, and more.
"""
from iMaT.src.analysis.utils import display_user_options_post_analysis
from iMaT.src.cli.menu_constructors import display_menu_print_results, util_convert_pd_dataframe_to_imat_datacont
from iMaT.src.score_selection.main import score_selection
from iMaT.src.score_selection.name_parts import selected_score_part_names
from iMaT.src.score_selection.select_parts_and_measures import select_parts_and_measures
from iMaT.src.utils.error_handling import handle_error
from iMaT.src.utils.misc import export_results_to_csv_auto
from iMaT.src.visualizations.analysis_results_graphs import map_analysis_functions_to_display_functions


def analysis_workflow_single_musical_piece(analysis_func: callable):
    """
    Handles the workflow for analyzing a single musical piece.

    This function manages the entire process of selecting a score,
    performing the analysis using the provided function, displaying the results,
    and handling post-analysis user options.

    Parameters
    ----------
    analysis_func : callable
        The function to use for performing the analysis.
        This function should accept two parameters:
        a music score object and a string identifier.

    Returns
    -------
    None

    Raises
    ------
    Exception
        Handles any exceptions that arise during the analysis workflow by passing them to handle_error(e).

    See Also
    --------
    display_user_options_post_analysis : function
        Presents the user with post-analysis options.
    select_parts_and_measures : function
        Selects parts and measures for the musical score.

    Examples
    --------
    >>> def my_analysis_func(score, identifier):
    ...     # Implement analysis logic here
    ...     pass
    ...
    >>> analysis_workflow_single_musical_piece(my_analysis_func)

    Notes
    -----
    If the score has not yet been selected, the score selection workflow is started.
    """
    try:
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
            option = display_user_options_post_analysis()

            # e. Depending on the user's choice ("repeat", "export", "display_results", or "back")
            if option == "repeat":
                analysis_workflow_single_musical_piece(analysis_func)
                break
            elif option == "export":
                export_results_to_csv_auto(analysis_results, identifier, analysis_func.__name__)
            elif option == "display_results":
                # Get the function to display the results from the mapping:
                display_results_func = map_analysis_functions_to_display_functions(analysis_func)

                if display_results_func is not None:
                    display_results_func(analysis_results, identifier)

            else:
                break

    except Exception as e:
        handle_error(e)
