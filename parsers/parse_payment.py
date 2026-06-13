import pandas as pd 


def parse_payment(val):

    if (
        pd.isnull(val)
        or str(val).strip() == ""
        or str(val).lower() == ["nan", "null", "n/a", "<na>"]

    ):
        return pd.NA
    val = str(val).strip().lower()

    return val.title()


# df["payment_clean"] = df["payment_method"].apply(parse_payment)


# unparsed_state = df["payment_clean"].apply(
#     lambda x: isinstance(x, str) and x is not pd.NA
# )


# print(df[unparsed_state][["payment_method", "payment_clean"]].drop_duplicates().to_string())