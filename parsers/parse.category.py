import pandas as pd
import os


def _parse_category(val):
    if (
        pd.isnull(val)
        or str(val).strip() == ""
        or str(val).lower() in ["nan", "null", "n/a", "<na>"]
    ):
        return pd.NA
    val = str(val).strip().lower()

  


    if "elec" in val:
        return "Electronics"

    elif "acce" in val or "access" in val:
        return "Accessories"

    elif "stat" in val:
        return "Stationery"

    elif "furn" in val:
        return "Furniture"

    return val.title()


def clean_category(df, original_df):
    

    
    df["category_clean"] = df["category"].apply(_parse_category)


    unparsed_category = df["category_clean"].apply(
    lambda x: isinstance(x, str) and x is not pd.NA
)
    
    failed_indexes = df[unparsed_category].index.tolist()

    
   
    if failed_indexes:
        os.makedirs(QUARANTINE_DIR, exist_ok=True)

        quarantine_rows = original_df.loc[failed_indexes].copy()
       
        quarantine_path = os.path.join(
            QUARANTINE_DIR,
            f"quarantine_date_{pd.Timestamp.now().strftime('%d-%m-%Y')}.csv"
        )
        quarantine_rows.to_csv(quarantine_path, index=False)
       

   
    clean_df = df.drop(index=failed_indexes)

    

    clean_df = clean_df.drop(columns=['category'])
    clean_df = clean_df.rename(columns={'category_clean': 'category'})

    clean_df['category'] = pd.to_datetime(
        clean_df['category'], errors='coerce'
    )

    
    return clean_df, failed_indexes







# df["category_clean"] = df["category"].apply(parse_category)


# unparsed_category = df["category_clean"].apply(
#     lambda x: isinstance(x, str) and x is not pd.NA
# )


# print(df[unparsed_category][["category", "category_clean"]].head(25))