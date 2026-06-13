from analysis import load_raw_data
from data_cleaning import clean_data

df = load_raw_data()

cleaned_df = clean_data(df)

print("Rows:", len(cleaned_df))

print("Cities:", cleaned_df["city"].nunique())

print("Missing Ratings:", cleaned_df["rating"].isna().sum())

print("Missing Costs:", cleaned_df["cost_for_two"].isna().sum())

print("Average Rating:", round(cleaned_df["rating"].mean(), 2))

print("Average Cost:", round(cleaned_df["cost_for_two"].mean(), 2))