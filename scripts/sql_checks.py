import pandas as pd
from pandasql import sqldf


def run_sql_checks(df):

    pysqldf = lambda q: sqldf(q, {"df": df})
    results = {}

    # NULL check for all columns
    for col in df.columns:
        query = f"SELECT COUNT(*) as c FROM df WHERE `{col}` IS NULL"
        results[f"null_{col}"] = pysqldf(query)["c"][0]

    # Duplicate check (first column)
    id_col = df.columns[0]

    query_dup = f"""
        SELECT COUNT(*) as c FROM (
            SELECT `{id_col}` FROM df
            GROUP BY `{id_col}` HAVING COUNT(*) > 1
        )
    """
    results["duplicates"] = pysqldf(query_dup)["c"][0]

    return results