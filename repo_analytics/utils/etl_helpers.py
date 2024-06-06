"""helper functions for ETL process"""
import os
import json
def combine_json_files(input_folder_path: str) -> dict:
    """
    Combine all JSON files into one large dictonary
    Input: a folder path containing all JSON files
    Output: a dictionary with all key-value pairs from the JSON files
    """
    json_files = sorted([file for file in os.listdir(input_folder_path) if file.endswith('.json')])
    # Initialize an empty dictionary to store the combined data
    combined_data = {}
    # Loop over the list of files
    for _, js in enumerate(json_files):
        # Construct the full file path
        file_path = os.path.join(input_folder_path, js)
        # Read the file
        with open(file_path) as json_file:
            data = json.load(json_file)
        # update the data to the combined_data dictionary
        combined_data.update(data)
    return combined_data
