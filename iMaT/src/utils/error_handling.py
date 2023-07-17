"""
Module: utils.error_handling.py
===============================

This module, which is part of the `utils` package, contains functions for handling and reporting errors in a detailed
and user-friendly manner. This allows for better debugging and understanding of any exceptions that occur during
the execution of the code.

Functions
---------
1. `text_exception_general(e: Exception) -> str`: This function takes an exception as an input and returns a detailed
   error message. The error message includes the file, function, and line number where the exception occurred, and
   also the exception message itself.

2. `handle_error(e: Exception) -> None`: This function also takes an exception as an input but instead of returning the
   error message, it prints the message to the console. This function utilizes `text_exception_general` to generate the
   error message.

Examples
--------
>>> try:
...     1 / 0  # Raises ZeroDivisionError
... except Exception as e:
...     handle_error(e)  # This will print a detailed error message to the console
"""
import sys
import traceback

from iMaT.src.constants import TITLE_TEXT


def text_exception_general(e: Exception) -> str:
    """
    Generate a detailed error message.

    This function extracts traceback information from an exception and generates a detailed error message.
    This includes information about the file, function and line number where the error occurred as well
    as the error message itself.

    Parameters
    ----------
    e : Exception
        The exception from which to generate the error message.

    Returns
    -------
    str
        A string containing the detailed error message.

    Raises
    ------
    Exception
        If there is an error during traceback extraction or error message creation.

    Examples
    --------
    >>> try:
    ...     1 / 0  # Raises ZeroDivisionError
    ... except Exception as e:
    ...     print(text_exception_general(e))
    """
    try:
        # Get the current traceback
        current_traceback = traceback.extract_tb(sys.exc_info()[2])

        # Get the last traceback record
        last_traceback_record = current_traceback[-1]

        # Extract the line number, function name, and file name
        line_number = last_traceback_record.lineno
        function_name = last_traceback_record.name
        file_name = last_traceback_record.filename

        # Generate the error message
        message = (
                "An error was encountered while executing the program:\n\n"
                "\nIn file: " + file_name +
                "\nIn function: " + function_name +
                "\nError in line: " + str(line_number) +
                "\nError code: " + str(e) +
                "\n\nIf the problem persists, please contact the person responsible for the project via GitHub.\n"
                "\nFor support contact: https://github.com/sebastian-eck\n"
        )

        return message

    except:
        pass


def handle_error(e: Exception) -> None:
    """
    Handle an error by displaying a detailed error message.

    This function takes an exception as input and prints a detailed error message to the console.
    The error message is generated using the `text_exception_general` function, and includes
    information about where the error occurred and the nature of the error.

    Parameters
    ----------
    e : Exception
        The exception to be handled.

    Returns
    -------
    None

    Raises
    ------
    Exception
        If there is an error during error message generation or printing.
    """
    try:
        print(TITLE_TEXT)

        # Generate the error message
        message = text_exception_general(e)

        # Print user-friendly error message
        print(message)

        input("<To continue, please press Enter>")

    except:
        pass
