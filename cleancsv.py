import pandas as pd

# Load CSV
df = pd.read_csv("covid_data_output.csv")

# Show first few records
print(df.head())

# Convert 'LastUpdated' to datetime
df['LastUpdated'] = pd.to_datetime(df['LastUpdated'], unit='ms')

# Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# Fill missing values with 0
df.fillna(0, inplace=True)

# Top 5 countries with highest confirmed cases
top_cases = df.sort_values(by='Confirmed', ascending=False).head(5)
print("\nTop 5 Countries by Confirmed Cases:\n", top_cases[['Country', 'Confirmed']])

# Global totals
global_summary = df[['Confirmed', 'Recovered', 'Deaths', 'Active']].sum()
print("\n🌐 Global Summary:\n", global_summary)

import matplotlib.pyplot as plt

# Bar plot of top 5 affected countries
top_cases.plot(x='Country', y='Confirmed', kind='bar', title='Top 5 COVID-19 Affected Countries')
plt.xlabel("Country")
plt.ylabel("Confirmed Cases")
plt.tight_layout()
plt.show()

