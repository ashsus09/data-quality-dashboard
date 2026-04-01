## 📊 Data Quality Dashboard with Automated Validation & SQL Checks

## 🚀 Overview

The Data Quality Dashboard is an end-to-end data validation system built
using Python, SQL, and Streamlit. It allows users to upload any dataset
and automatically performs data quality checks, business rule
validation, and generates interactive reports.

------------------------------------------------------------------------

## 🔥 Features

-   ✅ Dynamic Data Validation (works with any dataset)
-   ✅ Null, Invalid, and Duplicate Detection
-   ✅ SQL-based Data Checks (without database using pandasql)
-   ✅ Business Rule Validation (e.g., Total = Quantity × Price)
-   ✅ Data Profiling (summary statistics)
-   ✅ Interactive Dashboard (Streamlit UI)
-   ✅ Error Summary Visualization
-   ✅ Downloadable Error Reports (CSV)
-   ✅ Quality Score Calculation with Alerts

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   Python (Pandas, PandasQL)
-   Streamlit (UI)
-   SQL (in-memory queries)
-   Git & GitHub

------------------------------------------------------------------------

## 📁 Project Structure

    data-quality-dashboard/
    │
    ├── app.py
    ├── requirements.txt
    ├── scripts/
    │   ├── validations.py
    │   ├── sql_checks.py
    │   └── report_generator.py

------------------------------------------------------------------------

## ▶️ How to Run

1.  Clone the repository:

```{=html}
<!-- -->
```
    git clone https://github.com/ashsus09/data-quality-dashboard.git
    cd data-quality-dashboard

2.  Install dependencies:

```{=html}
<!-- -->
```
    pip install -r requirements.txt

3.  Run the app:

```{=html}
<!-- -->
```
    streamlit run app.py

------------------------------------------------------------------------

## 🌐 Live Demo

https://data-quality-dashboard-app.streamlit.app/

------------------------------------------------------------------------

## 📌 Use Cases

-   Data Quality Analysis
-   Data Cleaning Validation
-   Business Rule Enforcement
-   Exploratory Data Analysis

------------------------------------------------------------------------

## 🧠 Key Highlights

-   Handles real-world messy data (NULL, UNKNOWN, ERROR values)
-   Uses both Python and SQL for validation
-   Fully dynamic (no hardcoded schema)
-   Production-like data validation system

------------------------------------------------------------------------

## 📬 Author

Aastha


GitHub: https://github.com/ashsus09

