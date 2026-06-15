import pandas as pd 
import os



def _parse_payment(val):

    if (
        pd.isnull(val)
        or str(val).strip() == ""
        or str(val).lower() == ["nan", "null", "n/a", "<na>"]

    ):
        return pd.NA
    val = str(val).strip().lower()

    return val.title()


def clean_payment(df, original_df):
    

    
    df["payment_clean"] = df["payment_method"].apply(_parse_payment)


    unparsed_payment = df["payment_clean"].apply(
        lambda x: isinstance(x, str) and x is not pd.NA
)
    
    failed_indexes = df[unparsed_payment].index.tolist()

    
   
    if failed_indexes:
        os.makedirs(QUARANTINE_DIR, exist_ok=True)

        quarantine_rows = original_df.loc[failed_indexes].copy()
       
        quarantine_path = os.path.join(
            QUARANTINE_DIR,
            f"quarantine_date_{pd.Timestamp.now().strftime('%d-%m-%Y')}.csv"
        )
        quarantine_rows.to_csv(quarantine_path, index=False)
       

   
    clean_df = df.drop(index=failed_indexes)

    

    clean_df = clean_df.drop(columns=['payment_method'])
    clean_df = clean_df.rename(columns={'payment_clean': 'payment_method'})

    clean_df['payment_method'] = pd.to_datetime(
        clean_df['payment_method'], errors='coerce'
    )

    
    return clean_df, failed_indexes



# df["payment_clean"] = df["payment_method"].apply(parse_payment)


# unparsed_state = df["payment_clean"].apply(
#     lambda x: isinstance(x, str) and x is not pd.NA
# )


# print(df[unparsed_state][["payment_method", "payment_clean"]].drop_duplicates().to_string())