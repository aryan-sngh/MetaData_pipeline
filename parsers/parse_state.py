import pandas as pd
def parse_state(val):
    
    if (
        pd.isnull(val)
        or str(val).strip() == ""
        or str(val).lower() in ["nan", "null", "n/a", "<na>"]
    ):
        return pd.NA

    
    val = str(val).strip().lower()

   
    val = val.replace("@", "a")

    
    if "tamil" in val:
        return "Tamil Nadu"
    elif "maha" in val or "mah" in val:
        return "Maharashtra"
    elif "karn" in val:
        return "Karnataka"
    elif "guj" in val:
        return "Gujarat"
    elif "raj" in val:
        return "Rajasthan"
    elif "beng" in val or "west" in val:
        return "West Bengal"
    elif "tel" in val:
        return "Telangana"
    elif "delh" in val:
        return "Delhi"

    
    return val.title()





# df["state_clean"] = df["state"].apply(parse_state)


# unparsed_state = df["state_clean"].apply(
#     lambda x: isinstance(x, str) and x is not pd.NA
# )


# print(df[unparsed_state][["state", "state_clean"]].drop_duplicates().to_string())