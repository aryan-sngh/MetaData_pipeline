import pandas as pd
import os


def _parse_status(val):


    if (
        pd.isnull(val)
        or str(val).strip() == ""
        or str(val).lower() == "nan"
    ):
        return pd.NA


    val = str(val).strip().lower()

    val = val.replace("_dup","")


    if (
        "pend" in val
        or "p3nd" in val
        or val == "pending"
        or val == "p3nding"
        or val == "pendind"
    ):
        return "Pending"


    elif "ship" in val or "shipp3d" in val:
        return "Shipped"


    elif (
        "deliv" in val
        or "d3liv" in val
        or val == "delivered"
        or val == "deli"
        or val == "d3liv3r3d"
    ):
        return "Delivered"

    elif "canc" in val or "canc3l" in val:
        return "Cancelled"

    elif "retu" in val or "r3turn" in val:
        return "Returned"

    
    return val.title()

def clean_status(df, original_df):
    

    
    df["status_clean"] = df["status"].apply(_parse_status)


    unparsed_status = df["status_clean"].apply(
    lambda x: isinstance(x, str) and x is not pd.NA
)
    
    failed_indexes = df[unparsed_status].index.tolist()

    
   
    if failed_indexes:
        os.makedirs(QUARANTINE_DIR, exist_ok=True)

        quarantine_rows = original_df.loc[failed_indexes].copy()
       
        quarantine_path = os.path.join(
            QUARANTINE_DIR,
            f"quarantine_date_{pd.Timestamp.now().strftime('%d-%m-%Y')}.csv"
        )
        quarantine_rows.to_csv(quarantine_path, index=False)
       

   
    clean_df = df.drop(index=failed_indexes)

    

    clean_df = clean_df.drop(columns=['status'])
    clean_df = clean_df.rename(columns={'status_clean': 'status'})

    clean_df['status'] = pd.to_datetime(
        clean_df['status'], errors='coerce'
    )

    return clean_df, failed_indexes










# df["status_clean"] = df["status"].apply(parse_status)


# unparsed_status = df["status_clean"].apply(
#     lambda x: isinstance(x, str) and x is not pd.NA
# )

# print(df[unparsed_status][["status", "status_clean"]].head(25))