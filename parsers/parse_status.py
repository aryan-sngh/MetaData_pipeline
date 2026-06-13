import pandas as pd


def parse_status(val):


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




# df["status_clean"] = df["status"].apply(parse_status)


# unparsed_status = df["status_clean"].apply(
#     lambda x: isinstance(x, str) and x is not pd.NA
# )

# print(df[unparsed_status][["status", "status_clean"]].head(25))