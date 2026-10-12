import streamlit as st

st.set_page_config(
    page_title="John Isaac Mcharo | Portfolio",
    page_icon="💻",
    layout="wide"
)

# Header Section
st.title("John Isaac Mcharo")
st.subheader("Data Analyst & Software Developer")
st.caption("Sanmun • Nairobi, Kenya")

st.markdown("""
[GitHub](https://github.com/Avire123) | 
[LinkedIn](https://linkedin.com/in/john-isaac-mcharo-a12594217) | 
[Kaggle](https://www.kaggle.com/isaacmcharo) | 
[Portfolio](https://www.datascienceportfol.io/isaacmcharo9)
""")

st.divider()

# About Me
st.header("About Me")
st.write(
    "I'm a Data Analyst with experience turning complex data into meaningful insights "
    "that support better business decisions. Passionate about end-to-end data pipelines, "
    "machine learning applications, interactive web dashboards, and software development."
)

st.divider()

# Projects Data
PROJECTS = [
    {
        "name": "web3_data_project",
        "tech": ["Python", "Pandas", "Data Visualization"],
        "desc": "Full-stack Web3 intelligence platform combining GitHub developer activity with crypto market data to evaluate project maturity.",
        "url": "https://github.com/Avire123/web3_data_project"
    },
    {
        "name": "credit-risk-engine",
        "tech": ["Python", "Streamlit", "FastAPI", "XGBoost", "DuckDB", "Machine Learning"],
        "desc": "AI Credit Risk Engine for credit underwriting and portfolio analytics built with Python, FastAPI, Streamlit, XGBoost, and DuckDB.",
        "url": "https://github.com/Avire123/credit-risk-engine"
    },
    {
        "name": "news-sentiment-dashboard",
        "tech": ["Python", "FastAPI", "Streamlit", "NLP"],
        "desc": "End-to-end real-time news sentiment pipeline with RSS ingestion, VADER NLP, SQLAlchemy, FastAPI REST endpoints, and Streamlit.",
        "url": "https://github.com/Avire123/news-sentiment-dashboard"
    },
    {
        "name": "flight-forecaster",
        "tech": ["Python", "Streamlit", "Machine Learning"],
        "desc": "Streamlit app forecasting flight fare trends for African airlines and international routes using Kenyan shilling (KES) pricing models.",
        "url": "https://github.com/Avire123/flight-forecaster"
    },
    {
        "name": "used-car-price-intelligence",
        "tech": ["Python", "Machine Learning", "Pandas"],
        "desc": "Machine learning valuation tool estimating fair market value of vehicles and flagging bargain vs overpriced listings.",
        "url": "https://github.com/Avire123/used-car-price-intelligence"
    },
    {
        "name": "ecommerce-demand-app",
        "tech": ["Python", "XGBoost", "Streamlit", "Machine Learning"],
        "desc": "End-to-end ML application using XGBoost and Streamlit to forecast e-commerce sales volume and simulate price elasticity.",
        "url": "https://github.com/Avire123/ecommerce-demand-app"
    },
    {
        "name": "kiva-microfinance-intelligence",
        "tech": ["Python", "Jupyter", "Pandas"],
        "desc": "Data science analysis of 671K+ Kiva microfinance loans uncovering crowdfunding success drivers and borrowing behavior.",
        "url": "https://github.com/Avire123/kiva-microfinance-intelligence"
    },
    {
        "name": "UBER-DATA-ANALYSYS",
        "tech": ["Python", "Jupyter", "Pandas"],
        "desc": "Exploratory analysis of 200,000 Uber trip records uncovering demand patterns, peak hours, pickup hotspots, and fare dynamics.",
        "url": "https://github.com/Avire123/UBER-DATA-ANALYSYS"
    }
]

# Filter & Search Controls
st.header("GitHub Repositories")

col_search, col_tech = st.columns([2, 1])

with col_search:
    query = st.text_input("🔍 Search repositories by keyword...", "")

with col_tech:
    tech_filter = st.selectbox(
        "🛠️ Filter by Technology",
        ["All", "Streamlit", "FastAPI", "Machine Learning", "XGBoost", "Pandas", "Jupyter"]
    )

# Filtering Logic
filtered_projects = []
for p in PROJECTS:
    matches_search = (
        query.lower() in p["name"].lower() or 
        query.lower() in p["desc"].lower() or 
        any(query.lower() in t.lower() for t in p["tech"])
    )
    matches_tech = tech_filter == "All" or any(tech_filter.lower() in t.lower() for t in p["tech"])
    
    if matches_search and matches_tech:
        filtered_projects.append(p)

st.caption(f"Showing {len(filtered_projects)} of {len(PROJECTS)} repositories")

# Grid Rendering
cols = st.columns(2)
for idx, proj in enumerate(filtered_projects):
    with cols[idx % 2]:
        with st.container(border=True):
            st.subheader(proj["name"])
            st.caption(" • ".join(proj["tech"]))
            st.write(proj["desc"])
            st.link_button("View on GitHub ↗", proj["url"])