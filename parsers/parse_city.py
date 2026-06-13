import pandas as pd


def parse_city(val):


    if(

        pd.isnull(val)
        or str(val).strip() == ""
        or str(val).lower() in ["nan", "null", "n/a", "<na>","unknown"]
    ):
        return pd.NA
    
    val = str(val).strip().lower()

    val = val.replace(",", "").replace("_dup", "")
    val = val.strip()
    return val.title()



# df["city_clean"] = df["city"].apply(parse_city)


# unparsed_status = df["city_clean"].apply(
#     lambda x: isinstance(x, str) and x is not pd.NA
# )

# print(df[unparsed_status][["city", "city_clean"]].head(25))