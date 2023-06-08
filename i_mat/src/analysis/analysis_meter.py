import os
import sys

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from music21 import environment

import i_mat.config as config
from i_mat.src.cli.cli_general_display import text_export_fileName, text_general_exportGraph, \
    text_general_exportSuccessful, text_general_proceed
from i_mat.src.cli.cli_menu_entries import module_navigation_entries
from i_mat.src.cli.cli_results_export import show_resultslist, text_headers_entries
from i_mat.src.cli.cli_score_selection import select_score_completeOrIndividualVoice
from i_mat.src.cli.cli_structure_general import open_submenu_data_withExplanationsColumn
from i_mat.src.cli.cli_text_output import text_analysis_measures
from i_mat.src.utils.utils_error_handling import text_exception_general
from i_mat.src.utils.utils_without_userInput import utility_clear_screen, utility_export_as_csv, utility_getKeyToValue


def meter_metricWeight_textOutput():
    utility_clear_screen()

    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = temporary_selectedScore.stripTies()

        # --- Unterhalb: Code des Tools ---

        selectedScore_name = str(
            utility_getKeyToValue(config.global_selectedScore, config.global_catalogue_completeScoreWithIndividualParts)
        )

        score_label = (
                selectedScore_name
                + ", "
                + text_analysis_measures()
                + str(config.global_input_firstMeasure)
                + "-"
                + str(config.global_input_lastMeasure)
        )

        n_list, n_beat_strength = [], []

        l_bs = []

        for n in selectedScore_stripTies.flat.notes:
            c_n = str(n)

            n_list.append(c_n.replace(
                "<music21.note.Note ", "").replace(">", ""))

            n_beat_strength.append(float(n.beatStrength))

        pd_bs = pd.DataFrame(
            np.array([n_list, n_beat_strength]).T, columns=[
                "Notes", "Beat_Strength"]
        )

        n_uni = pd_bs["Notes"].unique()

        bs_uni = pd_bs["Beat_Strength"].unique()

        bs_int_indi = []

        for c_bs_uni in bs_uni:
            l = len(pd_bs.loc[(pd_bs["Beat_Strength"] == c_bs_uni)])

            bs_int_indi.append([score_label, c_bs_uni, l])

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = bs_int_indi

        show_resultslist(menu_header, data_values)

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(module_navigation_entries())

            if user_selection == "repeatSelection":
                meter_metricWeight_textOutput()

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
                    data=data_values,
                    columns=menu_header,
                    save_at=path_and_filename,
                    do_print=False,
                    do_return_pd=True,
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

                path_and_filename = str(score_export_path) + \
                                    "\\" + "Temp" + ".csv"

                pd_bs_indi_data = utility_export_as_csv(
                    data=data_values,
                    columns=menu_header,
                    save_at=path_and_filename,
                    do_print=False,
                    do_return_pd=True,
                )

                np_bs_indi_data = pd_bs_indi_data.to_numpy()
                fig2 = plt.figure()
                ax2 = fig2.add_subplot(111)
                ax2.bar(
                    np_bs_indi_data[:, 1],
                    np_bs_indi_data[:, 2],
                    width=0.5,
                    color="darkslateblue",
                    alpha=0.8,
                )
                ax2.set_title("Metric weight")
                ax2.set_xlabel("Metric position")
                ax2.set_ylabel("Frequency")

                plt.show()

                os.remove(path_and_filename)

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")
