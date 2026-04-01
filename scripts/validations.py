import pandas as pd

def run_all_checks(df):

    error_records = []
    invalid_values = ["None", "UNKNOWN", "ERROR", ""]

    for col in df.columns:

        # NULL + invalid values
        temp = df[df[col].isnull() | df[col].isin(invalid_values)].copy()
        if not temp.empty:
            temp["error"] = f"{col} INVALID"
            error_records.append(temp)

        # Numeric checks
        if pd.api.types.is_numeric_dtype(df[col]):
            temp = df[df[col] < 0].copy()
            if not temp.empty:
                temp["error"] = f"{col} NEGATIVE"
                error_records.append(temp)

        # Date check
        if "date" in col.lower():
            temp = df[pd.to_datetime(df[col], errors="coerce").isnull()].copy()
            if not temp.empty:
                temp["error"] = f"{col} INVALID DATE"
                error_records.append(temp)

    # 🔥 Business Rule (FIXED INDENTATION)
    if all(c in df.columns for c in ["Quantity", "Price Per Unit", "Total Spent"]):

        qty = pd.to_numeric(df["Quantity"], errors="coerce")
        price = pd.to_numeric(df["Price Per Unit"], errors="coerce")
        total = pd.to_numeric(df["Total Spent"], errors="coerce")

        temp = df[
            (qty * price != total) &
            qty.notnull() &
            price.notnull() &
            total.notnull()
        ].copy()

        if not temp.empty:
            temp["error"] = "BUSINESS_RULE_FAILED"
            error_records.append(temp)

    # Final return
    if error_records:
        return pd.concat(error_records, ignore_index=False)
    else:
        return pd.DataFrame()