import pandas as pd
import os



def _parse_quantity(val):

    if (
        pd.isnull(val)
        or str(val).strip() == ""
        or str(val).lower() in ["nan", "null", "n/a", "<na>"]
    ):
        return pd.NA

    val = str(val).strip()

    val = val.replace("-", "")

    try:
       
        num = int(float(val))

       
        if num == 9999:
            return pd.NA

        return num
    except ValueError:
        return val

def clean_quantity(df, original_df):
    

    df['quantity_clean'] = df['quantity'].apply(_parse_quantity)


    unparsed_quantity = df['quantity_clean'].apply(lambda x: isinstance(x, str))
    
    failed_indexes = df[unparsed_quantity].index.tolist()

    
   
    if failed_indexes:
        os.makedirs(QUARANTINE_DIR, exist_ok=True)

        quarantine_rows = original_df.loc[failed_indexes].copy()
       
        quarantine_path = os.path.join(
            QUARANTINE_DIR,
            f"quarantine_date_{pd.Timestamp.now().strftime('%d-%m-%Y')}.csv"
        )
        quarantine_rows.to_csv(quarantine_path, index=False)
       

   
    clean_df = df.drop(index=failed_indexes)

    

    clean_df = clean_df.drop(columns=['quantity'])
    clean_df = clean_df.rename(columns={'quantity_clean': 'quantity'})

    clean_df['quantity'] = pd.to_datetime(
        clean_df['quantity'], errors='coerce'
    )

    return clean_df, failed_indexes








# df['quantity_clean'] = df['quantity'].apply(parse_quantity)


# unparsed_total = df['quantity_clean'].apply(lambda x: isinstance(x, str))

# df[unparsed_total][['quantity', 'quantity_clean']