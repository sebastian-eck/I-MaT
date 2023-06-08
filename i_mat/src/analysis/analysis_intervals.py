import sys
from typing import List

from matplotlib import pyplot as plt
from music21 import analysis, environment

import i_mat.config as config
from i_mat.src.cli.cli_general_display import text_export_fileName, text_general_exportGraph, \
    text_general_exportSuccessful, text_general_proceed
from i_mat.src.cli.cli_menu_entries import module_navigation_entries
from i_mat.src.cli.cli_results_export import menuStructure_musicalParameters_withoutGraphicsExport, show_resultslist, \
    text_headers_entries
from i_mat.src.cli.cli_score_selection import select_score_completeOrIndividualVoice
from i_mat.src.cli.cli_structure_general import open_submenu_data_withExplanationsColumn
from i_mat.src.cli.cli_text_output import text_analysis_measures, text_analysis_notes_intervals, \
    text_analysis_scoreSelection
from i_mat.src.utils.utils_error_handling import text_exception_general
from i_mat.src.utils.utils_without_userInput import utility_clear_screen, utility_count, utility_export_as_csv, \
    utility_getKeyToValue


def intervalStructure_intervalTypes_quantity(temporary_selectedScore):
    try:
        selectedScore_stripTies = temporary_selectedScore.stripTies()

        intervalAnalyzer = analysis.discrete.MelodicIntervalDiversity()

        intervals_typesAndQuantity = intervalAnalyzer.countMelodicIntervals(
            selectedScore_stripTies,
            found=None,
            ignoreDirection=False,
            ignoreUnison=False,
        )

        intervalTypes_quantity = len(intervals_typesAndQuantity)

        # gibt die Anzahl der vorhandenen Intervalltypen als Integer zurück

        return intervalTypes_quantity

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def intervalStructure_intervalTypes_UniqueIntervals(temporary_selectedScore):
    try:
        selectedScore_stripTies = temporary_selectedScore.stripTies()

        intervalAnalyzer = analysis.discrete.MelodicIntervalDiversity()

        intervals_typesAndQuantity = intervalAnalyzer.countMelodicIntervals(
            selectedScore_stripTies,
            found=None,
            ignoreDirection=False,
            ignoreUnison=False,
        )

        intervals_types: list[str] = list(intervals_typesAndQuantity.keys())

        # gibt die Anzahl der vorhandenen Intervalltypen als Integer zurück

        return intervals_types

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def intervalStructure_intervalTypes_textOutput():
    utility_clear_screen()

    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        # --- Unterhalb: Code des Tools ---

        intervalTypes_quantity = intervalStructure_intervalTypes_quantity(
            temporary_selectedScore)

        intervals_types = str(
            intervalStructure_intervalTypes_UniqueIntervals(temporary_selectedScore)
        )

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

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = [[score_label, intervalTypes_quantity, intervals_types]]

        menuStructure_musicalParameters_withoutGraphicsExport(
            intervalStructure_intervalTypes_textOutput,
            menu_header,
            data_values,
            explanations=text_analysis_notes_intervals(),
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def intervalStructure_intervalTypes_quantity_textOutput():
    utility_clear_screen()

    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = temporary_selectedScore.stripTies()

        # --- Unterhalb: Code des Tools ---

        intList = analysis.segmentByRests.Segmenter.getIntervalList(
            selectedScore_stripTies
        )

        intervals = utility_count([x.directedName for x in intList])

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

        intervals_list = []

        for x, y in intervals.items():
            intervals_list.append([score_label, x, y])

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = intervals_list

        utility_clear_screen()

        show_resultslist(menu_header, data_values)
        print("")

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(module_navigation_entries())

            if user_selection == "repeatSelection":
                intervalStructure_intervalTypes_quantity_textOutput()

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

                names = []
                values = []

                for datensatz in data_values:
                    names.append(datensatz[1])
                    values.append(datensatz[2])

                plt.bar(names, values)
                plt.ylabel("Frequency")
                plt.xlabel("Interval types")
                plt.title("Interval types and corresponding frequency")

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


def intervalStructure_intervalTypes_comparison_textOutput():
    utility_clear_screen()

    try:
        print(text_analysis_scoreSelection()[0])
        print("")

        input(text_general_proceed())
        print("")

        selectedScore1 = select_score_completeOrIndividualVoice()

        selectedScore1_stripTies = selectedScore1.stripTies()

        selectedScore1_name = config.global_selectedScore

        input_bars_start_selectedScore1 = config.global_input_firstMeasure

        input_bars_end_selectedScore1 = config.global_input_lastMeasure

        print(text_analysis_scoreSelection()[1])
        print("")

        input(text_general_proceed())
        print("")

        selectedScore2 = select_score_completeOrIndividualVoice()

        selectedScore2_stripTies = selectedScore2.stripTies()

        selectedScore2_name = config.global_selectedScore

        input_bars_start_selectedScore2 = config.global_input_firstMeasure

        input_bars_end_selectedScore2 = config.global_input_lastMeasure

        allIntervals_list_selectedScore1 = (
            analysis.segmentByRests.Segmenter.getIntervalList(
                selectedScore1_stripTies)
        )

        a = utility_count([x.directedName for x in allIntervals_list_selectedScore1])

        allIntervals_list_selectedScore2 = (
            analysis.segmentByRests.Segmenter.getIntervalList(
                selectedScore2_stripTies)
        )

        b = utility_count([x.directedName for x in allIntervals_list_selectedScore2])

        selectedScore1_name = utility_getKeyToValue(
            selectedScore1_name, config.global_catalogue_completeScoreWithIndividualParts
        )

        score_label1 = (
                selectedScore1_name
                + ", "
                + text_analysis_measures()
                + str(input_bars_start_selectedScore1)
                + "-"
                + str(input_bars_end_selectedScore1)
        )

        selectedScore2_name = utility_getKeyToValue(
            selectedScore2_name, config.global_catalogue_completeScoreWithIndividualParts
        )

        score_label2 = (
                selectedScore2_name
                + ", "
                + text_analysis_measures()
                + str(input_bars_start_selectedScore2)
                + "-"
                + str(input_bars_end_selectedScore2)
        )

        intervals_comparison_list = []

        for i in a.keys():
            if i in b.keys():
                difference = a[i] - b[i]

                if difference < 0:
                    intervals_comparison_list.append(
                        [score_label1, i, a[i], str(difference)]
                    )

                else:
                    intervals_comparison_list.append(
                        [score_label1, i, a[i], str(difference)]
                    )

            else:
                intervals_comparison_list.append([score_label1, i, a[i], a[i]])

        for i in b.keys():
            if i in a.keys():
                difference = b[i] - a[i]

                if difference < 0:
                    intervals_comparison_list.append(
                        [score_label2, i, b[i], str(difference)]
                    )

                else:
                    intervals_comparison_list.append(
                        [score_label2, i, b[i], str(difference)]
                    )

            else:
                intervals_comparison_list.append([score_label2, i, b[i], b[i]])

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = intervals_comparison_list

        utility_clear_screen()

        show_resultslist(menu_header, data_values)
        print("")

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(module_navigation_entries())

            if user_selection == "repeatSelection":
                intervalStructure_intervalTypes_comparison_textOutput()

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

                interval_1 = []
                frequency_1 = []
                difference_1 = []

                interval_2 = []
                frequency_2 = []
                difference_2 = []

                for dataset in data_values:
                    if dataset[0] == score_label1:
                        interval_1.append(dataset[1])
                        frequency_1.append(int(dataset[2]))
                        difference_1.append(int(dataset[3]))

                for dataset in data_values:
                    if dataset[0] == score_label2:
                        interval_2.append(dataset[1])
                        frequency_2.append(int(dataset[2]))
                        difference_2.append(int(dataset[3]))

                fig, axs1 = plt.subplots(2, 1)
                axs1[0].bar(interval_1, frequency_1)
                axs1[0].set_title(score_label1)
                axs1[0].set(xlabel="Interval types", ylabel="Frequency")

                axs1[1].bar(interval_1, difference_1)
                axs1[1].set(
                    xlabel="Interval types", ylabel="Difference to other note selection"
                )

                fig.tight_layout()

                plt.show()

                fig, axs2 = plt.subplots(2, 1)

                axs2[0].set_title(score_label2)
                axs2[0].bar(interval_2, frequency_2)
                axs2[0].set(xlabel="Interval types", ylabel="Frequency")

                axs2[1].bar(interval_2, difference_2)
                axs2[1].set(
                    xlabel="Interval types", ylabel="Difference to other note selection"
                )

                fig.tight_layout()

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


def intervalStructure_Intervalle_quantity_textOutput():
    utility_clear_screen()

    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = temporary_selectedScore.stripTies()

        # --- Unterhalb: Code des Tools ---

        intList = analysis.segmentByRests.Segmenter.getIntervalList(
            selectedScore_stripTies
        )

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

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = [[score_label, len(intList)]]

        menuStructure_musicalParameters_withoutGraphicsExport(
            intervalStructure_Intervalle_quantity_textOutput,
            menu_header,
            data_values,
            explanations=text_analysis_notes_intervals(),
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")
