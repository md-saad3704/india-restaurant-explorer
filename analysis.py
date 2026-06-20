# ==========================================
# ANALYTICS AND DATA PROCESSING FUNCTIONS
# ==========================================

import pandas as pd


from config import (
    DATA_PATH,
    PROCESSED_DATA_PATH,
    MIN_AREA_RESTAURANTS,
    MIN_HIDDEN_GEM_VOTES,
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

    return pd.read_parquet(PROCESSED_DATA_PATH)


# ==========================================
# DATASET AUDIT FUNCTIONS
# ==========================================



RESTAURANT_COLUMNS = [
    "name",
    "area",
    "cuisine",
    "rating",
    "rating_count",
    "cost_for_two",
]



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
        "unique_restaurant_names": df["name"].nunique(),
    }


def get_missing_value_report(df):
    """
    Generate missing value statistics.

    Args:
        df (pd.DataFrame)

    Returns:
        pd.DataFrame
    """
    report = pd.DataFrame(
        {
            "column": df.columns,
            "missing_count": df.isnull().sum().values,
            "missing_percentage": (df.isnull().sum() / len(df) * 100).round(2).values,
        }
    )

    return report.sort_values(by="missing_percentage", ascending=False)


def get_city_distribution(df):
    """
    Get restaurant count per city.

    Args:
        df (pd.DataFrame)

    Returns:
        pd.DataFrame
    """

    city_distribution = df["city"].value_counts().reset_index()

    city_distribution.columns = ["city", "restaurant_count"]

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

    exact_duplicates = df.duplicated().sum()

    outlet_duplicates = df.duplicated(subset=["name", "city", "area", "address"]).sum()

    top_restaurant_chains = df["name"].value_counts().head(20).reset_index()

    top_restaurant_chains.columns = ["restaurant_name", "outlet_count"]

    return {
        "exact_duplicates": exact_duplicates,
        "outlet_duplicates": outlet_duplicates,
        "top_restaurant_chains": top_restaurant_chains,
    }


# ==========================================
# CITY-SPECIFIC ANALYSIS
# ==========================================


def get_city_data(df, city):
    """
    Filter dataset for a selected city.

    Args:
        df (pd.DataFrame)
        city (str)

    Returns:
        pd.DataFrame
    """

    city_df = df[df["city"] == city].copy()

    return city_df


# ==========================================
# CUISINE ANALYSIS
# ==========================================


def extract_cuisines(df):
    """
    Extract individual cuisines from a dataframe.

    Args:
        df (pd.DataFrame)

    Returns:
        pd.Series
    """

    cuisines = df["cuisine"].dropna().str.split(",").explode().str.strip()

    cuisines = cuisines[cuisines != ""]

    return cuisines


# ==========================================
# KPI GENERATION
# ==========================================


def get_city_kpis(df, city):
    """
    Generate KPI metrics for a city.

    Args:
        df (pd.DataFrame)
        city (str)

    Returns:
        dict
    """

    city_df = get_city_data(df, city)

    cuisines = extract_cuisines(city_df)

    kpis = {
        "total_restaurants": len(city_df),
        "average_rating": round(city_df["rating"].mean(), 2),
        "average_cost": int(round(city_df["cost_for_two"].mean())),
        "top_cuisine": cuisines.value_counts().idxmax(),
        "total_cuisines": cuisines.nunique(),
    }

    return kpis


# ==========================================
# TOP CUISINE ANALYSIS
# ==========================================


def get_top_cuisines(df, city, top_n=10):
    """
    Get most popular cuisines in a city.

    Args:
        df (pd.DataFrame)
        city (str)
        top_n (int)

    Returns:
        pd.DataFrame
    """

    city_df = get_city_data(df, city)

    cuisines = extract_cuisines(city_df)

    top_cuisines = cuisines.value_counts().head(top_n).reset_index()

    top_cuisines.columns = ["cuisine", "restaurant_count"]

    return top_cuisines


# ==========================================
# TOP LOCALITY ANALYSIS
# ==========================================


def get_top_localities(df, city, top_n=10):
    """
    Get localities with the highest
    restaurant concentration.

    Args:
        df (pd.DataFrame)
        city (str)
        top_n (int)

    Returns:
        pd.DataFrame
    """

    city_df = get_city_data(df, city)

    top_localities = city_df["area"].value_counts().head(top_n).reset_index()

    top_localities.columns = ["area", "restaurant_count"]

    return top_localities


# ==========================================
# LOCALITY COST ANALYSIS
# ==========================================


def get_locality_cost_analysis(df, city, min_restaurants=10, top_n=10):
    """
    Analyze average cost by locality.

    Args:
        df (pd.DataFrame)
        city (str)
        min_restaurants (int)

    Returns:
        pd.DataFrame
    """

    city_df = get_city_data(df, city)

    locality_analysis = (
        city_df.groupby("area")
        .agg(restaurant_count=("name", "count"), average_cost=("cost_for_two", "mean"))
        .reset_index()
    )

    locality_analysis = locality_analysis[
        locality_analysis["restaurant_count"] >= min_restaurants
    ]

    locality_analysis["average_cost"] = (
        locality_analysis["average_cost"].round().astype(int)
    )

    locality_analysis = locality_analysis.sort_values(
        by="average_cost", ascending=False
    ).reset_index(drop=True)

    locality_analysis = locality_analysis.head(top_n)

    return locality_analysis


# ==========================================
# HIGHEST RATED AREAS ANALYSIS
# ==========================================


def get_highest_rated_areas(df, city, min_restaurants=MIN_AREA_RESTAURANTS, top_n=10):
    """
    Get highest rated areas in a city.

    Args:
        df (pd.DataFrame)
        city (str)
        min_restaurants (int)
        top_n (int)

    Returns:
        pd.DataFrame
    """

    city_df = get_city_data(df, city)

    area_ratings = (
        city_df.groupby("area")
        .agg(restaurant_count=("name", "count"), average_rating=("rating", "mean"))
        .reset_index()
    )

    area_ratings = area_ratings[area_ratings["restaurant_count"] >= min_restaurants]

    area_ratings["average_rating"] = area_ratings["average_rating"].round(2)

    area_ratings = (
        area_ratings.sort_values(by="average_rating", ascending=False)
        .head(top_n)
        .reset_index(drop=True)
    )

    return area_ratings


# ==========================================
# RATING WEIGHTING FUNCTION
# ==========================================


def calculate_weighted_rating(rating, votes, average_rating, minimum_votes):
    """
    IMDb-style weighted rating.
    """

    return (votes / (votes + minimum_votes)) * rating + (
        minimum_votes / (votes + minimum_votes)
    ) * average_rating


# ==========================================
# HIDDEN GEMS ANALYSIS
# ==========================================


def get_hidden_gems(
    df, city, min_rating=4.0, max_cost=500, min_votes=MIN_HIDDEN_GEM_VOTES, top_n=20
):
    """
    Find affordable highly-rated restaurants.
    """

    city_df = get_city_data(df, city)

    city_average_rating = city_df["rating"].mean()

    gems = city_df[
        (city_df["rating"] >= min_rating)
        & (city_df["cost_for_two"] <= max_cost)
        & (city_df["rating_count"] >= min_votes)
    ].copy()

    gems["weighted_rating"] = gems.apply(
        lambda row: calculate_weighted_rating(
            rating=row["rating"],
            votes=row["rating_count"],
            average_rating=city_average_rating,
            minimum_votes=min_votes,
        ),
        axis=1,
    )

    gems = gems.sort_values(by="weighted_rating", ascending=False)


    gems["weighted_rating"] = gems["weighted_rating"].round(3)

    return gems[RESTAURANT_COLUMNS].head(top_n).reset_index(drop=True)


# ==========================================
# TOP RESTAURANTS ANALYSIS
# ==========================================


def get_top_restaurants(df, city, min_votes=MIN_HIDDEN_GEM_VOTES, top_n=10):
    """
    Get top restaurants in a city using
    weighted rating.

    Args:
        df (pd.DataFrame)
        city (str)
        min_votes (int)
        top_n (int)

    Returns:
        pd.DataFrame
    """

    city_df = get_city_data(df, city)

    city_average_rating = city_df["rating"].mean()

    restaurants = city_df[city_df["rating_count"] >= min_votes].copy()

    restaurants["weighted_rating"] = restaurants.apply(
        lambda row: calculate_weighted_rating(
            rating=row["rating"],
            votes=row["rating_count"],
            average_rating=city_average_rating,
            minimum_votes=min_votes,
        ),
        axis=1,
    )

    restaurants["weighted_rating"] = restaurants["weighted_rating"].round(3)

    restaurants = restaurants.sort_values(by="weighted_rating", ascending=False)

    return restaurants[RESTAURANT_COLUMNS].head(top_n).reset_index(drop=True)


# ==========================================
# MOST POPULAR RESTAURANTS ANALYSIS
# ==========================================


def get_most_popular_restaurants(df, city, top_n=10):
    """
    Get restaurants with the highest
    number of ratings.
    """

    city_df = get_city_data(df, city)

    restaurants = city_df.sort_values(by="rating_count", ascending=False)

    return restaurants[RESTAURANT_COLUMNS].head(top_n).reset_index(drop=True)


# ==========================================
# RESTAURANT SEARCH FUNCTION
# ==========================================


def search_restaurants(df, city, query, top_n=20):
    """
    Search restaurants by name.

    Args:
        df (pd.DataFrame)
        city (str)
        query (str)
        top_n (int)

    Returns:
        pd.DataFrame
    """

    city_df = get_city_data(df, city)

    results = city_df[city_df["name"].str.contains(query, case=False, na=False)].copy()

    return (
        results[RESTAURANT_COLUMNS]
        .sort_values(by=["rating_count", "rating"], ascending=[False, False])
        .head(top_n)
        .reset_index(drop=True)
    )



# ==========================================
# AREA ANALYSIS
# ==========================================

def get_city_areas(df, city):

    city_df = get_city_data(df, city)

    area_counts = city_df["area"].value_counts()

    valid_areas = area_counts[
        area_counts >=20
    ].index

    return sorted(valid_areas)

# ---------Gets Area's Data  


def get_area_data(df, city, area):
    """
    Filter dataset for
    selected city + area.
    """

    city_df = get_city_data(df, city)

    area_df = city_df[
        city_df["area"] == area
    ].copy()

    return area_df


# --------- Area's KPI Metrics

def get_area_kpis(df, city, area):
    """
    Generate KPI metrics
    for a selected area.
    """

    area_df = get_area_data(
        df,
        city,
        area
    )

    cuisines = extract_cuisines(
        area_df
    )

    return {
        "total_restaurants": len(area_df),
        "average_rating": round(
            area_df["rating"].mean(),
            2
        ),
        "average_cost": int(
            round(
                area_df["cost_for_two"].mean()
            )
        ),
        "top_cuisine": (
            cuisines.value_counts().idxmax()
            if len(cuisines) > 0
            else "N/A"
        ),
        "total_cuisines": cuisines.nunique(),
    }


# --------- Area's top Cuisine 

def get_area_top_cuisines(
    df,
    city,
    area,
    top_n=10
):
    """
    Top cuisines inside
    selected area.
    """

    area_df = get_area_data(
        df,
        city,
        area
    )

    cuisines = extract_cuisines(
        area_df
    )

    result = (
        cuisines
        .value_counts()
        .head(top_n)
        .reset_index()
    )

    result.columns = [
        "cuisine",
        "restaurant_count"
    ]

    return result


# --------- Area's Hidden gem

def get_area_hidden_gems(
    df,
    city,
    area,
    min_rating=4.0,
    max_cost=500,
    min_votes=MIN_HIDDEN_GEM_VOTES,
    top_n=10,
):

    area_df = get_area_data(df, city, area)

    area_average_rating = area_df["rating"].mean()

    gems = area_df[
        (area_df["rating"] >= min_rating)
        & (area_df["cost_for_two"] <= max_cost)
        & (area_df["rating_count"] >= min_votes)
    ].copy()

    gems["weighted_rating"] = gems.apply(
        lambda row: calculate_weighted_rating(
            rating=row["rating"],
            votes=row["rating_count"],
            average_rating=area_average_rating,
            minimum_votes=min_votes,
        ),
        axis=1,
    )

    gems = gems.sort_values(
        by="weighted_rating",
        ascending=False,
    )

    return gems[RESTAURANT_COLUMNS].head(top_n)



# --------- Area's top restaurant

def get_area_top_restaurants(
    df,
    city,
    area,
    min_votes=MIN_HIDDEN_GEM_VOTES,
    top_n=10,
):

    area_df = get_area_data(df, city, area)

    area_average_rating = area_df["rating"].mean()

    restaurants = area_df[
        area_df["rating_count"] >= min_votes
    ].copy()

    restaurants["weighted_rating"] = restaurants.apply(
        lambda row: calculate_weighted_rating(
            rating=row["rating"],
            votes=row["rating_count"],
            average_rating=area_average_rating,
            minimum_votes=min_votes,
        ),
        axis=1,
    )

    restaurants = restaurants.sort_values(
        by="weighted_rating",
        ascending=False,
    )

    return restaurants[RESTAURANT_COLUMNS].head(top_n)



# --------- Area's most popular Restaurants

def get_area_most_popular_restaurants(
    df,
    city,
    area,
    top_n=10,
):

    area_df = get_area_data(df, city, area)

    return (
        area_df
        .sort_values(
            by="rating_count",
            ascending=False
        )[RESTAURANT_COLUMNS]
        .head(top_n)
    )
    
    
    
#  --------- 



# ==========================================
# AREA RESTAURANT SEARCH
# ==========================================

def search_area_restaurants(
    df,
    city,
    area,
    query,
    top_n=20,
):
    """
    Search restaurants within
    a selected area.
    """

    area_df = get_area_data(
        df,
        city,
        area
    )

    results = area_df[
        area_df["name"].str.contains(
            query,
            case=False,
            na=False
        )
    ]

    return (
        results[RESTAURANT_COLUMNS]
        .sort_values(
            by=["rating_count", "rating"],
            ascending=[False, False]
        )
        .head(top_n)
        .reset_index(drop=True)
    )