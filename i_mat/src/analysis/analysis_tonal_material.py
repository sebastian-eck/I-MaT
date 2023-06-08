import sys

import i_mat.config as config
from i_mat.src.cli.cli_general_display import text_general_proceed
from i_mat.src.cli.cli_results_export import menuStructure_musicalParameters_withoutGraphicsExport, text_headers_entries
from i_mat.src.cli.cli_score_selection import select_score_completeOrIndividualVoice
from i_mat.src.cli.cli_text_output import text_analysis_measures
from i_mat.src.utils.utils_error_handling import text_exception_general
from i_mat.src.utils.utils_without_userInput import utility_clear_screen, utility_getKeyToValue


def notes_quantity_total_textOutput():
    utility_clear_screen()

    try:
        temporary_selectedScore = select_score_completeOrIndividualVoice()

        selectedScore_stripTies = temporary_selectedScore.stripTies()

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

        # --- Unterhalb: Code des Tools ---

        notes_amount = len(
            selectedScore_stripTies.flat.getElementsByClass("Note"))

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = [[score_label, notes_amount]]

        menuStructure_musicalParameters_withoutGraphicsExport(
            notes_quantity_total_textOutput, menu_header, data_values, explanations=""
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")
