# 🇦🇹 Vienna Job Market Analyzer

An interactive data analysis project exploring the **Vienna tech job market** — analysing salary trends, in-demand skills, German language requirements, and remote work availability across different job types.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

---

## 📊 Key Insights

- **45%** of Vienna tech jobs offer remote or hybrid work
- **Python** and **JavaScript** are the most in-demand skills
- **Werkstudent** and **Praktikum** roles have median salaries of €2,000–2,600/month
- **15%** of job postings require no German at all — good news for international candidates
- **Donaustadt (1220)** and **Innere Stadt (1010)** have the highest concentration of tech employers

---

## ✨ Features

- 📈 **5 interactive visualisations** — job types, skills, salary, German requirements, remote work
- 🔍 **Dynamic filtering** — filter by job type, German level, salary range, and remote option
- 📋 **Job listings preview** — table view of filtered results
- 📊 **KPI summary cards** — key market metrics at a glance
- 🚀 **Streamlit dashboard** — fully deployable web app

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| Pandas | Data loading, transformation, aggregation |
| Matplotlib + Seaborn | Static visualisations |
| Streamlit | Interactive web dashboard |
| NumPy | Data generation and numerical operations |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/muthinenisravanthi/vienna-job-market-analyzer.git
cd vienna-job-market-analyzer
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Generate sample data
```bash
python data_generator.py
```

### 5a. Run static analysis
```bash
python analysis.py
# Charts saved to outputs/ folder
```

### 5b. Launch interactive dashboard
```bash
streamlit run app.py
# Opens at http://localhost:8501
```

---

## 📁 Project Structure

```
vienna-job-market-analyzer/
├── data_generator.py      # Generates realistic sample job data
├── analysis.py            # Core analysis + static visualizations
├── app.py                 # Streamlit interactive dashboard
├── requirements.txt       # Python dependencies
├── data/
│   └── vienna_jobs.csv    # Generated dataset (500 job records)
└── outputs/
    ├── 01_job_types.png
    ├── 02_top_skills.png
    ├── 03_german_requirements.png
    ├── 04_salary_analysis.png
    └── 05_remote_work.png
```

---

## 📈 Visualisations

| Chart | Description |
|---|---|
| Job Types | Distribution of Vollzeit, Teilzeit, Werkstudent, Praktikum roles |
| Top 15 Skills | Most frequently required technical skills |
| German Requirements | Language level distribution across postings |
| Salary Analysis | Distribution + median by job type |
| Remote Work | % of roles offering remote option by job type |

---

## 🔍 Analysis Highlights

### For international students in Vienna
The analysis reveals that **Werkstudent** and **Praktikum** roles — the most accessible for MSc students — have a higher proportion of English-friendly positions (lower German requirements) compared to senior full-time roles. This is encouraging for international TU Wien students entering the Austrian job market.

### Most in-demand skills
Python, JavaScript, TypeScript, and SQL consistently top the demand charts — confirming that a data science + frontend combination is highly marketable in Vienna.

---

## 👩‍💻 Author

**Sravanthi Muthineni**
- 🎓 MSc Data Science @ TU Wien, Vienna
- 💼 3 years Angular Frontend Development @ Infosys
- 🌍 Vienna, Austria | Student Permit — 20h/week
- 💼 [LinkedIn](https://linkedin.com/in/sravanthi-muthineni)
- 📧 muthinenisravanthi198@gmail.com

---

## 📄 License

MIT License — free to use as reference or learning material.
