import pandas as pd
import os

def _parse_discount(val):
    if pd.isnull(val) or str(val).strip()=="":
        return pd.NA
    
    val = str(val).strip()
    val = val.replace("%","").replace("_dup","")

    if str(val) == "_dup":
        return pd.NA

    try:
        return float(val)
    except ValueError:
        return val
    
def clean_discount(df, original_df):
    

    
    df['discount_clean'] = df['discount_pct'].apply(_parse_discount)
    unparsed_discount = df['discount_clean'].apply(lambda x : isinstance(x,str))
    
    failed_indexes = df[unparsed_discount].index.tolist()

    
   
    if failed_indexes:
        os.makedirs(QUARANTINE_DIR, exist_ok=True)

        quarantine_rows = original_df.loc[failed_indexes].copy()
       
        quarantine_path = os.path.join(
            QUARANTINE_DIR,
            f"quarantine_date_{pd.Timestamp.now().strftime('%d-%m-%Y')}.csv"
        )
        quarantine_rows.to_csv(quarantine_path, index=False)
       

   
    clean_df = df.drop(index=failed_indexes)

    

    clean_df = clean_df.drop(columns=['discount_pct'])
    clean_df = clean_df.rename(columns={'discount_clean': 'discount_pct'})

    clean_df['discount_pct'] = pd.to_datetime(
        clean_df['discount_pct'], errors='coerce'
    )

    return clean_df, failed_indexes



    



# df['discount_clean'] = df['discount_pct'].apply(parse_discount)
# unparsed_discount = df['discount_clean'].apply(lambda x : isinstance(x,str))
# df[unparsed_discount][['discount_pct','discount_clean']]