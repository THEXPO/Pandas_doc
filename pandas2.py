import pandas as pd

#importing & exporting data

#CSV

#To import CSV 

#Basic
df = pd.read_csv("data.csv")

# With options
df = pd.read_csv("data.csv", delimiter=",", header=0, index_col=0, usecols=['Name','Age'])

#To export CSV
df.to_csv("output.csv", index=False)   # index=False → don’t write row numbers


#Excel

#To import Excel
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

#To export Excel
df.to_excel("output.xlsx", sheet_name="Results", index=False)


#JSON

#To import JSON
df = pd.read_json("data.json")

#To export JSON
df.to_json("output.json", orient="records", lines=True)


#SQL Databases

#To import SQL Databases
import sqlite3
conn = sqlite3.connect("mydb.db")
df = pd.read_sql("SELECT * FROM users", conn)

#To export SQL Databases
df.to_sql("users_copy", conn, if_exists="replace", index=False)
