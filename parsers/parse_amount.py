import pandas as pd


def parse_total_amount(val):
    
    if pd.isnull(val) or str(val).strip() == "" or str(val).lower() in ['nan', 'null', 'n/a']:
        return pd.NA
    
    val = str(val).strip()
    
   
    if val.lower() == 'inf':
        return pd.NA
    
  
    val = val.replace("Rs.", "").replace("$", "")
    val = val.replace(",", "")
    

    
    val = val.strip()
    
    try:
        return float(val)
    except ValueError:
        return val
    

# df['total_amount_clean'] = df['total_amount'].apply(parse_total_amount)


# unparsed_total = df['total_amount_clean'].apply(lambda x: isinstance(x, str))

# df[unparsed_total][['total_amount', 'total_amount_clean']]