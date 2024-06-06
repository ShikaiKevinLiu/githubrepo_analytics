"""helper functions for ETL process"""
import os
import json
from typing import Optional

def combine_json_files(input_folder_path: str, year: Optional[int] = None) -> dict:
    """
    Combine all JSON files into one large dictionary.
    If a year is specified, only combine files with filenames starting with the year.
    
    Input: 
    - input_folder_path: a folder path containing all JSON files
    - year: an optional year to filter files by their prefix
    
    Output: 
    - a dictionary with all key-value pairs from the JSON files
    """
    # Get a sorted list of JSON files in the directory
    json_files = sorted([file for file in os.listdir(input_folder_path) if file.endswith('.json')])
    
    # If a year is specified, filter files to include only those that start with the specified year
    if year is not None:
        json_files = [file for file in json_files if file.startswith("data_"+str(year))]
    
    # Initialize an empty dictionary to store the combined data
    combined_data = {}
    
    # Loop over the list of files
    for js in json_files:
        # Construct the full file path
        file_path = os.path.join(input_folder_path, js)
        # Read the file
        with open(file_path) as json_file:
            data = json.load(json_file)
        # Update the data to the combined_data dictionary
        combined_data.update(data)
    
    return combined_data

