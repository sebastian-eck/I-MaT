import sys
from copy import deepcopy

from music21 import environment, note, search, stream

import i_mat.config as config
from i_mat.src.cli.cli_general_display import text_display_showScoreSelection, text_export_fileName, \
    text_general_checkEntry, text_general_close_museScore3, text_general_exportSuccessful, \
    text_general_input_RestrictedToYesAndNo, text_general_input_restrictedToNumbers, text_general_proceed
from i_mat.src.cli.cli_patternsearch import module_navigation_patternSearch, open_submenu_patternSearch, \
    text_patternSearch_deleteSelection, text_patternSearch_enter_customRhythm, text_patternSearch_includeRests, \
    text_patternSearch_patternsFound, text_patternSearch_showPatternSelection
from i_mat.src.cli.cli_results_export import show_resultslist, text_headers_entries
from i_mat.src.cli.cli_structure_general import open_submenu_data_withExplanationsColumn
from i_mat.src.utils.utils_error_handling import text_exception_general
from i_mat.src.utils.utils_without_userInput import utility_clear_screen, utility_export_as_csv, utility_listToString, \
    utility_userInput_isAffirmative, utility_userInput_isNegative, utility_userInput_isNumber


def patternSearch_menuStructure_toneSequence_withoutTransposition_withoutRhythm():
    try:
        score_deepCopy = deepcopy(config.global_score.stripTies(inPlace=True))

        streamMot = patternSearch_enterSearchPattern_withoutRhythm()

        while True:
            utility_clear_screen()

            user_input = input(text_patternSearch_includeRests())
            print("")

            if utility_userInput_isAffirmative(user_input):
                full_piece_stream = score_deepCopy.recurse().notes

                break

            elif utility_userInput_isNegative(user_input):
                full_piece_stream = score_deepCopy.recurse().notesAndRests

                break

            else:
                print(text_general_input_RestrictedToYesAndNo())
                print("")

                input(text_general_proceed())
                print("")

        p_full_piece = search.noteNameSearch(full_piece_stream, streamMot)

        print(text_patternSearch_patternsFound(len(p_full_piece)))
        print("")

        input(text_general_proceed())
        print("")

        searchPattern_list = []

        counter = 1

        for position in p_full_piece:
            startingNote = full_piece_stream[position]
            startingMeasure = startingNote.measureNumber
            startingBeat = startingNote.beat
            startingPart = startingNote.getContextByClass("Part")

            searchPattern_list.append(
                [
                    counter,
                    startingNote,
                    startingMeasure,
                    startingBeat,
                    startingPart.id,
                    utility_listToString(config.global_searchPattern),
                ]
            )

            counter += 1

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = searchPattern_list

        show_resultslist(menu_header, data_values)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")

    while True:
        try:
            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_patternSearch())

            if user_selection == "repeatSelection":
                patternSearch_menuStructure_toneSequence_withoutTransposition_withoutRhythm()

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
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "Export_Notentext":
                for found in p_full_piece:
                    for ffound in range(len(streamMot)):
                        full_piece_stream[found + ffound].lyric = "*"
                        full_piece_stream[found + ffound].style.color = "red"

                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                        str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = score_deepCopy.write("xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print("")

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            input(text_general_proceed())
            print("")


def patternSearch_menuStructure_toneSequence_withTransposition_withoutRhythm():
    try:
        score_deepCopy = deepcopy(config.global_score.stripTies(inPlace=True))

        streamMot = patternSearch_enterSearchPattern_withoutRhythm()

        while True:
            utility_clear_screen()

            user_input = input(text_patternSearch_includeRests())
            print("")

            if utility_userInput_isAffirmative(user_input):
                s = score_deepCopy.recurse().notes

                break

            elif utility_userInput_isNegative(user_input):
                s = score_deepCopy.recurse().notesAndRests

                break

            else:
                print(text_general_input_RestrictedToYesAndNo())
                print("")

                input(text_general_proceed())
                print("")

        def pitchClassEqual(n1, n2):
            if not hasattr(n1, "pitch"):
                return False
            if not hasattr(n2, "pitch"):
                return False
            if n1.pitch.pitchClass == n2.pitch.pitchClass:
                return True
            else:
                return False

        results = []
        counter = 1
        iteration = 1

        # Die Ergebnisse müssen in einer extra Liste ("results") eingetragen werden.
        # Der "zähler" vereinfacht das Aufzählen der Töne, wenn man diese nacheinander zeigen will.

        searchPattern_list = []

        for egal in range(12):  # Suche 12 Mal
            s_len = [streamMot.notes[i].name for i in range(
                len(streamMot.notes))]
            p = search.streamSearchBase(
                s, streamMot, algorithm=pitchClassEqual)
            for notePosition in p:
                starting_note = s[notePosition]
                starting_measure = starting_note.measureNumber
                starting_beat = starting_note.beat
                starting_part = starting_note.getContextByClass("Part")
                results.append(notePosition)

                searchPattern_list.append(
                    [
                        counter,
                        starting_note,
                        starting_measure,
                        starting_beat,
                        starting_part.id,
                        utility_listToString(s_len),
                    ]
                )

                counter += 1

            [n.transpose(1, inPlace=True) for n in streamMot]

            iteration += 1

        print(text_patternSearch_patternsFound(len(results)))
        print("")

        input(text_general_proceed())
        print("")

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = searchPattern_list

        show_resultslist(menu_header, data_values)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")

    while True:
        try:
            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_patternSearch())

            if user_selection == "repeatSelection":
                patternSearch_menuStructure_toneSequence_withTransposition_withoutRhythm()

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
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "Export_Notentext":
                for found in results:
                    for ffound in range(len(streamMot)):
                        s[found + ffound].lyric = "*"
                        s[found + ffound].style.color = "red"

                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                        str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = score_deepCopy.write("xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print("")

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            input(text_general_proceed())
            print("")


def patternSearch_menuStructure_toneSequence_withoutTransposition_withRhythm():
    try:
        score_deepCopy = deepcopy(config.global_score.stripTies(inPlace=True))

        streamMot = patternSearch_enterSearchPattern_withRhythm()

        while True:
            utility_clear_screen()

            user_input = input(text_patternSearch_includeRests())
            print("")

            if utility_userInput_isAffirmative(user_input):
                s = score_deepCopy.recurse().notes

                break

            elif utility_userInput_isNegative(user_input):
                s = score_deepCopy.recurse().notesAndRests

                break

            else:
                print(text_general_input_RestrictedToYesAndNo())
                print("")

                input(text_general_proceed())
                print("")

        # Die Suche wird nun mit dem Befehl 'search.noteNameRhythmicSearch' erstellt.

        p = search.noteNameRhythmicSearch(s, streamMot)

        print(text_patternSearch_patternsFound(len(p)))
        print("")

        input(text_general_proceed())
        print("")

        counter = 1

        searchPattern_list = []

        for position in p:
            startingNote = s[position]
            startingMeasure = startingNote.measureNumber
            startingBeat = startingNote.beat
            startingPart = startingNote.getContextByClass("Part")

            searchPattern_list.append(
                [
                    counter,
                    startingNote,
                    startingMeasure,
                    startingBeat,
                    startingPart.id,
                    utility_listToString(config.global_searchPattern),
                ]
            )

            counter += 1

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = searchPattern_list

        show_resultslist(menu_header, data_values)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")

    while True:
        try:
            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_patternSearch())

            if user_selection == "repeatSelection":
                patternSearch_menuStructure_toneSequence_withoutTransposition_withRhythm()

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
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "Export_Notentext":
                for found in p:
                    for ffound in range(len(streamMot)):
                        s[found + ffound].lyric = "*"
                        s[found + ffound].style.color = "red"

                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                        str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = score_deepCopy.write("xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print("")

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            input(text_general_proceed())
            print("")


def patternSearch_menuStructure_toneSequence_withTransposition_withRhythm():
    try:
        score_deepCopy = deepcopy(config.global_score.stripTies(inPlace=True))

        streamMot = patternSearch_enterSearchPattern_withRhythm()

        while True:
            utility_clear_screen()

            user_input = input(text_patternSearch_includeRests())
            print("")

            if utility_userInput_isAffirmative(user_input):
                s = score_deepCopy.recurse().notes

                break

            elif utility_userInput_isNegative(user_input):
                s = score_deepCopy.recurse().notesAndRests

                break

            else:
                print(text_general_input_RestrictedToYesAndNo())
                print("")

                input(text_general_proceed())
                print("")

        results = []
        counter = 1
        iteration = 1

        # Die Ergebnisse müssen in einer extra Liste ("results") eingetragen werden.
        # Der "zähler" vereinfacht das Aufzählen der Töne, wenn man diese nacheinander zeigen will.

        searchPattern_list = []

        for egal in range(12):  # Suche 12 Mal
            s_len = [streamMot.notes[i].name for i in range(
                len(streamMot.notes))]
            p = search.noteNameRhythmicSearch(s, streamMot)
            for notePosition in p:
                startingNote = s[notePosition]
                startingMeasure = startingNote.measureNumber
                startingBeat = startingNote.beat
                startingPart = startingNote.getContextByClass("Part")
                results.append(notePosition)

                searchPattern_list.append(
                    [
                        counter,
                        startingNote,
                        startingMeasure,
                        startingBeat,
                        startingPart.id,
                        utility_listToString(s_len),
                    ]
                )

                counter += 1

            [n.transpose(1, inPlace=True) for n in streamMot]

            iteration += 1

        print(text_patternSearch_patternsFound(len(results)))
        print("")

        input(text_general_proceed())
        print("")

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = searchPattern_list

        show_resultslist(menu_header, data_values)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")

    while True:
        try:
            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_patternSearch())

            if user_selection == "repeatSelection":
                patternSearch_menuStructure_toneSequence_withTransposition_withRhythm()

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
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "Export_Notentext":
                for found in results:
                    for ffound in range(len(streamMot)):
                        s[found + ffound].lyric = "*"
                        s[found + ffound].style.color = "red"

                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                        str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = score_deepCopy.write("xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print("")

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            input(text_general_proceed())
            print("")


def patternSearch_menuStructure_withRhythm_withoutPitch():
    try:
        score_deepCopy = deepcopy(config.global_score.stripTies(inPlace=True))

        streamMot = patternSearch_enter_search_pattern_only_rhythm()

        while True:
            utility_clear_screen()

            user_input = input(text_patternSearch_includeRests())
            print("")

            if utility_userInput_isAffirmative(user_input):
                s = score_deepCopy.recurse().notes

                break

            elif utility_userInput_isNegative(user_input):
                s = score_deepCopy.recurse().notesAndRests

                break

            else:
                print(text_general_input_RestrictedToYesAndNo())
                print("")

                input(text_general_proceed())
                print("")

        # Die Suche wird nun mit dem Befehl 'search.noteNameRhythmicSearch' erstellt.

        p = search.rhythmicSearch(s, streamMot)

        print(text_patternSearch_patternsFound(len(p)))
        print("")

        input(text_general_proceed())
        print("")

        counter = 1

        searchPattern_list = []

        for position in p:
            startingNote = s[position]
            startingMeasure = startingNote.measureNumber
            startingBeat = startingNote.beat
            startingPart = startingNote.getContextByClass("Part")

            searchPattern_list.append(
                [
                    counter,
                    startingNote,
                    startingMeasure,
                    startingBeat,
                    startingPart.id,
                    utility_listToString(config.global_searchPattern),
                ]
            )

            counter += 1

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        data_values = searchPattern_list

        show_resultslist(menu_header, data_values)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")

    while True:
        try:
            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_patternSearch())

            if user_selection == "repeatSelection":
                patternSearch_menuStructure_withRhythm_withoutPitch()

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
                print()

                input(text_general_proceed())
                print("")

            elif user_selection == "Export_Notentext":
                for found in p:
                    for ffound in range(len(streamMot)):
                        s[found + ffound].lyric = "*"
                        s[found + ffound].style.color = "red"

                us = environment.UserSettings()

                score_export_path = us["directoryScratch"]

                filename = input(text_export_fileName())
                print("")

                path_and_filename = (
                        str(score_export_path) + "\\" + str(filename) + ".xml"
                )

                mf = score_deepCopy.write("xml", fp=path_and_filename)

                print(text_general_exportSuccessful(score_export_path, filename, ".xml"))
                print("")

                input(text_general_proceed())
                print("")

            elif user_selection == "return":
                break

        except Exception as e:
            print(text_exception_general(e, sys._getframe().f_code.co_name))
            print("")

            input(text_general_proceed())
            print("")


def patternSearch_enterSearchPattern_withRhythm():
    try:

        loop_done1 = False

        while not loop_done1:
            streamMot = stream.Stream()

            config.global_searchPattern = []

            loop_done2 = False

            while not loop_done2:
                searchPattern_toneSelection = open_submenu_patternSearch(
                    keySelection_menu_entries())

                utility_clear_screen()

                if searchPattern_toneSelection == "remove":
                    if len(config.global_searchPattern) > 0:
                        config.global_searchPattern.pop()

                elif searchPattern_toneSelection == "complete":
                    for Tonhoehe, Rhythmus in config.global_searchPattern:
                        if "/" in Rhythmus:
                            num, den = map(float, Rhythmus.split("/"))

                            streamMot.append(
                                note.Note(
                                    Tonhoehe, quarterLength=float(num / den))
                            )

                        else:
                            streamMot.append(
                                note.Note(
                                    Tonhoehe, quarterLength=float(Rhythmus))
                            )

                    loop_done3 = False

                    while not loop_done3:
                        utility_clear_screen()

                        user_input = input(text_display_showScoreSelection())
                        print("")

                        if utility_userInput_isAffirmative(user_input):
                            print(text_general_close_museScore3())
                            print()

                            streamMot.show()

                            loop_done3 = True

                        elif utility_userInput_isNegative(user_input):
                            loop_done3 = True

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loop_done3 = False

                            input(text_general_proceed())

                    loop_done3 = False

                    while not loop_done3:
                        utility_clear_screen()

                        print(text_patternSearch_showPatternSelection(config.global_searchPattern))
                        print("")

                        user_input = input(text_general_checkEntry())
                        print("")

                        if utility_userInput_isAffirmative(user_input):
                            loop_done1 = True
                            loop_done2 = True
                            loop_done3 = True

                            utility_clear_screen()

                        elif utility_userInput_isNegative(user_input):
                            loop_done1 = False
                            loop_done2 = True
                            loop_done3 = True

                            print(text_patternSearch_deleteSelection())
                            print("")

                            input(text_general_proceed())
                            print("")

                            utility_clear_screen()

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loop_done3 = False

                            input(text_general_proceed())
                            print("")

                else:
                    searchPattern_rhythmSelection = open_submenu_patternSearch(
                        rhythmSelection_menuEntries()
                    )

                    if searchPattern_rhythmSelection == "remove":
                        if len(config.global_searchPattern) > 0:
                            config.global_searchPattern.pop()

                    elif searchPattern_rhythmSelection == "custom":
                        loop_done4 = True

                        while loop_done4:
                            utility_clear_screen()

                            input_rhythm = input(
                                text_patternSearch_enter_customRhythm()
                            )
                            print("")

                            if utility_userInput_isNumber(input_rhythm):
                                config.global_searchPattern.append(
                                    [searchPattern_toneSelection, str(input_rhythm)])

                                loop_done4 = False

                            else:
                                print(text_general_input_restrictedToNumbers(
                                    input_rhythm))
                                print("")

                                input(text_general_proceed())
                                print("")

                    else:
                        config.global_searchPattern.append([searchPattern_toneSelection, str(searchPattern_rhythmSelection)])

        utility_clear_screen()

        return streamMot

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def patternSearch_enterSearchPattern_withoutRhythm():
    try:

        loop_done1 = False

        while not loop_done1:
            streamMot = stream.Stream()

            config.global_searchPattern = []

            loop_done2 = False

            while not loop_done2:
                searchPattern_toneSelection = open_submenu_patternSearch(
                    keySelection_menu_entries())

                utility_clear_screen()

                if searchPattern_toneSelection == "remove":
                    if len(config.global_searchPattern) > 0:
                        config.global_searchPattern.pop()

                elif searchPattern_toneSelection == "complete":
                    for Tonhoehe in config.global_searchPattern:
                        streamMot.append(note.Note(Tonhoehe))

                    loop_done3 = False

                    while not loop_done3:
                        utility_clear_screen()

                        user_input = input(text_display_showScoreSelection())
                        print("")

                        if utility_userInput_isAffirmative(user_input):
                            print(text_general_close_museScore3())
                            print()

                            streamMot.show()

                            loop_done3 = True

                        elif utility_userInput_isNegative(user_input):
                            loop_done3 = True

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loop_done3 = False

                            input(text_general_proceed())
                            print("")

                    loop_done3 = False

                    while not loop_done3:
                        utility_clear_screen()

                        print(text_patternSearch_showPatternSelection(config.global_searchPattern))
                        print("")

                        user_input = input(text_general_checkEntry())
                        print("")

                        if utility_userInput_isAffirmative(user_input):
                            loop_done1 = True
                            loop_done2 = True
                            loop_done3 = True

                            utility_clear_screen()

                        elif utility_userInput_isNegative(user_input):
                            loop_done1 = False
                            loop_done2 = True
                            loop_done3 = True

                            print(text_patternSearch_deleteSelection())
                            print("")

                            input(text_general_proceed())
                            print("")

                            utility_clear_screen()

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loop_done3 = False

                            input(text_general_proceed())
                            print("")

                else:
                    config.global_searchPattern.append(searchPattern_toneSelection)

        utility_clear_screen()

        return streamMot

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def patternSearch_enter_search_pattern_only_rhythm():
    try:

        loop_done1 = False

        while not loop_done1:
            streamMot = stream.Stream()

            config.global_searchPattern = []

            loop_done2 = False

            while not loop_done2:
                searchPattern_rhythmSelection = open_submenu_patternSearch(
                    rhythmSelection_menuEntries_onlyRhythm()
                )

                utility_clear_screen()

                if searchPattern_rhythmSelection == "remove":
                    if len(config.global_searchPattern) > 0:
                        config.global_searchPattern.pop()

                elif searchPattern_rhythmSelection == "custom":
                    loop_done4 = True

                    while loop_done4:
                        utility_clear_screen()

                        Rhythmuseingabe = input(
                            text_patternSearch_enter_customRhythm()
                        )
                        print("")

                        if utility_userInput_isNumber(Rhythmuseingabe):
                            config.global_searchPattern.append(str(Rhythmuseingabe))

                            loop_done4 = False

                        else:
                            print(text_general_input_restrictedToNumbers(
                                Rhythmuseingabe))
                            print("")

                            input(text_general_proceed())
                            print("")

                elif searchPattern_rhythmSelection == "complete":
                    for rhythm in config.global_searchPattern:
                        if "/" in rhythm:
                            num, den = map(float, rhythm.split("/"))

                            streamMot.append(
                                note.Note("G", quarterLength=float(num / den))
                            )

                        else:
                            streamMot.append(
                                note.Note("G", quarterLength=float(rhythm))
                            )

                    loop_done3 = False

                    while not loop_done3:
                        utility_clear_screen()

                        user_input = input(text_display_showScoreSelection())
                        print("")

                        if utility_userInput_isAffirmative(user_input):
                            print(text_general_close_museScore3())
                            print()

                            streamMot.show()

                            loop_done3 = True

                        elif utility_userInput_isNegative(user_input):
                            loop_done3 = True

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loop_done3 = False

                            input(text_general_proceed())
                            print("")

                    loop_done3 = False

                    while not loop_done3:
                        utility_clear_screen()

                        print(text_patternSearch_showPatternSelection(config.global_searchPattern))
                        print("")

                        user_input = input(text_general_checkEntry())
                        print("")

                        if utility_userInput_isAffirmative(user_input):
                            loop_done1 = True
                            loop_done2 = True
                            loop_done3 = True

                            utility_clear_screen()

                        elif utility_userInput_isNegative(user_input):
                            loop_done1 = False
                            loop_done2 = True
                            loop_done3 = True

                            print(text_patternSearch_deleteSelection())
                            print("")

                            input(text_general_proceed())
                            print("")

                            utility_clear_screen()

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loop_done3 = False

                            input(text_general_proceed())
                            print("")

                else:
                    config.global_searchPattern.append(str(searchPattern_rhythmSelection))

        utility_clear_screen()

        return streamMot

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def keySelection_menu_entries():
    list_de = [
        ["‾‾‾‾  -   Ces", "C-"],
        ["C         C", "C"],
        ["____  ♯   Cis", "C#"],
        ["‾‾‾‾  -   Des", "D-"],
        ["D         D", "D"],
        ["____  ♯   Dis", "D#"],
        ["‾‾‾‾  -   Es", "E-"],
        ["E         E", "E"],
        ["____  ♯   Eis", "E#"],
        ["‾‾‾‾  -   Fes", "F-"],
        ["F         F", "F"],
        ["____  ♯   Fis", "F#"],
        ["‾‾‾‾  -   Ges", "G-"],
        ["G         G", "G"],
        ["____  ♯   Gis", "G#"],
        ["‾‾‾‾  -   As", "A-"],
        ["A         A", "A"],
        ["____  ♯   Ais", "A#"],
        ["‾‾‾‾  -   B", "B-"],
        ["H         H", "B"],
        ["____  ♯   His", "B#"],
        ["BACK: Zuletzt eingegebene Note entfernen", "remove"],
        ["DONE: Eingabe beenden", "complete"],
    ]

    list_en = [
        ["‾‾‾‾  -   C-flat", "C-"],
        ["C         C", "C"],
        ["____  ♯   C-sharp", "C#"],
        ["‾‾‾‾  -   D-flat", "D-"],
        ["D         D", "D"],
        ["____  ♯   D-sharp", "D#"],
        ["‾‾‾‾  -   E-flat", "E-"],
        ["E         E", "E"],
        ["____  ♯   E-sharp", "E#"],
        ["‾‾‾‾  -   F-flat", "F-"],
        ["F         F", "F"],
        ["____  ♯   F-sharp", "F#"],
        ["‾‾‾‾  -   G-flat", "G-"],
        ["G         G", "G"],
        ["____  ♯   G-sharp", "G#"],
        ["‾‾‾‾  -   A-flat", "A-"],
        ["A         A", "A"],
        ["____  ♯   A-sharp", "A#"],
        ["‾‾‾‾  -   B-flat", "B-"],
        ["B         B", "B"],
        ["____  ♯   B-sharp", "B#"],
        ["BACK: Remove the last note entered", "remove"],
        ["DONE: Finish input", "complete"],
    ]

    if config.LANGUAGE == "DE":
        return list_de

    elif config.LANGUAGE == "EN":
        return list_en


def rhythmSelection_menuEntries():
    list_de = [
        ["[0.125]   32-tel-Note", 0.125],
        ["[0.25]    16-tel-Note", 0.25],
        ["[0.375]   16-tel-Note + Punktierung", 0.375],
        ["[1/3]     8-tel-Triole", "1/3"],
        ["[0.5]     8-tel-Note", 0.5],
        ["[0.75]    8-tel-Note + Punktierung", 0.75],
        ["[2/3]     4-tel-Triole", "2/3"],
        ["[1.0]     4-tel-Note", 1.0],
        ["[1.5]     4-tel-Note + Punktierung", 1.5],
        ["[4/3]     Halbe-Triole", "4/3"],
        ["[2.0]     Halbe-Note", 2.0],
        ["[3.0]     Halbe-Note + Punktierung", 3.0],
        ["[8/3]     Ganze-Triole", "8/3"],
        ["[4.0]     Ganze-Note", 4.0],
        ["[6.0]     Ganze-Note + Punktierung", 6.0],
        ["[16/3]    Doppelganze-Triole", "16/3"],
        ["[8.0]     Doppelganze-Note", 8.0],
        ["[12.0]    Doppelganze-Note + Punktierung", 12.0],
        ["[x.xx]    Selbstgewählten Notenwert eingeben", "custom"],
        ["BACK:     Zuletzt eingegebene Note entfernen", "remove"],
    ]

    list_en = [
        ["[0.125]   Thirty-second note", 0.125],
        ["[0.25]    Sixteenth note", 0.25],
        ["[0.375]   Sixteenth note (dotted)", 0.375],
        ["[1/3]     Eighth note triplet", "1/3"],
        ["[0.5]     Eighth note", 0.5],
        ["[0.75]    Eighth note (dotted)", 0.75],
        ["[2/3]     Quarter note triplet", "2/3"],
        ["[1.0]     Quarter note", 1.0],
        ["[1.5]     Quarter note (dotted)", 1.5],
        ["[4/3]     Half note triplet", "4/3"],
        ["[2.0]     Half note", 2.0],
        ["[3.0]     Half note (dotted)", 3.0],
        ["[8/3]     Whole note triplet", "8/3"],
        ["[4.0]     Whole note", 4.0],
        ["[6.0]     Whole note (dotted)", 6.0],
        ["[16/3]    Double whole triplet", "16/3"],
        ["[8.0]     Double whole note", 8.0],
        ["[12.0]    Double whole note (dotted)", 12.0],
        ["[x.xx]    Enter custom rhythm", "custom"],
        ["BACK:     Remove the last note entered", "remove"],
    ]

    if config.LANGUAGE == "DE":
        return list_de

    elif config.LANGUAGE == "EN":
        return list_en


def rhythmSelection_menuEntries_onlyRhythm():
    list_de = [
        ["[0.125]   32-tel-Note", 0.125],
        ["[0.25]    16-tel-Note", 0.25],
        ["[0.375]   16-tel-Note + Punktierung", 0.375],
        ["[1/3]     8-tel-Triole", "1/3"],
        ["[0.5]     8-tel-Note", 0.5],
        ["[0.75]    8-tel-Note + Punktierung", 0.75],
        ["[2/3]     4-tel-Triole", "2/3"],
        ["[1.0]     4-tel-Note", 1.0],
        ["[1.5]     4-tel-Note + Punktierung", 1.5],
        ["[4/3]     Halbe-Triole", "4/3"],
        ["[2.0]     Halbe-Note", 2.0],
        ["[3.0]     Halbe-Note + Punktierung", 3.0],
        ["[8/3]     Ganze-Triole", "8/3"],
        ["[4.0]     Ganze-Note", 4.0],
        ["[6.0]     Ganze-Note + Punktierung", 6.0],
        ["[16/3]    Doppelganze-Triole", "16/3"],
        ["[8.0]     Doppelganze-Note", 8.0],
        ["[12.0]    Doppelganze-Note + Punktierung", 12.0],
        ["[x.xx]    Selbstgewählten Notenwert eingeben", "custom"],
        ["BACK:     Zuletzt eingegebenen Notenwert entfernen", "remove"],
        ["DONE:     Eingabe beenden", "complete"],
    ]

    list_en = [
        ["[0.125]   Thirty-second note", 0.125],
        ["[0.25]    Sixteenth note", 0.25],
        ["[0.375]   Sixteenth note (dotted)", 0.375],
        ["[1/3]     Eighth note triplet", "1/3"],
        ["[0.5]     Eighth note", 0.5],
        ["[0.75]    Eighth note (dotted)", 0.75],
        ["[2/3]     Quarter note triplet", "2/3"],
        ["[1.0]     Quarter note", 1.0],
        ["[1.5]     Quarter note (dotted)", 1.5],
        ["[4/3]     Half note triplet", "4/3"],
        ["[2.0]     Half note", 2.0],
        ["[3.0]     Half note (dotted)", 3.0],
        ["[8/3]     Whole note triplet", "8/3"],
        ["[4.0]     Whole note", 4.0],
        ["[6.0]     Whole note (dotted)", 6.0],
        ["[16/3]    Double whole triplet", "16/3"],
        ["[8.0]     Double whole note", 8.0],
        ["[12.0]    Double whole note (dotted)", 12.0],
        ["[x.xx]    Enter custom rhythm", "custom"],
        ["BACK:     Remove the last rhythm entered", "remove"],
        ["DONE:     Finish input", "complete"],
    ]

    if config.LANGUAGE == "DE":
        return list_de

    elif config.LANGUAGE == "EN":
        return list_en


def keys_list():
    list_de = [
        ["C-Dur", "C"],
        ["G-Dur", "G"],
        ["D-Dur", "D"],
        ["A-Dur", "A"],
        ["E-Dur", "E"],
        ["H-Dur", "B"],
        ["Fis-Dur", "F#"],
        ["Cis-Dur", "C#"],
        ["Gis-Dur", "G#"],
        ["Dis-Dur", "D#"],
        ["Ais-Dur", "A#"],
        ["Eis-Dur", "E#"],
        ["His-Dur", "B#"],
        ["F-Dur", "F"],
        ["B-Dur", "B-"],
        ["Es-Dur", "E-"],
        ["As-Dur", "A-"],
        ["Des-Dur", "D-"],
        ["Ges-Dur", "G-"],
        ["Ces-Dur", "C-"],
        ["Fes-Dur", "F-"],
        ["C-Moll", "c"],
        ["G-Moll", "g"],
        ["D-Moll", "d"],
        ["A-Moll", "a"],
        ["E-Moll", "e"],
        ["H-Moll", "b"],
        ["Fis-Moll", "f#"],
        ["Cis-Moll", "c#"],
        ["Gis-Moll", "g#"],
        ["Dis-Moll", "d#"],
        ["Ais-Moll", "a#"],
        ["Eis-Moll", "e#"],
        ["His-Moll", "b#"],
        ["F-Moll", "f"],
        ["B-Moll", "b-"],
        ["Es-Moll", "e-"],
        ["As-Moll", "a-"],
        ["Des-Moll", "d-"],
        ["Ges-Moll", "g-"],
        ["Ces-Moll", "c-"],
        ["Fes-Moll", "f-"],
    ]

    list_en = [
        ["C-Major", "C"],
        ["G-Major", "G"],
        ["D-Major", "D"],
        ["A-Major", "A"],
        ["E-Major", "E"],
        ["B-Major", "B"],
        ["F-sharp-Major", "F#"],
        ["C-sharp-Major", "C#"],
        ["G-sharp-Major", "G#"],
        ["D-sharp-Major", "D#"],
        ["A-sharp-Major", "A#"],
        ["E-sharp-Major", "E#"],
        ["B-sharp-Major", "B#"],
        ["F-Major", "F"],
        ["B-flat-Major", "B-"],
        ["E-flat-Major", "E-"],
        ["A-flat-Major", "A-"],
        ["D-flat-Major", "D-"],
        ["G-flat-Major", "G-"],
        ["C-flat-Major", "C-"],
        ["F-flat-Major", "F-"],
        ["C-Minor", "c"],
        ["G-Minor", "g"],
        ["D-Minor", "d"],
        ["A-Minor", "a"],
        ["E-Minor", "e"],
        ["B-Minor", "b"],
        ["F-sharp-Minor", "f#"],
        ["C-sharp-Minor", "c#"],
        ["G-sharp-Minor", "g#"],
        ["D-sharp-Minor", "d#"],
        ["A-sharp-Minor", "a#"],
        ["E-sharp-Minor", "e#"],
        ["H-sharp-Minor", "b#"],
        ["F-Minor", "f"],
        ["B-flat-Minor", "b-"],
        ["E-flat-Minor", "e-"],
        ["A-flat-Minor", "a-"],
        ["D-flat-Minor", "d-"],
        ["G-flat-Minor", "g-"],
        ["C-flat-Minor", "c-"],
        ["F-flat-Minor", "f-"],
    ]

    if config.LANGUAGE == "DE":
        return list_de

    elif config.LANGUAGE == "EN":
        return list_en
