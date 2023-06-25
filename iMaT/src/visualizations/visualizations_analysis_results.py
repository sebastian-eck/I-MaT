from src.cli.cli_menu_structure import display_menu_print_textblock


def map_analysis_function_to_display_function(analysis_func: callable):
    """
    Returns the corresponding results display function for a provided analysis function.

    Parameters
    ----------
    analysis_func : callable
        The analysis function for which the corresponding results display function is to be returned.

    Returns
    -------
    function
        The corresponding results display function.

    Raises
    ------
    ValueError
        If the provided analysis function is not mapped to a results display function.
    """
    function_mapping = {

        'analysis_number_of_rests_per_rest_duration': display_analysis_number_of_rests_per_rest_duration,
        'analysis_number_of_intervals_per_type': display_analysis_number_of_intervals_per_type,
        'analysis_number_of_intervals_per_type_with_direction': display_analysis_number_of_intervals_per_type_with_direction,
        'analysis_number_of_sound_events_per_pitch': display_analysis_number_of_sound_events_per_pitch,
        'analysis_number_of_sound_events_per_pitch_class': display_analysis_number_of_sound_events_per_pitch_class,
        'analysis_number_of_sound_events_per_tone_duration': display_analysis_number_of_sound_events_per_tone_duration,
        'analysis_number_of_sound_events_per_metrical_position': display_analysis_number_of_sound_events_per_metrical_position,
        'analysis_number_of_pitches_per_tone_duration': display_analysis_number_of_pitches_per_tone_duration,
        'analysis_number_of_pitches_per_metrical_position': display_analysis_number_of_pitches_per_metrical_position,
        'analysis_number_of_pitches_per_offset': display_analysis_number_of_pitches_per_offset,
        'analysis_number_of_pitch_classes_per_tone_duration': display_analysis_number_of_pitch_classes_per_tone_duration,
        'analysis_number_of_pitch_classes_per_metrical_position': display_analysis_number_of_pitch_classes_per_metrical_position,
        'analysis_number_of_pitch_classes_per_offset': display_analysis_number_of_pitch_classes_per_offset,
        'analysis_advanced_compare_pitches_and_pitch_classes_per_duration': display_advanced_pitch_class_duration_analysis

    }

    function_name = analysis_func.__name__

    try:

        display_results_func = function_mapping[function_name]

        return display_results_func


    except KeyError:

        text_dict = {

            "menu_displayed_text": [
                "-- Attention --",
                f"\nFor the chosen analysis function is no display function available. Please see below for possible "
                f"reasons:",
                "<To continue, please press Enter>",
                ["", "Message"]

            ],

            "menu_entries_text": [
                ["Function in Question:", f"'{function_name}'."],
                ["Possible Reasons", "Not all analysis functions necessarily have a corresponding display function. "
                                     "The display functions are intended to provide visual representations of the "
                                     "analysis results, but for some analyses, that generate only very limited data, "
                                     "the numerical or tabular results shown in the previous window may be sufficient."],
                ["Possible Solution", "Check the function mapping or the available display functions in the code. "
                                      "It's also possible that a display function for the given analysis function has "
                                      "not been implemented yet. Feel free to contribute your own display function!"],

            ]

        }

        display_menu_print_textblock(text_dict)


def display_analysis_number_of_rests_per_rest_duration(analysis_results, identifier):
    """
    Display a bar diagram of the number of rests per rest duration.

    Parameters
    ----------
    analysis_results : pd.DataFrame
        The DataFrame with the results of the analysis.
    identifier : str
        The identifier string to be added to the plot title.
    """
    # Create the plot
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Rest Duration', y='Count', data=analysis_results, color='b')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=90)

    # Add labels and title
    plt.title(f'Number of Rests per Rest Duration for {identifier}')
    plt.ylabel('Count')
    plt.xlabel('Rest Duration')

    # Display the plot
    plt.show()


def display_analysis_number_of_intervals_per_type(analysis_results, identifier):
    """
    Display a bar diagram of the number of interval types.

    Parameters
    ----------
    analysis_results : pd.DataFrame
        The DataFrame with the results of the analysis.
    identifier : str
        The identifier string to be added to the plot title.
    """
    # Create the plot
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Interval Type', y='Count', data=analysis_results, color='b')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=90)

    # Add labels and title
    plt.title(f'Number of Interval Types for {identifier}')
    plt.ylabel('Count')
    plt.xlabel('Interval Type')

    # Display the plot
    plt.show()


def display_analysis_number_of_intervals_per_type_with_direction(analysis_results, identifier):
    """
    Display a bar diagram of the number of ascending and descending interval types.

    Parameters
    ----------
    analysis_results : pd.DataFrame
        The DataFrame with the results of the analysis.
    identifier : str
        The identifier string to be added to the plot title.
    """
    # Create the plot
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Interval', y='Count', data=analysis_results, color='b')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=90)

    # Add labels and title
    plt.title(f'Number of Ascending and Descending Interval Types for {identifier}')
    plt.ylabel('Count')
    plt.xlabel('Interval')

    # Display the plot
    plt.show()


def display_analysis_number_of_sound_events_per_pitch(analysis_results, identifier):
    """
    Display a bar diagram of the number of sound events per pitch.

    Parameters
    ----------
    analysis_results : pd.DataFrame
        The DataFrame with the results of the analysis.
    identifier : str
        The identifier string to be added to the plot title.
    """
    # Create the plot
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Pitch Name', y='Count', data=analysis_results, color='b')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=90)

    # Add labels and title
    plt.title(f'Number of Sound Events Per Pitch for {identifier}')
    plt.ylabel('Count')
    plt.xlabel('Pitch Name')

    # Display the plot
    plt.show()


def display_analysis_number_of_sound_events_per_pitch_class(analysis_results, identifier):
    """
    Display a bar diagram of the number of sound events per pitch class.

    Parameters
    ----------
    analysis_results : pd.DataFrame
        The DataFrame with the results of the analysis.
    identifier : str
        The identifier string to be added to the plot title.
    """

    # Create the plot
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Pitch Class Name', y='Count', data=analysis_results, color='b')

    # Add labels and title
    plt.title(f'Number of Sound Events Per Pitch Class for {identifier}')
    plt.ylabel('Count')
    plt.xlabel('Pitch Class Name')

    # Display the plot
    plt.show()


def display_analysis_number_of_sound_events_per_tone_duration(analysis_results, identifier):
    """
    Display a bar diagram of the number of sound events per tone duration.

    Parameters
    ----------
    analysis_results : pd.DataFrame
        The DataFrame with the results of the analysis.
    identifier : str
        The identifier string to be added to the plot title.
    """

    # Create the plot
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Tone Duration', y='Count', data=analysis_results, color='b')

    # Add labels and title
    plt.title(f'Number of Sound Events Per Tone Duration for {identifier}')
    plt.ylabel('Count')
    plt.xlabel('Tone Duration')

    # Display the plot
    plt.show()


def display_analysis_number_of_sound_events_per_metrical_position(analysis_results, identifier):
    """
    Display a bar diagram of the number of sound events per metrical position.

    Parameters
    ----------
    analysis_results : pd.DataFrame
        The DataFrame with the results of the analysis.
    identifier : str
        The identifier string to be added to the plot title.
    """

    # Create the plot
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Metrical Position', y='Count', data=analysis_results, color='b')

    # Add labels and title
    plt.title(f'Number of Sound Events Per Metrical Position for {identifier}')
    plt.ylabel('Count')
    plt.xlabel('Metrical Position')

    # Display the plot
    plt.show()


def display_analysis_number_of_pitches_per_tone_duration(analysis_results, identifier):
    """
    Display a matrix plot of the number of pitches per duration.

    Parameters
    ----------
    analysis_results : pd.DataFrame
        The DataFrame with the results of the analysis.
    identifier : str
        The identifier string to be added to the plot title.
    """

    # Pivot the DataFrame to create a matrix format for the heatmap
    df_pivot = analysis_results.pivot(index='Duration', columns='MIDI Pitches', values='Count')

    # Create the plot
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_pivot, cmap="YlGnBu", linewidths=.5)

    # Add labels and title
    plt.title(f'Pitches Over Durations for {identifier}')
    plt.ylabel('Duration')
    plt.xlabel('MIDI Pitches')

    # Invert the y-axis
    plt.gca().invert_yaxis()

    # Display the plot
    plt.show()


def display_analysis_number_of_pitches_per_metrical_position(analysis_results, identifier):
    """
    Display a matrix plot of the number of pitches per metrical position.

    Parameters
    ----------
    analysis_results : pd.DataFrame
        The DataFrame with the results of the analysis.
    identifier : str
        The identifier string to be added to the plot title.
    """

    # Pivot the DataFrame to create a matrix format for the heatmap
    df_pivot = analysis_results.pivot(index='Metrical Position', columns='MIDI Pitches', values='Count')

    # Create the plot
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_pivot, cmap="YlGnBu", linewidths=.5)

    # Add labels and title
    plt.title(f'Pitches Over Metrical Positions for {identifier}')
    plt.ylabel('Metrical Position')
    plt.xlabel('MIDI Pitches')

    # Invert the y-axis
    plt.gca().invert_yaxis()

    # Display the plot
    plt.show()


def display_not_available(pd_dataset, identifier):
    return


import seaborn as sns
import matplotlib.pyplot as plt


def display_analysis_number_of_pitches_per_offset(analysis_results, identifier):
    """
    Display a matrix plot of the number of pitches per offset.

    Parameters
    ----------
    analysis_results : pd.DataFrame
        The DataFrame with the results of the analysis.
    identifier : str
        The identifier string to be added to the plot title.
    """

    # Pivot the DataFrame to create a matrix format for the heatmap
    df_pivot = analysis_results.pivot(index='Offset', columns='MIDI Pitches', values='Count')

    # Create the plot
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_pivot, cmap="YlGnBu", linewidths=.5)

    # Add labels and title
    plt.title(f'Pitches Over Offsets for {identifier}')
    plt.ylabel('Offset')
    plt.xlabel('MIDI Pitches')

    # Invert the y-axis
    plt.gca().invert_yaxis()

    # Display the plot
    plt.show()


def display_analysis_number_of_pitch_classes_per_tone_duration(analysis_results, identifier):
    """
    Display a matrix plot of the number of pitch classes per duration.

    Parameters
    ----------
    analysis_results : pd.DataFrame
        The DataFrame with the results of the analysis.
    identifier : str
        The identifier string to be added to the plot title.
    """

    # Pivot the DataFrame to create a matrix format for the heatmap
    df_pivot = analysis_results.pivot(index='Duration', columns='Pitch Class', values='Count')

    # Create the plot
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_pivot, cmap="YlGnBu", linewidths=.5)

    # Add labels and title
    plt.title(f'Pitch Classes Over Duration for {identifier}')
    plt.ylabel('Duration (quarter length)')
    plt.xlabel('Pitch Class')

    # Invert the y-axis
    plt.gca().invert_yaxis()

    # Display the plot
    plt.show()


def display_analysis_number_of_pitch_classes_per_metrical_position(analysis_results, identifier):
    """
    Display a matrix plot of the number of pitch classes per metrical position.

    Parameters
    ----------
    analysis_results : pd.DataFrame
        The DataFrame with the results of the analysis.
    identifier : str
        The identifier string to be added to the plot title.
    """

    # Pivot the DataFrame to create a matrix format for the heatmap
    df_pivot = analysis_results.pivot(index='Metrical Position', columns='Pitch Class', values='Count')

    # Create the plot
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_pivot, cmap="YlGnBu", linewidths=.5)

    # Add labels and title
    plt.title(f'Pitch Classes Over Metrical Positions for {identifier}')
    plt.ylabel('Metrical Position')
    plt.xlabel('Pitch Class')

    # Invert the y-axis
    plt.gca().invert_yaxis()

    # Display the plot
    plt.show()


def display_analysis_number_of_pitch_classes_per_offset(analysis_results, identifier):
    """
    Display a matrix plot of the number of pitch classes per offset.

    Parameters
    ----------
    analysis_results : pd.DataFrame
        The DataFrame with the results of the analysis.
    identifier : str
        The identifier string to be added to the plot title.
    """

    # Pivot the DataFrame to create a matrix format for the heatmap
    df_pivot = analysis_results.pivot(index='Offset', columns='Pitch Class', values='Count')

    # Create the plot
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_pivot, cmap="YlGnBu", linewidths=.5)

    # Add labels and title
    plt.title(f'Pitch Classes Over Offsets for {identifier}')
    plt.ylabel('Offset')
    plt.xlabel('Pitch Class')

    # Invert the y-axis
    plt.gca().invert_yaxis()

    # Display the plot
    plt.show()


def display_advanced_pitch_class_duration_analysis(analysis_results, identifier):
    """
    Display a series of bar plots for the advanced pitch and pitch class duration analysis.

    Parameters
    ----------
    analysis_results : pd.DataFrame
        The DataFrame with the results of the analysis.
    identifier : str
        The identifier string to be added to the plot title.
    """

    # Generate subplots
    fig, axs = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

    # Plot data
    sns.barplot(x='Duration', y='Pitches Count', data=analysis_results, ax=axs[0], color='b')
    sns.barplot(x='Duration', y='Pitch Classes Count', data=analysis_results, ax=axs[1], color='g')
    ratio_plot = sns.barplot(x='Duration', y='Pitch to Pitch Class Ratio', data=analysis_results, ax=axs[2], color='r')

    # Apply transparency to bars below 1
    for patch in ratio_plot.patches:
        current_value = patch.get_height()
        if current_value < 1:
            patch.set_alpha(0.5)

    # Set labels and titles
    axs[0].set_ylabel('Pitches Count')
    axs[0].set_title(f'Number of Pitches per Duration for {identifier}')
    axs[1].set_ylabel('Pitch Classes Count')
    axs[1].set_title(f'Number of Pitch Classes per Duration for {identifier}')
    axs[2].set_ylabel('Pitch to Pitch Class Ratio')
    axs[2].set_title(f'Pitch to Pitch Class Ratio per Duration for {identifier}')

    # Set y-axis limit for the ratio plot to start at 0.75
    axs[2].set_ylim(0.75, None)

    # Add a horizontal line at y=1
    axs[2].axhline(1, color='white', linestyle='--')

    # Set x-axis labels to show duration values and rotate for better readability
    for ax in axs:
        ax.set_xticklabels(analysis_results['Duration'], rotation=90)

    # Display the plots
    plt.tight_layout()
    plt.show()


def example_analyis_display_results(analysis_result, identifier):
    """
    Display the results of analysis_func.

    Takes the results from the global imported variable `analysis_func` and plots a graph using matplotlib.
    """
    # This is just an example of a graphing implementation. The actual implementation would depend on the
    # structure of the 'previous_results' DataFrame and the specific graphing needs for 'analysis_func'.

    analysis_result.sort_values('Count', ascending=True, inplace=False)
    plt.figure(figsize=(12, 6))
    analysis_result.plot()
    plt.bar(analysis_result['Note'], analysis_result['Count'])
    plt.xlabel('Note')
    plt.ylabel('Count')
    plt.title('Note counts for ' + identifier)
    plt.show()


def display_interval_quantity(analysis_result, identifier):
    plt.figure(figsize=(10, 6))
    analysis_result.plot()
    plt.bar(analysis_result['Identifier'], analysis_result['Count'])
    plt.xlabel('Identifier')
    plt.ylabel('Count of Interval Types')
    plt.title('Quantity of Different Interval Types for {}'.format(identifier))
    plt.show()


# Visualization for intervalStructure_intervalTypes_UniqueIntervals
def display_unique_intervals(analysis_result, identifier):
    plt.figure(figsize=(10, 6))
    analysis_result.plot()
    plt.bar(analysis_result['Identifier'], analysis_result['Interval'])
    plt.xlabel('Identifier')
    plt.ylabel('Unique Interval Types')
    plt.title('Unique Interval Types for {}'.format(identifier))
    plt.xticks(rotation=90)
    plt.show()


# Visualization for intervalStructure_intervalTypes_quantity_textOutput
def display_interval_types(analysis_result, identifier):
    plt.figure(figsize=(10, 6))
    analysis_result.plot()
    df_filtered = analysis_result[analysis_result['Identifier'] == identifier]
    plt.bar(df_filtered['Interval'], df_filtered['Count'])
    plt.xlabel('Interval Types')
    plt.ylabel('Count')
    plt.title('Count of Each Interval Type for {}'.format(identifier))
    plt.xticks(rotation=90)
    plt.show()
