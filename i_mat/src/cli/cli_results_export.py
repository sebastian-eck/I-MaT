import sys

from music21 import environment

from i_mat import config as config
from i_mat.src.cli.cli_general_display import text_export_fileName, text_general_exportSuccessful, \
    text_general_exportToDiagrammUnavailable, text_general_noResults, text_general_proceed
from i_mat.src.cli.cli_menu_entries import module_navigation_entries
from i_mat.src.cli.cli_structure_general import open_submenu_data_withExplanationsColumn
from i_mat.src.utils.utils_error_handling import text_exception_general
from i_mat.src.utils.utils_without_userInput import utility_clear_screen, utility_export_as_csv


def menuStructure_musicalParameters_withoutGraphicsExport(
        function_name, menu_header, data_values, explanations
):
    try:
        utility_clear_screen()

        show_resultslist(menu_header, data_values)
        print("")

        if explanations != "":
            print(explanations)
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
                print(text_general_exportToDiagrammUnavailable())
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


def text_headers_entries(identifier):
    dict_de = {
        "range_analysis_textOutput": ["Notenauswahl", "Ambitus"],
        "range_comparison_textOutput": ["Notenauswahl", "Ambitus"],
        "intervalStructure_intervalTypes_textOutput": [
            "Notenauswahl",
            "Anzahl der Intervalltypen",
            "Intervalltypen",
        ],
        "intervalStructure_intervalTypes_quantity_textOutput": [
            "Notenauswahl",
            "Intervall",
            "Vorkommen",
        ],
        "intervalStructure_intervalTypes_comparison_textOutput": [
            "Notenauswahl",
            "Intervall",
            "Vorkommen",
            "Differenz zur anderen Notenauswahl (+/-)",
        ],
        "intervalStructure_Intervalle_quantity_textOutput": [
            "Notenauswahl",
            "Anzahl Intervalle",
        ],
        "meter_metricWeight_textOutput": [
            "Kennung",
            "Metrisches Gewicht (x-Achse)",
            "Haeufigkeit (y-Achse)",
        ],
        "meter_pitchClass_metricPosition_textOutput": [
            "Kennung",
            "Tonhoehe (x-Achse)",
            "Metrisches Gewicht (y-Achse)",
            "Haeufigkeit (z-Achse)",
        ],
        "notes_quantity_total_textOutput": ["Kennung", "Anzahl Töne"],
        "notes_notesQuantity_pitches_textOutput": [
            "Kennung",
            "Tonhoehen",
            "Pitch",
        ],
        "predefinedVisualizations_HistogramPitchSpace": [
            "Kennung",
            "Tonstufe (Midi)",
            "Tonstufenname (x-Achse)",
            "Haeufigkeit (y-Achse)",
        ],
        "predefinedVisualizations_HistogramPitchClass": [
            "Kennung",
            "Tonklasse (Midi)",
            "Tonklassenname (x-Achse)",
            "Haeufigkeit (y-Achse)",
        ],
        "predefinedVisualizations_HistogramQuarterLength": [
            "Kennung",
            "Notenwert (Viertel = 1.0)",
            "Notenwertname (x-Achse)",
            "Haeufigkeit (y-Achse)",
        ],
        "predefinedVisualizations_HorizontalBarPitchSpaceOffset": [
            "Kennung",
            "Tonstufe (Midi)",
            "Tonstufenname (y-Achse)",
            "Offset (x-Achse)",
            "Dargestellte Tonlaenge",
        ],
        "predefinedVisualizations_ScatterWeightedPitchSpaceQuarterLength": [
            "Kennung",
            "Notenwert (Viertel = 1.0)",
            "Notenwertname (x-Achse)",
            "Tonstufe (Midi)",
            "Tonstufenname (y-Achse)",
            "Haeufigkeit",
        ],
        "predefinedVisualizations_Plot3DBarsPitchSpaceQuarterLength": [
            "Kennung",
            "Notenwert (Viertel = 1.0)",
            "Notenwertname (x-Achse)",
            "Tonstufe (Midi)",
            "Tonstufenname (y-Achse)",
            "Haeufigkeit (z-Achse)",
        ],
        "predefinedVisualizations_ScatterWeightedPitchClassQuarterLength": [
            "Kennung",
            "Notenwert (Viertel = 1.0)",
            "Notenwertname (x-Achse)",
            "Tonklasse (Midi)",
            "Tonklassenname (y-Achse)",
            "Haeufigkeit",
        ],
        "predefinedVisualizations_ScatterPitchClassOffset": [
            "Kennung",
            "Tonklasse",
            "Tonklassenname (y-Achse)",
            "Offset (x-Achse)",
        ],
        "predefinedVisualizations_ScatterWeightedPitchSpaceDynamicSymbol": [
            "Kennung",
            "Tonstufe (Midi)",
            "Tonstufenname (x-Achse)",
            "Dynamik (y-Achse)",
            "Haeufigkeit",
        ],
        "predefinedVisualizations_HorizontalBarPitchClassOffset": [
            "Kennung",
            "Tonklasse (Midi)",
            "Tonklassenname (y-Achse)",
            "Offset (x-Achse)",
            "Dargestellte Tonlaenge",
        ],
        "patternSearch_menuStructure_toneSequence_withoutTransposition_withoutRhythm": [
            "Nr.",
            "Tonhoehe",
            "Takt",
            "Zaehlzeit",
            "Stimme",
            "Suchmuster",
        ],
        "patternSearch_menuStructure_toneSequence_withTransposition_withoutRhythm": [
            "Nr.",
            "Tonhoehe",
            "Takt",
            "Zaehlzeit",
            "Stimme",
            "Suchmuster",
        ],
        "patternSearch_menuStructure_toneSequence_withoutTransposition_withRhythm": [
            "Nr.",
            "Tonhoehe",
            "Takt",
            "Zaehlzeit",
            "Stimme",
            "Suchmuster (1.0 = Viertelnote)",
        ],
        "patternSearch_menuStructure_toneSequence_withTransposition_withRhythm": [
            "Nr.",
            "Tonhoehe",
            "Takt",
            "Zaehlzeit",
            "Stimme",
            "Suchmuster (1.0 = Viertelnote",
        ],
        "patternSearch_menuStructure_withRhythm_withoutPitch": [
            "Nr.",
            "Tonhoehe",
            "Takt",
            "Zaehlzeit",
            "Stimme",
            "Suchmuster (1.0 = Viertelnote",
        ],
        "show_names_individualVoices": ["Nr.", "Name der Stimme"],
        "name_individualVoices": ["Nr.", "Name der Stimme"],
        "show_score_metadata": ["Nr.", "Metadata", "Wert"],
    }

    dict_en = {
        "range_analysis_textOutput": ["Notenauswahl", "Ambitus"],
        "range_comparison_textOutput": ["Note selection", "Ambitus"],
        "intervalStructure_intervalTypes_textOutput": [
            "Note selection",
            "Number of interval types",
            "Interval types",
        ],
        "intervalStructure_intervalTypes_quantity_textOutput": [
            "Note selection",
            "Interval",
            "Frequency",
        ],
        "intervalStructure_intervalTypes_comparison_textOutput": [
            "Note selection",
            "Interval",
            "Frequency",
            "Difference to other note selection (+/-)",
        ],
        "intervalStructure_Intervalle_quantity_textOutput": [
            "Note selection",
            "Number of intervals",
        ],
        "meter_metricWeight_textOutput": [
            "Identifier",
            "Metric weight (x-axis)",
            "Frequency (y-axis)",
        ],
        "meter_pitchClass_metricPosition_textOutput": [
            "Identifier",
            "Pitch (x-axis)",
            "Metric weight (y-axis)",
            "Frequency (z-axis)",
        ],
        "notes_quantity_total_textOutput": ["Identifier", "Number of tones"],
        "notes_notesQuantity_pitches_textOutput": [
            "Identifier",
            "Pitch",
            "Pitch",
        ],
        "predefinedVisualizations_HistogramPitchSpace": [
            "Identifier",
            "Pitch (midi)",
            "Pitch name (x-axis)",
            "Frequency (y-axis)",
        ],
        "predefinedVisualizations_HistogramPitchClass": [
            "Identifier",
            "Tone class (Midi)",
            "Tone class name (x-axis)",
            "Frequency (y-axis)",
        ],
        "predefinedVisualizations_HistogramQuarterLength": [
            "Identifier",
            "Rhythm value (quarter = 1.0)",
            "Rhythm value name (x-axis)",
            "Frequency (y-axis)",
        ],
        "predefinedVisualizations_HorizontalBarPitchSpaceOffset": [
            "Identifier",
            "Pitch (midi)",
            "Pitch name (y-axis)",
            "Offset (x-axis)",
            "Displayed length",
        ],
        "predefinedVisualizations_ScatterWeightedPitchSpaceQuarterLength": [
            "Identifier",
            "Rhythm value (quarter = 1.0)",
            "Rhythm value name (x-axis)",
            "Pitch (midi)",
            "Pitch name (y-axis)",
            "Frequency",
        ],
        "predefinedVisualizations_Plot3DBarsPitchSpaceQuarterLength": [
            "Identifier",
            "Rhythm value (quarter = 1.0)",
            "Rhythm value name (x-axis)",
            "Pitch (midi)",
            "Pitch name (y-axis)",
            "Frequency (z-axis)",
        ],
        "predefinedVisualizations_ScatterWeightedPitchClassQuarterLength": [
            "Identifier",
            "rhythm value (quarter = 1.0)",
            "rhythm value name (x-axis)",
            "pitch class (midi)",
            "pitch class name (y-axis)",
            "frequency",
        ],
        "predefinedVisualizations_ScatterPitchClassOffset": [
            "Identifier",
            "pitch class",
            "pitch class name (y-axis)",
            "offset (x-axis)",
        ],
        "predefinedVisualizations_ScatterWeightedPitchSpaceDynamicSymbol": [
            "Identifier",
            "Pitch (midi)",
            "Pitch name (x-axis)",
            "Dynamics (y-axis)",
            "Frequency",
        ],
        "predefinedVisualizations_HorizontalBarPitchClassOffset": [
            "Identifier",
            "Tone class (Midi)",
            "Tone class name (y-axis)",
            "Offset (x-axis)",
            "Displayed pitch length",
        ],
        "patternSearch_menuStructure_toneSequence_withoutTransposition_withoutRhythm": [
            "No.",
            "Pitch",
            "Measure",
            "Beat",
            "Voice",
            "Search pattern",
        ],
        "patternSearch_menuStructure_toneSequence_withTransposition_withoutRhythm": [
            "No.",
            "Pitch",
            "Measure",
            "Beat",
            "Voice",
            "Search pattern",
        ],
        "patternSearch_menuStructure_toneSequence_withoutTransposition_withRhythm": [
            "No.",
            "Pitch",
            "Measure",
            "Beat",
            "Voice",
            "Search pattern (1.0 = quarter)",
        ],
        "patternSearch_menuStructure_toneSequence_withTransposition_withRhythm": [
            "No.",
            "Pitch",
            "Measure",
            "Beat",
            "Voice",
            "Search pattern (1.0 = quarter)",
        ],
        "patternSearch_menuStructure_withRhythm_withoutPitch": [
            "No.",
            "Pitch",
            "Measure",
            "Beat",
            "Voice",
            "Search pattern (1.0 = quarter)",
        ],
        "show_names_individualVoices": ["No.", "Part name"],
        "name_individualVoices": ["No.", "Part name"],
        "show_score_metadata": ["No.", "Metadata", "Value"],
    }

    if config.LANGUAGE == "DE":
        return dict_de[identifier]

    elif config.LANGUAGE == "EN":
        return dict_en[identifier]


def text_menu_headers_withoutExplanationsColumn():
    list_de = ["Nr.", "Menüpunkt"]

    list_en = ["No.", "Menu item"]

    if config.LANGUAGE == "DE":
        return list_de

    elif config.LANGUAGE == "EN":
        return list_en


def text_menu_headers_withExplanationsColumn():
    list_de = ["Nr.", "Menüpunkt", "<Erläuterung>"]

    list_en = ["No.", "Menu item", "<Explanation>"]

    if config.LANGUAGE == "DE":
        return list_de

    elif config.LANGUAGE == "EN":
        return list_en


def text_menu_headers(identifier):
    dict_de = {
        "open_mainmenu_individualPiece": "-- Hauptmenü Einzelwerk --",
        "open_submenu_individualPiece_files": "-- Untermenü Einzelwerk (Files) --",
        "open_submenu_individualPiece_statisticalAnalyses": "-- Untermenü Einzelwerk (statistische Analysen) --",
        "open_submenu_individualPiece_statisticalAnalyses_visualizations": "-- Untermenü Einzelwerk (statistische Analysen - Darstellungen zweidimensionaler Häufigkeitsverteilungen) --",
        "open_submenu_individualPiece_visualizations": "-- Untermenü Einzelwerk (Darstellungen) --",
        "open_submenu_individualPiece_patternSearch": "-- Untermenü Einzelwerk (Mustersuche) --",
        "open_submenu_individualPiece_settings": "-- Untermenü Einzelwerk (Einstellungen) --ACHTUNG: Erstellen Sie vor der Bearbeitung der Environment-Datei eine Sicherungskopie!",
        "open_startmenu": "-- Startmenü --",
        "show_environmentFile_settings": "Ihre Environment-Datei 'music21-settings' ist wie folgt definiert:",
        "open_submenu_patternSearch": "Bitte geben Sie hier das zur Mustersuche verwendete Noten-/Rhythmusmuster (1.0 = Viertelnote) ein:",
        "select_score_filePath": "-- Auswahl einer Notendatei zur weiteren Analyse --",
        "select_score_completeOrIndividualVoice": "-- Auswahl der gesamten Partitur oder einer Einzelstimme --",
        "select_bars": "-- Auswahl der Takte --",
        "show_names_individualVoices": "-- Allgemeine Informationen (Stimmennamen) --",
        "show_score_metadata": "-- Allgemeine Informationen (Metadaten) --",
        "show_resultslist": "-- Ergebnisse --",
        "name_individualVoices": "-- Konfiguration: Stimmnamen --",
    }

    dict_en = {
        "open_mainmenu_individualPiece": "-- main menu individual piece --",
        "open_submenu_individualPiece_files": "-- Submenu individual piece (Files) --",
        "open_submenu_individualPiece_statisticalAnalyses": "-- Submenu individual piece (statistical analysis) --",
        "open_submenu_individualPiece_statisticalAnalyses_visualizations": "-- Submenu individual piece (statistical analyzes - representations of two-dimensional frequency distributions) --",
        "open_submenu_individualPiece_visualizations": "-- Submenu individual piece (Visualisations) --",
        "open_submenu_individualPiece_patternSearch": "-- Submenu individual piece (Pattern search) --",
        "open_submenu_individualPiece_settings": "-- Submenu individual piece (Settings) --ATTENTION: Make a backup copy before editing the environment file!",
        "open_startmenu": "-- Start menu --",
        "show_environmentFile_settings": "Your environment file 'music21-settings' is defined as follows:",
        "open_submenu_patternSearch": "Please enter the note / rhythm pattern (1.0 = quarter) used for the pattern search here.",
        "select_score_filePath": "-- Selection of a score file for further analysis --",
        "select_score_completeOrIndividualVoice": "-- Selection of the entire score or a single part --",
        "select_bars": "-- Selection of bars --",
        "show_names_individualVoices": "-- General information (part names) --",
        "show_score_metadata": "-- General information (Metadata) --",
        "show_resultslist": "-- Results --",
        "name_individualVoices": "-- Configuration: part names --",
    }

    if config.LANGUAGE == "DE":
        return dict_de[identifier]

    elif config.LANGUAGE == "EN":
        return dict_en[identifier]


def module_navigation_transformedScores():
    list_de = [
        [
            "REPT: Neue Notenauswahl",
            "repeatSelection",
            "<Wiederholung des Tools mit neuer Notenauswahl>",
        ],
        [
            "SHOW: Notenauswahl anzeigen (MuseScore)",
            "visualizations_MuseScore",
            "<Öffnet MuseScore und zeigt den transformierten Notentext an>",
        ],
        [
            "SAVE: Datei speichern",
            "save_file",
            '<Speichert den transformierten Notentext als .xml-Datei im "scratch-Ordner" von music21>',
        ],
        ["BACK: Zurück ins Hauptmenü", "return", "<Rückkehr ins Hauptmenü>"],
    ]

    list_en = [
        [
            "REPT: New score selection",
            "repeatSelection",
            "<Repeat the tool with new score selection>",
        ],
        [
            "SHOW: Show score selection (MuseScore)",
            "visualizations_MuseScore",
            "<Opens MuseScore and shows the transformed note text>",
        ],
        [
            "SAVE: Save file",
            "save_file",
            '<Saves the transformed music text as an .xml file in the "scratch folder" of music21>',
        ],
        ["BACK: Back to the main menu", "return", "<Return to the main menu>"],
    ]

    if config.LANGUAGE == "DE":
        return list_de

    elif config.LANGUAGE == "EN":
        return list_en


def show_resultslist(description, received_data):
    try:
        # Beschreibung = ['Beschreibung1', 'Beschreibung2', ...]

        utility_clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("\n")

        if len(received_data) == 0:
            print(text_general_noResults())
            print("")

        else:
            menu_header = ""

            # converts every item in List to a string

            m = 0

            n = 0

            for item in received_data:
                m = received_data.index(item)

                for content in item:
                    n = item.index(content)

                    received_data[m][n] = str(content)

            description_and_receivedData = [description] + received_data

            max_lengths_dict = {}

            n = 0

            while n < len(description):
                max_lengths_dict[n] = 0

                n = n + 1

            for item in description_and_receivedData:
                for content in item:
                    if len(content) >= max_lengths_dict[item.index(content)]:
                        max_lengths_dict[item.index(content)] = len(content)

            for item in description:
                menu_header = (
                        menu_header
                        + f"{item:<{max_lengths_dict[description.index(item)] + 7}s}"
                )

            print(menu_header)
            print("\n")

            for item in received_data:
                data_string = ""

                for content in item:
                    data_string = (
                            data_string
                            + f"{content:<{max_lengths_dict[item.index(content)] + 7}s}"
                    )

                print(data_string)
                print("")

            print("\n")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    input(text_general_proceed())
    print("")
