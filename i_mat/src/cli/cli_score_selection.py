import sys
import time

from music21 import converter

import i_mat.config as config
from i_mat.src.cli.cli_general_display import text_general_checkEntry, text_general_close_museScore3, \
    text_general_enter_newPath, text_general_input_RestrictedToYesAndNo, text_general_proceed, \
    text_general_show_enteredPath
from i_mat.src.cli.cli_menu_entries import module_navigation_selectedScore
from i_mat.src.cli.cli_results_export import text_headers_entries, text_menu_headers
from i_mat.src.cli.cli_structure_general import open_submenu_data_withExplanationsColumn, \
    open_submenu_data_withoutExplanationsColumn
from i_mat.src.cli.cli_text_output import text_menu_exception_selectionOutOfRange, text_metadata_availableMetadata, \
    text_metadata_availableMetadata_none, text_metadata_partsNames, text_metadata_partsNames_checkEnteredName, \
    text_metadata_partsNames_chooseName, text_metadata_partsNames_chooseName_notUnique
from i_mat.src.utils.utils_error_handling import text_exception_general
from i_mat.src.utils.utils_without_userInput import utility_clear_screen, utility_getKeyToValue, \
    utility_userInput_isAffirmative, utility_userInput_isNegative


def select_score_filePath():
    try:
        # Erstellen einer globalen Variabel 'Partitur', auf die von jeder Stelle im Programm aus zugegriffen werden kann.

        utility_clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        # Ausgabe eines Auswahlmenüs, das den Benutzer zwischen einer "Beispiel-Datei" und einer "Eigenen Auswahl" auswählen lässt (s. .

        user_selection = open_submenu_data_withExplanationsColumn(
            menue_entries_score_selection())

        if user_selection == "Beispiel-Datei":
            config.global_score = converter.parse(
                "https://analyse.hfm-weimar.de/database/02/PrJode_Jos0602_COM_1-5_MissaLhomm_002_00066.xml"
            )

        else:
            loop_done = False

            while not loop_done:
                utility_clear_screen()

                print(menu_header)
                print("")

                print(text_score_selection())
                print("")

                config.global_score_path_input = input(text_general_enter_newPath())
                print("")

                try:
                    loop2Done = False

                    while not loop2Done:
                        utility_clear_screen()

                        print(menu_header)
                        print("")

                        print(text_score_selection())
                        print("")

                        config.global_score_path = config.global_score_path_input.replace(
                            '"', "")

                        print(text_general_show_enteredPath(config.global_score_path))
                        print("")

                        user_input = input(text_general_checkEntry())
                        print("")

                        if utility_userInput_isAffirmative(user_input):
                            start = time.time()

                            try:
                                config.global_score = converter.parse(config.global_score_path)

                                print(
                                    text_score_selectionSuccessful(
                                        time.time() - start)
                                )
                                print("")

                                input(text_general_proceed())
                                print("")

                                loop_done = True
                                loop2Done = True

                                utility_clear_screen()

                            except Exception as e:
                                print(
                                    text_exception_general(
                                        e, sys._getframe().f_code.co_name
                                    )
                                )
                                print("")

                                print(text_score_selectionException())
                                print("")

                                input(text_general_proceed())
                                print("")

                                loop_done = False
                                loop2Done = True

                                utility_clear_screen()

                        elif utility_userInput_isNegative(user_input):
                            loop_done = False
                            loop2Done = True

                            utility_clear_screen()

                            print(menu_header)
                            print("")

                        else:
                            print(text_general_input_RestrictedToYesAndNo())
                            print("")

                            loop2Done = False

                            input(text_general_proceed())
                            print("")

                except Exception as e:
                    print(text_exception_general(
                        e, sys._getframe().f_code.co_name))
                    print("")

                    input(text_general_proceed())
                    print("")

        show_score_metadata()

        name_individualVoices()

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def menue_entries_score_selection():
    list_de = [
        [
            "Notenauswahl: Beispiel-Datei",
            "Beispiel-Datei",
            "<Datei: Josquin des Prez (1450/55-1521): Missa L'homme arme sexti toni - Kyrie (Online-Datenbank)",
        ],
        [
            "Notenauswahl: Eigene Auswahl",
            "Eigene Auswahl",
            "<Auswahl einer lokal gespeicherten Datei (Pfad)/einer Datei aus der Online-Datenbank (URL)>",
        ],
    ]

    list_en = [
        [
            "Note selection: example file",
            "Beispiel-Datei",
            "<File: Josquin des Prez (1450/55-1521): Missa L'homme arme sexti toni - Kyrie (online database)",
        ],
        [
            "Note selection: custom selection ",
            "Eigene Auswahl",
            "<Selection of a locally saved file (path)/a file from the online database (URL)>",
        ],
    ]

    if config.LANGUAGE == "DE":
        return list_de

    elif config.LANGUAGE == "EN":
        return list_en


def name_individualVoices():
    try:
        parts_names = ["none"] * len(config.global_score.parts)
        parts_data = ["none"] * len(config.global_score.parts)

        n = 0

        while n < len(config.global_score.parts):
            parts_data[n] = config.global_score.parts[n]

            n = n + 1

        user_selection = open_submenu_data_withExplanationsColumn(
            module_navigation_name_individualVoices()
        )

        if user_selection == "visualizations_MuseScore":
            print(text_general_close_museScore3())
            print()

            config.global_score.show()

            name_individualVoices()

        elif user_selection == "customDesignations":
            loop1Done = False

            while not loop1Done:
                n = 0

                while n < len(config.global_score.parts):
                    utility_clear_screen()

                    menu_header = text_menu_headers(sys._getframe().f_code.co_name)

                    print(menu_header)
                    print("")

                    Input_Stimmen_Namen = input(
                        text_metadata_partsNames_chooseName(
                            len(config.global_score.parts), n + 1)
                    )
                    print("")

                    if not Input_Stimmen_Namen in parts_names:
                        loop2Done = False

                        while not loop2Done:
                            utility_clear_screen()

                            menu_header = text_menu_headers(
                                sys._getframe().f_code.co_name)

                            print(menu_header)
                            print("")

                            print(
                                text_metadata_partsNames_checkEnteredName(
                                    len(config.global_score.parts), n +
                                                                    1, Input_Stimmen_Namen
                                )
                            )
                            print("")

                            user_input = input(text_general_checkEntry())
                            print("")

                            if utility_userInput_isAffirmative(user_input):
                                parts_names[n] = Input_Stimmen_Namen

                                n = n + 1

                                loop2Done = True

                            elif utility_userInput_isNegative(user_input):
                                loop2Done = True

                            else:
                                print(text_general_input_RestrictedToYesAndNo())
                                print("")

                                input(text_general_proceed())
                                print("")

                    else:
                        print(text_metadata_partsNames_chooseName_notUnique())

                        input(text_general_proceed())
                        print("")

                loop2Done = False

                while not loop2Done:
                    utility_clear_screen()

                    menu_header = text_menu_headers(sys._getframe().f_code.co_name)

                    print(menu_header)
                    print("")

                    print(text_metadata_partsNames())
                    print("")

                    menu_header = text_headers_entries(sys._getframe().f_code.co_name)

                    print("{:<4} {:<65}\n".format(menu_header[0], menu_header[1]))

                    Index = 1

                    for i in parts_names:
                        print("{:<4} {:<65}".format(Index, i))

                        Index += 1

                    print("")

                    user_input = input(text_general_checkEntry())
                    print("")

                    if utility_userInput_isAffirmative(user_input):
                        utility_clear_screen()

                        loop1Done = True
                        loop2Done = True

                    elif utility_userInput_isNegative(user_input):
                        loop1Done = False
                        loop2Done = True

                        parts_names = ["none"] * len(config.global_score.parts)

                        utility_clear_screen()

                    else:
                        print(text_general_input_RestrictedToYesAndNo())
                        print("")

                        loop2Done = False

                        input(text_general_proceed())
                        print("")

            # Erstellen eines Dictionarys mit den Namen der Instrumente als 'keys' und den zugehörigen Music21-Pfaden als 'values':

            keys = parts_names

            vals = parts_data

            # Zusammenführen der Listen in ein Dictionary

            config.global_catalogue_individualParts = dict(zip(keys, vals))

            keys.insert(0, "Score")

            vals.insert(0, config.global_score)

            config.global_catalogue_completeScoreWithIndividualParts = dict(zip(keys, vals))

            utility_clear_screen()

        elif user_selection == "genericDesignations":
            if config.LANGUAGE == "DE":
                n = 0

                while n < len(config.global_score.parts):
                    parts_names[n] = "Stimme " + str(n + 1)

                    n = n + 1

            elif config.LANGUAGE == "EN":
                n = 0

                while n < len(config.global_score.parts):
                    parts_names[n] = "Part " + str(n + 1)

                    n = n + 1

            utility_clear_screen()

            menu_header = text_menu_headers(sys._getframe().f_code.co_name)

            print(menu_header)
            print("")

            print(text_metadata_partsNames())
            print("")

            menu_header = text_headers_entries(sys._getframe().f_code.co_name)

            print("{:<4} {:<65}\n".format(menu_header[0], menu_header[1]))

            Index = 1

            for i in parts_names:
                print("{:<4} {:<65}".format(Index, i))

                Index += 1

            print("")

            input(text_general_proceed())
            print("")

            # Erstellen eines Dictionarys mit den Namen der Instrumente als 'keys' und den zugehörigen Music21-Pfaden als 'values':

            keys = parts_names

            vals = parts_data

            # Zusammenführen der Listen in ein Dictionary

            config.global_catalogue_individualParts = dict(zip(keys, vals))

            keys.insert(0, "Score")

            vals.insert(0, config.global_score)

            config.global_catalogue_completeScoreWithIndividualParts = dict(zip(keys, vals))

            utility_clear_screen()

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def select_score_completeOrIndividualVoice():
    try:
        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        while True:
            utility_clear_screen()

            user_selection = open_submenu_data_withExplanationsColumn(
                module_navigation_selectedScore())

            if user_selection == "completeScore":

                config.global_selectedScore = config.global_score

                config.global_input_firstMeasure = "1"

                number_of_measures = len(
                    config.global_score.parts[0].getElementsByClass("Measure"))

                config.global_input_lastMeasure = number_of_measures

                config.global_previously_selectedScore = config.global_selectedScore

                return config.global_selectedScore

            elif user_selection == "newSelection":

                config.global_selectedScore = menu_askUser_selectCompleteScoreOrIndividualPart()

                selected_measures = select_bars(config.global_selectedScore)

                config.global_previously_selectedScore = selected_measures

                return selected_measures

            elif user_selection == "repeatPreviousSelection":
                utility_clear_screen()

                if config.global_previously_selectedScore is not None:

                    return config.global_previously_selectedScore

                else:
                    print(text_menu_selection_noPreviousSelection())
                    print("")

                    input(text_general_proceed())
                    print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def menu_askUser_selectCompleteScoreOrIndividualPart():
    try:
        utility_clear_screen()

        config.global_selectedScore = open_submenu_data_withoutExplanationsColumn(
            list(config.global_catalogue_completeScoreWithIndividualParts.items())
        )

        return config.global_selectedScore

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def select_bars(received_scores):
    try:
        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        number_of_measures = len(config.global_score.parts[0].getElementsByClass("Measure"))

        loop_done = False

        while not loop_done:
            utility_clear_screen()

            print(menu_header)
            print("")

            config.global_input_firstMeasure = input(
                text_score_selectFirstMeasure(
                    number_of_measures,
                    utility_getKeyToValue(
                        received_scores, config.global_catalogue_completeScoreWithIndividualParts),
                )
            )
            print("")

            if str.isdigit(config.global_input_firstMeasure):
                selected_firstMeasure = int(config.global_input_firstMeasure)

                if 1 <= selected_firstMeasure <= number_of_measures:
                    loop_done = True

                else:
                    print(text_menu_exception_selectionOutOfRange(number_of_measures))
                    print("")

                    input(text_general_proceed())
                    print("")

            else:
                print(text_score_bars_exception_notNumber())
                print("")

                input(text_general_proceed())
                print("")

        loop_done = False

        while not loop_done:
            utility_clear_screen()

            print(menu_header)
            print("")

            config.global_input_lastMeasure = input(
                text_score_selectLastMeasure(
                    number_of_measures,
                    utility_getKeyToValue(
                        received_scores, config.global_catalogue_completeScoreWithIndividualParts),
                    selected_firstMeasure,
                )
            )
            print("")

            if str.isdigit(config.global_input_lastMeasure):
                selected_last_measure = int(config.global_input_lastMeasure)

                if (
                        selected_firstMeasure <= selected_last_measure <= number_of_measures
                ):
                    loop_done = True

                else:
                    print(
                        text_score_bars_exception_outOfRange(
                            selected_firstMeasure, number_of_measures
                        )
                    )
                    print("")

                    input(text_general_proceed())
                    print("")

            else:
                print(text_score_bars_exception_notNumber())
                print("")

                input(text_general_proceed())
                print("")

        return received_scores.measures(selected_firstMeasure, selected_last_measure)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

        input(text_general_proceed())
        print("")


def text_menu_selection_noPreviousSelection():
    text_de = (
        "Es liegt noch keine Notenauswahl vor, auf die zurückgegriffen werden kann.\n\n"
        "Bitte wählen Sie aus Menüpunkt 1 oder 2."
    )

    text_en = (
        "There is not yet a selection of notes that can be used.\n\n"
        "Please choose from menu item 1 or 2."
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_score_selection():
    text_de = (
        "Bitte wählen Sie eine Notendatei aus, die sie in das Programm laden möchten. Verwendet Sie falls möglich eine .xml-Datei.\n\n"
        "NOTENDATENBANK:\n\n"
        "Die Notendatenbank umfasst mehrere Tausend nach Komponisten geordnete Notendateien, die für eigene Analyseprojekte,\n"
        "insbesondere für Korpusanalysen, verwendet werden können. Die Noten stammen aus einer Reihe von im Internet frei verfügbaren\n"
        "Online-Datenbanken sowie weiteren Forschungsdatenbanken, vgl. Liste der Datenbanken. Alle Dateien können unter Beachtung der\n"
        "Creative-Commons-Lizenzierung verwendet werden. Alle Notendateien wurden ins MusicXML-Format konvertiert.\n\n"
        "Achtung: Die Qualität der einzelnen MusicXML-Dateien wurde nicht überprüft und kann daher stark variieren; Fehler sind nicht ausgeschlossen.\n\n"
        'Notendatenbank: "<https://analyse.hfm-weimar.de/doku.php?id=komponisten">\n\n'
        "SUBKORPUS DER NOTENDATENBANK:\n\n"
        "Der Subkorpus der Notendatenbank entspricht einem (subjekt geprägten) chronologischen Gang durch die europäische Musikgeschichte\n"
        "anhand verschiedener Komponisten und Kompositionen (s. Inhaltsverzeichnis rechts).\n"
        "Dabei wurden vier verschiedene Gattungen berücksichtigt:\n\n"
        " - Vokalsatz,\n"
        " - Piano solo,\n"
        " - Streichquartett und Sinfonie.\n\n"
        "Alle MusicXML-Dateien wurden auf ihre Qualität und auf mögliche Fehler geprüft. In dieser Auswahl sind alle Noten enthalten,\n"
        "die in den Modulen zur Notenanalyse und den entsprechenden Aufgaben verwendet werden.\n\n"
        "Subkorpus der Notendatenbank: <https://analyse.hfm-weimar.de/doku.php?id=notenauswahl#subkorpus_der_notendatenbank>\n\n"
        "Kopieren Sie sich die URL der gewünschten Datei (Rechtsklick > Link kopieren) und fügen Sie diesen nachfolgend ein.\n\n"
        "Alternativ können Sie auch eine auf Ihrem Rechner lokal gespeicherte Datei öffnen. Ziehen Sie diese einfach per Drag & Drop\n"
        "in das Fenster des Terminals.\n\n"
        "Achten Sie darauf, am Ende des Pfades keine Leerzeichen zu setzen."
    )
    text_en = (
        "Please select a note file that you want to load into the program. Use an .xml file if possible.\n\n"
        "SHEET MUSIC DATABASE:\n\n"
        "The sheet music database includes several thousand sheet music files listed by composer name, which can be used for\n"
        "your own analysis projects, especially for corpus analysis. The scores come from a number of online databases freely\n"
        "available on the Internet as well as other research databases, cf. list of databases. All files can be used in\n"
        "compliance with Creative Commons licensing.\n\n"
        "Attention: The quality of the individual MusicXML files have not been checked and can therefore vary greatly; errors are not excluded.\n\n"
        "Sheet Music Database: <https://analyse.hfm-weimar.de/doku.php?id=en:datenbank>\n\n"
        "SUBCORPUS OF THE SHEET MUSIC DATABASE:\n\n"
        "This subcorpus of the sheet music database corresponds to a (subjective) chronological walk through European music history\n"
        "on the basis of various composers and compositions (see table of contents on the right).\n"
        "Four different genres were considered:\n\n"
        " - Vocal,\n"
        " - Piano solo,\n"
        " - String quartet and Symphony.\n\n"
        "All MusicXML-files were checked for quality and possible errors. This selection contains all scores used in\n"
        "the two modules for score analysis and the corresponding tasks.\n\n"
        "Subcorpus of the sheet music database: <https://analyse.hfm-weimar.de/doku.php?id=en:notenauswahl>\n\n"
        "Copy the URL of the desired file (right click > copy link) and paste it below.\n\n"
        "Alternatively, you can also open a file saved locally on your computer. Simply drag and drop the file into the terminal window.\n\n"
        "Be careful not to put any spaces at the end of the path."
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_score_selectionSuccessful(time):
    text_de = (
            "Datei erfolgreich eingelesen.\n\n"
            "Zum Öffnen benötigte Zeit: " + str(time) + "s"
    )

    text_en = (
            "File successfully loaded. \n\n" "Time required to open: " +
            str(time) + "s"
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_score_selectionException():
    text_de = (
        "Geben Sie den Pfad/die URL erneut ein und achten Sie auf die richtige Schreibweise.\n\n"
        "Falls Sie die URL nicht öffnen können, speichern Sie die Datei Lokal (Rechtsklick > Ziel speichern unter..) und öffnen Sie die heruntergeladene Datei lokal über deren Pfad.\n\n"
        "Achten Sie darauf, am Ende des Pfades keine Leerzeichen zu setzen."
    )

    text_en = (
        "Re-enter the path / URL and make sure that the spelling is correct.\n\n"
        "If you cannot open the URL, save the file locally (right click > Save target as ..) and open the downloaded file locally using its path.\n\n"
        "Be careful not to put any spaces at the end of the path."
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_score_selectFirstMeasure(number_of_bars, selected_score):
    text_de = (
            "Anzahl Takte: " + str(number_of_bars) + " Takte\n\n"
                                                     "Notenauswahl: " + str(selected_score) + "\n\n"
                                                                                              "Taktauswahl ab Takt: [Nr. des Taktes] "
    )

    text_en = (
            "Number of bars: " + str(number_of_bars) + " bars\n\n"
                                                       "Score selection: " + str(selected_score) + "\n\n"
                                                                                                   "Selection starting from bar: [No. of the bar] "
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_score_selectLastMeasure(number_of_bars, selected_score, bars_selection_start):
    text_de = (
            "Anzahl Takte: " + str(number_of_bars) + " Takte\n\n"
                                                     "Notenauswahl: " + str(selected_score) + "\n\n"
                                                                                              "Taktauswahl ab Takt: " + str(
        bars_selection_start) + "\n\n"
                                "Taktauswahl bis einschließlich Takt: "
    )

    text_en = (
            "Number of bars: " + str(number_of_bars) + " bars\n\n"
                                                       "Score selection: " + str(selected_score) + "\n\n"
                                                                                                   "Selection starting from bar: " + str(
        bars_selection_start) + "\n\n"
                                "Selection endling including bar: "
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_score_bars_exception_notNumber():
    text_de = "Bitte eine positive Zahl ohne Buchstaben/Sonderzeichen eingeben."

    text_en = "Please enter a positive number without letters/special characters."

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_score_bars_exception_outOfRange(start, end):
    text_de = (
            "Der eingegebene Wert muss zwischen "
            + str(start)
            + " und "
            + str(end)
            + "liegen."
    )

    text_en = (
            "The entered value must be between " +
            str(start) + " and " + str(end) + "."
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def show_names_individualVoices():
    try:
        utility_clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        print(text_metadata_partsNames())
        print("")

        menu_header = text_headers_entries(sys._getframe().f_code.co_name)

        print("{:<4} {:<65}\n".format(menu_header[0], menu_header[1]))

        Index = 1

        for i in config.global_catalogue_individualParts.keys():
            print("{:<4} {:<65}".format(Index, i))

            Index += 1

        print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    input(text_general_proceed())
    print("")


def show_score_metadata():
    try:
        utility_clear_screen()

        menu_header = text_menu_headers(sys._getframe().f_code.co_name)

        print(menu_header)
        print("")

        loop_done = False

        while not loop_done:
            if len(config.global_score.metadata.all()) > 0:
                print(text_metadata_availableMetadata(
                    len(config.global_score.metadata.all())))
                print("")

                menu_header = text_headers_entries(sys._getframe().f_code.co_name)

                print("{:<4} {:<30} {:<30}\n".format(
                    menu_header[0], menu_header[1], menu_header[2]))

                Index = 1

                for k, v in dict(config.global_score.metadata.all()).items():
                    print("{:<4} {:<30} {:<30}".format(Index, k, v))

                    Index += 1

            else:
                print(text_metadata_availableMetadata_none())
                print("")

            loop_done = True

        print("")

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    input(text_general_proceed())
    print("")


def module_navigation_name_individualVoices():
    list_de = [
        [
            "SHOW: Notenauswahl anzeigen (MuseScore)",
            "visualizations_MuseScore",
            "<Öffnet MuseScore und zeigt die Notenauswahl an>",
        ],
        [
            "NAME: generische Stimmenbezeichnungen",
            "genericDesignations",
            "<Vergabe generischer Stimmenbezeichnungen (Stimme 1, Stimme 2 etc.)>",
        ],
        [
            "NAME: selbstgewählte Stimmenbezeichnungen",
            "customDesignations",
            "<Vergabe selbstgewählter Stimmenbezeichnungen>",
        ],
    ]

    list_en = [
        [
            "SHOW: Show score selection (MuseScore)",
            "visualizations_MuseScore",
            "<Opens MuseScore and displays the selected score>",
        ],
        [
            "NAME: generic voice/part designations",
            "genericDesignations",
            "<Assignment of generic voice/part designations (Part 1, Part 2 etc.)>",
        ],
        [
            "NAME: self-selected voice/part designations",
            "customDesignations",
            "<assignment of self-selected voice/part designations>",
        ],
    ]

    if config.LANGUAGE == "DE":
        return list_de

    elif config.LANGUAGE == "EN":
        return list_en
