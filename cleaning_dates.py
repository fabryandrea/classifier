import numpy as np
import pandas as pd

# turn panda df coluns into datetime
def encode_dates(df, col):
    df[col] = pd.to_datetime(df[col])
    return df[col]

def date_transformer(df, cols):
    for col in cols:
        encode_dates(df, col)
    return df

# create not_active label for people who have not ridden in 30 days
# since last_trip_date
def create_not_active(df, col, label):
    df[label] = df[col] < (df[col].max() - np.timedelta64(30, 'D'))
    return df[label]
