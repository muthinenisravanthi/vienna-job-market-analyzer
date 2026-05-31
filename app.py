"""
Vienna Job Market Analyzer — Streamlit Dashboard
Run: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import os

st.set_page_config(
    page_title="Vienna Job Market Analyzer",
    page_icon="🇦🇹",
    layout="wide"
)

NAVY  = "#1A3A5C"
BLUE  = "#2C5F8A"
AMBER = "#E85D04"
LIGHT = "#F4A261"
GRAY  = "#888888"

@st.cache_data
def load_data():
    import os, random
    os.makedirs("data", exist_ok=True)
    if not os.path.exists("data/vienna_jobs.csv"):
        np.random.seed(42)
        random.seed(42)
        roles = ["Software Engineer","Data Scientist","Frontend Developer","Backend Developer","Full Stack Developer","Data Analyst","Machine Learning Engineer","DevOps Engineer","Werkstudent IT","Werkstudent Data Science","Praktikum Frontend","Praktikum Data","Angular Developer","Python Developer"]
        companies = ["Wien Energie","Raiffeisen Bank","A1 Telekom","OMV","Erste Group","Siemens Austria","Bosch Austria","IBM Austria","Microsoft Austria","Amazon Austria","Kapsch","AVL List","Red Bull","Verbund","Austrian Airlines","NHM Wien"]
        job_types = ["Vollzeit","Teilzeit","Werkstudent","Praktikum","Remote","Hybrid"]
        german_levels = ["Keine","A1","A2","B1","B2","C1","Muttersprachlich"]
        skills_pool = ["Python","JavaScript","TypeScript","Angular","React","SQL","PostgreSQL","Docker","AWS","Machine Learning","Pandas","TensorFlow","REST API","Git","Agile","Power BI","Java","C#","Node.js","FastAPI"]
        n = 500
        data = {
            "job_title": np.random.choice(roles, n),
            "company": np.random.choice(companies, n),
            "job_type": np.random.choice(job_types, n, p=[0.35,0.20,0.15,0.15,0.08,0.07]),
            "german_required": np.random.choice(german_levels, n, p=[0.15,0.05,0.08,0.20,0.25,0.15,0.12]),
            "salary_min": np.random.randint(1800, 4500, n),
            "remote_possible": np.random.choice([True, False], n, p=[0.45,0.55]),
            "skills_required": [", ".join(random.sample(skills_pool, random.randint(3,7))) for _ in range(n)]
        }
        df = pd.DataFrame(data)
        df["salary_max"] = df["salary_min"] + np.random.randint(300, 1500, n)
        df.to_csv("data/vienna_jobs.csv", index=False)
    return pd.read_csv("data/vienna_jobs.csv")
    

def main():
    st.title("🇦🇹 Vienna Tech Job Market Analyzer")
    st.markdown("*Interactive analysis of tech job postings in Vienna, Austria*")
    st.divider()

    df = load_data()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Jobs Analysed", f"{len(df):,}")
    col2.metric("Median Min Salary", f"€{int(df['salary_min'].median()):,}/mo")
    col3.metric("Remote Friendly", f"{df['remote_possible'].mean()*100:.0f}%")
    col4.metric("No German Required", f"{(df['german_required']=='Keine').mean()*100:.0f}%")

    st.divider()

    with st.sidebar:
        st.header("🔍 Filters")
        job_types = st.multiselect(
            "Job Type",
            options=df["job_type"].unique().tolist(),
            default=df["job_type"].unique().tolist()
        )
        german_filter = st.multiselect(
            "German Level Required",
            options=df["german_required"].unique().tolist(),
            default=df["german_required"].unique().tolist()
        )
        salary_range = st.slider(
            "Min Salary Range (€/month)",
            min_value=int(df["salary_min"].min()),
            max_value=int(df["salary_min"].max()),
            value=(int(df["salary_min"].min()), int(df["salary_min"].max()))
        )
        remote_only = st.checkbox("Remote / Hybrid only", value=False)

    filtered = df[
        df["job_type"].isin(job_types) &
        df["german_required"].isin(german_filter) &
        df["salary_min"].between(*salary_range)
    ]
    if remote_only:
        filtered = filtered[filtered["remote_possible"] == True]

    st.subheader(f"📊 Analysis Results — {len(filtered)} jobs match your filters")

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("**Jobs by Type**")
        counts = filtered["job_type"].value_counts()
        fig, ax = plt.subplots(figsize=(6, 4))
        fig.patch.set_facecolor("#F8FAFC")
        ax.set_facecolor("#F8FAFC")
        colors = [NAVY, BLUE, AMBER, LIGHT, GRAY, "#CBD5E0"]
        ax.barh(counts.index, counts.values,
                color=colors[:len(counts)], height=0.6)
        ax.spines[:].set_visible(False)
        ax.grid(axis="x", color="#E2E8F0", linewidth=0.8)
        st.pyplot(fig)
        plt.close()

    with col_b:
        st.markdown("**German Requirements**")
        order = ["Keine", "A1", "A2", "B1", "B2", "C1", "Muttersprachlich"]
        gcounts = filtered["german_required"].value_counts().reindex(order).fillna(0)
        fig, ax = plt.subplots(figsize=(6, 4))
        fig.patch.set_facecolor("#F8FAFC")
        ax.set_facecolor("#F8FAFC")
        palette = [LIGHT, AMBER, AMBER, BLUE, BLUE, NAVY, NAVY]
        ax.bar(gcounts.index, gcounts.values,
               color=palette, width=0.6)
        ax.spines[:].set_visible(False)
        ax.grid(axis="y", color="#E2E8F0", linewidth=0.8)
        st.pyplot(fig)
        plt.close()

    st.markdown("**Top In-Demand Skills**")
    all_skills = []
    for row in filtered["skills_required"].dropna():
        all_skills.extend([s.strip() for s in row.split(",")])
    skill_counts = pd.Series(all_skills).value_counts().head(12)
    fig, ax = plt.subplots(figsize=(12, 4))
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    colors = [NAVY if i < 4 else BLUE if i < 8 else LIGHT
              for i in range(len(skill_counts))]
    ax.bar(skill_counts.index, skill_counts.values,
           color=colors, width=0.65)
    ax.spines[:].set_visible(False)
    ax.grid(axis="y", color="#E2E8F0", linewidth=0.8)
    st.pyplot(fig)
    plt.close()

    col_c, col_d = st.columns(2)

    with col_c:
        st.markdown("**Salary Distribution**")
        fig, ax = plt.subplots(figsize=(6, 4))
        fig.patch.set_facecolor("#F8FAFC")
        ax.set_facecolor("#F8FAFC")
        ax.hist(filtered["salary_min"], bins=20,
                color=NAVY, alpha=0.85, edgecolor="white")
        ax.axvline(filtered["salary_min"].median(), color=AMBER,
                   linewidth=2, linestyle="--",
                   label=f'Median: €{int(filtered["salary_min"].median()):,}')
        ax.spines[:].set_visible(False)
        ax.grid(axis="y", color="#E2E8F0", linewidth=0.8)
        ax.legend()
        st.pyplot(fig)
        plt.close()

    with col_d:
        st.markdown("**Remote Work by Job Type**")
        remote_pct = filtered.groupby("job_type")["remote_possible"].mean() * 100
        remote_pct = remote_pct.sort_values(ascending=False)
        fig, ax = plt.subplots(figsize=(6, 4))
        fig.patch.set_facecolor("#F8FAFC")
        ax.set_facecolor("#F8FAFC")
        colors = [NAVY if v > 50 else BLUE for v in remote_pct.values]
        ax.bar(remote_pct.index, remote_pct.values,
               color=colors, width=0.55)
        ax.axhline(50, color=AMBER, linewidth=1.5, linestyle="--")
        ax.spines[:].set_visible(False)
        ax.grid(axis="y", color="#E2E8F0", linewidth=0.8)
        st.pyplot(fig)
        plt.close()

    st.divider()
    st.markdown("**📋 Job Listings Preview**")
    display_cols = ["job_title", "company", "job_type",
                    "salary_min", "german_required", "remote_possible"]
    st.dataframe(
        filtered[display_cols].head(20).rename(columns={
            "job_title": "Role", "company": "Company",
            "job_type": "Type", "salary_min": "Min Salary (€)",
            "german_required": "German", "remote_possible": "Remote"
        }),
        use_container_width=True
    )

    st.caption("Built by Sravanthi Muthineni | MSc Data Science @ TU Wien | github.com/muthinenisravanthi")

if __name__ == "__main__":
    main()
