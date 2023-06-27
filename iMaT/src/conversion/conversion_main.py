import os
import os.path
from datetime import datetime

from music21 import converter
from openpyxl import Workbook
from tqdm import tqdm

from src.conversion.conversion_utils import create_log_entry, display_parseable_files_in_folder, display_success_rate, \
    select_conversion_format, select_folder


def convert_multiple_files_filetype():
    """
    Main function for the conversion of music files found in a pre-defined folder.
    The function lists parsable music files, allows the user to select a conversion format,
    and attempts conversion. Successfully converted files are saved in a newly created directory.
    Failures during parsing and conversion are logged to respective .xlsx files.

    Returns
    -------
    None
    """
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
