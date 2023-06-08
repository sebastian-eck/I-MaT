import sys

from matplotlib import pyplot as plt
from music21 import duration, environment, graph, pitch

import i_mat.config as config
from i_mat.src.cli.cli_general_display import text_export_fileName, text_general_exportGraph, \
    text_general_exportSuccessful, text_general_proceed
from i_mat.src.cli.cli_menu_entries import module_navigation_entries
from i_mat.src.cli.cli_results_export import text_headers_entries
from i_mat.src.cli.cli_score_selection import select_score_completeOrIndividualVoice
from i_mat.src.cli.cli_structure_general import open_submenu_data_withExplanationsColumn
from i_mat.src.cli.cli_text_output import text_analysis_measures, text_analysis_notes_predefinedVisualizations_Dolan
from i_mat.src.cli.cli_visualizations import menu_structures_predefined_visualizations
from i_mat.src.utils.utils_error_handling import text_exception_general
from i_mat.src.utils.utils_with_userInput import menu_askUser_repeatPreviousTool
from i_mat.src.utils.utils_without_userInput import utility_clear_screen, utility_export_as_csv, utility_getKeyToValue


def predefinedVisualizations_HistogramPitchSpace():
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

        selectedGraph = graph.plot.HistogramPitchSpace

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        values_list = []

        for item in graph_processed.data:
            values_list.append(
                [score_label, item[0], pitch.Pitch(
                    item[0]).nameWithOctave, item[1]]
            )

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = values_list

        menu_structures_predefined_visualizations(
            predefinedVisualizations_HistogramPitchSpace,
            menu_header,
            data_values,
            graph_processed,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def predefinedVisualizations_HistogramPitchClass():
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

        selectedGraph = graph.plot.HistogramPitchClass

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        values_list = []

        for item in graph_processed.data:
            values_list.append(
                [score_label, item[0], pitch.Pitch(
                    item[0]).nameWithOctave, item[1]]
            )

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = values_list

        menu_structures_predefined_visualizations(
            predefinedVisualizations_HistogramPitchClass,
            menu_header,
            data_values,
            graph_processed,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def predefinedVisualizations_HistogramQuarterLength():
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

        selectedGraph = graph.plot.HistogramQuarterLength

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        values_list = []

        for item in graph_processed.data:
            values_list.append(
                [
                    score_label,
                    item[0],
                    duration.Duration(quarterLength=float(item[0])).fullName,
                    item[1],
                ]
            )

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = values_list

        menu_structures_predefined_visualizations(
            predefinedVisualizations_HistogramQuarterLength,
            menu_header,
            data_values,
            graph_processed,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def predefinedVisualizations_HorizontalBarPitchSpaceOffset():
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

        selectedGraph = graph.plot.HorizontalBarPitchSpaceOffset

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        onsets_list = []

        for x in graph_processed.data:
            x[0] = x[0].replace("♭", "-").replace("♯", "#")

            octave = ""

            if any(chr.isdigit() for chr in str(x[0])):
                for c in x[0]:
                    if c.isdigit():
                        number = c

            if not any(chr.isdigit() for chr in str(x[0])):
                octave = number

            if len(x) != 0:
                for y in x:
                    if type(y) == list and len(y) != 0:
                        for z in y:
                            if type(z) == tuple:
                                if "B#/D--/C" in x[0] or "B##/D-/C#" in x[0]:
                                    x[0] = x[0].replace("/D", octave + "/D")

                                    x[0] = x[0].replace(
                                        "/C", str(int(octave) + 1) + "/C"
                                    )

                                    x[0] = x[0] + str(int(octave) + 1)

                                    n = x[0].rfind("/")

                                    onsets_list.append(
                                        [
                                            score_label,
                                            pitch.Pitch(
                                                str(x[0][n + 1:])).midi,
                                            x[0],
                                            z[0],
                                            z[1],
                                        ]
                                    )

                                elif "B#/C/D--" in x[0] or "B##/C#/D-" in x[0]:
                                    x[0] = x[0].replace("/C", octave + "/C")

                                    x[0] = x[0].replace(
                                        "/D", str(int(octave) + 1) + "/D"
                                    )

                                    x[0] = x[0] + str(int(octave) + 1)

                                    n = x[0].rfind("/")

                                    onsets_list.append(
                                        [
                                            score_label,
                                            pitch.Pitch(
                                                str(x[0][n + 1:])).midi,
                                            x[0],
                                            z[0],
                                            z[1],
                                        ]
                                    )

                                elif "B#/D--" in x[0] or "B##/D-" in x[0]:
                                    x[0] = x[0].replace("/", octave + "/")

                                    x[0] = x[0] + str(int(octave) + 1)

                                    n = x[0].rfind("/")

                                    onsets_list.append(
                                        [
                                            score_label,
                                            pitch.Pitch(
                                                str(x[0][n + 1:])).midi,
                                            x[0],
                                            z[0],
                                            z[1],
                                        ]
                                    )

                                elif (
                                    "B-/C--" in x[0]
                                    or "B/C-" in x[0]
                                    or "B#/C" in x[0]
                                    or "B##/C#" in x[0]
                                ):
                                    x[0] = x[0].replace("/", octave + "/")

                                    x[0] = x[0] + str(int(octave) + 1)

                                    n = x[0].rfind("/")

                                    onsets_list.append(
                                        [
                                            score_label,
                                            pitch.Pitch(
                                                str(x[0][n + 1:])).midi,
                                            x[0],
                                            z[0],
                                            z[1],
                                        ]
                                    )

                                else:
                                    if any(chr.isdigit() for chr in str(x[0])):
                                        if "/" in x[0]:
                                            n = x[0].rfind("/")

                                            onsets_list.append(
                                                [
                                                    score_label,
                                                    pitch.Pitch(
                                                        str(x[0][n + 1:])
                                                    ).midi,
                                                    x[0],
                                                    z[0],
                                                    z[1],
                                                ]
                                            )

                                        else:
                                            onsets_list.append(
                                                [
                                                    score_label,
                                                    pitch.Pitch(
                                                        str(x[0])).midi,
                                                    x[0],
                                                    z[0],
                                                    z[1],
                                                ]
                                            )

                                    else:
                                        if "/" in x[0]:
                                            x[0] = x[0].replace(
                                                "/", octave + "/")

                                            x[0] = x[0] + str(octave)

                                            n = x[0].rfind("/")

                                            onsets_list.append(
                                                [
                                                    score_label,
                                                    pitch.Pitch(
                                                        str(x[0][n + 1:])
                                                    ).midi,
                                                    x[0],
                                                    z[0],
                                                    z[1],
                                                ]
                                            )

                                        else:
                                            x[0] = x[0] + str(octave)

                                            onsets_list.append(
                                                [
                                                    score_label,
                                                    pitch.Pitch(
                                                        str(x[0])).midi,
                                                    x[0],
                                                    z[0],
                                                    z[1],
                                                ]
                                            )

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = onsets_list

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(module_navigation_entries())

            if user_selection == "repeatSelection":
                predefinedVisualizations_HorizontalBarPitchSpaceOffset()

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


def predefinedVisualizations_ScatterWeightedPitchSpaceQuarterLength():
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

        selectedGraph = graph.plot.ScatterWeightedPitchSpaceQuarterLength

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        ax = graph.axis.QuarterLengthAxis(graph_processed)

        toneDurations_dict = {}

        for item in ax.ticks():
            toneDurations_dict.update({item[0]: item[1]})

        values_list = []

        for item in graph_processed.data:
            values_list.append(
                [
                    score_label,
                    toneDurations_dict[item[0]],
                    duration.Duration(
                        quarterLength=float(toneDurations_dict[item[0]])
                    ).fullName,
                    item[1],
                    pitch.Pitch(item[1]).nameWithOctave,
                    item[2],
                ]
            )

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = values_list

        menu_structures_predefined_visualizations(
            predefinedVisualizations_ScatterWeightedPitchSpaceQuarterLength,
            menu_header,
            data_values,
            graph_processed,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def predefinedVisualizations_Plot3DBarsPitchSpaceQuarterLength():
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

        selectedGraph = graph.plot.Plot3DBarsPitchSpaceQuarterLength

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        ax = graph.axis.QuarterLengthAxis(graph_processed)

        toneDurations_dict = {}

        for item in ax.ticks():
            toneDurations_dict.update({item[0]: item[1]})

        values_list = []

        for item in graph_processed.data:
            values_list.append(
                [
                    score_label,
                    toneDurations_dict[item[0]],
                    duration.Duration(
                        quarterLength=float(toneDurations_dict[item[0]])
                    ).fullName,
                    item[1],
                    pitch.Pitch(item[1]).nameWithOctave,
                    item[2],
                ]
            )

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = values_list

        menu_structures_predefined_visualizations(
            predefinedVisualizations_Plot3DBarsPitchSpaceQuarterLength,
            menu_header,
            data_values,
            graph_processed,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def predefinedVisualizations_ScatterWeightedPitchClassQuarterLength():
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

        selectedGraph = graph.plot.ScatterWeightedPitchClassQuarterLength

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        ax = graph.axis.QuarterLengthAxis(graph_processed)

        toneDurations_dict = {}

        for item in ax.ticks():
            toneDurations_dict.update({item[0]: item[1]})

        values_list = []

        for item in graph_processed.data:
            values_list.append(
                [
                    score_label,
                    toneDurations_dict[item[0]],
                    duration.Duration(
                        quarterLength=float(toneDurations_dict[item[0]])
                    ).fullName,
                    item[1],
                    pitch.Pitch(item[1]).nameWithOctave,
                    item[2],
                ]
            )

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = values_list

        menu_structures_predefined_visualizations(
            predefinedVisualizations_ScatterWeightedPitchClassQuarterLength,
            menu_header,
            data_values,
            graph_processed,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def predefinedVisualizations_ScatterPitchClassOffset():
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

        selectedGraph = graph.plot.ScatterPitchClassOffset

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        values_list = []

        for item in graph_processed.data:
            values_list.append(
                [score_label, item[1], pitch.Pitch(
                    item[1]).nameWithOctave, item[0]]
            )

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = values_list

        menu_structures_predefined_visualizations(
            predefinedVisualizations_ScatterPitchClassOffset,
            menu_header,
            data_values,
            graph_processed,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def predefinedVisualizations_ScatterWeightedPitchSpaceDynamicSymbol():
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

        selectedGraph = graph.plot.ScatterWeightedPitchSpaceDynamicSymbol

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        ax = graph.axis.DynamicsAxis(graph_processed)

        Verzeichnis_Dynamiken = {}

        for item in ax.ticks():
            Verzeichnis_Dynamiken.update({item[0]: item[1].replace("$", "")})

        values_list = []

        for item in graph_processed.data:
            values_list.append(
                [
                    score_label,
                    item[0],
                    pitch.Pitch(item[0]).nameWithOctave,
                    Verzeichnis_Dynamiken[item[1]],
                    item[2],
                ]
            )

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = values_list

        menu_structures_predefined_visualizations(
            predefinedVisualizations_ScatterWeightedPitchSpaceDynamicSymbol,
            menu_header,
            data_values,
            graph_processed,
            notes="",
        )

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def predefinedVisualizations_HorizontalBarPitchClassOffset():
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

        selectedGraph = graph.plot.HorizontalBarPitchClassOffset

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.extractData()

        onsets_list = []

        for x in graph_processed.data:
            x[0] = x[0].replace("♭", "-").replace("♯", "#")

            if len(x) != 0:
                for y in x:
                    if type(y) == list and len(y) != 0:
                        for z in y:
                            if type(z) == tuple:
                                if "/" in x[0]:
                                    n = x[0].rfind("/")

                                    onsets_list.append(
                                        [
                                            score_label,
                                            pitch.Pitch(
                                                str(x[0][n + 1:])).pitchClass,
                                            str(x[0]),
                                            z[0],
                                            z[1],
                                        ]
                                    )

                                else:
                                    onsets_list.append(
                                        [
                                            score_label,
                                            pitch.Pitch(str(x[0])).pitchClass,
                                            str(x[0]),
                                            z[0],
                                            z[1],
                                        ]
                                    )

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = onsets_list

        while True:
            user_selection = open_submenu_data_withExplanationsColumn(module_navigation_entries())

            if user_selection == "repeatSelection":
                predefinedVisualizations_HorizontalBarPitchClassOffset()

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


def predefinedVisualizations_Dolan():
    utility_clear_screen()

    # --- Unterhalb: Code des Tools ---

    temporary_selectedScore = select_score_completeOrIndividualVoice()

    selectedScore_stripTies = temporary_selectedScore.stripTies()

    print(text_analysis_notes_predefinedVisualizations_Dolan())
    print("")

    try:
        selectedGraph = graph.plot.Dolan

        graph_processed = selectedGraph(selectedScore_stripTies)

        graph_processed.doneAction = None
        graph_processed.run()

        plt.show()

        print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    input(text_general_proceed())
    print("")

    # --- Oberhalb: Code des Tools ---

    menu_askUser_repeatPreviousTool(predefinedVisualizations_Dolan)
