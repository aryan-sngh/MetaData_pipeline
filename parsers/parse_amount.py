import pandas as pd
import os

def _parse_total_amount(val):
    
    if pd.isnull(val) or str(val).strip() == "" or str(val).lower() in ['nan', 'null', 'n/a']:
        return pd.NA
    
    val = str(val).strip()
    
   
    if val.lower() == 'inf':
        return pd.NA
    
  
    val = val.replace("Rs.", "").replace("$", "")
    val = val.replace(",", "")
    

    
    val = val.strip()
    
    try:
        return float(val)
    except ValueError:
        return val
    

def clean_amount(df, original_df):
    

    
    df['total_amount_clean'] = df['total_amount'].apply(_parse_total_amount)


    unparsed_total = df['total_amount_clean'].apply(lambda x: isinstance(x, str))
    
    failed_indexes = df[unparsed_total].index.tolist()

    
   
    if failed_indexes:
        os.makedirs(QUARANTINE_DIR, exist_ok=True)

        quarantine_rows = original_df.loc[failed_indexes].copy()
       
        quarantine_path = os.path.join(
            QUARANTINE_DIR,
            f"quarantine_date_{pd.Timestamp.now().strftime('%d-%m-%Y')}.csv"
        )
        quarantine_rows.to_csv(quarantine_path, index=False)
       

   
    clean_df = df.drop(index=failed_indexes)

    

    clean_df = clean_df.drop(columns=['total_amount'])
    clean_df = clean_df.rename(columns={'total_amount_clean': 'total_amount'})

    clean_df['total_amount'] = pd.to_datetime(
        clean_df['total_amount'], errors='coerce'
    )


    return clean_df, failed_indexes


    

# df['total_amount_clean'] = df['total_amount'].apply(parse_total_amount)


# unparsed_total = df['total_amount_clean'].apply(lambda x: isinstance(x, str))

# df[unparsed_total][['total_amount', 'total_amount_clean']]