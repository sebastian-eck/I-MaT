import sys

from matplotlib import pyplot as plt
from music21 import environment

from i_mat.src.cli.cli_general_display import text_export_fileName, text_general_exportGraph, \
    text_general_exportSuccessful, text_general_proceed
from i_mat.src.cli.cli_menu_entries import module_navigation_entries
from i_mat.src.cli.cli_results_export import show_resultslist
from i_mat.src.cli.cli_structure_general import open_submenu_data_withExplanationsColumn
from i_mat.src.utils.utils_error_handling import text_exception_general
from i_mat.src.utils.utils_without_userInput import utility_clear_screen, utility_export_as_csv


def menu_structures_predefined_visualizations(
        function_name, menu_header, data_values, graph_processed, notes
):
    try:
        utility_clear_screen()

        show_resultslist(menu_header, data_values)
        print("")

        if notes != "":
            print(notes)
            print("")

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(module_navigation_entries())

            if user_selection == "repeatSelection":
                function_name()

                break

            elif user_selection == "export_CSV":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                        str(score_export_path) + "\\" + str(filename) + ".csv"
                )

                utility_export_as_csv(
                    data=data_values, columns=menu_header, save_at=path_and_filename, do_print=False
                )

                print(text_general_exportSuccessful(score_export_path, filename, ".csv"))
                print("")

                input(text_general_proceed())
                print("")

            elif user_selection == "export_visualization":
                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                print(text_general_exportGraph(score_export_path))
                print()

                graph_processed.doneAction = None
                graph_processed.run()

                plt.show()

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")
