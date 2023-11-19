# Goal : Write data into a SQLite database called “trainstops.sqlite”, in the table “trainstops”


import pandas as pd
import io
import re
from sqlalchemy import create_engine

# SQLAlchemy is a popular library in Python used for working with databases. 
# The create_engine function is a key component of SQLAlchemy and is used to create a connection to a database. \
# use "pip install sqlalchemy" to install it

# Defines CSV URL mentioned in exercise 
csv_url = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
# Reads the CSV File into a DataFrame
df = pd.read_csv(csv_url, delimiter=';')

# First, drop the "Status" column
del df["Status"]

# Then, drop all rows with invalid values:

# Valid "Verkehr" values are "FV", "RV", "nur DPN"
valid_verkehr = {"FV": None, "RV": None, "nur DPN": None}

# Empty cells are considered invalid
df = df.dropna(axis=0, how='any')  
df = df.query("Verkehr in @valid_verkehr")

# Valid "Laenge", "Breite" values are geographic coordinate system values between and including -90 and 90

df['Laenge'] = df['Laenge'].str.replace(r',', '.')
df['Breite'] = df['Breite'].str.replace(r',', '.')

df['Laenge'] = df['Laenge'].astype(float)
df = df.query("-90 <= Laenge <= 90")

df['Breite'] = df['Breite'].astype(float)
df = df.query("-90 <= Breite <= 90")

# Valid "IFOPT" values follow this pattern:
# <exactly two characters>:<any amount of numbers>:<any amount of numbers><optionally another colon followed by any amount of numbers>
# This is not the official IFOPT standard, please follow our guidelines and not the official standard

pattern = re.compile(r"^\w{2}:\d+:\d+(?::\d+)?$")
valid_ifopt = df["IFOPT"].astype(str).str.contains(pattern, regex=True)
df = df.loc[valid_ifopt]

# this part was for showing unique values to be sure of pattern definition
# unique_ifopt = df["IFOPT"].unique()
# print("Unique IFOPT values after filtering based on pattern :")
# print(unique_ifopt)


table_name = "trainstops"

column_types = {
    "DS100": str,
    "EVA_NR": int,
    "Laenge": float,
    "Breite": float,
    "Verkehr": str,
    "IFOPT": str,
    "NAME": str,
    "Betreiber_Name": str,
    "Betreiber_Nr": int
    
    
}
df = df.astype(column_types)

# Create table and insert data using sqlalchemy and create_engine
df.to_sql(table_name, 'sqlite:///trainstops.sqlite', if_exists="replace", index=False)

