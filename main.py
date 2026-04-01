import pandas as pd
import json
from scripts.validations import run_all_checks
from scripts.report_generator import generate_summary, generate_html_report
from scripts.logger import log
import config

from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("mysql+pymysql://root:password@localhost/cafe_data")

df = pd.read_sql("SELECT * FROM sales", engine)

def main():
    log("Pipeline started")

    # Load data
    df = pd.read_csv(config.DATA_PATH)
    log("Data loaded")

    # Load rules
    with open(config.RULES_PATH) as f:
        rules = json.load(f)

    # Run validation
    errors = run_all_checks(df, rules)
    log("Validation completed")

    # Generate summary
    summary = generate_summary(df, errors)

    # Save CSV
    errors.to_csv(config.OUTPUT_PATH + "error_report.csv", index=False)

    # Generate HTML report
    generate_html_report(errors, summary, config.OUTPUT_PATH)

    print("Quality Score:", summary["quality_score"])

    # Alert
    if summary["quality_score"] < config.QUALITY_THRESHOLD:
        print("⚠️ ALERT: Data Quality Below Threshold!")

    log("Pipeline finished")

if __name__ == "__main__":
    main()