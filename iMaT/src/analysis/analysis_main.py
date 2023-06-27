from src.analysis.analysis_utils import display_user_options_post_analysis, export_results_to_csv_auto
from src.cli.cli_menu_structures import display_menu_print_results, util_convert_pd_dataframe_to_imat_datacont
from src.score_selection.score_selection_name_parts import selected_score_part_names
from src.score_selection.score_selection_main import score_selection
from src.score_selection.score_selection_select_parts_and_measures import select_parts_and_measures
from src.utils.utils_error_handling import handle_error
from src.visualizations.visualizations_analysis_results import map_analysis_function_to_display_function


def analysis_workflow_single_piece(analysis_func: callable):
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
                analysis_workflow_single_piece(analysis_func)
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

    except Exception as e:
        handle_error(e)
