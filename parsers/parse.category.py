import pandas as pd


def parse_category(val):
    if (
        pd.isnull(val)
        or str(val).strip() == ""
        or str(val).lower() in ["nan", "null", "n/a", "<na>"]
    ):
        return pd.NA
    val = str(val).strip().lower()

  


    if "elec" in val:
        return "Electronics"

    elif "acce" in val or "access" in val:
        return "Accessories"

    elif "stat" in val:
        return "Stationery"

    elif "furn" in val:
        return "Furniture"

    return val.title()




# df["category_clean"] = df["category"].apply(parse_category)


# unparsed_category = df["category_clean"].apply(
#     lambda x: isinstance(x, str) and x is not pd.NA
# )


# print(df[unparsed_category][["category", "category_clean"]].head(25))