import pandas as pd
import os


def _parse_pincode(val):

    
    if (
        pd.isnull(val)
        or str(val).strip() == ""
        or str(val).lower() in ["nan", "null", "n/a", "<na>"]
        ):
        return pd.NA
    val = str(val).strip()

    if str(val) == 'DUPLICATE':
        return pd.NA
    

    val = val.rstrip("_dup").rstrip(".").strip()




    try:
        num = int(val)
        return num
    
    except ValueError:
        return val
    
def clean_pincode(df, original_df):
    

    
    df['pincode_clean'] = df['pincode'].apply(_parse_pincode)
    unparsed_pincode = df['pincode_clean'].apply(lambda x:isinstance(x,str))
    
    failed_indexes = df[unparsed_pincode].index.tolist()

    
   
    if failed_indexes:
        os.makedirs(QUARANTINE_DIR, exist_ok=True)

        quarantine_rows = original_df.loc[failed_indexes].copy()
       
        quarantine_path = os.path.join(
            QUARANTINE_DIR,
            f"quarantine_date_{pd.Timestamp.now().strftime('%d-%m-%Y')}.csv"
        )
        quarantine_rows.to_csv(quarantine_path, index=False)
       

   
    clean_df = df.drop(index=failed_indexes)

    

    clean_df = clean_df.drop(columns=['pincode'])
    clean_df = clean_df.rename(columns={'pincode_clean': 'pincode'})

    clean_df['pincode'] = pd.to_datetime(
        clean_df['pincode'], errors='coerce'
    )

    return clean_df, failed_indexes



# df['pincode_clean'] = df['pincode'].apply(parse_pincode)
# unparsed_price = df['pincode_clean'].apply(lambda x:isinstance(x,str))
# df[unparsed_price][['pincode','pincode_clean']]