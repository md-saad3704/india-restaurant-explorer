import streamlit as st
import plotly.express as px

from analysis import (
    load_clean_data,
    get_city_kpis,
    get_top_cuisines,
    get_top_localities,
    get_highest_rated_areas,
    get_locality_cost_analysis,
    get_hidden_gems,
    get_top_restaurants,
    get_most_popular_restaurants
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Zomato India Restaurant Explorer",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():
    return load_clean_data()

df = load_data()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("Zomato Explorer")

cities = sorted(
    df["city"]
    .dropna()
    .unique()
)

selected_city = st.sidebar.selectbox(
    "Select City",
    cities
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("Zomato India Restaurant Explorer")

st.markdown(
    f"### Exploring Restaurants in {selected_city}"
)

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

kpis = get_city_kpis(
    df,
    selected_city
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Restaurants",
    f"{kpis['total_restaurants']:,}"
)

col2.metric(
    "Avg Rating",
    kpis["average_rating"]
)

col3.metric(
    "Avg Cost",
    f"₹{kpis['average_cost']}"
)

col4.metric(
    "Top Cuisine",
    kpis["top_cuisine"]
)

col5.metric(
    "Cuisine Types",
    kpis["total_cuisines"]
)

# --------------------------------------------------
# CUISINE + LOCALITY DISTRIBUTION
# --------------------------------------------------

st.markdown("---")

col1, col2 = st.columns(
    [1, 1],
    gap="large"
)

# Top Cuisines

with col1:

    with st.container(border=True):

        st.subheader("Top Cuisines")

        top_cuisines = get_top_cuisines(
            df,
            selected_city
        )

        fig = px.bar(
            top_cuisines,
            x="restaurant_count",
            y="cuisine",
            orientation="h",
            title=f"Top Cuisines in {selected_city}"
        )

        fig.update_layout(
            height=500,
            title_x=0.5
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# Top Areas

with col2:

    with st.container(border=True):

        st.subheader("Top Restaurant Areas")

        top_localities = get_top_localities(
            df,
            selected_city
        )

        fig = px.bar(
            top_localities,
            x="restaurant_count",
            y="area",
            orientation="h",
            title=f"Top Restaurant Areas in {selected_city}"
        )

        fig.update_layout(
            height=500,
            title_x=0.5
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# --------------------------------------------------
# LOCALITY ANALYTICS
# --------------------------------------------------

st.markdown("---")

col1, col2 = st.columns(
    [1, 1],
    gap="large"
)

# Highest Rated Areas

with col1:

    with st.container(border=True):

        st.subheader("Highest Rated Areas")

        highest_rated = get_highest_rated_areas(
            df,
            selected_city
        )

        fig = px.bar(
            highest_rated,
            x="average_rating",
            y="area",
            orientation="h",
            title=f"Highest Rated Areas in {selected_city}"
        )

        fig.update_layout(
            height=500,
            title_x=0.5
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# Most Expensive Areas

with col2:

    with st.container(border=True):

        st.subheader("Most Expensive Areas")

        locality_costs = get_locality_cost_analysis(
            df,
            selected_city
        )

        fig = px.bar(
            locality_costs.head(10),
            x="average_cost",
            y="area",
            orientation="h",
            title=f"Most Expensive Areas in {selected_city}"
        )

        fig.update_layout(
            height=500,
            title_x=0.5
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# --------------------------------------------------
# HIDDEN GEMS
# --------------------------------------------------

st.markdown("---")

with st.container(border=True):

    st.subheader("Hidden Gems")

    hidden_gems = get_hidden_gems(
        df,
        selected_city
    )

    hidden_gems_display = hidden_gems.rename(
        columns={
            "name": "Restaurant",
            "area": "Area",
            "cuisine": "Cuisine",
            "rating": "Rating",
            "rating_count": "Votes",
            "cost_for_two": "Cost for Two",
            "weighted_rating": "Weighted Rating"
        }
    )

    st.dataframe(
        hidden_gems_display,
        use_container_width=True,
        hide_index=True
    )

# --------------------------------------------------
# RESTAURANT LEADERBOARDS
# --------------------------------------------------

st.markdown("---")

st.subheader("Restaurant Leaderboards")

col1, col2 = st.columns(
    [1, 1],
    gap="large"
)

# Top Restaurants

with col1:

    with st.container(border=True):

        st.subheader("Top Restaurants")

        top_restaurants = get_top_restaurants(
            df,
            selected_city
        )

        top_restaurants_display = (
            top_restaurants.rename(
                columns={
                    "name": "Restaurant",
                    "area": "Area",
                    "rating": "Rating",
                    "rating_count": "Votes",
                    "cost_for_two": "Cost",
                    "weighted_rating": "Score"
                }
            )
        )

        st.dataframe(
            top_restaurants_display,
            use_container_width=True,
            hide_index=True
        )

# Most Popular Restaurants

with col2:

    with st.container(border=True):

        st.subheader("Most Popular Restaurants")

        popular_restaurants = (
            get_most_popular_restaurants(
                df,
                selected_city
            )
        )

        popular_restaurants_display = (
            popular_restaurants.rename(
                columns={
                    "name": "Restaurant",
                    "area": "Area",
                    "rating": "Rating",
                    "rating_count": "Votes",
                    "cost_for_two": "Cost"
                }
            )
        )

        st.dataframe(
            popular_restaurants_display,
            use_container_width=True,
            hide_index=True
        )