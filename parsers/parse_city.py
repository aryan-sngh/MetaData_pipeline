import pandas as pd
import os


def _parse_city(val):


    if(

        pd.isnull(val)
        or str(val).strip() == ""
        or str(val).lower() in ["nan", "null", "n/a", "<na>","unknown"]
    ):
        return pd.NA
    
    val = str(val).strip().lower()

    val = val.replace(",", "").replace("_dup", "")
    val = val.strip()
    return val.title()


def clean_city(df, original_df):
    

    
    df["city_clean"] = df["city"].apply(_parse_city)


    unparsed_city = df["city_clean"].apply(
    lambda x: isinstance(x, str) and x is not pd.NA
)
    
    failed_indexes = df[unparsed_city].index.tolist()

    
   
    if failed_indexes:
        os.makedirs(QUARANTINE_DIR, exist_ok=True)

        quarantine_rows = original_df.loc[failed_indexes].copy()
       
        quarantine_path = os.path.join(
            QUARANTINE_DIR,
            f"quarantine_date_{pd.Timestamp.now().strftime('%d-%m-%Y')}.csv"
        )
        quarantine_rows.to_csv(quarantine_path, index=False)
       

   
    clean_df = df.drop(index=failed_indexes)

    

    clean_df = clean_df.drop(columns=['city'])
    clean_df = clean_df.rename(columns={'city_clean': 'city'})

    clean_df['city'] = pd.to_datetime(
        clean_df['city'], errors='coerce'
    )

    return clean_df, failed_indexes





# df["city_clean"] = df["city"].apply(parse_city)


# unparsed_status = df["city_clean"].apply(
#     lambda x: isinstance(x, str) and x is not pd.NA
# )

# print(df[unparsed_status][["city", "city_clean"]].head(25))