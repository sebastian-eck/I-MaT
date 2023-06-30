"""
pattern_search.functions.py
===========================

This module contains the functions to search for specific musical patterns in a given score.
The search can be performed with various combinations of considerations for transposition and rhythm.
There are a total of six functions provided for the search.

The module depends on the pandas and music21 libraries for data manipulation and musical score parsing.

Functions
---------
- 'pattern_search_without_transposition_without_rhythm': Search for a specific musical pattern in a score without considering transposition and rhythm.
- 'pattern_search_with_transposition_without_rhythm': Search for a specific musical pattern in a score considering transposition but not rhythm.
- 'pattern_search_without_transposition_with_rhythm': Search for a specific musical pattern in a score considering rhythm but not transposition.
- 'pattern_search_with_transposition_with_rhythm': Search for a specific musical pattern in a score considering both transposition and rhythm.
- 'pattern_search_only_rhythm': Search for a specific musical pattern in a score considering only rhythm.

Examples
--------
For usage examples, refer to the individual function docstrings.

"""
import pandas as pd
from music21 import search

from src.utils.error_handling import handle_error


def pattern_search_without_transposition_without_rhythm(identifier, selected_score_deepcopy,
                                                        search_pattern, search_pattern_clear_names):
    """
    Search for a specific musical pattern in a score without considering transposition and rhythm.

    Parameters
    ----------
    identifier : str
        Identifier for the selected score.
    selected_score_deepcopy : music21.stream.Stream
        A deep copy of the selected musical score.
    search_pattern : list
        A list representing the musical pattern to be searched.
    search_pattern_clear_names : list
        A list of clear names for the search pattern.

    Returns
    -------
    pandas.DataFrame
        A dataframe containing the search results.

    Examples
    --------
    >>> identifier = "example_score"
    >>> selected_score = music21.converter.parse("example_score.mxl")
    >>> selected_score_deepcopy = copy.deepcopy(selected_score)
    >>> search_pattern = ["C4", "E4", "G4"]
    >>> search_pattern_clear_names = ["C", "E", "G"]
    >>> pattern_search_without_transposition_without_rhythm(identifier, selected_score_deepcopy, search_pattern, search_pattern_clear_names)
    """
    pattern_search_hits = search.noteNameSearch(selected_score_deepcopy, search_pattern)

    pattern_search_hits_result_list = []
    no_results_list = []

    for note_position in pattern_search_hits:
        startingNote = selected_score_deepcopy[note_position]
        startingMeasure = startingNote.measureNumber
        startingBeat = startingNote.beat
        startingPart = startingNote.getContextByClass("Part")

        pattern_search_hits_result_list.append(
            [
                identifier,
                startingNote.nameWithOctave,
                startingMeasure,
                startingBeat,
                startingPart.id,
                str(search_pattern_clear_names),
            ]
        )

    no_results_list.append(
        [
            identifier,
            "- No Matches Found -",
            "- No Matches Found -",
            "- No Matches Found -",
            "- No Matches Found -",
            str(search_pattern_clear_names)
        ]
    )

    header_titles = ["Selected Score", "Pattern Starting Pitch", "Measure", "Beat", "Part/Voice", "Search Pattern"]

    if len(pattern_search_hits_result_list) == 0:

        return pd.DataFrame(no_results_list, columns=header_titles)

    else:

        return pd.DataFrame(pattern_search_hits_result_list, columns=header_titles)


def pattern_search_with_transposition_without_rhythm(identifier, selected_score_deepcopy,
                                                     search_pattern, search_pattern_clear_names):
    """
    Search for a specific musical pattern in a score considering transposition but not rhythm.

    Parameters
    ----------
    identifier : str
        Identifier for the selected score.
    selected_score_deepcopy : music21.stream.Stream
        A deep copy of the selected musical score.
    search_pattern : list
        A list representing the musical pattern to be searched.
    search_pattern_clear_names : list
        A list of clear names for the search pattern.

    Returns
    -------
    pandas.DataFrame
        A dataframe containing the search results.

    Examples
    --------
    >>> identifier = "example_score"
    >>> selected_score = music21.converter.parse("example_score.mxl")
    >>> selected_score_deepcopy = copy.deepcopy(selected_score)
    >>> search_pattern = ["C4", "E4", "G4"]
    >>> search_pattern_clear_names = ["C", "E", "G"]
    >>> pattern_search_with_transposition_without_rhythm(identifier, selected_score_deepcopy, search_pattern, search_pattern_clear_names)
    """
    def pitch_class_equal(n1, n2):
        try:
            if not hasattr(n1, "pitch"):
                return False
            if not hasattr(n2, "pitch"):
                return False
            if n1.pitch.pitchClass == n2.pitch.pitchClass:
                return True
            else:
                return False

        except Exception as e:
            handle_error(e)

    try:
        pattern_search_hits = []
        iteration = 1

        pattern_search_hits_result_list = []
        no_results_list = []

        for n in range(12):  # Search 12 times (= through all notes in one octave)
            iteration_search_pattern = [pattern_note.name for pattern_note in search_pattern]
            iteration_search_pattern_hit = search.streamSearchBase(selected_score_deepcopy, search_pattern,
                                                                   algorithm=pitch_class_equal)
            for note_position in iteration_search_pattern_hit:
                startingNote = selected_score_deepcopy[note_position]
                startingMeasure = startingNote.measureNumber
                startingBeat = startingNote.beat
                startingPart = startingNote.getContextByClass("Part")
                pattern_search_hits.append(note_position)

                pattern_search_hits_result_list.append(
                    [
                        identifier,
                        startingNote.nameWithOctave,
                        startingMeasure,
                        startingBeat,
                        startingPart.id,
                        str(iteration_search_pattern),
                    ]
                )

            [n.transpose(1, inPlace=True) for n in search_pattern]

            no_results_list.append(
                [
                    identifier,
                    "- No Matches Found -",
                    "- No Matches Found -",
                    "- No Matches Found -",
                    "- No Matches Found -",
                    str(iteration_search_pattern)
                ]
            )

            iteration += 1

        header_titles = ["Selected Score", "Pattern Starting Pitch", "Measure", "Beat", "Part/Voice", "Search Pattern"]

        if len(pattern_search_hits_result_list) == 0:

            return pd.DataFrame(no_results_list, columns=header_titles)

        else:

            return pd.DataFrame(pattern_search_hits_result_list, columns=header_titles)

    except Exception as e:
        handle_error(e)


def pattern_search_without_transposition_with_rhythm(identifier, selected_score_deepcopy,
                                                     search_pattern, search_pattern_clear_names):
    """
    Search for a specific musical pattern in a score considering rhythm but not transposition.

    Parameters
    ----------
    identifier : str
        Identifier for the selected score.
    selected_score_deepcopy : music21.stream.Stream
        A deep copy of the selected musical score.
    search_pattern : list
        A list representing the musical pattern to be searched.
    search_pattern_clear_names : list
        A list of clear names for the search pattern.

    Returns
    -------
    pandas.DataFrame
        A dataframe containing the search results.
    """
    try:
        pattern_search_hits = search.noteNameRhythmicSearch(selected_score_deepcopy, search_pattern)

        pattern_search_hits_result_list = []
        no_results_list = []

        for note_position in pattern_search_hits:
            startingNote = selected_score_deepcopy[note_position]
            startingMeasure = startingNote.measureNumber
            startingBeat = startingNote.beat
            startingPart = startingNote.getContextByClass("Part")

            pattern_search_hits_result_list.append(
                [
                    identifier,
                    startingNote.nameWithOctave,
                    startingMeasure,
                    startingBeat,
                    startingPart.id,
                    str(search_pattern_clear_names),
                ]
            )

        no_results_list.append(
            [
                identifier,
                "- No Matches Found -",
                "- No Matches Found -",
                "- No Matches Found -",
                "- No Matches Found -",
                str(search_pattern_clear_names)
            ]
        )

        header_titles = ["Selected Score", "Pattern Starting Pitch", "Measure", "Beat", "Part/Voice", "Search Pattern"]

        if len(pattern_search_hits_result_list) == 0:

            return pd.DataFrame(no_results_list, columns=header_titles)

        else:

            return pd.DataFrame(pattern_search_hits_result_list, columns=header_titles)

    except Exception as e:
        handle_error(e)


def pattern_search_with_transposition_with_rhythm(identifier, selected_score_deepcopy,
                                                  search_pattern, search_pattern_clear_names):
    """
    Search for a specific musical pattern in a score considering both transposition and rhythm.

    Parameters
    ----------
    identifier : str
        Identifier for the selected score.
    selected_score_deepcopy : music21.stream.Stream
        A deep copy of the selected musical score.
    search_pattern : list
        A list representing the musical pattern to be searched.
    search_pattern_clear_names : list
        A list of clear names for the search pattern.

    Returns
    -------
    pandas.DataFrame
        A dataframe containing the search results.
    """
    try:
        pattern_search_hits = []
        iteration = 1

        pattern_search_hits_result_list = []
        no_results_list = []

        for n in range(12):  # Search 12 times (= through all notes in one octave)
            iteration_search_pattern = [[pattern_note.name, pattern_note.duration.quarterLength] for pattern_note in
                                        search_pattern]
            iteration_search_pattern_hit = search.noteNameRhythmicSearch(selected_score_deepcopy, search_pattern)
            for notePosition in iteration_search_pattern_hit:
                startingNote = selected_score_deepcopy[notePosition]
                startingMeasure = startingNote.measureNumber
                startingBeat = startingNote.beat
                startingPart = startingNote.getContextByClass("Part")
                pattern_search_hits.append(notePosition)

                pattern_search_hits_result_list.append(
                    [
                        identifier,
                        startingNote.nameWithOctave,
                        startingMeasure,
                        startingBeat,
                        startingPart.id,
                        str(iteration_search_pattern),
                    ]
                )

            [n.transpose(1, inPlace=True) for n in search_pattern]

            no_results_list.append(
                [
                    identifier,
                    "- No Matches Found -",
                    "- No Matches Found -",
                    "- No Matches Found -",
                    "- No Matches Found -",
                    str(iteration_search_pattern)
                ]
            )

            iteration += 1

        header_titles = ["Selected Score", "Pattern Starting Pitch", "Measure", "Beat", "Part/Voice", "Search Pattern"]

        if len(pattern_search_hits_result_list) == 0:

            return pd.DataFrame(no_results_list, columns=header_titles)

        else:

            return pd.DataFrame(pattern_search_hits_result_list, columns=header_titles)

    except Exception as e:
        handle_error(e)


def pattern_search_only_rhythm(identifier, selected_score_deepcopy,
                               search_pattern, search_pattern_clear_names):
    """
    Search for a specific musical pattern in a score considering only rhythm.

    Parameters
    ----------
    identifier : str
        Identifier for the selected score.
    selected_score_deepcopy : music21.stream.Stream
        A deep copy of the selected musical score.
    search_pattern : list
        A list representing the musical pattern to be searched.
    search_pattern_clear_names : list
        A list of clear names for the search pattern.

    Returns
    -------
    pandas.DataFrame
        A dataframe containing the search results.

    Examples
    --------
    >>> identifier = "example_score"
    >>> selected_score = music21.converter.parse("example_score.mxl")
    >>> selected_score_deepcopy = copy.deepcopy(selected_score)
    >>> search_pattern = [1.0, 0.5, 0.5]
    >>> search_pattern_clear_names = ["quarter", "eighth", "eighth"]
    >>> pattern_search_only_rhythm(identifier, selected_score_deepcopy, search_pattern, search_pattern_clear_names)
    """
    try:
        pattern_search_hits = search.rhythmicSearch(selected_score_deepcopy, search_pattern)

        pattern_search_hits_result_list = []
        no_results_list = []

        for note_position in pattern_search_hits:
            startingNote = selected_score_deepcopy[note_position]
            startingMeasure = startingNote.measureNumber
            startingBeat = startingNote.beat
            startingPart = startingNote.getContextByClass("Part")

            pattern_search_hits_result_list.append(
                [
                    identifier,
                    startingNote.nameWithOctave,
                    startingMeasure,
                    startingBeat,
                    startingPart.id,
                    str(search_pattern_clear_names),
                ]
            )

        no_results_list.append(
            [
                identifier,
                "- No Matches Found -",
                "- No Matches Found -",
                "- No Matches Found -",
                "- No Matches Found -",
                str(search_pattern_clear_names)
            ]
        )

        header_titles = ["Selected Score", "Pattern Starting Pitch", "Measure", "Beat", "Part/Voice", "Search Pattern"]

        if len(pattern_search_hits_result_list) == 0:

            return pd.DataFrame(no_results_list, columns=header_titles)

        else:

            return pd.DataFrame(pattern_search_hits_result_list, columns=header_titles)

    except Exception as e:
        handle_error(e)
