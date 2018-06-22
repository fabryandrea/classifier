import pandas as pd
import os

def load_csv_data(name, data_path='data'):
    csv_path = os.path.join(data_path, name)
    return pd.read_csv(csv_path)
