import os
import zipfile
from collections import defaultdict

import pandas as pd


# Step 1: Extract the file folder hierarchy from the zip folder
def get_zip_info(zip_file_path):
    file_hierarchy = defaultdict(str)

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        for file in zip_ref.namelist():
            if file.endswith('.krn'):
                # remove file extension and the first level of hierarchy
                file_key = os.path.splitext(os.path.basename(file))[0]
                file_path = os.path.dirname(file)
                # store the file hierarchy in the dictionary
                file_hierarchy[file_key] = file_path.split(os.sep)[1:]
    return file_hierarchy

zip_file_path = 'C:\\Users\\sebas\\Downloads\\essen (1).zip'
file_hierarchy = get_zip_info(zip_file_path)

# Step 2: Add columns to the existing csv file
def update_csv(csv_file_path, file_hierarchy):
    df = pd.read_csv(csv_file_path)

    # find maximum number of hierarchy levels
    max_hierarchy_level = max(len(v) for v in file_hierarchy.values())
    for i in range(max_hierarchy_level):
        df[f'level_{i}'] = ''

    # fill the hierarchy information in the csv
    for index, row in df.iterrows():
        filename = row['filename']  # assuming 'filename' column contains the filenames
        if filename in file_hierarchy:
            for i, level in enumerate(file_hierarchy[filename]):
                df.at[index, f'level_{i}'] = level

    # save updated dataframe to csv
    df.to_csv(csv_file_path, index=False)

csv_file_path = 'path_to_your_csv_file.csv'
update_csv(csv_file_path, file_hierarchy)
