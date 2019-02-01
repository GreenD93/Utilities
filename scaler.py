from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

import pandas as pd

class scaler:
    def __init__(self, data):
        self.data = data

    def standard_scaler(self):
        scaler = StandardScaler()
        scaled_data = scaler.fit(self.data)
        scaled_data = pd.DataFrame(scaler.transform(scaled_data),columns = scaled_data.columns)
        return scaled_data

    def minmax_scaler(self):
        scaler = MinMaxScaler()
        scaled_data = scaler.fit(self.data)
        scaled_data = pd.DataFrame(scaler.transform(scaled_data),columns = scaled_data.columns)
        return scaled_data