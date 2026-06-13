import pandas as pd


import re
def parse_phone(val):
    if pd.isnull(val) or str(val).strip() =="":
        return pd.NA
    val = str(val).strip()
    digits = re.sub(r'\D', '', val)
    if len(digits) == 12 and digits.startswith("91"):
        digits = digits[2:]
    elif len(digits) == 11 and digits.startswith("0"):
        digits= digits[1:]
    if len(digits) == 10:
        return digits
    else:
        return val



# df["phone_clean"] = df["phone"].apply(parse_phone)

# # Verification ke liye filter
# unparsed_price = df['phone_clean'].apply(lambda x:isinstance(x,str))
# df[unparsed_price][['phone','phone_clean']]
