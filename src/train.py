import pandas as pd
import numpy as np

import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier

from scipy.io import arff
import pandas as pd

# Load ARFF file
data, meta = arff.loadarff(r'Training Dataset.arff')

# Convert to Pandas DataFrame
df = pd.DataFrame(data)

# Decode all byte-string columns into strings
for column in df.columns:
    if df[column].dtype == 'object':  # Byte strings are usually stored as 'object' dtype
        try:
            df[column] = df[column].str.decode('utf-8')  # Decode to regular strings
        except AttributeError:
            pass  # Column doesn't contain byte strings

df.columns = df.columns.str.lower().str.replace(' ', '_')

#Change the result as type int
df['result'] = df['result'].astype(int)


df_full_train, df_test = train_test_split(df, test_size = 0.2, random_state = 11)
df_train, df_val = train_test_split(df_full_train, test_size = 0.25, random_state = 11)

df_train = df_train.reset_index(drop = True)
df_val   = df_val.reset_index(drop = True)
df_test = df_test.reset_index(drop = True)
df_full_train = df_full_train.reset_index(drop = True)

y_train = df_train.result.values
y_val = df_val.result.values
y_test = df_test.result.values
y_full_train = df_full_train.result.values

del df_train['result']
del df_val['result']
del df_test['result']


categorical = list(df_train.dtypes[df.dtypes == 'object'].index)
numerical = list(df_train.dtypes[df.dtypes != 'object'].index)

#create train dict for hot encoding
train_dict = df_train[categorical + numerical].to_dict(orient='records')



dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(train_dict)
rf = RandomForestClassifier(n_estimators=25,
                                    max_depth=15,
                                    random_state=1)

rf.fit(X_train, y_train)

import pickle 

with open('spam_website.bin', 'wb') as f_out:
    pickle.dump((dv, rf), f_out)


