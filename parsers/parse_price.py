import pandas as pd 

def parse_price(val):


    if pd.isnull(val) or str(val).strip()=="":
        return pd.NA
    val = str(val).strip()

    if val.lower()=='inf':
        return pd.NA

    val = val.replace("Rs.","").replace("$","").strip()
    val = val.replace(",","")
    val = val.rstrip("#").rstrip(".").strip()

    try:
        return float(val)
    except ValueError:
        return val
    

# df['unit_price_clean'] = df['unit_price'].apply(parse_price)
# unparsed_price = df['unit_price_clean'].apply(lambda x:isinstance(x,str))
# df[unparsed_price][['unit_price','unit_price_clean']]