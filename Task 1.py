# Step 1: Import necessary libraries
import pandas as pd

# Step 2: Load the dataset
df = pd.read_csv("Mall_Customers.csv")

# Step 3: Display basic info
print(" *** Initial Dataset Info:")
print(df.info())
print("\n *** First 5 rows of data:")
print(df.head())



# Step 4: Check for missing values
print("\n *** Missing Values Before Cleaning:")
print(df.isnull().sum())


# Step 5: Handle missing values (example handling if any exist)
if df['Age'].isnull().sum() > 0:
    df['Age'].fillna(df['Age'].mean(), inplace=True)

if df['Gender'].isnull().sum() > 0:
    df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)

# Step 6: Remove duplicate rows
df.drop_duplicates(inplace=True)


# Step 7: Standardize text data (e.g., Gender column)
if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].str.strip().str.lower()

# Step 8: Rename columns to be consistent
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')


# Step 9: Fix data types
if 'age' in df.columns:
    df['age'] = df['age'].astype(int)


# Step 10: Final check after cleaning
print("\n *** Cleaned Dataset Info:")
print(df.info())

print("\n *** First 5 rows after cleaning:")
print(df.head())

# Step 11: Check for missing values again
print("\n ***Missing Values After Cleaning:")
print(df.isnull().sum())

# Step 12: Save the cleaned dataset
df.to_csv("Mall_Customers_Cleaned.csv", index=False)
print("\n *** Cleaned dataset saved as 'Mall_Customers_Cleaned.csv'")


# Step 13: Summary of cleaning
print("\n📋 SUMMARY OF CLEANING STEPS:")
print("""
1️. Filled missing values in 'Age' with mean and in 'Gender' with mode.
2️. Removed duplicate records.
3️. Standardized text data (e.g., all gender values in lowercase).
4️. Renamed all column headers to lowercase with underscores.
5️. Ensured correct data types (Age as int, etc.).
6️. Saved cleaned dataset for analysis or modeling.
""")
