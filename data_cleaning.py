# ==========================================
# DATA CLEANING PIPELINE
# ==========================================

import pandas as pd
import numpy as np

from datetime import (
datetime,
time
)

from config import (
PROCESSED_DATA_PATH
)

# ==========================================
# RESTAURANT NAME CLEANING
# ==========================================

def clean_restaurant_names(df):
    """
    Remove invalid restaurant names.
    Args:
        df (pd.DataFrame)

    Returns:
        pd.DataFrame
    """

    df = df.copy()

    invalid_mask = (
        df["name"].isna()
        |
        df["name"].apply(
            lambda x: isinstance(
                x,
                (datetime, time)
            )
        )
    )

    df = df[~invalid_mask]

    return df

# ==========================================
# RATING CLEANING
# ==========================================

def clean_rating_column(df):
    """
    Clean rating column.

    Rules:
        - NEW -> NaN
        - 0 -> NaN

    Args:
        df (pd.DataFrame)

    Returns:
        pd.DataFrame
    """

    df = df.copy()

    df["rating"] = df["rating"].replace(
        {
            "NEW": np.nan,
            0: np.nan,
            "0": np.nan
        }
    )  

    df["rating"] = pd.to_numeric(
        df["rating"],
        errors="coerce"
    )

    return df


# ==========================================
# COST CLEANING
# ==========================================

def clean_cost_column(df):
    """
    Clean cost_for_two column.

    Rules:
        - 0 -> NaN

    Args:
        df (pd.DataFrame)

    Returns:
        pd.DataFrame
    """

    df = df.copy()

    df["cost_for_two"] = (
        df["cost_for_two"]
        .replace(0, np.nan)
    )

    return df


# ==========================================
# CITY CLEANIN
# ==========================================

def clean_city_column(df):
    """
    Standardize city names.
    Args:
        df (pd.DataFrame)

    Returns:
        pd.DataFrame
    """

    df = df.copy()

    df["city"] = (
        df["city"]
        .astype(str)
        .str.strip()
    )

    return df


# ==========================================
# TEXT COLUMN CLEANING
# ==========================================

def clean_text_columns(df):
    """
    Standardize text-based columns.

    Args:
        df (pd.DataFrame)

    Returns:
        pd.DataFrame
    """
    pd.DataFrame


    df = df.copy()

    text_columns = [
        "name",
        "city",
        "area",
        "cuisine",
        "address",
        "telephone",
        "timings",
        "famous_food"
    ]

    for col in text_columns:

        if col in df.columns:

            df[col] = (
                df[col]
                .fillna("")
                .astype(str)
                .str.strip()
            )

    return df


# ==========================================
# MASTER CLEANING PIPELINE
# ==========================================

def clean_data(df):
    """
    Execute complete cleaning pipeline.
    Args:
        df (pd.DataFrame)

    Returns:
        pd.DataFrame
    """

    df = clean_restaurant_names(df)

    df = clean_rating_column(df)

    df = clean_cost_column(df)

    df = clean_city_column(df)

    df = clean_text_columns(df)

    return df


# ==========================================
# SAVE CLEANED DATA
# ==========================================

def save_processed_data(df):
    """
    Save cleaned dataset as parquet.
    Args:
        df (pd.DataFrame)

    Returns:
        None
    """

    df.to_parquet(
        PROCESSED_DATA_PATH,
        index=False
    )

