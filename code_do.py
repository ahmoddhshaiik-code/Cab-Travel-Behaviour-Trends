import pandas as pd

# Load dataset
df = pd.read_excel("cab_data.xlsx")

# -----------------------------------
# 1. Clean column names
# -----------------------------------
df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

# check column names
print(df.columns)

# -----------------------------------
# 2. Check missing values
# -----------------------------------
print(df.isnull().sum())

# fill missing purpose with mode
df['purpose'] = df['purpose'].fillna(df['purpose'].mode()[0])

# fill missing miles with median
df['miles'] = df['miles'].fillna(df['miles'].median())

# -----------------------------------
# 3. Convert date columns
# -----------------------------------
df['start_date'] = pd.to_datetime(df['start_date'])
df['end_date'] = pd.to_datetime(df['end_date'])

# -----------------------------------
# 4. Create new feature columns
# -----------------------------------

# trip duration in minutes
df['trip_duration'] = (df['end_date'] - df['start_date']).dt.total_seconds() / 60

# extract hour
df['hour'] = df['start_date'].dt.hour

# extract day name
df['day'] = df['start_date'].dt.day_name()

# extract month
df['month'] = df['start_date'].dt.month_name()

# weekend column
df['is_weekend'] = df['day'].isin(['Saturday', 'Sunday'])

# route column
df['route'] = df['start'] + ' - ' + df['stop']

# high distance trip
df['high_distance'] = df['miles'] > 20

# -----------------------------------
# 5. Basic Analysis
# -----------------------------------

# top starting locations
print("Top Start Locations")
print(df['start'].value_counts().head(10))

# top stop locations
print("Top Stop Locations")
print(df['stop'].value_counts().head(10))

# top routes
print("Top Routes")
print(df['route'].value_counts().head(10))

# category count
print("Category Count")
print(df['category'].value_counts())

# purpose count
print("Purpose Count")
print(df['purpose'].value_counts())

# average miles
print("Average Miles")
print(df['miles'].mean())

# longest trips
print("Longest Trips")
print(df[['start','stop','miles']].sort_values(by='miles', ascending=False).head(10))

# hourly trips
print("Trips by Hour")
print(df['hour'].value_counts().sort_index())

# day wise trips
print("Trips by Day")
print(df['day'].value_counts())

# -----------------------------------
# 6. Save cleaned dataset
# -----------------------------------
df.to_excel("cab_cleaned_output.xlsx", index=False)

print("File saved successfully")



----------------------
import pandas as pd

# Load cleaned dataset
df = pd.read_excel("cab_cleaned_output.xlsx")

# -----------------------------------
# 1. Check duplicates
# -----------------------------------
print("Duplicate rows:")
print(df.duplicated().sum())

# View duplicate rows
print(df[df.duplicated()])

# Remove duplicates
df = df.drop_duplicates()

# -----------------------------------
# 2. Check datatypes
# -----------------------------------
print("Datatypes before fixing:")
print(df.dtypes)

# -----------------------------------
# 3. Fix correct datatypes
# -----------------------------------

# datetime columns
df['start_date'] = pd.to_datetime(df['start_date'])
df['end_date'] = pd.to_datetime(df['end_date'])

# text columns
df['category'] = df['category'].astype(str)
df['start'] = df['start'].astype(str)
df['stop'] = df['stop'].astype(str)
df['purpose'] = df['purpose'].astype(str)
df['day'] = df['day'].astype(str)
df['month'] = df['month'].astype(str)
df['route'] = df['route'].astype(str)

# numeric columns
df['miles'] = pd.to_numeric(df['miles'])
df['trip_duration'] = pd.to_numeric(df['trip_duration'])
df['hour'] = pd.to_numeric(df['hour'])

# boolean column
df['is_weekend'] = df['is_weekend'].astype(bool)
df['high_distance'] = df['high_distance'].astype(bool)

# -----------------------------------
# 4. Final datatype check
# -----------------------------------
print("Datatypes after fixing:")
print(df.dtypes)

# -----------------------------------
# 5. Save final file
# -----------------------------------
df.to_excel("cab_final_ready.xlsx", index=False)

print("Final cleaned file saved")