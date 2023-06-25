import sys
import traceback

from src.cli.cli_menu_static_text import text_general_title


# Set up logging
# logging.basicConfig(filename='error_log.txt', level=logging.ERROR)


def text_exception_general(e: Exception) -> str:

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
            "In file: " + file_name +
            "\nIn function: " + function_name +
            "\nError in line: " + str(line_number) +
            "\nError code: " + str(e) +
            "\n\nIf the problem persists, please contact the person responsible for the project via GitHub.\n\n"
            "Support: https://github.com/sebastian-eck"
    )

    return message


def handle_error(e: Exception) -> None:

    print(text_general_title())

    # Generate the error message
    message = text_exception_general(e)

    # Print user-friendly error message
    print(message)

    input("<To continue, please press Enter>")

    # # Log the error details for debugging
    # logging.error(message, exc_info=True)
