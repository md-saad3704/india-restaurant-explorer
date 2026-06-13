from analysis import (
load_raw_data
)

from data_cleaning import (
clean_data,
save_processed_data
)

def main():
    df = load_raw_data()

    cleaned_df = clean_data(df)

    save_processed_data(
        cleaned_df
    )

    print(
        "Cleaning pipeline completed successfully."
    )


if __name__ == "__main__":
    main()
