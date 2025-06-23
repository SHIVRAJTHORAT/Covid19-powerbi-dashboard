from sqlalchemy import create_engine
import pandas as pd

# Load data
df = pd.read_csv("covid_data_output.csv")
df['LastUpdated'] = pd.to_datetime(df['LastUpdated'], unit='ms')

# ✅ Correct connection details
username = 'postgres'        # Your actual PostgreSQL username
password = 'Shivraj%40123'   # Replace with your PostgreSQL password
host = 'localhost'           # Usually localhost unless using remote DB
port = '5432'                # Default PostgreSQL port
database = 'covid_db'        # Your database name

# ✅ Correct connection string
engine = create_engine('postgresql+psycopg2://postgres:Shivraj%40123@localhost:5432/covid_db')


# Push to DB
df.to_sql('covid_summary', engine, if_exists='replace', index=False)

print("✅ Data pushed successfully!")
