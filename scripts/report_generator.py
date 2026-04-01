def generate_summary(df, errors):

    total_rows = len(df)

    if errors.empty:
        error_rows = 0
    else:
        error_rows = errors.index.nunique()

    quality_score = ((total_rows - error_rows) / total_rows) * 100

    return {
        "total_rows": total_rows,
        "error_rows": error_rows,
        "quality_score": round(quality_score, 2)
    }

def generate_html_report(errors, summary, output_path):
    html = f"""
    <h1>Data Quality Report</h1>
    <p>Total Rows: {summary['total_rows']}</p>
    <p>Failed Rows: {summary['failed_rows']}</p>
    <p>Quality Score: {summary['quality_score']}%</p>
    <hr>
    {errors.to_html()}
    """

    with open(output_path + "report.html", "w") as f:
        f.write(html)


