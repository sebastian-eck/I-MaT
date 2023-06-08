import sys

from music21 import environment

import i_mat.config as config
from i_mat.src.utils.utils_error_handling import text_exception_general


def environment_list():
    try:

        us = environment.UserSettings()

        environmentFile_settings = [
            ["autoDownload", "autoDownload", str(us["autoDownload"])],
            ["braillePath", "braillePath", str(us["braillePath"])],
            ["debug", "debug", str(us["debug"])],
            ["directoryScratch", "directoryScratch", str(us["directoryScratch"])],
            ["graphicsPath", "graphicsPath", str(us["graphicsPath"])],
            ["ipythonShowFormat", "ipythonShowFormat", str(us["ipythonShowFormat"])],
            ["lilypondBackend", "lilypondBackend", str(us["lilypondBackend"])],
            ["lilypondFormat", "lilypondFormat", str(us["lilypondFormat"])],
            ["lilypondPath", "lilypondPath", str(us["lilypondPath"])],
            ["lilypondVersion", "lilypondVersion", str(us["lilypondVersion"])],
            ["localCorporaSettings", "localCorporaSettings", str(us["localCorporaSettings"])],
            ["localCorpusPath", "localCorpusPath", str(us["localCorpusPath"])],
            ["localCorpusSettings", "localCorpusSettings", str(us["localCorpusSettings"])],
            ["manualCoreCorpusPath", "manualCoreCorpusPath", str(us["manualCoreCorpusPath"])],
            ["midiPath", "midiPath", str(us["midiPath"])],
            ["musescoreDirectPNGPath", "musescoreDirectPNGPath", str(us["musescoreDirectPNGPath"])],
            ["musicxmlPath", "musicxmlPath", str(us["musicxmlPath"])],
            ["pdfPath", "pdfPath", str(us["pdfPath"])],
            ["showFormat", "showFormat", str(us["showFormat"])],
            ["vectorPath", "vectorPath", str(us["vectorPath"])],
            ["warnings", "warnings", str(us["warnings"])],
            ["writeFormat", "writeFormat", str(us["writeFormat"])],
        ]

        return environmentFile_settings

    except Exception as e:
        print(text_exception_general(e, sys._getframe().f_code.co_name))
        print("")

    # #### Modul-Navigation


def module_navigation_entries():
    list_de = [
        [
            "REPT: Neue Notenauswahl",
            "repeatSelection",
            "<Wiederholung des Tools mit neuer Notenauswahl>",
        ],
        [
            "EXPT: Ergebnisse als CSV-Datei exportieren",
            "export_CSV",
            "<Exportiert und speichert die Ergebnisse als CSV-Datei>",
        ],
        [
            "GRPH: Ergebnisse als Grafik anzeigen",
            "export_visualization",
            "<Exportiert und speichert die Ergebnisse als Grafik>",
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
            "EXPT: Export results as CSV file",
            "export_CSV",
            "<Exports and saves the results as CSV file>",
        ],
        [
            "GRPH: Display results as graphic",
            "export_visualization",
            "<Exports and saves the results as graphic>",
        ],
        ["BACK: Back to the main menu", "return", "<Return to the main menu>"],
    ]

    if config.LANGUAGE == "DE":
        return list_de

    elif config.LANGUAGE == "EN":
        return list_en


def module_navigation_selectedScore():
    list_de = [
        [
            "Notenauswahl: vollständige Partitur",
            "completeScore",
            "<Auswahl der gesamten Partitur>",
        ],
        [
            "Notenauswahl: Taktausschnitt (Stimme/Partitur)",
            "newSelection",
            "<Taktauswahl aus der Partitur oder einer Einzelstimme>",
        ],
        [
            "Notenauswahl: vorherige Auswahl wiederholen",
            "repeatPreviousSelection",
            "<Wiederholung der letzten Notenauswahl>",
        ],
    ]

    list_en = [
        [
            "Score selection: complete score",
            "completeScore",
            "<Selection of the entire score>",
        ],
        [
            "Score selection: bar excerpt (part / score)",
            "newSelection",
            "<bar selection from the score or a single part>",
        ],
        [
            "Score selection: repeat previous selection",
            "repeatPreviousSelection",
            "<Repeat last score selection>",
        ],
    ]

    if config.LANGUAGE == "DE":
        return list_de

    elif config.LANGUAGE == "EN":
        return list_en


def module_navigation_conversion():
    list_de = [
        [
            "XML : Konvertierung nach .xml",
            "XML",
            "<Konvertiert die Datei ins .xml-Format>",
        ],
        [
            "XML : Konvertierung nach .xml",
            "XML_chords",
            "<Konvertiert die Datei ins .xml-Format (Transformation zu Akkordverbindungen)>",
        ],
        [
            "XML : Konvertierung nach .xml",
            "XML_chords_figuredBass",
            "<Konvertiert die Datei ins .xml-Format (Transformation zu Akkordverbindungen + Generalbass>",
        ],
        [
            "XML : Konvertierung nach .xml",
            "XML_chords_romanNumerals",
            "<Konvertiert die Datei ins .xml-Format (Transformation zu Akkordverbindungen + Stufenbezifferung)>",
        ],
        [
            "MIDI: Konvertierung nach .midi",
            "MIDI",
            "<Konvertiert die Datei ins .midi-Format>",
        ],
        [
            "BRLL: Konvertierung nach .txt (music21)",
            "TXT_music21",
            "<Exportiert die Notenauswahl im music21-Format als .txt-Datei>",
        ],
        [
            "BRLL: Konvertierung nach .txt (music21/textline)",
            "TXT_music21_textline",
            "<Exportiert die Notenauswahl im music21-Format als .txt-Datei (textline)>",
        ],
        [
            "BRLL: Konvertierung nach .txt (Braille)",
            "TXT_braille",
            "<Speichert die Datei im .txt-Braille-Format>",
        ],
        [
            "LILY: Konvertierung nach .ly (LilyPond)",
            "lilypond",
            "<Konvertiert die Datei ins .ly-Format>",
        ],
        [
            "PDF : Als PDF exportieren",
            "PDF",
            "<Speichert die Datei im .pdf-Format. Setzt eine Installation von Lilypond voraus!>",
        ],
        [
            "PNG : Als PNG exportieren",
            "PNG",
            "<Speichert die Datei im .png-Format. Setzt eine Installation von Lilypond voraus!>",
        ],
        ["BACK: Zurück ins Hauptmenü", "return", "<Rückkehr ins Hauptmenü>"],
    ]

    list_en = [
        ["XML : Conversion to .xml", "XML", "<Converts the file to .xml format>"],
        [
            "XML : conversion to .xml",
            "XML_chords",
            "<Converts the file to .xml format (transformation to chord connections)>",
        ],
        [
            "XML : conversion to .xml",
            "XML_chords_figuredBass",
            "<Converts the file to .xml format (transformation to chord connections + figured bass>",
        ],
        [
            "XML : conversion to .xml",
            "XML_chords_romanNumerals",
            "<Converts the file to .xml format (transformation to chord connections + numbering of levels)>",
        ],
        ["MIDI: Conversion to .midi", "MIDI",
         "<Converts the file to .midi format>"],
        [
            "BRLL: Conversion to .txt (music21)",
            "TXT_music21",
            "<Exports the note selection in music21 format as a .txt file>",
        ],
        [
            "BRLL: Conversion to .txt (music21 / textline)",
            "TXT_music21_textline",
            "<Exports the sheet music selection in music21 format as a .txt file (textline)>",
        ],
        [
            "BRLL: Conversion to .txt (Braille)",
            "TXT_braille",
            "<Saves the file in .txt Braille format>",
        ],
        [
            "LILY: Conversion to .ly (LilyPond)",
            "lilypond",
            "<Converts the file to .ly format>",
        ],
        [
            "PDF : Export as PDF",
            "PDF",
            "<Saves the file in .pdf format. Requires an installation of Lilypond!> ",
        ],
        [
            "PNG : Export as PNG",
            "PNG",
            "<Saves the file in .png format. Requires an installation of Lilypond!> ",
        ],
        ["BACK: Back to the main menu", "return", "<Return to the main menu>"],
    ]

    if config.LANGUAGE == "DE":
        return list_de

    elif config.LANGUAGE == "EN":
        return list_en
