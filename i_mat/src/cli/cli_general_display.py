import sys

import i_mat.config as config
from i_mat.src.utils.utils_error_handling import text_exception_general
from i_mat.src.utils.utils_without_userInput import utility_clear_screen





def text_general_checkEntry():
    text_de = "Ist die Eingabe korrekt? (ja/nein): "

    text_en = "Is the entry correct? (yes/no): "

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_general_proceed():
    text_de = "<Um fortzufahren, bitte Eingabe drücken>"

    text_en = "<To continue, please press Enter>"

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_general_input_RestrictedToYesAndNo():
    text_de = (
        "<Eingabe beschränkt auf ja/nein (alternativ: 1/0). Bitte erneut eingeben.>"
    )

    text_en = "<Input restricted to yes/no (alternatively: 1/0). Please re-enter.>"

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_general_input_restrictedToNumbers(input_text):
    text_de = (
            "Fehler: '"
            + input_text
            + "' - Eingabe beschränkt auf Zahlen. Bitte erneut eingeben."
    )

    text_en = "Error: '" + input_text + "' - Input restricted to numbers. Please re-enter."

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_general_close_museScore3():
    text_de = (
        "Hinweis 1: um fortzufahren, bitte MuseScore schließen.\n\n"
        "Hinweis 2: zum Exportieren der Datei als PDF in MuseScore bitte '> Datei > Export...' verwenden.\n\n"
        "WICHTIG: Ladezeit variiert mit Größe der importierten Datei."
    )

    text_en = (
        "Note 1: Please close MuseScore to continue.\n\n"
        "Note 2: to export the file as PDF in MuseScore please use '> File > Export ...'.\n\n"
        "IMPORTANT: Loading time varies with the size of the imported file."
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_general_close_audioPlayer():
    text_de = "Hinweis: um fortzufahren, bitte den Audio-Player schließen."

    text_en = "Note: please close the audio player to continue."

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_general_enter_newPath():
    text_de = "Geben Sie den Pfad/die URL ein: "

    text_en = "Enter Path/URL: "

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_general_show_enteredPath(enteredPath):
    text_de = 'Folgender Pfad/Url wurde eingegeben: "' + str(enteredPath) + '"'

    text_en = 'The following path/URL was entered: "' + str(enteredPath) + '"'

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_general_projectDescription():
    text_de = (
        "Lehrveranstaltungen zur musikalischen Analyse sind an Universitäten und Musikhochschulen ein fester Bestandteil\n"
        "sowohl der musikwissenschaftlichen Studiengänge als auch der Ausbildung von Musiklehrer*innen und Musiker*innen.\n"
        "Ziel des Fellowship-Projektes ist es, unter Rückgriff auf verschiedene computerbasierte Analyse-Tools mehrere\n"
        "flexibel einsetzbare Unterrichtsmodule zur Musikanalyse zu konzipieren, zu erproben, zu evaluieren und zu vermitteln.\n"
        "Die Unterrichtsmodule widmen sich u.a. der computerbasierten Annotation und Visualisierung von Notentexten und\n"
        "Audiodateien, der statistischen Analyse von Musik-Korpora, der Suche nach musikalischen Mustern (Melodien, Rhythmen usw.)\n"
        "Sie sollen herkömmliche Analysekurse ergänzen, wurden bereits in mehreren Lehrveranstaltungen an der HfM Weimar\n"
        "erprobt und evaluiert und werden über diese Internetplattform einem breiteren Interessentenkreis kostenfrei zur\n"
        "Verfügung gestellt. Computer können als Hilfsmittel der Analyse von Notentexten und Musikaufnahmen eingesetzt werden.\n\n"
        "Mit Computerprogrammen können schnell und verlässlich\n\n"
        " - musikalische Abläufe und Strukturen visualisiert,\n"
        " - musikalische Merkmale der betreffenden Stücke (z.B. Häufigkeiten von Tonhöhen) statistisch beschrieben\n"
        " - und nach bestimmten Mustern (z.B. melodischen Motiven) durchsucht werden.\n\n"
        "Dadurch werden herkömmliche Analyseansätze erweitert und neue Perspektiven der musikalischen Analyse in\n"
        "Musikwissenschaft und Musiktheorie eröffnet und erkundet. Zum einen können mit den Computer-Tools gezielt\n"
        "analytischen Fragestellungen weiterverfolgt werden, zum anderen ermöglicht ein spielerischer Umgang mit den\n"
        "Tools und Notendateien ein Entdecken von unerwarteten Zusammenhängen - was dann zu neuen analytischen \n"
        "Fragestellungen führen kann.\n\n"
        "Im Rahmen des Projektes werden Unterrichtmodule und Tutorials (<https://analyse.hfm-weimar.de/doku.php?id=tutorials>\n"
        "bereitgestellt, die anhand von musikanalytischen Fragestellungen in verschiedene Möglichkeiten der computergestützten\n"
        "Analyse von Noten- bzw. Audio-Dateien einführen. Jede Unterrichtsmodule setzt sich aus einem Grundlagen-Modul (Basics)\n"
        "sowie einer Spezialisierung (Advanced) zusammen. Die Unterrichtseinheiten können im Selbststudium oder innerhalb von\n"
        "Lehrveranstaltungen eingesetzt werden. Die Dauer der beiden Unterrichtsmodule beträgt jeweils ca. drei 90-minütige\n"
        "Sitzungen mit zusätzlichen Vorbereitungen, Hausaufgaben und optionalen Vertiefungen.\n\n"
        "Alle in den Unterrichtsmodule verwendete Software (<https://analyse.hfm-weimar.de/doku.php?id=installation>) ist frei\n"
        "zugänglich und lizenzfrei nutzbar. Damit folgt das Projekt dem Prinzip des Open Access, des offenen Zugangs zu\n"
        "öffentlich geförderten Projektergebnissen und der Unabhängigkeit von kommerziell orientierten IT-Konzernen.\n\n"
        "Weitere Informationen zu den Zielsetzungen, Mitarbeiter*innen, Veröffentlichungen des Projekts usw. finden Sie\n"
        "unter 'Das Projekt' (<https://analyse.hfm-weimar.de/doku.php?id=forschung>).\n\n"
        "Das Projekt Computergestützte Musikanalyse in der digitalen Hochschullehre ist am Institut für Musikwissenschaft\n"
        "Weimar-Jena der Hochschule für Musik Franz Liszt Weimar angesiedelt. Es wird gefördert vom Thüringer Ministerium\n"
        "für Wirtschaft, Wissenschaft und Digitalen Wandel und dem Stifterverband. Das Projekt versteht sich als Beitrag\n"
        "zur Computational Musicology bzw. Digital Musicology innerhalb der Digital Humanities.\n\n"
        "Das Projekt befindet sich derzeit in der Testphase. Rückmeldungen sind erwünscht: analyse@hfm-weimar.de\n\n"
        "Impressum:\n\n"
        "Hochschule für Musik Franz Liszt Weimar\n"
        "Institut für Musikwissenschaft Weimar | Jena\n"
        "Hochschulzentrum am Horn\n"
        "Carl-Alexander-Platz 1\n"
        "99425 Weimar\n\n"
    )

    text_en = (
        "Courses on musical analysis are an integral part of both musicology courses and the training of music teachers\n"
        "and musicians at universities and conservatories. The goal of the fellowship project is to design, test, evaluate,\n"
        "and teach several flexibly applicable teaching modules on music analysis, with recourse to various computer-based\n"
        "analysis tools. The teaching modules are dedicated to computer-based annotation and visualization of musical texts\n"
        "and audio files, statistical analysis of music corpora, and search for musical patterns (melodies, rhythms etc.).\n"
        "They are intended to complement conventional analysis courses, have been and evaluated within several courses at the HfM\n"
        "Weimar, and will are publicly available to a wider circle of interested parties via this Internet platform.\n\n"
        "Computers can be used as aids in the analysis of musical texts and recordings.\n\n"
        "Computer programs can be used to quickly and reliably\n\n"
        " - visualize musical sequences and structures,\n"
        " - statistically describe musical characteristics of the pieces in question (e.g. frequencies of pitches)\n"
        " - and searched for specific patterns (e.g. melodic motifs).\n\n"
        "This extends conventional approaches to analysis and opens up and explores new perspectives of musical analysis\n"
        "in musicology and music theory. On the one hand, the computer tools can be used to pursue specific analytical questions,\n"
        "and on the other hand, a playful approach to the tools and note files enables the discovery of unexpected\n"
        "relationships - which can then lead to new analytical questions.\n\n"
        "The Teaching modules and tutorials (<https://analyse.hfm-weimar.de/doku.php?id=en:tutorials>) are provided that\n"
        "introduce various possibilities of computer-assisted analysis of sheet music or audio files on the basis of\n"
        "music-analytical issues. Each teaching unit consists of a basic module(Basics Sheet Music or Basics Audio)\n"
        "and a specialization (Advanced). The teaching units can be used in self-study or within courses. The duration\n"
        "of the teaching units is approximately three sessions of 90-minutes, with additional preparation, homework\n"
        "and optional specializations.\n\n"
        "All software (<https://analyse.hfm-weimar.de/doku.php?id=en:installation>) used in the teaching units is freely\n"
        "accessible and license-free. Thus, the project follows the principle of open access - open access to publicly\n"
        "funded project results and independence from commercially oriented IT corporations.\n\n"
        "The project Computergestützte Musikanalyse in der digitalen Hochschullehre (computer-aided music analysis\n"
        "within digital higher education) is located at the Institute of Musicology Weimar-Jena of the Franz Liszt University\n"
        "of Music Weimar. It is funded by the Thuringian Ministry for Economy, Science and Digital Change and the Stifterverband.\n"
        "The project sees itself as a contribution to Computational Musicology or Digital Musicology within Digital Humanities.\n\n"
        "Further information about the project's objectives, staff etc. can be found on\n\n"
        " -> 'The project' (<https://analyse.hfm-weimar.de/doku.php?id=en:research>).\n\n"
        "The project is currently in the test phase. Feedback is welcome: analyse@hfm-weimar.de\n\n"
        "Imprint:\n\n"
        "University of Music Franz Liszt Weimar\n"
        "Institute for Musicology Weimar | Jena\n"
        "University Center at the Horn\n"
        "Carl-Alexander-Platz 1\n"
        "99425 Weimar\n\n"
    )

    try:
        if config.LANGUAGE == "DE":
            utility_clear_screen()

            print(text_de)

        elif config.LANGUAGE == "EN":
            utility_clear_screen()

            print(text_en)

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    input(text_general_proceed())
    print("")


def text_general_chooseKey():
    text_de = "Wählen Sie im nachfolgenden Auswahlmenü die Tonart des ausgewählten Notenabschnittes aus."

    text_en = "Please select the key of the selected score section in the following selection menu."

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_general_exportToDiagrammUnavailable():
    text_de = "Für dieses previousTool ist ein Datenexport als Grafikdiagramm nicht vorgesehen."

    text_en = "data_values export as a graphic is not intended for this tool."

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_general_noResults():
    text_de = "Fehler: Die Auswertung der Notendatei lieferte keine Ergebnisse."

    text_en = "Error: The analysis of the score file did not produce any results."

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_display_showScoreSelection():
    text_de = "Möchten Sie den ausgewählten/eingegebenen Notentext anzeigen lassen? (ja/nein): "

    text_en = "Would you like to display the selected/entered music text? (yes/no): "

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_export_fileName():
    text_de = "Unter welchem Namen soll die Datei gespeichert werden? filename: "

    text_en = "Under what name should the file be saved? Filename: "

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_general_terminateProgram():
    text_de = "<Um das Programm zu beenden, bitte Eingabe drücken>"

    text_en = "<To terminate the program, please press Enter>"

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_general_exportSuccessful(path, filename, extension):
    text_de = (
            "Die Datei wurde erfolgreich gespeichert.\n\n"
            "Speicherort: " + str(path) + "\n\n"
                                          "filename: " + str(filename) + str(extension)
    )

    text_en = (
            "The file was saved successfully.\n\n"
            "Location: " + str(path) + "\n\n"
                                       "Filename: " + str(filename) + str(extension)
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_general_exportGraph(path):
    text_de = (
            "Die Datei wurde erfolgreich gespeichert.\n\n"
            "Speicherort: " + str(path) + "\n\n"
                                          "Um fortfahren zu können, müssen Sie eventuell die sich soeben geöffneten Grafikansichten schließen."
    )

    text_en = (
            "The file was saved successfully.\n\n"
            "Location: " + str(path) + "\n\n"
                                       "In order to be able to continue, you may have to close the graphic views that have just opened."
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_general_exportGraphName():
    text_de = (
        "Bitte wählen Sie einen Titel für das zu exportierende Grafikdiagramm aus: "
    )

    text_en = "Please select a title for the graphic diagram to be exported: "

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en
