import pandas as pd


def parse_pincode(val):

    
    if (
        pd.isnull(val)
        or str(val).strip() == ""
        or str(val).lower() in ["nan", "null", "n/a", "<na>"]
        ):
        return pd.NA
    val = str(val).strip()

    if str(val) == 'DUPLICATE':
        return pd.NA
    

    val = val.rstrip("_dup").rstrip(".").strip()




    try:
        num = int(val)
        return num
    
    except ValueError:
        return val
    


# df['pincode_clean'] = df['pincode'].apply(parse_pincode)
# unparsed_price = df['pincode_clean'].apply(lambda x:isinstance(x,str))
# df[unparsed_price][['pincode','pincode_clean']]