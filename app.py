import streamlit as st
import plotly.express as px

from utils import apply_space_theme


from styles import (
    PAGE_TITLE,
    OVERVIEW_CHART_HEIGHT,
    DATASET_DISCLAIMER,
    CUSTOM_CSS,
)

from analysis import (
    load_clean_data,
    get_city_kpis,
    get_top_cuisines,
    get_top_localities,
    get_highest_rated_areas,
    get_locality_cost_analysis,
    get_hidden_gems,
    get_top_restaurants,
    get_most_popular_restaurants,
    search_restaurants,
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(page_title=PAGE_TITLE, layout="wide")

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------


@st.cache_data
def load_data():
    return load_clean_data()


df = load_data()


# --------------------------------------------------
# COMPONENTS
# --------------------------------------------------


def page_title(title):

    st.markdown(
        f"""
        <h1 style="
            color:#00D4FF;
            font-family:Orbitron;
            letter-spacing:2px;
        ">
            {title}
        </h1>
        """,
        unsafe_allow_html=True,
    )


def section_title(title, color="#00D4FF"):
    st.markdown(
        f"""
        <h2 style="
            color:{color};
            font-family:Orbitron;
            letter-spacing:2px;
            text-shadow:0 0 10px rgba(0,212,255,0.4);
        ">
            {title}
        </h2>
        """,
        unsafe_allow_html=True,
    )


def render_bar_chart(fig, x_label=None, y_label=None):

    fig.update_layout(height=OVERVIEW_CHART_HEIGHT, margin=dict(l=20, r=20, t=20, b=20))
    

    fig.update_yaxes(categoryorder="total ascending", title=y_label)

    fig.update_xaxes(title=x_label)

    fig = apply_space_theme(fig)

    st.plotly_chart(fig, use_container_width=True)


def page_subtitle(text):
    st.markdown(
        f"""
        <p style="
            color:#8888AA;
            font-size:18px;
        ">
            {text}
        </p>
        """,
        unsafe_allow_html=True,
    )


def render_footer():
    st.markdown("---")

    st.markdown(
        """
        <center>

        <h3 style="color:#00D4FF;">
        ZOMATO INDIA RESTAURANT EXPLORER
        </h3>

        <p>Built by Muhammad Saad Kamal</p>

        <p>Restaurant Intelligence Dashboard | 224K+ Restaurants | 83 Cities</p>

        <p>Historical Dataset (2019)</p>

        </center>
        """,
        unsafe_allow_html=True,
    )


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.markdown(
    """
    <h1 style="
        text-align:center;
        color:#00D4FF;
        font-family:Orbitron;
        font-size:28px;
        text-shadow:
            0 0 10px rgba(0,212,255,0.6);
    ">
        <br>
        MISSION <br>
        CONTROL
    </h1>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown("---")


st.sidebar.markdown(
    """
    <p style="
        color:#00D4FF;
        font-family:Orbitron;
        letter-spacing:2px;
        font-size:14px;
    ">
        NAVIGATION
    </p>
    """,
    unsafe_allow_html=True,
)


selected_page = st.sidebar.selectbox(
    "MISSION MODULE",
    ["Overview", "Cuisine Insights", "Locality Analysis", "Restaurant Discovery"],
)

cities = sorted(df["city"].dropna().unique())

selected_city = st.sidebar.selectbox("Select City", cities)


st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    <p style="
        color:#00D4FF;
        font-family:Orbitron;
        letter-spacing:2px;
        font-size:14px;
    ">
        MISSION ZONE
    </p>
    """,
    unsafe_allow_html=True,
)

st.sidebar.info(f"{selected_city}")


st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    <p style="
        color:#00D4FF;
        font-family:Orbitron;
        letter-spacing:2px;
        font-size:14px;
    ">
        DATA STATUS
    </p>
    """,
    unsafe_allow_html=True,
)

st.sidebar.success("Historical Dataset 2019 Snapshot")


# ==================================================
# OVERVIEW PAGE
# ==================================================

if selected_page == "Overview":

    st.markdown(
        """
        <h1 style="
            text-align:center;
            color:#00D4FF;
            font-size:52px;
            font-family:Orbitron,sans-serif;
            letter-spacing:3px;
            text-shadow:
                0 0 10px rgba(0,212,255,0.6),
                0 0 20px rgba(0,212,255,0.3);
        ">
            ZOMATO INDIA EXPLORER
        </h1>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <p style="
            text-align:center;
            color:#8888AA;
            font-size:18px;
            letter-spacing:2px;
            margin-top:-15px;
        ">
            Navigating India's Food Galaxy • Mission Zone: <span style="
    color:#00FF88;
    font-weight:700;
    text-shadow:
        0 0 10px rgba(0,255,136,0.5);
">
    {selected_city}
</span>
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # DATASET DISCLAIMER

    st.info(DATASET_DISCLAIMER)

    kpis = get_city_kpis(df, selected_city)

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Restaurants", f"{kpis['total_restaurants']:,}")

    col2.metric("Avg Rating", kpis["average_rating"])

    col3.metric("Avg Cost", f"₹{kpis['average_cost']}")

    col4.metric("Top Cuisine", kpis["top_cuisine"])

    col5.metric("Cuisine Types", kpis["total_cuisines"])

    st.markdown("---")

    col1, col2 = st.columns(2)

    # Top Cuisines Snapshot

    with col1:

        with st.container(border=True):

            section_title("CUISINE INTELLIGENCE")

            top_cuisines = get_top_cuisines(df, selected_city, top_n=5)

            fig = px.bar(
                top_cuisines, x="restaurant_count", y="cuisine", orientation="h"
            )

            render_bar_chart(fig, x_label="Restaurant Count", y_label="Cuisine")

    # Top Areas Snapshot

    with col2:

        with st.container(border=True):

            section_title("AREA HEATMAP")

            top_areas = get_top_localities(df, selected_city, top_n=5)

            fig = px.bar(top_areas, x="restaurant_count", y="area", orientation="h")

            render_bar_chart(fig, x_label="Restaurant Count", y_label="Area")

# ==================================================
# CUISINE INSIGHTS PAGE
# ==================================================

elif selected_page == "Cuisine Insights":

    page_title("CUISINE INSIGHTS")

    page_subtitle(f"Culinary distribution analysis for {selected_city}")

    with st.container(border=True):

        st.subheader("Top Cuisines")

        top_cuisines = get_top_cuisines(df, selected_city)

        fig = px.bar(
            top_cuisines,
            x="restaurant_count",
            y="cuisine",
            orientation="h",
        )

        render_bar_chart(fig, x_label="Restaurant Count", y_label="Cuisine")

# ==================================================
# LOCALITY ANALYSIS PAGE
# ==================================================

elif selected_page == "Locality Analysis":

    page_title("LOCALITY ANALYSIS")

    page_subtitle(f"Locality Insights for {selected_city}")

    col1, col2 = st.columns([1, 1], gap="large")

    # Top Restaurant Areas

    with col1:

        with st.container(border=True):

            section_title("AREA DENSITY")

            top_localities = get_top_localities(df, selected_city)

            fig = px.bar(
                top_localities, x="restaurant_count", y="area", orientation="h"
            )

            render_bar_chart(fig, x_label="Restaurant Count", y_label="Area")

    # Highest Rated Areas

    with col2:

        with st.container(border=True):

            section_title("QUALITY INDEX")

            highest_rated = get_highest_rated_areas(df, selected_city)

            fig = px.bar(highest_rated, x="average_rating", y="area", orientation="h")

            render_bar_chart(fig, x_label="Average Rating", y_label="Area")
    st.markdown("")

    with st.container(border=True):

        section_title("COST INTELLIGENCE")

        locality_costs = get_locality_cost_analysis(df, selected_city)

        fig = px.bar(
            locality_costs.head(10), x="average_cost", y="area", orientation="h"
        )

        render_bar_chart(fig, x_label="Average Cost for Two (₹)", y_label="Area")

# ==================================================
# RESTAURANT DISCOVERY PAGE
# ==================================================

elif selected_page == "Restaurant Discovery":

    page_title("RESTAURANT DISCOVERY")

    page_subtitle(f"Discover Restaurants in {selected_city}")

    # --------------------------------------------------
    # RESTAURANT SEARCH
    # --------------------------------------------------

    with st.container(border=True):

        st.markdown(
            "<h2 style='color:#00D4FF;'>RESTAURANT SEARCH</h2>", unsafe_allow_html=True
        )

        search_query = st.text_input("", placeholder="Search restaurants...")

        if search_query:

            search_results = search_restaurants(df, selected_city, search_query)

            if not search_results.empty:

                search_results_display = search_results.rename(
                    columns={
                        "name": "Restaurant",
                        "area": "Area",
                        "cuisine": "Cuisine",
                        "rating": "Rating",
                        "rating_count": "Votes",
                        "cost_for_two": "Cost for Two",
                    }
                )

                st.dataframe(
                    search_results_display,
                    use_container_width=True,
                    hide_index=True,
                    height=350,
                )

            else:

                st.warning("No restaurants found.")

    # Hidden Gems

    with st.container(border=True):

        st.markdown(
            """
    <h2 style="
        color:#00FF88;
        font-family:Orbitron;
        letter-spacing:2px;
        text-shadow:
            0 0 12px rgba(0,255,136,0.4);
    ">
        HIDDEN GEMS
    </h2>
    """,
            unsafe_allow_html=True,
        )

        hidden_gems = get_hidden_gems(df, selected_city)

        hidden_gems_display = hidden_gems.rename(
            columns={
                "name": "Restaurant",
                "area": "Area",
                "cuisine": "Cuisine",
                "rating": "Rating",
                "rating_count": "Votes",
                "cost_for_two": "Cost for Two",
                "weighted_rating": "Weighted Rating",
            }
        )

        st.dataframe(
            hidden_gems_display, use_container_width=True, hide_index=True, height=350
        )

    st.markdown("---")

    col1, col2 = st.columns([1, 1], gap="large")

    # Top Restaurants

    with col1:

        with st.container(border=True):

            st.subheader("Top Restaurants")

            top_restaurants = get_top_restaurants(df, selected_city)

            st.dataframe(
                top_restaurants.rename(
                    columns={
                        "name": "Restaurant",
                        "area": "Area",
                        "rating": "Rating",
                        "rating_count": "Votes",
                        "cost_for_two": "Cost",
                        "weighted_rating": "Score",
                    }
                ),
                use_container_width=True,
                hide_index=True,
                height=350,
            )

    # Most Popular Restaurants

    with col2:

        with st.container(border=True):

            st.subheader("Most Popular Restaurants")

            popular_restaurants = get_most_popular_restaurants(df, selected_city)

            st.dataframe(
                popular_restaurants.rename(
                    columns={
                        "name": "Restaurant",
                        "area": "Area",
                        "rating": "Rating",
                        "rating_count": "Votes",
                        "cost_for_two": "Cost",
                    }
                ),
                use_container_width=True,
                hide_index=True,
                height=350,
            )

# ==================================================
# FOOTER
# ==================================================


render_footer()
