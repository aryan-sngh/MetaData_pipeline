import pandas as pd


def parse_quantity(val):

    if (
        pd.isnull(val)
        or str(val).strip() == ""
        or str(val).lower() in ["nan", "null", "n/a", "<na>"]
    ):
        return pd.NA

    val = str(val).strip()

    val = val.replace("-", "")

    try:
       
        num = int(float(val))

       
        if num == 9999:
            return pd.NA

        return num
    except ValueError:
        return val




# df['quantity_clean'] = df['quantity'].apply(parse_quantity)


# unparsed_total = df['quantity_clean'].apply(lambda x: isinstance(x, str))

# df[unparsed_total][['quantity', 'quantity_clean']]