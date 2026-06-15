# Zomato India Restaurant Explorer

An interactive multi-city restaurant analytics dashboard built using Python, Pandas, Plotly, and Streamlit.

## Project Overview

Zomato India Restaurant Explorer is a data analytics and visualization project that transforms raw restaurant data into actionable insights through an interactive dashboard.

The project analyzes over 224,000 restaurant records across 83 Indian cities and provides insights into restaurant trends, cuisine preferences, locality dynamics, pricing patterns, and restaurant discovery.

## Dataset

* Source: Kaggle Zomato India Restaurants Dataset
* Records: 224,514 cleaned restaurant records
* Cities Covered: 83
* Data Collection Year: 2019

## Dashboard Features

### City Overview

* Total Restaurants
* Average Rating
* Average Cost for Two
* Top Cuisine
* Cuisine Diversity

### Cuisine Analytics

* Top Cuisine Distribution
* Cuisine Popularity Analysis

### Locality Analytics

* Top Restaurant Areas
* Highest Rated Areas
* Most Expensive Areas

### Restaurant Discovery

* Hidden Gems Recommendation Engine
* Top Restaurants Leaderboard
* Most Popular Restaurants Leaderboard
* Restaurant Search Analytics

## Data Engineering Pipeline

Raw Excel Dataset

→ Data Audit

→ Data Cleaning

→ Data Validation

→ Parquet Dataset

→ Analytics Engine

→ Interactive Dashboard

## Cleaning Steps Implemented

* Removed invalid restaurant names
* Removed invalid datetime-based restaurant names
* Converted NEW ratings to missing values
* Converted zero ratings to missing values
* Converted zero cost values to missing values
* Standardized city names
* Standardized text columns
* Fixed mixed datatype issues
* Generated optimized Parquet dataset

## Analytics Engine

### Dataset Analytics

* Dataset Summary
* Missing Value Analysis
* Duplicate Analysis
* City Distribution Analysis

### KPI Analytics

* get_city_kpis()

### Cuisine Analytics

* get_top_cuisines()

### Locality Analytics

* get_top_localities()
* get_locality_cost_analysis()
* get_highest_rated_areas()

### Restaurant Discovery

* calculate_weighted_rating()
* get_hidden_gems()
* get_top_restaurants()
* get_most_popular_restaurants()
* search_restaurants()

## Project Structure

```text
zomato/

├── data/
│   ├── raw/
│   ├── processed/
│   └── reports/
│
├── app.py
├── analysis.py
├── data_cleaning.py
├── run_cleaning.py
├── styles.py
├── utils.py
├── config.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
└── tests/
    ├── test_cleaning.py
    └── test_analytics.py
```

## Project Status

#### Phase 1: Project Setup 
* Repository structure 
* Configuration management 
* Documentation 
* GitHub setup 
#### Phase 2: Data Audit 
* Dataset summary 
* Missing value analysis 
* City distribution analysis 
* Duplicate analysis 
#### Phase 3: Data Cleaning 
* Rating cleaning 
* Cost cleaning 
* Restaurant name validation 
* Text standardization 
* Parquet dataset generation 
#### Phase 4: Analytics Engine
* City KPI generation 
* Cuisine analytics 
* Locality analytics 
* Hidden Gems recommendation engine 
* Weighted restaurant ranking
* Analytics Functions: 
    * get_city_data() 
    * extract_cuisines() 
    * get_city_kpis() 
    * get_top_cuisines() 
    * get_top_localities() 
    * get_locality_cost_analysis() 
    * get_highest_rated_areas() 
    * calculate_weighted_rating() 
    * get_hidden_gems()
    * get_top_restaurants()
    * get_most_popular_restaurants()
    * search_restaurants()
* Restaurant Leaderboards 
* Smart Search 

### Phase 5: Dashboard Development (In Progress)

Implemented:

* City Selector
* KPI Cards
* Top Cuisines Visualization
* Top Restaurant Areas Visualization
* Highest Rated Areas Visualization
* Most Expensive Areas Visualization
* Hidden Gems Dashboard
* Top Restaurants Dashboard
* Most Popular Restaurants Dashboard
* Responsive Card Layout

## Upcoming Features

* Sidebar Navigation
* Multi-Page Dashboard Layout
* Advanced Restaurant Search Interface
* City Comparison Analytics
* Dashboard Styling Enhancements
* Streamlit Cloud Deployment

## Tech Stack

* Python
* Pandas
* NumPy
* Plotly
* Streamlit
* PyArrow
* OpenPyXL
* Git
* GitHub

## Current Progress

Project Completion Estimate: ~80%

The data engineering pipeline, cleaning workflow, analytics engine, and initial dashboard have been completed. Remaining work focuses on dashboard architecture, user experience improvements, and deployment.
