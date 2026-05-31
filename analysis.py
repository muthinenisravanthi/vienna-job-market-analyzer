"""
Vienna Job Market Analyzer
Core analysis module — generates all visualizations and insights
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import os

os.makedirs("data", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

NAVY   = "#1A3A5C"
BLUE   = "#2C5F8A"
AMBER  = "#E85D04"
LIGHT  = "#F4A261"
GRAY   = "#888888"
BG     = "#F8FAFC"

plt.rcParams.update({
    "figure.facecolor": BG,
    "axes.facecolor":   BG,
    "axes.spines.top":  False,
    "axes.spines.right":False,
    "axes.spines.left": False,
    "axes.spines.bottom": False,
    "axes.grid":        True,
    "grid.color":       "#E2E8F0",
    "grid.linewidth":   0.8,
    "font.family":      "DejaVu Sans",
    "font.size":        11,
})

def load_data():
    df = pd.read_csv("data/vienna_jobs.csv")
    return df

def plot_job_types(df):
    counts = df["job_type"].value_counts()
    colors = [NAVY, BLUE, AMBER, LIGHT, GRAY, "#CBD5E0"]
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(counts.index, counts.values,
                   color=colors[:len(counts)], height=0.6)
    for bar, val in zip(bars, counts.values):
        ax.text(val + 2, bar.get_y() + bar.get_height()/2,
                str(val), va="center", fontsize=10, color=NAVY)
    ax.set_xlabel("Number of Job Postings", color=GRAY)
    ax.set_title("Vienna Tech Jobs by Employment Type",
                 fontsize=14, fontweight="bold", color=NAVY, pad=16)
    plt.tight_layout()
    plt.savefig("outputs/01_job_types.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: outputs/01_job_types.png")

def plot_top_skills(df):
    all_skills = []
    for row in df["skills_required"].dropna():
        all_skills.extend([s.strip() for s in row.split(",")])
    skill_counts = pd.Series(all_skills).value_counts().head(15)
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = [NAVY if i < 5 else BLUE if i < 10 else LIGHT
              for i in range(len(skill_counts))]
    bars = ax.barh(skill_counts.index[::-1], skill_counts.values[::-1],
                   color=colors[::-1], height=0.65)
    for bar, val in zip(bars, skill_counts.values[::-1]):
        ax.text(val + 1, bar.get_y() + bar.get_height()/2,
                str(val), va="center", fontsize=9, color=NAVY)
    ax.set_xlabel("Frequency in Job Postings", color=GRAY)
    ax.set_title("Top 15 In-Demand Skills — Vienna Tech Market",
                 fontsize=14, fontweight="bold", color=NAVY, pad=16)
    plt.tight_layout()
    plt.savefig("outputs/02_top_skills.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: outputs/02_top_skills.png")

def plot_german_requirement(df):
    counts = df["german_required"].value_counts()
    order = ["Keine", "A1", "A2", "B1", "B2", "C1", "Muttersprachlich"]
    counts = counts.reindex(order).fillna(0)
    fig, ax = plt.subplots(figsize=(9, 5))
    palette = [LIGHT, AMBER, AMBER, BLUE, BLUE, NAVY, NAVY]
    bars = ax.bar(counts.index, counts.values,
                  color=palette, width=0.6)
    for bar, val in zip(bars, counts.values):
        ax.text(bar.get_x() + bar.get_width()/2, val + 1,
                str(int(val)), ha="center", fontsize=10, color=NAVY)
    ax.set_xlabel("German Level Required", color=GRAY)
    ax.set_ylabel("Job Postings", color=GRAY)
    ax.set_title("German Language Requirements in Vienna Tech Jobs",
                 fontsize=14, fontweight="bold", color=NAVY, pad=16)
    no_patch   = mpatches.Patch(color=LIGHT, label="No / Basic German")
    mid_patch  = mpatches.Patch(color=BLUE,  label="Intermediate (B1-C1)")
    high_patch = mpatches.Patch(color=NAVY,  label="Native / Advanced")
    ax.legend(handles=[no_patch, mid_patch, high_patch], fontsize=9)
    plt.tight_layout()
    plt.savefig("outputs/03_german_requirements.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: outputs/03_german_requirements.png")

def plot_salary_distribution(df):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].hist(df["salary_min"], bins=25, color=NAVY,
                 alpha=0.85, edgecolor="white")
    axes[0].axvline(df["salary_min"].median(), color=AMBER,
                    linewidth=2, linestyle="--",
                    label=f'Median: €{int(df["salary_min"].median()):,}')
    axes[0].set_title("Minimum Salary Distribution", fontsize=13,
                       fontweight="bold", color=NAVY)
    axes[0].set_xlabel("Gross Monthly (€)", color=GRAY)
    axes[0].legend()
    salary_by_type = df.groupby("job_type")["salary_min"].median().sort_values()
    colors = [NAVY if v > salary_by_type.median() else BLUE
              for v in salary_by_type.values]
    axes[1].barh(salary_by_type.index, salary_by_type.values,
                 color=colors, height=0.6)
    for i, (idx, val) in enumerate(salary_by_type.items()):
        axes[1].text(val + 20, i, f"€{int(val):,}",
                     va="center", fontsize=9, color=NAVY)
    axes[1].set_title("Median Salary by Job Type", fontsize=13,
                       fontweight="bold", color=NAVY)
    axes[1].set_xlabel("Gross Monthly (€)", color=GRAY)
    plt.suptitle("Vienna Tech Salary Analysis", fontsize=15,
                 fontweight="bold", color=NAVY, y=1.02)
    plt.tight_layout()
    plt.savefig("outputs/04_salary_analysis.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: outputs/04_salary_analysis.png")

def plot_remote_trend(df):
    remote_by_type = df.groupby("job_type")["remote_possible"].mean() * 100
    remote_by_type = remote_by_type.sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(9, 5))
    colors = [NAVY if v > 50 else BLUE for v in remote_by_type.values]
    bars = ax.bar(remote_by_type.index, remote_by_type.values,
                  color=colors, width=0.55)
    for bar, val in zip(bars, remote_by_type.values):
        ax.text(bar.get_x() + bar.get_width()/2,
                val + 0.5, f"{val:.0f}%",
                ha="center", fontsize=10, color=NAVY)
    ax.axhline(50, color=AMBER, linewidth=1.5,
               linestyle="--", label="50% threshold")
    ax.set_ylabel("% Offering Remote Option", color=GRAY)
    ax.set_title("Remote Work Availability by Job Type — Vienna",
                 fontsize=14, fontweight="bold", color=NAVY, pad=16)
    ax.legend(fontsize=9)
    plt.tight_layout()
    plt.savefig("outputs/05_remote_work.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: outputs/05_remote_work.png")

def generate_summary(df):
    summary = {
        "total_jobs": len(df),
        "avg_salary_min": int(df["salary_min"].mean()),
        "median_salary_min": int(df["salary_min"].median()),
        "remote_pct": round(df["remote_possible"].mean() * 100, 1),
        "no_german_pct": round((df["german_required"] == "Keine").mean() * 100, 1),
        "top_role": df["job_title"].value_counts().index[0],
        "top_skill": pd.Series(
            [s.strip() for row in df["skills_required"]
             for s in row.split(",")]
        ).value_counts().index[0],
        "most_hiring": df["company"].value_counts().index[0],
    }
    print("\n===== VIENNA JOB MARKET SUMMARY =====")
    for k, v in summary.items():
        print(f"  {k:25s}: {v}")
    return summary

def run_all():
    print("Loading data...")
    df = load_data()
    print(f"Loaded {len(df)} records\n")
    print("Generating visualizations...")
    plot_job_types(df)
    plot_top_skills(df)
    plot_german_requirement(df)
    plot_salary_distribution(df)
    plot_remote_trend(df)
    generate_summary(df)
    print("\nAll done! Check the outputs/ folder.")

if __name__ == "__main__":
    run_all()
