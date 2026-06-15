import os 
import pandas as pd



QUARANTINE_DIR = os.path.join("quarantine", "quarantine_date")

from datetime import datetime
ist_offset = pd.Timedelta(hours = 5,minutes = 30)
def _parse_date(val):
    date_formats= [
        "%Y-%m-%d", # 2023-09-2026
        "%d/%m/%Y", # 26/09/2023
        "%d-%m-%Y", # 17-01-2024
        "%b %d, %Y",# Sep 20, 2023
        "%d-%b-%Y", # 13-Jun-2024
    ]

    if pd.isnull(val) or str(val).strip()=="":
        return pd.NaT
    
    if val.isdigit():
        return pd.Timestamp(int(val),unit='s') + ist_offset
    
    for fmt in date_formats:
        try:
            return datetime.strptime(val,fmt)
        except ValueError:
            continue
    return val

def clean_date(df, original_df):
    

    
    
    df['order_date_parsed'] = df['order_date'].apply(_parse_date)

    unparsed_mask  = df['order_date_parsed'].apply(lambda x: isinstance(x, str))
    failed_indexes = df[unparsed_mask].index.tolist()

    
   
    if failed_indexes:
        os.makedirs(QUARANTINE_DIR, exist_ok=True)

        quarantine_rows = original_df.loc[failed_indexes].copy()
       
        quarantine_path = os.path.join(
            QUARANTINE_DIR,
            f"quarantine_date_{pd.Timestamp.now().strftime('%d-%m-%Y')}.csv"
        )
        quarantine_rows.to_csv(quarantine_path, index=False)
       

   
    clean_df = df.drop(index=failed_indexes)

    

    clean_df = clean_df.drop(columns=['order_date'])
    clean_df = clean_df.rename(columns={'order_date_parsed': 'order_date'})

    clean_df['order_date'] = pd.to_datetime(
        clean_df['order_date'], errors='coerce'
    )

    
    return clean_df, failed_indexes






