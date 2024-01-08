# importing necessary modules

import pandas as pd
import zipfile
import urllib.request
import os


# 1. Download and unzip data

# using urllib.request.urlretrieve as mentioned
url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
path = "./exercises/mowesta-dataset-20221107.zip"
urllib.request.urlretrieve(url, path)

# Extracting CSV file from provided zip
with zipfile.ZipFile(path, 'r') as zip_ref:
    zip_ref.extractall('./exercises')

# Delete the ZIP file and extracted file
os.remove('./exercises/mowesta-dataset-20221107.zip')
os.remove('./exercises/README.pdf')



# Getting CSV from extracted files
# we Only use the columns "Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"

df = pd.read_csv("./exercises/data.csv", delimiter=";", decimal=",", index_col=False, 
                 usecols=["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"])


# 2. Reshape data
# Renaming "Temperatur in °C (DWD)" to "Temperatur" and Renaming "Batterietemperatur in °C" to "Batterietemperatur"
df = df.rename(columns={"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur"})

# 3. Transform data

# Transform temperatures in Celsius to Fahrenheit (formula is (TemperatureInCelsius * 9/5) + 32) in place (keep the same column names)
# Columns Temperatur and Batterietemperatur

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

df["Temperatur"] = celsius_to_fahrenheit(df["Temperatur"])
df["Batterietemperatur"] = celsius_to_fahrenheit(df["Batterietemperatur"])

# 4. Validate data


# Using validations as we see fit, e.g., for “Geraet” to be an id over 0
# Using fitting SQLite types (e.g., BIGINT, TEXT or FLOAT) for all columns


column_types = {
    'Geraet': int,
    'Hersteller': str,
    'Model': str,
    'Monat': int,
    'Temperatur': float,
    'Batterietemperatur': float,
    'Geraet aktiv': str
}
df = df.astype(column_types)

# Writing data into a SQLite database called “temperatures.sqlite”, in the table “temperatures”
df.to_sql('temperatures', 'sqlite:///temperatures.sqlite', if_exists='replace', index=False)

# Delete the CSV file 
os.remove('./exercises/data.csv')