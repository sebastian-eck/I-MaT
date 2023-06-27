import music21
from music21 import environment, roman
from tqdm import tqdm

from src.cli.menu_constructors import display_menu_print_textblock, display_menu_request_selection
from src.constants import KEYS_LIST
from src.utils.error_handling import handle_error


def play_midi_score(selected_score):
    """
    Plays the selected score in MIDI format and prints the directory where it's exported.

    Parameters
    ----------
    selected_score : music21 stream
        Music21 stream object of the selected score.
    """
    try:
        selected_score.show("midi")
        display_file_export_directory()

    except Exception as e:
        handle_error(e)


def show_musescore(selected_score):
    """
    Shows the selected score in MuseScore and prints the directory where it's exported.

    Parameters
    ----------
    selected_score : music21 stream
        Music21 stream object of the selected score.
    """
    try:
        message = {
            "menu_displayed_text": [
                "Notice",
                "Please read the following message:",
                "<To open the program, please press Enter>",
                ["", "Message"],
            ],
            "menu_entries_text": [
                ["Message 1", "The program used to view the sheet music probably needs to be closed in order to "
                              "continue with the tool."]
            ]
        }
        display_menu_print_textblock(message)

        print("\nRendering the score. This might take some time...")

        selected_score.show()
        display_file_export_directory()

    except Exception as e:
        handle_error(e)


def show_chord_connections(selected_score):
    """
    Shows chord connections of the selected score and prints the directory where it's exported.

    Parameters
    ----------
    selected_score : music21 stream
        Music21 stream object of the selected score.
    """
    try:
        selected_score_chord_connections = selected_score.chordify()

        message = {
            "menu_displayed_text": [
                "Notice",
                "Please read the following message:",
                "<To open the program, please press Enter>",
                ["", "Message"],
            ],
            "menu_entries_text": [
                ["Message 1", "The program used to view the sheet music probably needs to be closed in order to "
                              "continue with the tool."]
            ]
        }
        display_menu_print_textblock(message)

        print("\nRendering the score. This might take some time...")

        selected_score_chord_connections.show()
        display_file_export_directory()

    except Exception as e:
        handle_error(e)


# Function to show figured bass
def show_figured_bass(selected_score):
    """
    Shows figured bass notation of the selected score and prints the directory where it's exported.

    Parameters
    ----------
    selected_score : music21 stream
        Music21 stream object of the selected score.
    """
    try:
        selected_score_chord_connections = selected_score.chordify()
        chords = list(selected_score_chord_connections.recurse().getElementsByClass("Chord"))

        for item in tqdm(chords, desc="Processing chords..."):
            item.closedPosition(forceOctave=4, inPlace=True)
            item.annotateIntervals()

        message = {
            "menu_displayed_text": [
                "Notice",
                "Please read the following message:",
                "<To open the program, please press Enter>",
                ["", "Message"],
            ],
            "menu_entries_text": [
                ["Message 1", "The program used to view the sheet music probably needs to be closed in order to "
                              "continue with the tool."]
            ]
        }
        display_menu_print_textblock(message)

        print("\nRendering the score. This might take some time...")
        selected_score_chord_connections.show()

        display_file_export_directory()

    except Exception as e:
        handle_error(e)


def show_chord_scale_system(selected_score):
    """
    Shows chord-scale system of the selected score and prints the directory where it's exported.

    Parameters
    ----------
    selected_score : music21 stream
        Music21 stream object of the selected score.
    """
    try:
        imat_data_container = {
            "menu_displayed_text": [
                "Key Selection Menu",
                "Please select a key from the following options by entering the corresponding index number:",
                "Which key do you want to select? (<No. of key item>): ",
                ["Key name", "<Key>"],
            ],
            "menu_entries": [[f"{key[0]}", key[1]] for key in KEYS_LIST]
        }

        selected_key = display_menu_request_selection(imat_data_container)

        selected_score_chord_connections = selected_score.chordify()
        chords = list(selected_score_chord_connections.recurse().getElementsByClass("Chord"))

        for item in tqdm(chords, desc="Processing chords..."):
            rn = roman.romanNumeralFromChord(item, music21.key.Key(selected_key))
            item.addLyric(str(rn.figure))

        message = {
            "menu_displayed_text": [
                "Notice",
                "Please read the following message:",
                "<To open the program, please press Enter>",
                ["", "Message"],
            ],
            "menu_entries_text": [
                ["Message 1", "The program used to view the sheet music probably needs to be closed in order to "
                              "continue"
                              "with the tool."]
            ]
        }
        display_menu_print_textblock(message)

        print("\nRendering the score. This might take some time...")

        selected_score_chord_connections.show()
        display_file_export_directory()

    except Exception as e:
        handle_error(e)



def show_pianoroll(selected_score):
    """
    Shows a pianoroll view of the selected score and prints the directory where it's exported.

    Parameters
    ----------
    selected_score : music21 stream
        Music21 stream object of the selected score.
    """
    try:
        selected_score_stripTies = selected_score.stripTies()

        print("\nRendering the graph. This might take some time...")

        selected_score_stripTies.plot('pianoroll')

        print("\nRendering complete. You can close the windows safely now that might have been displayed.")

        display_file_export_directory()

    except Exception as e:
        handle_error(e)


def show_voice_progression(selected_score):
    """
    Shows voice progression of the selected score and prints the directory where it's exported.

    Parameters
    ----------
    selected_score : music21 stream
        Music21 stream object of the selected score.
    """
    try:
        selected_score_stripTies = selected_score.stripTies()

        print("\nRendering the graph. This might take some time...")

        selected_score_stripTies.plot('horizontalbar')

        print("\nRendering complete. You can close the windows safely now that might have been displayed.")

        display_file_export_directory()

    except Exception as e:
        handle_error(e)


def show_volume_change(selected_score):
    """
    Shows volume change over time of the selected score and prints the directory where it's exported.

    Parameters
    ----------
    selected_score : music21 stream
        Music21 stream object of the selected score.
    """
    try:
        selected_score_stripTies = selected_score.stripTies()

        print("\nRendering the graph. This might take some time...")

        selected_score_stripTies.plot('horizontalbarweighted')

        print("\nRendering complete. You can close the windows safely now that might have been displayed.")

        display_file_export_directory()

    except Exception as e:
        handle_error(e)


def show_key_analysis(selected_score):
    """
    Shows key analysis of the selected score and prints the directory where it's exported.

    Parameters
    ----------
    selected_score : music21 stream
        Music21 stream object of the selected score.
    """
    try:
        selected_score_stripTies = selected_score.stripTies()

        print("\nRendering the graph. This might take some time...")

        selected_score_stripTies.plot('colorgrid')

        print("\nRendering complete. You can close the windows safely now that might have been displayed.")

        display_file_export_directory()

    except Exception as e:
        handle_error(e)


def display_file_export_directory():
    """
    Prints the directory where the files are exported and waits for the user to press enter to continue.
    """
    try:
        dir_scratch = environment.UserSettings()["directoryScratch"]

        print(f"\nFile exported to the directory: {dir_scratch}\n")
        input("<To continue, please press Enter>")

    except Exception as e:
        handle_error(e)
