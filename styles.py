# ==================================================
# APPLICATION SETTINGS
# ==================================================

PAGE_TITLE = "Zomato India Restaurant Explorer"

TOP_N = 10

# ==================================================
# CHART SETTINGS
# ==================================================

CHART_HEIGHT = 500

OVERVIEW_CHART_HEIGHT = 350

CHART_MARGIN = dict(
    l=20,
    r=20,
    t=20,
    b=20
)

# ==================================================
# TABLE SETTINGS
# ==================================================

TABLE_HEIGHT = 400

# ==================================================
# COLORS
# ==================================================

PRIMARY_COLOR = "#00D4FF"

# ==================================================
# TEXT
# ==================================================

DATASET_DISCLAIMER = """
"🔴 Historical Dataset (2019) — Verify restaurant status before visiting."
"""

# ==================================================
# CUSTOM CSS
# ==================================================

CUSTOM_CSS = """
<style>

/* ==================================================
   GOOGLE FONTS
================================================== */

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700&family=Exo+2:wght@300;400;500;600&display=swap');

/* ==================================================
   COLOR VARIABLES
================================================== */

:root {

    --bg: #000008;
    --card-bg: #0A0A1A;
    --cyan: #00D4FF;
    --purple: #7B2FBE;
    --orange: #FF6B35;
    --text: #E8E8FF;
    --text-secondary: #8888AA;
    --border: #1A1A3E;
    --success: #00FF88;
    --warning: #FFB800;
}

/* ==================================================
   MAIN BACKGROUND
================================================== */

.stApp {

    background:
        radial-gradient(
            circle at top left,
            rgba(123,47,190,0.15),
            transparent 40%
        ),
        radial-gradient(
            circle at bottom right,
            rgba(0,212,255,0.10),
            transparent 40%
        ),
        #000008;

    color: var(--text);

    font-family: 'Exo 2', sans-serif;
}

/* Main Content Spacing */

.block-container {

    padding-top: 2rem;

    padding-left: 2rem;

    padding-right: 2rem;
}

/* ==================================================
   GLOBAL TEXT
================================================== */

h1, h2, h3 {

    font-family: 'Orbitron', sans-serif !important;

    color: var(--cyan);
}

p, span, div, label {

    font-family: 'Exo 2', sans-serif;
}

/* ==================================================
   SIDEBAR
================================================== */

[data-testid="stSidebar"] {

    background-color: #05050F;

    border-right: 1px solid rgba(0,212,255,0.25);
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {

    color: var(--cyan);
}

/* ==================================================
   KPI CARDS
================================================== */

[data-testid="stMetric"] {

    background: rgba(10,10,26,0.95);

    border: 1px solid rgba(0,212,255,0.25);

    border-radius: 18px;

    padding: 20px;

    box-shadow:
        0 0 12px rgba(0,212,255,0.08);

    transition: all 0.3s ease;
}

[data-testid="stMetric"]:hover {

    transform: translateY(-5px);

    border-color: rgba(0,212,255,0.60);

    box-shadow:
        0 0 25px rgba(0,212,255,0.25);
}

[data-testid="stMetricValue"] {

    font-family: 'Orbitron', sans-serif !important;

    color: #00D4FF !important;

    text-shadow:
        0 0 12px rgba(0,212,255,0.5);
}

[data-testid="stMetricLabel"] {

    color: #8888AA !important;

    font-size: 14px;
}

/* ==================================================
   ANALYTICS PANELS
================================================== */

div[data-testid="stVerticalBlockBorderWrapper"] {

    background: rgba(10,10,26,0.95);

    border: 1px solid rgba(0,212,255,0.20);

    border-radius: 18px;

    box-shadow:
        0 0 25px rgba(0,212,255,0.12);

    transition: all 0.3s ease;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {

    border-color: rgba(0,212,255,0.55);

    box-shadow:
        0 0 25px rgba(0,212,255,0.18);

    transform: translateY(-2px);
}

/* ==================================================
   DROPDOWNS
================================================== */

.stSelectbox > div > div {

    background-color: #0A0A1A;

    border: 1px solid rgba(0,212,255,0.25);

    border-radius: 10px;
}

/* ==================================================
   DATAFRAMES
================================================== */

[data-testid="stDataFrame"] {

    border: 1px solid rgba(0,212,255,0.20);

    border-radius: 12px;
}

/* ==================================================
   INFO BANNER
================================================== */

[data-testid="stAlert"] {

    background-color: rgba(255,184,0,0.08);

    border: 1px solid rgba(255,184,0,0.30);

    border-radius: 12px;
}

/* ==================================================
   BUTTONS
================================================== */

.stButton > button {

    background-color: #0A0A1A;

    color: #00D4FF;

    border: 1px solid rgba(0,212,255,0.30);

    border-radius: 10px;

    transition: all 0.3s ease;
}

.stButton > button:hover {

    border-color: rgba(0,212,255,0.70);

    box-shadow:
        0 0 15px rgba(0,212,255,0.25);
}

/* ==================================================
   SCROLLBAR
================================================== */

::-webkit-scrollbar {

    width: 10px;
}

::-webkit-scrollbar-track {

    background: #05050F;
}

::-webkit-scrollbar-thumb {

    background: rgba(0,212,255,0.30);

    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {

    background: rgba(0,212,255,0.50);
}







/* ==================================================
   HERO SECTION
================================================== */

.hero-container {

    text-align: center;

    padding: 20px 0 30px 0;
}

.hero-title {

    font-family: 'Orbitron', sans-serif;

    font-size: 48px;

    font-weight: 700;

    color: #00D4FF;

    letter-spacing: 3px;

    text-shadow:
        0 0 10px rgba(0,212,255,0.5),
        0 0 20px rgba(0,212,255,0.3);

    animation: pulseGlow 4s infinite;
}

.hero-subtitle {

    color: #8888AA;

    font-size: 18px;

    margin-top: 10px;

    letter-spacing: 2px;
}

.hero-divider {

    width: 300px;

    height: 2px;

    margin: 20px auto;

    background: #00D4FF;

    box-shadow:
        0 0 12px rgba(0,212,255,0.8);
}

@keyframes pulseGlow {

    0% {

        text-shadow:
            0 0 10px rgba(0,212,255,0.5);
    }

    50% {

        text-shadow:
            0 0 25px rgba(0,212,255,0.9);
    }

    100% {

        text-shadow:
            0 0 10px rgba(0,212,255,0.5);
    }
}

</style>
"""



