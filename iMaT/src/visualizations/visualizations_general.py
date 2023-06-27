import music21
from music21 import environment, roman

from src.cli.cli_menu_structures import display_menu_request_selection
from src.constants import keys_list


def play_midi_score(selected_score):
    """
    Plays the selected score in MIDI format and prints the directory where it's exported.

    Parameters
    ----------
    selected_score : music21 stream
        Music21 stream object of the selected score.
    """
    selected_score.show("midi")
    export_directory()


def show_musescore(selected_score):
    """
    Shows the selected score in MuseScore and prints the directory where it's exported.

    Parameters
    ----------
    selected_score : music21 stream
        Music21 stream object of the selected score.
    """
    selected_score.show()
    export_directory()


def show_chord_connections(selected_score):
    """
    Shows chord connections of the selected score and prints the directory where it's exported.

    Parameters
    ----------
    selected_score : music21 stream
        Music21 stream object of the selected score.
    """
    selected_score_chord_connections = selected_score.chordify()
    selected_score_chord_connections.show()
    export_directory()


# Function to show figured bass
def show_figured_bass(selected_score):
    """
    Shows figured bass notation of the selected score and prints the directory where it's exported.

    Parameters
    ----------
    selected_score : music21 stream
        Music21 stream object of the selected score.
    """
    selected_score_chord_connections = selected_score.chordify()
    for item in selected_score_chord_connections.recurse().getElementsByClass("Chord"):
        item.closedPosition(forceOctave=4, inPlace=True)

        item.annotateIntervals()

    selected_score_chord_connections.show()
    export_directory()


def show_chord_scale_system(selected_score):
    """
    Shows chord-scale system of the selected score and prints the directory where it's exported.

    Parameters
    ----------
    selected_score : music21 stream
        Music21 stream object of the selected score.
    """
    imat_data_container = {
        "menu_displayed_text": [
            "Key Selection Menu",
            "Please select a key from the following options by entering the corresponding index number:",
            "Which key do you want to select? (<No. of key item>): ",
            ["Key name", "<Key>"],
        ],
        "menu_entries": [[f"{key[0]}", key[1]] for key in keys_list]
    }

    selected_key = display_menu_request_selection(imat_data_container)

    selected_score_chord_connections = selected_score.chordify()

    for item in selected_score_chord_connections.recurse().getElementsByClass("Chord"):
        rn = roman.romanNumeralFromChord(item, music21.key.Key(selected_key))
        item.addLyric(str(rn.figure))

    selected_score_chord_connections.show()
    export_directory()


def show_pianoroll(selected_score):
    """
    Shows a pianoroll view of the selected score and prints the directory where it's exported.

    Parameters
    ----------
    selected_score : music21 stream
        Music21 stream object of the selected score.
    """
    selected_score_stripTies = selected_score.stripTies()

    selected_score_stripTies.plot('pianoroll')
    export_directory()


def show_voice_progression(selected_score):
    """
    Shows voice progression of the selected score and prints the directory where it's exported.

    Parameters
    ----------
    selected_score : music21 stream
        Music21 stream object of the selected score.
    """
    selected_score_stripTies = selected_score.stripTies()

    selected_score_stripTies.plot('horizontalbar')
    export_directory()


def show_volume_change(selected_score):
    """
    Shows volume change over time of the selected score and prints the directory where it's exported.

    Parameters
    ----------
    selected_score : music21 stream
        Music21 stream object of the selected score.
    """
    selected_score_stripTies = selected_score.stripTies()

    selected_score_stripTies.plot('horizontalbarweighted')
    export_directory()


def show_key_analysis(selected_score):
    """
    Shows key analysis of the selected score and prints the directory where it's exported.

    Parameters
    ----------
    selected_score : music21 stream
        Music21 stream object of the selected score.
    """
    selected_score_stripTies = selected_score.stripTies()

    selected_score_stripTies.plot('colorgrid')
    export_directory()

def export_directory():
    """
    Prints the directory where the files are exported and waits for the user to press enter to continue.
    """
    dir_scratch = environment.UserSettings()["directoryScratch"]

    print(f"\nFile exported to the directory: {dir_scratch}\n")
    input("<To continue, please press Enter>")
