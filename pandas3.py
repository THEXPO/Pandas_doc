import pandas as pd

# All the basic functions that will be used 90% of the time

data = {
    "ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 29],
    "Department": ["HR", "IT", "Finance", "IT", "HR"],
    "Salary": [50000, 60000, 75000, 80000, 52000]
}

df = pd.DataFrame(data)
print(df)


df = pd.DataFrame(data)
df

#Basic Info

df.head()        # First 5 rows
df.tail(3)       # Last 3 rows
df.shape         # (rows, columns)
df.columns       # Column names
df.dtypes        # Data types
df.info()        # Summary (non-null, dtype, memory)
df.describe()    # Stats summary (mean, std, min, max, etc.)

#Selecting Data

df['Name']                   # Single column
df[['Name','Salary']]        # Multiple columns
df.loc[2]                    # Row by label (index=2)
df.iloc[2]                   # Row by position
df.loc[1, 'Age']             # Specific cell (row 1, column "Age")
df[['Name','Department']].head(3)   # Subset

#Filtering Data

df[df['Age'] > 30]                       # Age > 30
df[(df['Department']=='IT') & (df['Salary'] > 65000)]
df[df['Department'].isin(['HR','Finance'])]
df[df['Name'].str.contains("a", case=False)]

#Handling Missing Data
df2 = df.copy()
df2.loc[2, 'Salary'] = None   # Add a missing value
df2.isnull().sum()            # Count missing
df2.fillna(0)                 # Replace with 0
df2.fillna(df2['Salary'].mean())  # Replace with mean
df2.dropna()                  # Drop missing rows

#Adding and Modifying Data

df['Bonus'] = df['Salary'] * 0.1       # New column
df.loc[0, 'Age'] = 26                  # Update value
df.drop('Bonus', axis=1, inplace=True) # Drop column
df.drop(3, axis=0, inplace=True)       # Drop row (row index 3)

#Sorting
df.sort_values(by='Age', ascending=True)     # Sort by Age
df.sort_values(by=['Department','Salary'], ascending=[True, False])   # Multiple columns
df.sort_index(ascending=False)               # Sort by index

#GroupBy & Aggregation
df.groupby('Department')['Salary'].mean()
df.groupby('Department').agg({'Salary':'mean','Age':'max'})

#Merging & Concatenation
dept_info = pd.DataFrame({
    "Department": ["HR","IT","Finance"],
    "Manager": ["John","Sarah","Mike"]
})

# Merge
pd.merge(df, dept_info, on="Department", how="left")

# Concat
df_part1 = df.iloc[:2]
df_part2 = df.iloc[2:]
pd.concat([df_part1, df_part2])

#Time Series
df['Date'] = pd.date_range("2024-01-01", periods=len(df), freq="M")
df.set_index('Date').resample('Y')['Salary'].mean() # Resample by year
df['Salary'].rolling(2).mean() # Rolling mean

# Apply & Lambda
df['Age*2'] = df['Age'].apply(lambda x: x*2)
df.apply(lambda row: row['Salary']/row['Age'], axis=1)

#Useful functions
df['Department'].value_counts()  # Frequency
df['Salary'].nlargest(3)         # Top 3 salaries
df.sample(2)                     # Random rows
df.duplicated()                  # Check duplicates
df.drop_duplicates(inplace=True) # Remove duplicates

#Summary & Stats
df['Salary'].mean()        # Average salary
df['Age'].max()            # Maximum age
df['Department'].value_counts()   # Frequency of each department

