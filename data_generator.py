import pandas as pd
import numpy as np
import random

np.random.seed(42)
random.seed(42)

roles = [
    "Software Engineer", "Data Scientist", "Frontend Developer",
    "Backend Developer", "Full Stack Developer", "Data Analyst",
    "Machine Learning Engineer", "DevOps Engineer", "Product Manager",
    "UX Designer", "Angular Developer", "Python Developer",
    "Cloud Engineer", "Business Analyst", "Werkstudent IT",
    "Werkstudent Data Science", "Praktikum Frontend", "Praktikum Data"
]

companies = [
    "Wien Energie", "Raiffeisen Bank", "A1 Telekom", "OMV",
    "Erste Group", "Siemens Austria", "Bosch Austria", "IBM Austria",
    "Microsoft Austria", "Amazon Austria", "Kapsch", "AVL List",
    "Red Bull", "Spar", "Verbund", "Austrian Airlines",
    "TU Wien Spinoff", "Startup Vienna", "NHM Wien", "WU Wien"
]

districts = [
    "1010 Innere Stadt", "1020 Leopoldstadt", "1030 Landstrasse",
    "1040 Wieden", "1050 Margareten", "1060 Mariahilf",
    "1070 Neubau", "1080 Josefstadt", "1090 Alsergrund",
    "1100 Favoriten", "1110 Simmering", "1120 Meidling",
    "1130 Hietzing", "1140 Penzing", "1150 Rudolfsheim",
    "1160 Ottakring", "1190 Döbling", "1200 Brigittenau",
    "1210 Floridsdorf", "1220 Donaustadt"
]

skills_pool = [
    "Python", "JavaScript", "TypeScript", "Angular", "React", "Vue.js",
    "SQL", "PostgreSQL", "MongoDB", "Docker", "Kubernetes", "AWS",
    "Machine Learning", "Data Analysis", "Pandas", "TensorFlow",
    "REST API", "Git", "Agile", "Scrum", "Power BI", "Tableau",
    "Java", "C#", ".NET", "Node.js", "FastAPI", "Flask"
]

job_types = ["Vollzeit", "Teilzeit", "Werkstudent", "Praktikum", "Remote", "Hybrid"]
german_levels = ["Keine", "A1", "A2", "B1", "B2", "C1", "Muttersprachlich"]
experience_levels = ["Entry Level", "Junior", "Mid Level", "Senior", "Lead"]

n = 500
data = {
    "job_title": np.random.choice(roles, n),
    "company": np.random.choice(companies, n),
    "district": np.random.choice(districts, n),
    "job_type": np.random.choice(job_types, n, p=[0.35, 0.20, 0.15, 0.15, 0.08, 0.07]),
    "german_required": np.random.choice(german_levels, n, p=[0.15, 0.05, 0.08, 0.20, 0.25, 0.15, 0.12]),
    "experience_level": np.random.choice(experience_levels, n, p=[0.15, 0.25, 0.30, 0.20, 0.10]),
    "salary_min": np.random.randint(1800, 4500, n),
    "remote_possible": np.random.choice([True, False], n, p=[0.45, 0.55]),
    "posted_month": np.random.choice(
        ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], n
    ),
    "skills_required": [
        ", ".join(random.sample(skills_pool, random.randint(3, 7))) for _ in range(n)
    ]
}

df = pd.DataFrame(data)
df["salary_max"] = df["salary_min"] + np.random.randint(300, 1500, n)
df.to_csv("data/vienna_jobs.csv", index=False)
print(f"Generated {n} job records -> data/vienna_jobs.csv")
