import pandas as pd
from music21 import search


def pattern_search_without_transposition_without_rhythm(identifier, selected_score_deepcopy,
                                                        search_pattern, search_pattern_clear_names):

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

    def pitchClassEqual(n1, n2):
        if not hasattr(n1, "pitch"):
            return False
        if not hasattr(n2, "pitch"):
            return False
        if n1.pitch.pitchClass == n2.pitch.pitchClass:
            return True
        else:
            return False

    pattern_search_hits = []
    iteration = 1

    pattern_search_hits_result_list = []
    no_results_list = []

    for n in range(12):  # Search 12 times (= through all notes in one octave)
        iteration_search_pattern = [pattern_note.name for pattern_note in search_pattern]
        iteration_search_pattern_hit = search.streamSearchBase(selected_score_deepcopy, search_pattern,
                                                               algorithm=pitchClassEqual)
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


def pattern_search_without_transposition_with_rhythm(identifier, selected_score_deepcopy,
                                                     search_pattern, search_pattern_clear_names):

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


def pattern_search_with_transposition_with_rhythm(identifier, selected_score_deepcopy,
                                                  search_pattern, search_pattern_clear_names):

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

def pattern_search_only_rhythm(identifier, selected_score_deepcopy,
                               search_pattern, search_pattern_clear_names):

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
