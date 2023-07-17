"""
conversion.main.py
==================

This module provides functionality to convert multiple music files from a user-selected folder to a user-selected format.

The main function in this module is convert_multiple_files_filetype(). This function allows the user to select a
folder containing music files and choose a format to convert these files into. The function will then convert each
file in the folder into the selected format. Any errors or issues encountered during the conversion process are
logged to specific .xlsx files for easy tracking and debugging.

Other utility functions imported from the src.conversion.utils and src.utils.error_handling modules are used to handle
various tasks such as creating log entries, selecting conversion formats and folders, displaying success rates, and
handling exceptions.

Functions
---------
- convert_multiple_files_filetype: Convert multiple music files from a user-selected folder to a user-selected format.

Utilities:
----------
- 'create_log_entry': Used to create log entries in the .xlsx files for errors occurred during parsing and conversion.
- 'display_parseable_files_in_folder': Displays all parsable music files in a selected folder.
- 'display_success_rate': Calculates and displays the success rate of the conversion process.
- 'select_conversion_format': Prompts the user to select a conversion format from the available options.
- 'select_folder': Prompts the user to select a folder containing music files for conversion.
- 'handle_error': Handles any exceptions that occur during the execution of the function and displays the error to the user.
"""
import os
import os.path
from datetime import datetime

from music21 import converter
from openpyxl import Workbook
from tqdm import tqdm

from iMaT.src.conversion.utils import create_log_entry, display_parseable_files_in_folder, display_success_rate, \
    select_conversion_format, select_folder
from iMaT.src.utils.error_handling import handle_error


def convert_multiple_files_filetype():
    """
    Convert multiple music files from a user-selected folder to a user-selected format.

    This function first lists all parsable music files in a user-selected folder.
    Then it prompts the user to select a conversion format from the available options.
    The function then attempts to convert each file to the selected format and saves them in a newly created directory.
    Any failures during the parsing and conversion processes are logged to respective .xlsx files.

    Returns
    -------
    None

    Raises
    ------
    Exception
        Any exception that occurs during the execution of the function is handled and displayed to the user.

    Note
    ----
    The function can convert files to different formats based on the options provided by the music21 converter.
    The available options include 'musicxml', 'midi', 'braille', etc.
    Not all formats may be available for all files. If a conversion is not possible, an error will be logged.
    """
    try:
        # get the file directory
        folder_path = select_folder()
        if folder_path is None:
            return

        parsable_files = display_parseable_files_in_folder(folder_path)

        conversion_format = select_conversion_format()

        conversion_dir = os.path.join(folder_path, "converted_" + datetime.now().strftime("%Y%m%d_%H%M%S"))
        os.mkdir(conversion_dir)

        # initialize logging .xlsx-files
        workbook1 = Workbook()
        workbook1.save(conversion_dir + r'\parsing_log.xlsx')

        workbook2 = Workbook()
        workbook2.save(conversion_dir + r'\conversion_log.xlsx')

        num_files = len(parsable_files)
        num_converted = 0
        files_status = []

        print("\nConverting files...")
        for file in tqdm(parsable_files, ncols=70):  # Wrap parsable_files with tqdm for progress bar
            try:
                file_path = os.path.join(folder_path, file)
                score = converter.parse(file_path)
                try:
                    converted_file_path = os.path.join(conversion_dir,
                                                       os.path.splitext(os.path.basename(file))[0] + conversion_format)
                    fp = score.write(conversion_format, fp=converted_file_path)
                    num_converted += 1
                    files_status.append([file, "<successfully converted>"])
                except Exception as e:
                    files_status.append([file, str(e)])
                    list = [file_path, str(e)]
                    create_log_entry(list, conversion_dir + '\conversion_log.xlsx')
            except Exception as e:
                files_status.append([file, str(e)])
                list = [file_path, str(e)]
                create_log_entry(list, conversion_dir + '\parsing_log.xlsx')

        display_success_rate(files_status, num_converted, num_files)

    except Exception as e:
        handle_error(e)