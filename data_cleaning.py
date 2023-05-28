import pandas as pd
import requests
from math import radians, sin, cos, sqrt, atan2
from collections import defaultdict
import os

# Directory path containing the CSV files
directory = os.path.join(os.getcwd(), "Data")
print(directory)
# Initialize an empty list to store data from CSV files
all_data = []

# Loop through all files in the directory
for filename in os.listdir(directory):
    print(filename)
    if filename.endswith(".csv"):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        
        data = pd.read_csv(file_path, encoding='latin-1')
        
        # Append the DataFrame to the list
        all_data.append(data)

# Concatenate all DataFrames into one
combined_data = pd.concat(all_data, ignore_index=True)

# Print the combined DataFrame
print(combined_data)

combined_data.head()
