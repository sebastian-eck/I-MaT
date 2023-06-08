import i_mat.config as config
from i_mat.src.cli.cli_general_display import text_general_proceed
from i_mat.src.utils.utils_without_userInput import utility_clear_screen


def text_menu_exception_selectionOutOfRange(max_value):
    text_de = (
            "Der eingegebene Wert muss eine Zahl zwischen 1 und "
            + str(max_value)
            + " sein."
    )

    text_en = (
            "The entered value must be a number between 1 and " +
            str(max_value) + "."
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_metadata_partsNames():
    text_de = "Namen der Einzelstimmen:"

    text_en = "Names of the individual parts/voices:"

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_metadata_partsNames_chooseName(parts_quantity, part_number):
    text_de = (
            "Die Partitur enthält " + str(parts_quantity) + " Stimmen.\n\n"
                                                            "Bitte ordnen Sie den Einzelstimmen eindeutige Bezeichnungen zu (z.B. Violine I, Violine II etc.).\n\n"
                                                            "Über diese Namen greifen Sie bei Verwendung der nachfolgenden Tools direkt auf die jeweiligen Einzelstimmen zu.\n\n"
                                                            "Beginnen Sie bitte bei der höchsten Stimme im Notensystem. Es folgt dann jeweils die im Notensystem direkt darunterliegende.\n\n"
                                                            "Benenne Stimme " + str(part_number) + ": "
    )

    text_en = (
            "The score contains " + str(parts_quantity) + " parts.\n\n"
                                                          "Please assign unique names to the individual parts/voices (e.g. violin I, violin II, etc.).\n\n"
                                                          "You can use these names to access the individual parts/voices directly when using the following tools.\n\n"
                                                          "Please start with the highest voice/part in the staff. This is followed by the one directly below.\n\n"
                                                          "Name part " + str(part_number) + ": "
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_metadata_partsNames_chooseName_notUnique():
    text_de = "Name bereits vergeben. Wählen Sie einen eindeutigen Namen."

    text_en = "Name already given. Choose a unique name."

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_metadata_partsNames_checkEnteredName(
        parts_quantity, part_number, name_entered
):
    text_de = (
            "Die Partitur enthält " + str(parts_quantity) + " Stimmen.\n\n"
            "Bitte ordnen Sie den Einzelstimmen eindeutige Bezeichnungen zu (z.B. Violine I, Violine II etc.).\n\n"
            "Über diese Namen greifen Sie bei Verwendung der nachfolgenden Tools direkt auf die jeweiligen Einzelstimmen zu.\n\n"
            "Beginnen Sie bitte bei der höchsten Stimme im Notensystem. Es folgt dann jeweils die im Notensystem direkt darunterliegende.\n\n"
            "Stimme " + str(part_number) + ": " + str(name_entered)
    )

    text_en = (
            "The score contains " + str(parts_quantity) + " parts.\n\n"
            "Please assign unique names to the individual parts/voices (e.g. violin I, violin II, etc.).\n\n"
            "You can use these names to access the individual parts/voices directly when using the following tools.\n\n"
            "Please start with the highest voice/part in the score. This is followed by the one directly below.\n\n"
            "Part " + str(part_number) + ": " + str(name_entered)
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_metadata_availableMetadata(number):
    text_de = "Anzahl enthaltener Metadaten: " + str(number)

    text_en = "Number of metadata contained: " + str(number)

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_metadata_availableMetadata_none():
    text_de = "Die ausgewählte Notendatei enthält keine Metadaten!"

    text_en = "The selected scores do not contain any metadata!"

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_analysis_scoreSelection():
    list_de = [
        "Wählen Sie bitte im nachfolgenden Menü die zu analysierenden Noten aus (Notendatei 1).",
        "Wählen Sie bitte im nachfolgenden Menü die zu analysierenden Noten aus (Notendatei 2)",
    ]

    list_en = [
        "Please select the scores to be analyzed in the following menu (scores file 1).",
        "Please select the scores to be analyzed in the following menu (scores file 2).",
    ]

    if config.LANGUAGE == "DE":
        return list_de

    elif config.LANGUAGE == "EN":
        return list_en


def text_analysis_measures():
    text_de = "T. "

    text_en = "Meas. "

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_analysis_notes_intervals():
    text_de = "Hinweis 1: Auf- und absteigende Intervalle werden gesondert gezählt.\nHinweis 2: Intervalle, zwischen denen Pausen stehen werden nicht mitgezählt."

    text_en = "Note 1: ascending and descending intervals are counted separately. Note 2: Intervals between which there are rests are not counted."

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_analysis_notes_melody_melodicProgression_visualization_lineGraph():
    text_de = (
        "Hinweis 1: Auswahl auf einzelne Taktausschnitte der vollständigen Partitur beschränkt.\n\n"
        "Hinweis 2: Die ausgewählten Abschnitte müssen in allen Einzelstimmen durchgängig einstimmig sein!\n\n"
        "Hinweis 3: Die Taktauswahl muss mindestens zwei Takte umfassen!"
    )

    text_en = (
        "Note 1: Selection limited to individual bar excerpts from the full score.\n\n"
        "Note 2: The selected sections must be consistently monodic in all individual parts/voices!\n\n"
        "Note 3: The measure selection must include at least two measures!"
    )

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def text_analysis_notes_predefinedVisualizations_Dolan():
    text_de = "Hinweis: Bei manchen Notendateien gelten die Dynamikbezeichnungen einer Stimme für die komplette Partitur."

    text_en = "Note: With some sheet music files, the dynamics of a part apply to the entire score."

    if config.LANGUAGE == "DE":
        return text_de

    elif config.LANGUAGE == "EN":
        return text_en


def start_printText():
    utility_clear_screen()

    text = (
        "Funding period: one year; Start: January 1, 2021\n\n"
        "Funded by the Stifterverband together with the Thuringian Ministry of Economics,\n"
        "Science and Digital Society as part of the fellowship program for innovations in digital university teaching.\n\n"
        "-- Project team --\n\n\n"
        "-- Project management  --\n\n"
        "{:<50} {}\n\n".format(
            "Prof. Dr. Martin Pfleiderer", "<martin.pfleiderer@hfm-weimar.de>"
        ),
        "Institute for Musicology Weimar-Jena - University of Music FRANZ LISZT Weimar\n\n",
        "-- Scientific Assistants --\n\n",
        "{:<50} {}\n".format("Egor Polyakov", "<egor.polyakov@hfm-weimar.de>"),
        "{:<50} {}\n\n".format("Christon-Ragavan Nadar", ""),
        "-- Student staff --\n\n",
        "{:<50} {}\n".format("Sebastian Oliver Eck",
                             "<sebastian.eck@hfm.uni-weimar.de>"),
        "{:<50} {}\n".format("Juan Sebastián Paez Medina",
                             "<juan.sebastian.paez.medina@hfm.uni-weimar.de>"),
        "{:<50} {}\n".format("Andres Romero Varon",
                             "<andres.romero.varon@hfm.uni-weimar.de>"),
        "{:<50} {}\n".format("Esther Johanna Barta", ""),
        "{:<50} {}\n\n".format("Clarissa Henriette Mühlhausen", ""),
        "-- Program code --\n\n",
        "{:<50} {}\n\n".format("Sebastian Oliver Eck",
                               "<sebastian.eck@hfm.uni-weimar.de>"),
        "-- Search routines --\n\n",
        "{:<50} {}\n".format("Sebastian Oliver Eck",
                             "<sebastian.eck@hfm.uni-weimar.de>"),
        "{:<50} {}\n".format("Juan Sebastián Paez Medina",
                             "<juan.sebastian.paez.medina@hfm.uni-weimar.de>"),
        "{:<50} {}\n".format("Andres Romero Varon",
                             "<andres.romero.varon@hfm.uni-weimar.de>"),
        "{:<50} {}\n".format("Egor Polyakov", "<egor.polyakov@hfm-weimar.de>"),
        "{:<50} {}\n\n".format("Christon-Ragavan Nadar", ""),
        "Using Music21 (MIT, Massachusetts, Cambridge, USA): [https://web.mit.edu/music21/]\n\n",
        "<Please use the program in full screen mode if possible>\n\n"
    )

    print("".join(text))
    input(text_general_proceed())

    utility_clear_screen()
