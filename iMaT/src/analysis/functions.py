import music21.stream
import pandas as pd
from music21 import interval, note

from src.constants import PITCH_CLASS_NAMES
from src.utils.error_handling import handle_error


def analysis_ambitus(music_obj, identifier):
    """
    Calculate the ambitus (range) of a music21 stream object.

    Parameters
    ----------
    music_obj : music21.stream.Stream
        The music21 stream object to analyze.
    identifier : str
        The identifier string to be added to the analysis.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the identifier and the ambitus range.

    Notes
    -----
    The ambitus refers to the range of pitches (notes) covered by a piece of music. It is determined by
    identifying the lowest and highest pitches in the music. The function calculates the MIDI pitch values
    (integer representation of pitches) and the note names (pitch names with octave) of the lowest and highest
    pitches, as well as the interval (distance) between them. The ambitus provides insight into the melodic
    and tonal span of the music.

    The resulting DataFrame contains the identifier (to distinguish different analysis results), the MIDI pitch
    value of the lowest and highest pitches, the ambitus range in MIDI pitches, the note name of the lowest and
    highest pitches, and the interval name (distance between the lowest and highest pitches) in music theory terms.
    If there are no pitches in the music, the ambitus values will be indicated with dashes ("-").
    """
    try:
        music_obj = music_obj.stripTies()

        pitches = [n.pitch for n in music_obj.recurse().notes if n.pitch is not None]
        if pitches:
            min_pitch = min(pitches)
            max_pitch = max(pitches)
            min_pitch_name = min_pitch.nameWithOctave
            max_pitch_name = max_pitch.nameWithOctave
            interval_name = interval.Interval(min_pitch, max_pitch).name

            ambitus = max_pitch.midi - min_pitch.midi

            df = pd.DataFrame({'Identifier': [identifier],
                               'MIDI Pitch (min)': [min_pitch.midi],
                               'MIDI Pitch (max)': [max_pitch.midi],
                               'Ambitus (MIDI Interval)': [ambitus],
                               'Note Name (min)': [min_pitch_name],
                               'Note Name (max)': [max_pitch_name],
                               'Ambitus (Interval Name)': [interval_name]})


        else:
            df = pd.DataFrame({'Identifier': [identifier],
                               'MIDI Pitch (min)': ['-'],
                               'MIDI Pitch (max)': ['-'],
                               'Ambitus (MIDI Interval)': ['-'],
                               'Note Name (min)': ['-'],
                               'Note Name (max)': ['-'],
                               'Ambitus (Interval Name)': ['-']})

        return df

    except Exception as e:
        handle_error(e)

def analysis_number_of_notes(music_obj, identifier):
    """
    Analyze the number of notes (individual pitches) in a music21 stream object.

    Parameters
    ----------
    music_obj : music21.stream.Stream
        The music21 stream object to analyze.
    identifier : str
        The identifier string to be added to the analysis.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the identifier and the count of notes.

    Notes
    -----
    In music, a tone refers to an individual pitch, typically represented by a note. This function analyzes the
    music21 stream object and counts the number of occurrences of notes within the stream.

    The function considers any note object present in the stream, including notes with different durations, pitches,
    and other attributes. Rests and other non-pitched elements are excluded from the count.

    The resulting DataFrame contains the identifier (to distinguish different analysis results) and the count of
    notes in the stream.
    """
    try:
        music_obj = music_obj.stripTies()

        num_tones = len(list(music_obj.recurse().notes))

        df = pd.DataFrame({'Identifier': [identifier], 'Number of Notes': [num_tones]})

        return df

    except Exception as e:
        handle_error(e)


def analysis_number_of_rests(music_obj, identifier):
    """
    Count the number of rests in a music21 stream object.

    Parameters
    ----------
    music_obj : music21.stream.Stream
        The music21 stream object to analyze.
    identifier : str
        The identifier string to be added to the analysis.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the identifier and the count of rests.

    Notes
    -----
    In music notation, a rest indicates a period of silence or absence of musical sound. Rests are used to
    indicate pauses or breaks in the music. This function analyzes the music21 stream object and counts the
    number of rest elements present in the music.

    The resulting DataFrame contains the identifier (to distinguish different analysis results) and the count
    of rests in the music.
    """
    try:
        num_rests = 0

        music_obj = music_obj.stripTies()

        for rest in music_obj.flat.getElementsByClass('Rest'):
            num_rests += 1

        df = pd.DataFrame({'Identifier': [identifier], 'Number of Rests': [num_rests]})

        return df

    except Exception as e:
        handle_error(e)


def analysis_number_of_rests_per_rest_duration(music_obj, identifier):
    """
    Count the number of rests per duration in a music21 stream object.

    Parameters
    ----------
    music_obj : music21.stream.Stream
        The music21 stream object to analyze.
    identifier : str
        The identifier string to be added to the analysis.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the identifier, rest durations, rest names, and their counts.

    Notes
    -----
    In music notation, rests indicate periods of silence or absence of musical sound. Rests are assigned
    specific durations, indicating the length of the pause or break in the music. This function analyzes the
    music21 stream object and counts the number of rests per duration.

    The resulting DataFrame contains the identifier (to distinguish different analysis results), the rest
    durations (quarter lengths), the rest names (duration representations), and the counts of rests for each
    duration in the music.
    """
    try:
        rest_durations = {}

        music_obj = music_obj.stripTies()

        for rest in music_obj.flat.getElementsByClass('Rest'):
            duration_value = rest.duration.quarterLength
            duration_name = rest.fullName
            if duration_value not in rest_durations:
                rest_durations[duration_value] = {'Duration Name': duration_name, 'Count': 1}
            else:
                rest_durations[duration_value]['Count'] += 1

        df = pd.DataFrame.from_dict(rest_durations, orient='index').reset_index()
        df.columns = ['Rest Duration', 'Duration Name', 'Count']
        df['Identifier'] = identifier
        df = df[['Identifier', 'Rest Duration', 'Duration Name', 'Count']]
        df.sort_values('Rest Duration', ascending=True, inplace=True)

        return df

    except Exception as e:
        handle_error(e)

def analysis_number_of_intervals_per_type(music_obj, identifier):
    """
    Analyze the number of interval types in a music21 stream object.

    Parameters
    ----------
    music_obj : music21.stream.Stream
        The music21 stream object to analyze.
    identifier : str
        The identifier string to be added to the analysis.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the identifier, interval types, their nice names, and positive MIDI pitch value intervals.

    Notes
    -----
    In music theory and analysis, intervals refer to the distance between two pitches. This function analyzes
    the music21 stream object and counts the number of occurrences of different interval types.

    The interval types are represented by their name, and the nice name provides a more descriptive representation.
    The MIDI pitch value intervals are calculated as the absolute difference between the MIDI pitch values of
    consecutive notes in the stream. Only positive MIDI pitch value intervals are considered to avoid duplication
    of intervals with reverse directions.

    The resulting DataFrame contains the identifier (to distinguish different analysis results), the interval
    types, their nice names, the positive MIDI pitch value intervals, and the counts of occurrences for each
    interval type in the music.
    """
    try:
        interval_types = {}

        music_obj = music_obj.stripTies()

        notes = [n for n in music_obj.recurse().notes if n.pitch is not None]
        for i in range(len(notes) - 1):
            interval_obj = note.interval.notesToInterval(notes[i], notes[i + 1])
            interval_type = interval_obj.name
            interval_name = interval_obj.niceName
            midi_interval = abs(notes[i + 1].pitch.midi - notes[i].pitch.midi)
            if interval_type not in interval_types:
                interval_types[interval_type] = {"Count": 1, "Interval Name": interval_name, "MIDI Interval": midi_interval}
            else:
                interval_types[interval_type]["Count"] += 1

        df = pd.DataFrame(interval_types.values(), index=interval_types.keys())
        df.index.name = 'Interval Type'
        df = df.reset_index()
        df['Identifier'] = identifier
        df = df[['Identifier', 'MIDI Interval', 'Interval Type', 'Interval Name', 'Count']]
        df.sort_values('MIDI Interval', ascending=True, inplace=True)

        return df

    except Exception as e:
        handle_error(e)

def analysis_number_of_intervals_per_type_with_direction(music_obj, identifier):
    """
    Analyze the number of ascending and descending interval types in a music21 stream object.

    Parameters
    ----------
    music_obj : music21.stream.Stream
        The music21 stream object to analyze.
    identifier : str
        The identifier string to be added to the analysis.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the identifier, interval types, their nice names, MIDI pitch value intervals, and their frequencies.

    Notes
    -----
    In music theory and analysis, intervals refer to the distance between two pitches. Interval directions indicate
    whether the interval moves upwards (ascending) or downwards (descending) in pitch. This function analyzes the
    music21 stream object and counts the number of occurrences of different interval types in both ascending and
    descending directions.

    The interval types are represented by their directed name, which indicates the direction (e.g., "A2" for an
    ascending second, "d5" for a descending fifth). The nice name provides a more descriptive representation of the
    interval. The MIDI pitch value intervals represent the difference in MIDI pitch values between consecutive notes
    in the stream.

    The resulting DataFrame contains the identifier (to distinguish different analysis results), the interval types,
    their nice names, the MIDI pitch value intervals, and the frequencies of occurrence for each interval type in
    both ascending and descending directions.
    """
    try:
        intervals = {}

        music_obj = music_obj.stripTies()

        notes = [n for n in music_obj.recurse().notes if n.pitch is not None]
        for i in range(len(notes) - 1):
            interval_obj = note.interval.notesToInterval(notes[i], notes[i + 1])
            interval_type = interval_obj.directedName
            interval_name = interval_obj.niceName
            midi_interval = notes[i + 1].pitch.midi - notes[i].pitch.midi
            if interval_type not in intervals:
                intervals[interval_type] = {"Count": 1, "Interval Name": interval_name, "MIDI Interval": midi_interval}
            else:
                intervals[interval_type]["Count"] += 1

        df = pd.DataFrame(intervals.values(), index=intervals.keys())
        df.index.name = 'Interval'
        df = df.reset_index()
        df['Identifier'] = identifier
        df = df[['Identifier', 'MIDI Interval', 'Interval', 'Interval Name', 'Count']]
        df.sort_values('MIDI Interval', ascending=True, inplace=True)

        return df

    except Exception as e:
        handle_error(e)


def analysis_number_of_sound_events_per_pitch(music_obj, identifier):
    """
    Analyze the number of sound events per pitch in a music21 stream object.

    Parameters
    ----------
    music_obj : music21.stream.Stream
        The music21 stream object to analyze.
    identifier : str
        The identifier string to be added to the analysis.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the identifier, MIDI Pitch, pitch name, and the count of sound events per pitch.

    Notes
    -----
    Sound events refer to individual occurrences of pitches in the music stream. This function analyzes the
    music21 stream object and counts the number of sound events (notes) per pitch.

    The analysis considers the MIDI pitch value, the pitch name with octave information, and the count of sound
    events for each pitch.

    The resulting DataFrame contains the identifier (to distinguish different analysis results), the MIDI pitch
    value, the pitch name, and the count of sound events for each pitch.
    """
    try:
        sound_events_per_pitch = {}

        music_obj = music_obj.stripTies()

        for note_obj in music_obj.recurse().notes:
            pitch_name = note_obj.pitch.nameWithOctave
            midi_pitch = note_obj.pitch.midi
            if pitch_name not in sound_events_per_pitch:
                sound_events_per_pitch[pitch_name] = {"MIDI Pitch": midi_pitch, "Count": 1}
            else:
                sound_events_per_pitch[pitch_name]["Count"] += 1

        df = pd.DataFrame(sound_events_per_pitch.values(), index=sound_events_per_pitch.keys())
        df.index.name = 'Pitch Name'
        df = df.reset_index()
        df['Identifier'] = identifier
        df = df[['Identifier', 'MIDI Pitch', 'Pitch Name', 'Count']]
        df.sort_values('MIDI Pitch', ascending=True, inplace=True)

        return df

    except Exception as e:
        handle_error(e)


def analysis_number_of_sound_events_per_pitch_class(music_obj, identifier):
    """
    Analyze the number of sound events per pitch class in a music21 stream object.

    Parameters
    ----------
    music_obj : music21.stream.Stream
        The music21 stream object to analyze.
    identifier : str
        The identifier string to be added to the analysis.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the identifier, MIDI Pitch Class, pitch class symbol, and the count of sound events per pitch class.

    Notes
    -----
    Sound events refer to individual occurrences of pitches in the music stream. This function analyzes the
    music21 stream object and counts the number of sound events (notes) per pitch class.

    The pitch class represents the chromatic pitch value without octave information. The analysis assigns
    pitch class symbols (e.g., "C", "D#", "G") to each pitch class. The count of sound events (notes) for
    each pitch class is also calculated.

    The resulting DataFrame contains the identifier (to distinguish different analysis results), the MIDI pitch
    class value, the pitch class symbol, and the count of sound events for each pitch class.
    """
    try:
        sound_events_per_pitch_class = {}

        music_obj = music_obj.stripTies()

        for note_obj in music_obj.recurse().notes:
            pitch_class = note_obj.pitch.pitchClass
            if pitch_class not in sound_events_per_pitch_class:
                sound_events_per_pitch_class[pitch_class] = {"Pitch Class Name": PITCH_CLASS_NAMES[pitch_class],
                                                             "Count": 1}
            else:
                sound_events_per_pitch_class[pitch_class]["Count"] += 1

        df = pd.DataFrame(sound_events_per_pitch_class.values(), index=sound_events_per_pitch_class.keys())
        df.index.name = 'MIDI Pitch Class'
        df = df.reset_index()
        df['Identifier'] = identifier
        df = df[['Identifier', 'MIDI Pitch Class', 'Pitch Class Name', 'Count']]
        df.sort_values('MIDI Pitch Class', ascending=True, inplace=True)

        return df

    except Exception as e:
        handle_error(e)


def analysis_number_of_sound_events_per_tone_duration(music_obj, identifier):
    """
    Analyze the number of sound events per tone duration (quarter length) in a music21 stream object.

    Parameters
    ----------
    music_obj : music21.stream.Stream
        The music21 stream object to analyze.
    identifier : str
        The identifier string to be added to the analysis.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the identifier, tone duration, tone duration name, and the count of sound events per tone duration.

    Notes
    -----
    Sound events refer to individual occurrences of tones in the music stream. This function analyzes the music21
    stream object and counts the number of sound events (notes) per tone duration.

    The tone duration is represented by the quarter length, which indicates the duration of a tone in terms of
    musical beats. The analysis includes the tone duration name (e.g., "Whole", "Half", "Quarter") and the count
    of sound events for each tone duration.

    The resulting DataFrame contains the identifier (to distinguish different analysis results), the tone duration,
    the tone duration name, and the count of sound events for each tone duration.
    """
    try:
        sound_events_per_tone_durations = {}

        music_obj = music_obj.stripTies()

        for note_obj in music_obj.recurse().notes:
            tone_duration = note_obj.duration.quarterLength
            tone_duration_name = note_obj.duration.fullName
            if tone_duration not in sound_events_per_tone_durations:
                sound_events_per_tone_durations[tone_duration] = {"Tone Duration Name": tone_duration_name, "Count": 1}
            else:
                sound_events_per_tone_durations[tone_duration]["Count"] += 1

        df = pd.DataFrame(sound_events_per_tone_durations.values(), index=sound_events_per_tone_durations.keys())
        df.index.name = 'Tone Duration'
        df = df.reset_index()
        df['Identifier'] = identifier
        df = df[['Identifier', 'Tone Duration', 'Tone Duration Name', 'Count']]
        df.sort_values('Tone Duration', ascending=True, inplace=True)

        return df

    except Exception as e:
        handle_error(e)


def analysis_number_of_sound_events_per_metrical_position(music_obj, identifier):
    """
    Analyze the number of sound events that start on the same metrical positions in a music21 stream object.

    Parameters
    ----------
    music_obj : music21.stream.Stream
        The music21 stream object to analyze.
    identifier : str
        The identifier string to be added to the analysis.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the identifier, metrical position, and the count of sound events.

    Notes
    -----
    Metrical positions refer to the specific positions within the musical meter, typically measured in beats.
    This analysis counts the number of sound events (tones) that start on the same metrical positions in the music.

    The resulting DataFrame contains the identifier (to distinguish different analysis results), the metrical position,
    and the count of sound events for each metrical position.
    """
    try:
        tone_counts = {}

        music_obj = music_obj.stripTies()

        for note_obj in music_obj.recurse().notes:
            metrical_position = note_obj.beat
            if metrical_position in tone_counts:
                tone_counts[metrical_position] += 1
            else:
                tone_counts[metrical_position] = 1

        results = []
        for metrical_position, count in tone_counts.items():
            results.append((identifier, metrical_position, count))

        df = pd.DataFrame(results, columns=['Identifier', 'Metrical Position', 'Count'])
        df.sort_values('Metrical Position', ascending=True, inplace=True)

        return df

    except Exception as e:
        handle_error(e)


def analysis_number_of_pitches_per_tone_duration(music_obj, identifier):
    """
    Analyze the number of pitches per duration (quarter length) in a music21 stream object.

    Parameters
    ----------
    music_obj : music21.stream.Stream
        The music21 stream object to analyze.
    identifier : str
        The identifier string to be added to the analysis.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the identifier, MIDI Pitches, Pitch Names, Duration, Duration Names, and Count of the sound events.

    Notes
    -----
    This function analyzes the music21 stream object and counts the number of pitches per duration (quarter length).

    The analysis considers each pitch occurring in the music stream along with its associated duration. The duration
    is represented by the quarter length, indicating the length of the pitch in terms of musical beats. The count of
    sound events (pitches) is calculated for each combination of pitch and duration.

    The resulting DataFrame contains the identifier (to distinguish different analysis results), the MIDI Pitches,
    Pitch Names, Duration, Duration Names, and the count of sound events for each combination of pitch and duration.
    """
    try:
        pitch_over_durations = {}

        music_obj = music_obj.stripTies()

        for note_obj in music_obj.recurse().notes:
            pitch = note_obj.pitch.midi
            pitch_name = note_obj.pitch.nameWithOctave
            duration = note_obj.duration.quarterLength
            duration_name = note_obj.duration.fullName
            key = (pitch, pitch_name, duration, duration_name)
            if key in pitch_over_durations:
                pitch_over_durations[key] += 1
            else:
                pitch_over_durations[key] = 1

        results = []
        for (pitch, pitch_name, duration, duration_name), count in pitch_over_durations.items():
            results.append((identifier, pitch, pitch_name, duration, duration_name, count))

        df = pd.DataFrame(results,
                          columns=['Identifier', 'MIDI Pitches', 'Pitch Names', 'Duration', 'Duration Names', 'Count'])
        df.sort_values(['MIDI Pitches', 'Duration'], ascending=True, inplace=True)

        return df

    except Exception as e:
        handle_error(e)


def analysis_number_of_pitches_per_metrical_position(music_obj, identifier):
    """
    Analyze the number of occurrences of each pitch at each metrical position in a music21 stream object.

    Parameters
    ----------
    music_obj : music21.stream.Stream
        The music21 stream object to analyze.
    identifier : str
        The identifier string to be added to the analysis.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the identifier, metrical position, pitch, pitch name, and the count of each pitch.

    Notes
    -----
    Metrical positions refer to the specific positions within the musical meter, typically measured in beats. This analysis
    counts the number of occurrences of each pitch (including octave information) that start on the same metrical
    positions in the music.

    The resulting DataFrame contains the identifier (to distinguish different analysis results), the metrical position,
    the MIDI number and name of each pitch, and the count of each pitch at each metrical position.
    """
    try:
        pitches_per_metrical_position = {}

        music_obj = music_obj.stripTies()

        for note_obj in music_obj.recurse().notes:
            metrical_position = note_obj.beat
            pitch = note_obj.pitch.midi
            pitch_name = note_obj.pitch.nameWithOctave
            key = (pitch, pitch_name, metrical_position)
            if key in pitches_per_metrical_position:
                pitches_per_metrical_position[key] += 1
            else:
                pitches_per_metrical_position[key] = 1

        results = [(identifier, pitch, pitch_name, metrical_position, count)
                   for (pitch, pitch_name, metrical_position), count in pitches_per_metrical_position.items()]

        df = pd.DataFrame(results, columns=['Identifier', 'MIDI Pitches', 'Pitch Name', 'Metrical Position', 'Count'])
        df.sort_values(['MIDI Pitches', 'Metrical Position'], ascending=True, inplace=True)

        return df

    except Exception as e:
        handle_error(e)


def analysis_number_of_pitches_per_offset(music_obj, identifier):
    """
    Analyze the number of pitches per offset (time position) in a music21 stream object.

    Parameters
    ----------
    music_obj : music21.stream.Stream
        The music21 stream object to analyze.
    identifier : str
        The identifier string to be added to the analysis.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the identifier, offset (time position), MIDI pitch, pitch name, and count of the sound events.

    Notes
    -----
    An offset refers to the time position of a musical event within a piece of music. It represents the time elapsed
    since the beginning of the music or a specific reference point. In this analysis, the function examines the pitches
    (notes) occurring at different offsets (time positions) in the music and counts the number of occurrences for each
    pitch at each offset.

    The offset values represent the time positions in the music stream, usually measured in beats or fractions of beats.
    By analyzing the pitches over offsets, it is possible to gain insights into the distribution of pitches and their
    temporal relationships within the music.

    The resulting DataFrame contains the identifier (to distinguish different analysis results), the offset (time
    position), the MIDI pitch, the pitch name, and the count of sound events (number of occurrences) for each combination
    of offset and pitch.
    """
    try:
        pitches_over_offsets = {}

        music_obj = music_obj.stripTies()

        for element in music_obj.recurse():
            if isinstance(element, note.Note):
                midi_pitch = element.pitch.midi
                pitch_name = element.pitch.nameWithOctave
                offset = element.offset
                key = (offset, midi_pitch, pitch_name)
                if key in pitches_over_offsets:
                    pitches_over_offsets[key] += 1
                else:
                    pitches_over_offsets[key] = 1

        pitches_list = []
        for key, count in pitches_over_offsets.items():
            pitches_list.append((identifier, key[1], key[2], key[0], count))

        df = pd.DataFrame(pitches_list, columns=['Identifier', 'MIDI Pitches', 'Pitch Name', 'Offset', 'Count'])
        df.sort_values(['MIDI Pitches', 'Offset'], ascending=True, inplace=True)

        return df

    except Exception as e:
        handle_error(e)


def analysis_number_of_pitch_classes_per_tone_duration(music_obj, identifier):
    """
    Analyze the number of pitch classes per duration (quarter length) in a music21 stream object.

    Parameters
    ----------
    music_obj : music21.stream.Stream
        The music21 stream object to analyze.
    identifier : str
        The identifier string to be added to the analysis.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the identifier, pitch class, duration (quarter length), pitch class symbol, and count of the sound events.
    """
    try:
        pitch_classes_over_durations = {}

        music_obj = music_obj.stripTies()

        for note_obj in music_obj.recurse().notes:
            pitch_class = note_obj.pitch.pitchClass
            duration = note_obj.duration.quarterLength
            duration_names = note_obj.duration.fullName
            key = (pitch_class, duration, duration_names)
            if key in pitch_classes_over_durations:
                pitch_classes_over_durations[key] += 1
            else:
                pitch_classes_over_durations[key] = 1

        results = []
        for (pitch_class, duration, duration_names), count in pitch_classes_over_durations.items():
            pitch_class_symbol = PITCH_CLASS_NAMES[pitch_class]
            results.append((identifier, pitch_class, pitch_class_symbol, duration, duration_names, count))

        df = pd.DataFrame(results, columns=['Identifier', 'Pitch Class', 'Pitch Class Symbol', 'Duration', 'Duration Names',
                                            'Count'])
        df.sort_values(['Pitch Class', 'Duration'], ascending=True, inplace=True)

        return df

    except Exception as e:
        handle_error(e)


def analysis_number_of_pitch_classes_per_metrical_position(music_obj, identifier):
    """
    Analyze the number of occurrences of each pitch class at each metrical position in a music21 stream object.

    Parameters
    ----------
    music_obj : music21.stream.Stream
        The music21 stream object to analyze.
    identifier : str
        The identifier string to be added to the analysis.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the identifier, metrical position, pitch class, pitch class name, and the count of each pitch class.

    Notes
    -----
    Metrical positions refer to the specific positions within the musical meter, typically measured in beats. This analysis
    counts the number of occurrences of each pitch class (without octave information) that start on the same metrical
    positions in the music.

    The resulting DataFrame contains the identifier (to distinguish different analysis results), the metrical position,
    the number and name of each pitch class, and the count of each pitch class at each metrical position.
    """
    try:
        pitch_classes_per_metrical_position = {}

        music_obj = music_obj.stripTies()

        for note_obj in music_obj.recurse().notes:
            metrical_position = note_obj.beat
            pitch_class = note_obj.pitch.pitchClass
            pitch_class_name = PITCH_CLASS_NAMES[pitch_class]
            key = (pitch_class, pitch_class_name, metrical_position)
            if key in pitch_classes_per_metrical_position:
                pitch_classes_per_metrical_position[key] += 1
            else:
                pitch_classes_per_metrical_position[key] = 1

        results = [(identifier, pitch_class, pitch_class_name, metrical_position, count)
                   for (pitch_class, pitch_class_name, metrical_position), count in
                   pitch_classes_per_metrical_position.items()]

        df = pd.DataFrame(results, columns=['Identifier', 'Pitch Class', 'Pitch Class Name', 'Metrical Position', 'Count'])
        df.sort_values(['Pitch Class', 'Metrical Position'], ascending=True, inplace=True)

        return df

    except Exception as e:
        handle_error(e)


def analysis_number_of_pitch_classes_per_offset(music_obj, identifier):
    """
    Analyze the number of pitch classes per offset (time position) in a music21 stream object.

    Parameters
    ----------
    music_obj : music21.stream.Stream
        The music21 stream object to analyze.
    identifier : str
        The identifier string to be added to the analysis.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the identifier, offset (time position), pitch class, pitch class name, and count of the sound events.

    Notes
    -----
    An offset refers to the time position of a musical event within a piece of music. It represents the time elapsed
    since the beginning of the music or a specific reference point. In this analysis, the function examines the pitch
    classes (chromatic pitch values without octave) occurring at different offsets (time positions) in the music and
    counts the number of occurrences for each pitch class at each offset.

    The offset values represent the time positions in the music stream, usually measured in beats or fractions of beats.
    By analyzing the pitch classes over offsets, it is possible to observe the distribution of pitch classes and their
    temporal relationships within the music.

    The resulting DataFrame contains the identifier (to distinguish different analysis results), the offset (time
    position), the pitch class (chromatic pitch value without octave), the pitch class name, and the count of sound
    events (number of occurrences) for each combination of offset and pitch class.
    """
    try:
        pitch_classes_over_offsets = {}

        music_obj = music_obj.stripTies()

        for element in music_obj.recurse():
            if isinstance(element, note.Note):
                pitch_class = element.pitch.pitchClass
                pitch_class_name = PITCH_CLASS_NAMES[pitch_class]
                offset = element.offset
                key = (offset, pitch_class, pitch_class_name)
                if key in pitch_classes_over_offsets:
                    pitch_classes_over_offsets[key] += 1
                else:
                    pitch_classes_over_offsets[key] = 1

        pitch_classes_list = []
        for key, count in pitch_classes_over_offsets.items():
            pitch_classes_list.append((identifier, key[1], key[2], key[0], count))

        df = pd.DataFrame(pitch_classes_list, columns=['Identifier', 'Pitch Class', 'Pitch Class Name', 'Offset', 'Count'])
        df.sort_values(['Pitch Class', 'Offset'], ascending=True, inplace=True)

        return df

    except Exception as e:
        handle_error(e)

# combination functions


def analysis_advanced_calculate_activity_rate(music_obj, identifier):
    """
    Calculate the activity index in a music21 stream object.

    Parameters
    ----------
    music_obj : music21.stream.Stream
        The music21 stream object to analyze.
    identifier : str
        The identifier string to be added to the analysis.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the identifier, number of notes, number of rests, and the activity index.

    Notes
    -----
    The activity index is defined as the ratio of the number of notes to the number of rests in a piece of music.
    This can be seen as an indication of the "density" of musical events in the piece. A higher activity index means
    more notes relative to rests, while a lower activity index means more rests relative to notes.

    The resulting DataFrame contains the identifier (to distinguish different analysis results), the number of notes,
    the number of rests, and the activity index for the piece.
    """
    try:
        notes_df = analysis_number_of_notes(music_obj, identifier)
        rests_df = analysis_number_of_rests(music_obj, identifier)

        num_notes = notes_df.loc[notes_df['Identifier'] == identifier, 'Number of Notes'].values[0]
        num_rests = rests_df.loc[rests_df['Identifier'] == identifier, 'Number of Rests'].values[0]

        # Avoid division by zero
        if num_rests == 0:
            activity_rate = float('NaN')
        else:
            activity_rate = num_notes / num_rests

        df = pd.DataFrame({'Identifier': [identifier], 'Number of Notes': [num_notes], 'Number of Rests': [num_rests],
                           'Activity Index': [activity_rate]})
        df.sort_values('Activity Index', ascending=False)

        return df

    except Exception as e:
        handle_error(e)


def analysis_advanced_compare_pitches_and_pitch_classes_per_duration(music_obj, identifier):
    """
    Compare the number of pitches and pitch classes per duration in a music21 stream object.

    Parameters
    ----------
    music_obj : music21.stream.Stream
        The music21 stream object to analyze.
    identifier : str
        The identifier string to be added to the analysis.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the identifier, duration, duration names, count of pitches, count of pitch classes,
        and pitch to pitch class ratio for each duration.

    Notes
    -----
    This function combines the analysis of the number of pitches per duration and the number of pitch classes
    per duration. By comparing these two analyses, it's possible to observe how the tonal distribution (both
    specific pitches and pitch classes) changes with note duration in the music piece.

    The resulting DataFrame contains the identifier, duration (quarter length), duration names, count of pitches,
    count of pitch classes, and the ratio of pitches to pitch classes for each duration.

    The pitch to pitch class ratio provides a measure of tonal complexity and variety for each note duration:
    * Ratio = 1: This indicates that every pitch for a given duration is unique, i.e., all the pitches
      belong to different pitch classes. It suggests a high degree of tonal variety for that duration.
    * Ratio > 1: This indicates that some pitches are being repeated for notes of that duration.
      The higher the ratio, the greater the repetition of certain pitches, suggesting a focus or emphasis on these
      specific pitch classes in that duration.
    """
    try:
        pitches_df = analysis_number_of_pitches_per_tone_duration(music_obj, identifier)
        pitch_classes_df = analysis_number_of_pitch_classes_per_tone_duration(music_obj, identifier)

        # Group and count the number of pitches and pitch classes per duration
        pitches_count_df = pitches_df.groupby(['Duration', 'Duration Names']).size().reset_index(name='Pitches Count')
        pitch_classes_count_df = pitch_classes_df.groupby(['Duration', 'Duration Names']).size().reset_index(
            name='Pitch Classes Count')

        # Merge the two dataframes on Duration and Duration Names
        df = pd.merge(pitches_count_df, pitch_classes_count_df, on=['Duration', 'Duration Names'])

        # Calculate the pitch to pitch class ratio
        df['Pitch to Pitch Class Ratio'] = df['Pitches Count'] / df['Pitch Classes Count']

        # Add identifier column
        df['Identifier'] = identifier

        # Reorder columns
        df = df[['Identifier', 'Duration', 'Duration Names', 'Pitches Count', 'Pitch Classes Count',
                 'Pitch to Pitch Class Ratio']]

        df.sort_values('Pitch to Pitch Class Ratio', ascending=False)

        return df

    except Exception as e:
        handle_error(e)
