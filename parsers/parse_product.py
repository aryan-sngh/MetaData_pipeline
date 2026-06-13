
import pandas as pd


def parse_product_name(val):


    
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


# df["product_name_clean"] = df['product_name'].apply(parse_product_name)

# unparsed_date = df["product_name_clean"].apply(lambda x: isinstance(x,str) and x is not pd.NA)

# df[unparsed_date][["product_name","product_name_clean"]].head(20)