from analysis import load_raw_data

from data_cleaning import (
    clean_data,
    save_processed_data
)

from config import PROCESSED_DATA_PATH
import pandas as pd

def main():
    df = load_raw_data()

    cleaned_df = clean_data(df)

    save_processed_data(
        cleaned_df
    )

    df_check = pd.read_parquet(
        PROCESSED_DATA_PATH
    )
    
    print(
        "Cleaning pipeline completed successfully."
    )


if __name__ == "__main__":
    main()