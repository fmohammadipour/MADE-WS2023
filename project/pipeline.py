# for this part you need to use kaggle api to get dataset 
# instruction on how to get API and use it can be found here : https://github.com/Kaggle/kaggle-api


import subprocess
import zipfile
import os
import shutil
import pandas as pd
import sqlite3


# Get Everything done for first dataset
# First step : Download the Kaggle dataset using the Kaggle API
# Define the command to download the dataset
command = 'kaggle datasets download -d synful/world-happiness-report'

# Execute the command using subprocess
subprocess.run(command, shell=True)

# Path to the downloaded ZIP file
zip_file_path = 'world-happiness-report.zip'

# Destination folder for extracted files
extract_folder = 'world-happiness-report'

# Extract the contents of the ZIP file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

# Access and read the CSV file
csv_file_path = os.path.join(extract_folder, '2019.csv')  # Path to the CSV file

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Second step : Perform operations, fix errors, and manipulate the DataFrame as needed

df = df.dropna()  # Remove rows with missing values

# Third step : Save DataFrame as SQLite Database in the /data directory
data_folder = 'data'  # Relative path to the data directory

# Create the /data directory if it doesn't exist
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# SQLite database file path
sqlite_file = os.path.join(data_folder, '2019report.sqlite')

# Create a connection to SQLite database
conn = sqlite3.connect(sqlite_file)

# Store DataFrame in the SQLite database
df.to_sql('world_happiness_2019', conn, index=False, if_exists='replace')

# last step : time to clean up
# Close the connection
conn.close()

# Delete the ZIP file and extracted folder
os.remove(zip_file_path)
shutil.rmtree(extract_folder)


# Get Everything done for Second dataset

# First step : Download the Kaggle dataset using the Kaggle API

# Define the command to download the dataset
command = 'kaggle datasets download -d usamabuttar/world-happiness-report-2005-present'

# Execute the command using subprocess
subprocess.run(command, shell=True)

# Path to the downloaded ZIP file
zip_file_path = 'world-happiness-report-2005-present.zip'

# Destination folder for extracted files
extract_folder = 'world-happiness-report-2005-present'

# Extract the contents of the ZIP file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

# Access and read the CSV file
csv_file_path = os.path.join(extract_folder, 'world happiness report.csv')  # Path to the CSV file

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Second step : Perform operations, fix errors, and manipulate the DataFrame as needed

df = df.dropna()  # Remove rows with missing values


# Third step : Save DataFrame as SQLite Database in the /data directory
data_folder = 'data'  # Relative path to the data directory

# SQLite database file path
sqlite_file = os.path.join(data_folder, 'world-happiness-report.sqlite')

# Create a connection to SQLite database
conn = sqlite3.connect(sqlite_file)

# Store DataFrame in the SQLite database
df.to_sql('world-happiness-report', conn, index=False, if_exists='replace')


# last step : time to clean up
# Close the connection
conn.close()

# Delete the ZIP file and extracted folder
os.remove(zip_file_path)
shutil.rmtree(extract_folder)