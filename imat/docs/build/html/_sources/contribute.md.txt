# How to Contribute

## Writing New Analysis Functions for I-MaT: A Comprehensive Tutorial

### Introduction

In this tutorial, I will provide you with a comprehensive guide on how to write new analysis functions that can be incorporated into I-MaT, an easy-to-use tool for analyzing musical pieces. This guide assumes no prior knowledge of programming. By the end of this tutorial, you will be able to write your own analysis functions, incorporate them into I-MaT, and select them from a CLI (Command Line Interface) menu.

### An Overview of an Analysis Function

Let's start by understanding what an analysis function is. In simple terms, an analysis function is a piece of code that takes some input data (in our case, a music object), performs some operations on this data, and returns a result (often in the form of a pandas DataFrame).

The main parts of a function include:

1) Function name: This is what we use to call (or "invoke") the function.
2) Parameters: These are the inputs to the function. We pass these when we call the function.
3) Body: This is where the main operation of the function is performed.
4) Return value: This is the result that the function produces.

In I-MaT, an analysis function generally takes two parameters: a music_obj (a music21.stream.Stream object) and an identifier (a string used for labeling the analysis result), and it returns a pandas DataFrame.

### Example Function

    def calculate_total_duration(music_obj, identifier):
        """
        Calculate the total duration of a music21 stream object.
    
        Parameters
        ----------
        music_obj : music21.stream.Stream
            A music21 stream object representing a musical piece to be analyzed.
        identifier : str
            A string used to label the analysis result.
    
        Returns
        -------
        pd.DataFrame
            A pandas DataFrame that contains the total duration of the musical piece.
    
        Notes
        -----
        This function calculates the sum of the durations of all notes in the piece. Rests are not included in this calculation.
        """
    
        try:
            # Initialize total_duration to 0
            total_duration = 0
    
            # Iterate over all notes in the music object
            for note in music_obj.recurse().notes:
                # Add the duration of the current note to total_duration
                total_duration += note.duration.quarterLength
    
            # Create a new pandas DataFrame for the results
            df = pd.DataFrame({'Identifier': [identifier], 'Total Duration': [total_duration]})
    
            # Return the results
            return df
    
        except Exception as e:
            handle_error(e)  # This is a function to handle any errors that might occur.

This function 'calculate_total_duration' takes as input a 'music21' stream object and an identifier string. It calculates the total duration of the music piece by summing the durations of all notes, and returns the results in a pandas DataFrame.

The 'recurse().notes' method is used to iterate over all notes in the music object, and the 'duration.quarterLength' attribute of each note object is used to get its duration.

### Creating an Empty Frame for a New Analysis Function

Here's an example of how to create an empty frame for a new analysis function:

    def my_new_analysis_function(music_obj, identifier):
        """
        Write a brief description of your function here.
        
        Parameters
        ----------
        music_obj : music21.stream.Stream
            A music21 stream object representing a musical piece to be analyzed.
        identifier : str
            A string used to label the analysis result.
        
        Returns
        -------
        pd.DataFrame
            A pandas DataFrame that contains the results of the analysis.
        
        Notes
        -----
        Write any additional notes about your function here.
        """
        
        try:
            # Write the main code of your function here
        
            # Create a new pandas DataFrame for your results
            df = pd.DataFrame({'Identifier': [identifier], 'Result Name': [Result Values]})
        
            # Return the results
            return df
        
        except Exception as e:
            handle_error(e) # This is a function to handle any errors that might occur.


When you're ready to implement your function, replace the comment '# Write the main code of your function here' with your code.

But for now, let's break down the function into its four seperate parts:

#### 1) Defining the function:

    def my_new_analysis_function(music_obj, identifier):

The 'def' keyword is used to define a function in Python. 'my_new_analysis_function is the name of the function that we're creating. 'music_obj' and 'identifier' are the inputs or parameters of this function. The colon ':' marks the start of the function body.

#### 2) Documenting the function:

    """
    Write a brief description of your function here.
    
    Parameters
    ----------
    music_obj : music21.stream.Stream
        A music21 stream object representing a musical piece to be analyzed.
    identifier : str
        A string used to label the analysis result.
    
    Returns
    -------
    pd.DataFrame
        A pandas DataFrame that contains the results of the analysis.
    
    Notes
    -----
    Write any additional notes about your function here.
    """

This part is the documentation (or "docstring") of the function. It's a good practice to document your functions, as it helps other people (and your future self) understand what the function does. The documentation includes a description of the function, the parameters, the return value, and any additional notes.

#### 3) The main body of the function:

    try:
        # Write the main code of your function here
    
        # Create a new pandas DataFrame for your results
        df = pd.DataFrame({'Identifier': [identifier], 'Result Name': [Result Values]})
    
        # Return the results
        return df

1) The 'try' statement allows you to handle errors gracefully. The code that you want to "try" running goes inside this block.
2) The '# Write the main code of your function here' comment is a placeholder for where you'll add your own code. The details of this will depend on what you want your function to do.
3) 'df = pd.DataFrame({'Identifier': [identifier], 'Result Name': [Result Values]})' creates a new pandas DataFrame. This is where you'll store the results of your analysis.
4) The 'return df' statement specifies that your function should return the DataFrame 'df'. This is the result that your function produces.

#### 4) Error handling:

    except Exception as e:
        handle_error(e) # This is a function to handle any errors that might occur.

The 'except' statement specifies what should happen if an error occurs in the 'try' block. In this case, we're saying that if any kind of 'Exception' (error) occurs, it should be handled by the 'handle_error(e)' function. This is a function that you would define elsewhere in your code to specify how to handle different types of errors.

### Incorporating Your Analysis Function into I-MaT

Once you've written your analysis function, you'll need to incorporate it into I-MaT so that it can be used as part of the analysis workflow. Here's how to do this:

1) Add your function to the relevant Python module where all the other analysis functions are defined. All the analysis functions are defined in the [analysis.functions.py module](analysis_functions).
2) Add an menu entry for your analysis function within the relevant menu. All the menu entries are defined in the [iMaT.src.cli.menu_entries.py module](menu_entries).

#### Adding a menu entry for your new anylsis function

As an example, you can find the following menu entries function within the [iMaT.src.cli.menu_entries.py module](menu_entries):

    def submenu_single_musical_piece_statistical_analysis_page2_entries():
        """
        Submenu dedicated to advanced statistical analyses for a single piece of music.
    
        Level: Third Child (Parent: submenu_single_musical_piece_statistical_analysis_page1_entries)
    
        This function defines the fourth level menu for performing
        advanced statistical calculations on a single piece of music.
        """
        return {
            "menu_displayed_text": [
                "LOCATION: Start Menu >> Main Menu: Individual Piece >> Statistical Analysis Tools (Page 2)",
                "Please make a selection from the options below by entering the entry index number:",
                "Which menu item should be executed? (<No. of menu item>): ",
                ["Menu item", "<Explanation>"],
            ],
            "menu_entries": [
                ["ADV: Activity Index", (analysis_workflow_single_musical_piece, analysis_advanced_calculate_activity_rate), "<Calculates ratio of notes to rests [= Activity Index]>"],
                ["ADV: Pitches vs Pitch Classes/Dur.", (analysis_workflow_single_musical_piece, analysis_advanced_compare_pitches_and_pitch_classes_per_duration), "<Compares pitch & pitch class counts per duration, including pitch to pitch class ratio>"],
                ["BACK: Return to Last Menu", 'back', "<Returns to previous menu>"],
            ]
        }

To add your analysis function 'my_new_analysis_function' to the menu displayed above, simply add the function name as a menu entry to the list:

    def submenu_single_musical_piece_statistical_analysis_page2_entries():
        """
        Submenu dedicated to advanced statistical analyses for a single piece of music.
    
        Level: Third Child (Parent: submenu_single_musical_piece_statistical_analysis_page1_entries)
    
        This function defines the fourth level menu for performing
        advanced statistical calculations on a single piece of music.
        """
        return {
            "menu_displayed_text": [
                "LOCATION: Start Menu >> Main Menu: Individual Piece >> Statistical Analysis Tools (Page 2)",
                "Please make a selection from the options below by entering the entry index number:",
                "Which menu item should be executed? (<No. of menu item>): ",
                ["Menu item", "<Explanation>"],
            ],
            "menu_entries": [
                ["ADV: Activity Index", (analysis_workflow_single_musical_piece, analysis_advanced_calculate_activity_rate), "<Calculates ratio of notes to rests [= Activity Index]>"],
                ["ADV: Pitches vs Pitch Classes/Dur.", (analysis_workflow_single_musical_piece, analysis_advanced_compare_pitches_and_pitch_classes_per_duration), "<Compares pitch & pitch class counts per duration, including pitch to pitch class ratio>"],
    ------>     ["ADV: My function", (analysis_workflow_single_musical_piece, my_new_analysis_function), "<This is a new analysis function>"],
                ["BACK: Return to Last Menu", 'back', "<Returns to previous menu>"],
            ]
        }

Your new analysis function will now be displayed within I-MaT! If your code does not work properly, don't worry. The exception part of your function will tell you what to change!

Please contact the author of this documentation via GitHub or per mail (imat.inquiries[at]gmail.com), if you want to contribute to the tool, so that everyone can profit from your ideas. :)

I hope you enjoy contributing to the Interactive Music Analysis Tool I-MaT!
