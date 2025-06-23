CREATE TABLE covid_summary(
Country TEXT,
Confirmed INTEGER,
Recovered Integer,
Death Integer,
Active Integer,
LastUpdated Timestamp
);

select*from covid_summary limit 10;
