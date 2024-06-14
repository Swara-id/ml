# class Mobil:
#     def __init__(self, merk, model, tahun):
#         self.merk = merk
#         self.model = model
#         self.tahun = tahun

#     def deskripsi(self):
#         return f"{self.merk} {self.model} keluaran tahun {self.tahun}"

#     def start(self):
#         return f"{self.merk} {self.model} sedang dinyalakan."
import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD


class Singular_Features:
    def __init__(self, default_features):
        self.default_features = default_features

    def cos_angle(self, v1, v2):
        dot_product = np.dot(v1, v2)
        norm_v1 = np.linalg.norm(v1)
        norm_v2 = np.linalg.norm(v2)
        cos_theta = dot_product / (norm_v1 * norm_v2)
        return cos_theta

    def coordinate2angle(self):
        results = []
        for index, row in self.default_features.iterrows():
            singular_row_data = []
            singular_row_data.append(row['filename'])
            for data in range(4, 21, 4):
                first = np.array([row[f'x_{data}'], row[f'y_{data}'], row[f'z_{data}']])
                second = np.array([row[f'x_{data-1}'], row[f'y_{data-1}'], row[f'z_{data-1}']])
                third = np.array([row[f'x_{data-2}'], row[f'y_{data-2}'], row[f'z_{data-2}']])
                fourth = np.array([row[f'x_{data-3}'], row[f'y_{data-3}'], row[f'z_{data-3}']])
                
                ct1_v1 = first - second
                ct1_v2 = third - second
                
                ct2_v1 = second - third
                ct2_v2 = fourth - third
        
                singular_row_data.append(self.cos_angle(ct1_v1, ct1_v2))
                singular_row_data.append(self.cos_angle(ct2_v1, ct2_v2))
                
            singular_row_data.append(row['label'])
            results.append(singular_row_data)
        df = pd.DataFrame(results)
        df.columns = ['filename','0CT1','0CT2','1CT1','1CT2','2CT1','2CT2','3CT1','3CT2','4CT1','4CT2','label']
        return df

    def SingleValueDecomposition(self):
        svd = TruncatedSVD(n_components=5)
        svd_result = svd.fit_transform(self.default_features.iloc[:,4:-1])
        svd_result = pd.DataFrame(svd_result)
        
        svd_result.columns = ['SVD1','SVD2','SVD3','SVD4','SVD5']
        svd_result['filename'] = self.default_features['filename'].values
        
        return svd_result

    def extractFeatures(self):
        df1 = self.coordinate2angle()
        df2 = self.SingleValueDecomposition()
        # Merge df1 and df2 on 'filename'
        merged_df = pd.merge(df1, df2, on='filename')
        
        return merged_df

    def export2CSV(self, datasets, name):
        datasets.to_csv(f'{name}.csv', index=False)