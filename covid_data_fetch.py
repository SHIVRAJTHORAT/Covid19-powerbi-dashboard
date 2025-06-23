import requests
import pandas as pd

# Step 1: API URL
url = "https://disease.sh/v3/covid-19/countries"

# Step 2: Fetch Data
response = requests.get(url)

# Step 3: Check for successful response
if response.status_code == 200:
    data = response.json()
    print("✅ Data fetched successfully!\n")
else:
    print(f"❌ Failed to fetch data. Status Code: {response.status_code}")

# Step 4: Convert JSON to DataFrame
df = pd.json_normalize(data)

# Step 5: Filter important fields
df = df[['country', 'cases', 'recovered', 'deaths', 'active', 'updated']]
df.columns = ['Country', 'Confirmed', 'Recovered', 'Deaths', 'Active', 'LastUpdated']

# Step 6: Show top 5 records
print(df.head())

df.to_csv('covid_data_output.csv', index=False)
print("📁 Data saved to covid_data_output.csv")


from sqlalchemy import create_engine
import pandas as pd

# Load the cleaned CSV
df = pd.read_csv("covid_data_output.csv")

# Convert timestamp column
df['LastUpdated'] = pd.to_datetime(df['LastUpdated'], unit='ms')

# PostgreSQL connection info
username = 'Shivraj'        # replace with your username
password = 'Shivraj@123'   # replace with your password
host = 'localhost'
port = '5432'
database = 'covid_db'

# Create engine
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

# Push data
df.to_sql('covid_summary', engine, if_exists='replace', index=False)

print("✅ Data pushed to PostgreSQL successfully!")
