from analysis import (
    load_raw_data,
    get_dataset_summary,
    get_missing_value_report,
    get_city_distribution,
    get_duplicate_report
)
import pandas as pd

df = load_raw_data()

# print("\nSUMMARY")
# print(get_dataset_summary(df))

# print("\nMISSING VALUES")
# print(get_missing_value_report(df).head(10))

# print("\nTOP 10 CITIES")
# print(get_city_distribution(df).head(10))

# print(df["rating"].dtype)

# print("\nUnique Rating Examples:")
# print(df["rating"].sample(20).tolist())

# print("\nTop Rating Values:")
# print(df["rating"].value_counts().head(20))

# rating_numeric = pd.to_numeric(
#     df["rating"],
#     errors="coerce"
# )

# print(
#     "Non-numeric ratings:",
#     rating_numeric.isna().sum()
# )

# print(df[df["rating"] == "NEW"][["rating", "rating_count"]].head(20))

# print(df[df["rating"] == 0][["rating", "rating_count"]].head(20))

# print(
#     df[df["rating"] == "NEW"]["rating_count"]
#     .value_counts()
#     .head(10)
# )

# print(
#     df[df["rating"] == 0]["rating_count"]
#     .value_counts()
#     .head(10)
# )

# print(df["cost_for_two"].dtype)

# print(df["cost_for_two"].describe())

# print(df["cost_for_two"].isnull().sum())

# print(df["cost_for_two"].value_counts().head(20))


# print(
#     df[df["cost_for_two"] == 0][
#         ["name", "city", "area", "cost_for_two"]
#     ].head(20)
# )


# print(
#     df.nlargest(
#         20,
#         "cost_for_two"
#     )[
#         [
#             "name",
#             "city",
#             "cost_for_two",
#             "rating"
#         ]
#     ]
# )


# duplicate_report = get_duplicate_report(df)

# print("\nEXACT DUPLICATES")
# print(duplicate_report["exact_duplicates"])

# print("\nOUTLET DUPLICATES")
# print(duplicate_report["outlet_duplicates"])

# print("\nTOP RESTAURANT CHAINS")
# print(
#     duplicate_report["top_restaurant_chains"]
# )

cities = sorted(df["city"].unique())

for city in cities:
    print(city)