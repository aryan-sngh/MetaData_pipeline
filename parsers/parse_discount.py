import pandas as pd

def parse_discount(val):
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
    



# df['discount_clean'] = df['discount_pct'].apply(parse_discount)
# unparsed_discount = df['discount_clean'].apply(lambda x : isinstance(x,str))
# df[unparsed_discount][['discount_pct','discount_clean']]