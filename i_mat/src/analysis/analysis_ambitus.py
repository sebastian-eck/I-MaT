import sys

from music21 import analysis

import i_mat.config as config
from i_mat.src.cli.cli_general_display import text_general_proceed
from i_mat.src.cli.cli_results_export import menuStructure_musicalParameters_withoutGraphicsExport, text_headers_entries
from i_mat.src.cli.cli_score_selection import select_score_completeOrIndividualVoice
from i_mat.src.cli.cli_text_output import text_analysis_measures, text_analysis_scoreSelection
from i_mat.src.utils.utils_error_handling import text_exception_general
from i_mat.src.utils.utils_without_userInput import utility_clear_screen, utility_getKeyToValue


def range_analysis(temporary_selectedScore):
    try:
        selectedScore_stripTies = temporary_selectedScore.stripTies()

        rangeAnalyzer = analysis.discrete.Ambitus()

        range = rangeAnalyzer.getSolution(selectedScore_stripTies).name

        return range

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def range_analysis_textOutput():
    utility_clear_screen()

    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        # --- Unterhalb: Code des Tools ---

        range = range_analysis(temporary_selectedScore)

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

        data_values = [[score_label, range]]

        menuStructure_musicalParameters_withoutGraphicsExport(
            range_analysis_textOutput, menu_header, data_values, explanations=""
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def range_comparison_textOutput():
    utility_clear_screen()

    try:
        print(text_analysis_scoreSelection()[0])
        print("")

        input(text_general_proceed())
        print("")

        selectedScore1 = select_score_completeOrIndividualVoice()

        selectedScore1_name = config.global_selectedScore

        input_bars_start_selectedScore1 = config.global_input_firstMeasure

        input_bars_end_selectedScore1 = config.global_input_lastMeasure

        print(text_analysis_scoreSelection()[1])
        print("")

        input(text_general_proceed())
        print("")

        selectedScore2 = select_score_completeOrIndividualVoice()

        selectedScore2_name = config.global_selectedScore

        input_bars_start_selectedScore2 = config.global_input_firstMeasure

        input_bars_end_selectedScore2 = config.global_input_lastMeasure

        range_Noten1 = range_analysis(selectedScore1)

        range_Noten2 = range_analysis(selectedScore2)

        score_label1 = (
                utility_getKeyToValue(
                    selectedScore1_name, config.global_catalogue_completeScoreWithIndividualParts
                )
                + ", "
                + text_analysis_measures()
                + str(input_bars_start_selectedScore1)
                + "-"
                + str(input_bars_end_selectedScore1)
        )

        score_label2 = (
                utility_getKeyToValue(
                    selectedScore2_name, config.global_catalogue_completeScoreWithIndividualParts
                )
                + ", "
                + text_analysis_measures()
                + str(input_bars_start_selectedScore2)
                + "-"
                + str(input_bars_end_selectedScore2)
        )

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = [[score_label1, range_Noten1], [score_label2, range_Noten2]]

        menuStructure_musicalParameters_withoutGraphicsExport(
            range_comparison_textOutput, menu_header, data_values, explanations=""
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")
