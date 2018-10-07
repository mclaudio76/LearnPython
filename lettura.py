import os
import tarfile
import pandas as pd 
from six.moves import urllib
import numpy as np
import hashlib
import matplotlib.pyplot as plt

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH  = os.path.join("datasets","housing")
HOUSING_URL   = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


def fetch_housing_data(hUrl = HOUSING_URL, hPath = HOUSING_PATH) :
    if not os.path.isdir(hPath):
        os.makedirs(hPath)
    tgz_path = os.path.join(hPath, "housing.tgz")
    urllib.request.urlretrieve(hUrl,tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=hPath)
    housing_tgz.close()

def load_housing_data(hPath=HOUSING_PATH):
    csv_path = os.path.join(hPath, "housing.csv")
    data = pd.read_csv(csv_path)
    # Creo un indice virtuale
    data["id"] = data["longitude"] * 1000  + data["latitude"]
    return data

def createRandomTrainAndTestDatasets(dataset, ratio) :
    np.random.seed(42)
    shuffle_idx = np.random.permutation(len(dataset))
    idxLimit     = int(len(dataset) * ratio)
    idx_test     = shuffle_idx[:idxLimit]
    idx_train    = shuffle_idx[idxLimit:]
    return dataset.iloc[idx_train], dataset.iloc[idx_test]

def acceptItem(idValue, ratio=0.2):
    return hashlib.md5(np.int64(idValue)).digest()[-1] < 256 * ratio

def createTrainAndTestDatasets(dataset, ratio) :
    idx = dataset["id"]
    selection = idx.apply(lambda v : acceptItem(v))
    return dataset.loc[~selection], dataset.loc[selection]
# Main 
#fetch_housing_data()
housing = load_housing_data()
dsetTrain, dsetTest = createTrainAndTestDatasets(housing, 0.2)
print("Done, train set = ",len(dsetTrain)," test set ",len(dsetTest))
# Utilizzo splitter già esistenti
housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)
income = pd.DataFrame()
income["cat"] = housing["income_cat"].unique()
income["cat_count"] = housing["income_cat"].value_counts()
#print(income)
income.plot(kind='hist')
#print(housing["income_cat"].value_counts())
#housing.plot(kind='scatter',  x='longitude', y='latitude')
plt.show()