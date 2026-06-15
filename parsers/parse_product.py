
import pandas as pd
import os


def _parse_product_name(val):
    
    if (
        pd.isnull(val)
        or str(val).strip() == ""
        or str(val).lower() in ["nan", "null", "n/a", "<na>"]
        ):
        return pd.NA

    val = str(val).strip()

    val = val.replace(" (New)", "").replace(" (New )", "")
    val = val.replace(" - Imported", "")
    val = val.replace(", Pack of 3", "")
    val = val.strip()  # Ek baar fir safe side ke liye strip


    
    return val
    
def clean_product_name(df, original_df):
    

    
    df["product_name_clean"] = df['product_name'].apply(_parse_product_name)

    unparsed_product_name = df["product_name_clean"].apply(lambda x: isinstance(x,str) and x is not pd.NA)
    
    failed_indexes = df[unparsed_product_name].index.tolist()

    
   
    if failed_indexes:
        os.makedirs(QUARANTINE_DIR, exist_ok=True)

        quarantine_rows = original_df.loc[failed_indexes].copy()
       
        quarantine_path = os.path.join(
            QUARANTINE_DIR,
            f"quarantine_date_{pd.Timestamp.now().strftime('%d-%m-%Y')}.csv"
        )
        quarantine_rows.to_csv(quarantine_path, index=False)
       

   
    clean_df = df.drop(index=failed_indexes)

    

    clean_df = clean_df.drop(columns=['product_name'])
    clean_df = clean_df.rename(columns={'product_name_clean': 'product_name'})

    clean_df['product_name'] = pd.to_datetime(
        clean_df['product_name'], errors='coerce'
    )

    
    return clean_df, failed_indexes





# df["product_name_clean"] = df['product_name'].apply(parse_product_name)

# unparsed_date = df["product_name_clean"].apply(lambda x: isinstance(x,str) and x is not pd.NA)

# df[unparsed_date][["product_name","product_name_clean"]].head(20)