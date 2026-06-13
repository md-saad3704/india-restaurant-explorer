# ==========================================
# ANALYTICS AND DATA PROCESSING FUNCTIONS
# ==========================================

import pandas as pd

from config import (
DATA_PATH,
PROCESSED_DATA_PATH
)

# ==========================================
# DATA LOADING
# ==========================================

def load_raw_data():
    """
    Load raw Zomato dataset.
    Returns:
        pd.DataFrame
    """

    return pd.read_excel(DATA_PATH)


def load_clean_data():
    """
Load cleaned dataset.
    Returns:
        pd.DataFrame
    """

    return pd.read_parquet(
        PROCESSED_DATA_PATH
    )


# ==========================================
# DATASET AUDIT FUNCTIONS
# ==========================================

def get_dataset_summary(df):
    """
    Generate dataset summary.

    Args:
        df (pd.DataFrame)

    Returns:
        dict
    """

    return {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "total_cities": df["city"].nunique(),
        "unique_restaurant_names": df["name"].nunique()
    }


def get_missing_value_report(df):
    """
    Generate missing value statistics.

    Args:
        df (pd.DataFrame)

    Returns:
        pd.DataFrame
    """
    report = pd.DataFrame({
        "column": df.columns,
        "missing_count": df.isnull().sum().values,
        "missing_percentage": (
            df.isnull().sum() / len(df) * 100
        ).round(2).values
    })

    return report.sort_values(
        by="missing_percentage",
        ascending=False
    )


def get_city_distribution(df):
    """
    Get restaurant count per city.

    Args:
        df (pd.DataFrame)

    Returns:
        pd.DataFrame
    """

    pd.DataFrame
    

    city_distribution = (
        df["city"]
        .value_counts()
        .reset_index()
    )

    city_distribution.columns = [
        "city",
        "restaurant_count"
    ]

    return city_distribution


# ==========================================
# DUPLICATE ANALYSIS
# ==========================================

def get_duplicate_report(df):
    """
Analyze duplicate records.

    Args:
        df (pd.DataFrame)

    Returns:
        dict
    """

    exact_duplicates = (
        df.duplicated()
        .sum()
    )

    outlet_duplicates = (
        df.duplicated(
            subset=[
                "name",
                "city",
                "area",
                "address"
            ]
        )
        .sum()
    )

    top_restaurant_chains = (
        df["name"]
        .value_counts()
        .head(20)
        .reset_index()
    )

    top_restaurant_chains.columns = [
        "restaurant_name",
        "outlet_count"
    ]

    return {
        "exact_duplicates": exact_duplicates,
        "outlet_duplicates": outlet_duplicates,
        "top_restaurant_chains": top_restaurant_chains
}
