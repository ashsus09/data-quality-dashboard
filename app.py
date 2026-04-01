import streamlit as st
import pandas as pd

from scripts.validations import run_all_checks
# from scripts.sql_checks import run_sql_checks   # enable if needed
from scripts.report_generator import generate_summary

st.set_page_config(page_title="Data Quality App", layout="wide")

st.title("📊 Data Quality Dashboard")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    # 🔥 Clean dirty values
    df = df.replace(["None", "UNKNOWN", "ERROR", ""], pd.NA)

    # 🔥 Convert ONLY numeric columns (IMPORTANT FIX)
    numeric_cols = ["Price Per Unit", "Quantity", "Total Spent"]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    st.subheader("📄 Raw Data")
    st.dataframe(df)

    # ✅ Run validations
    errors = run_all_checks(df)

    # ✅ Summary
    summary = generate_summary(df, errors)

    # 🎯 Quality Score
    st.subheader("📊 Quality Score")
    st.metric("Score", f"{summary['quality_score']}%")

    if summary["quality_score"] < 80:
        st.error("🚨 Critical Data Quality Issue")
    elif summary["quality_score"] < 95:
        st.warning("⚠️ Moderate Issues Found")
    else:
        st.success("✅ High Quality Data")

    # 📊 Data Profiling
    st.subheader("📊 Data Profile")
    st.write(df.describe(include="all"))

    # 🗄️ SQL checks (optional)
    # sql_result = run_sql_checks(df)
    # st.subheader("🗄️ SQL Checks")
    # st.write(sql_result)

    # 📊 Error Summary Chart
    st.subheader("📊 Error Summary")
    if not errors.empty and "error" in errors.columns:
        st.bar_chart(errors["error"].value_counts())
    else:
        st.info("No error summary available")

    # ❌ Errors Table
    st.subheader("❌ Errors")

    if not errors.empty:
        errors_display = errors.reset_index(drop=True)
        st.dataframe(errors_display)
        st.write(f"Total Errors: {len(errors_display)}")
    else:
        st.success("No errors found")

    # 📥 Download Report
    if not errors.empty:
        csv = errors.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📥 Download Error Report",
            csv,
            "error_report.csv",
            "text/csv"
        )
