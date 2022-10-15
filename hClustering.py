import numpy as np
import pandas as pd
import os
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

inline_rc = dict(mpl.rcParams)

reviews = []
with open('data/yelp_academic_dataset_review.json') as fl:
    for i, line in enumerate(fl):
        reviews.append(json.loads(line))
        if i + 1 >= 200000:
            break

df_review = pd.DataFrame(reviews)
print(df_review.head())

business = []
with open('data/yelp_academic_dataset_business.json') as fl:
    for i, line in enumerate(fl):
        business.append(json.loads(line))

df_business = pd.DataFrame(business)
print(df_business.head())

# Eliminamos las columnas innecesarias

df_review = df_review.drop(["review_id", "user_id", "useful", "funny", "cool", "date"], axis=1)
df_business = df_business.drop(["name", "address", "city", "state", "postal_code", "latitude", "longitude", "stars", "review_count", "is_open", "attributes", "hours"], axis=1)

print(df_review.head())
print(df_business.head())

