import logging
import sys
import traceback

from src.constants import TITLE_TEXT

# Set up logging
logging.basicConfig(filename='error_logs/error_log.txt', level=logging.ERROR, format='%(asctime)s - '
                                                                                     '%(levelname)s - %(message)s')


def text_exception_general(e: Exception) -> str:
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
    try:
        print(TITLE_TEXT)

        # Generate the error message
        message = text_exception_general(e)

        # Print user-friendly error message
        print(message)

        input("<To continue, please press Enter>")

        # Log the error details for debugging
        logging.exception(message)

    except:
        pass
