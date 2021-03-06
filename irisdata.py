# -*- coding: utf-8 -*-
"""irisdata.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OkyURnxgYlISHzVJTMbYOZYo3wJoSEyk

**IRIS Dataset**

Import the dataset from local system
"""

from google.colab import files
files.upload()
import pandas as pd

"""**or**
Import by google drive in the colab

Import the pandas library to access the data
"""

import pandas as pd
from google.colab import drive
drive.mount('/content/driver/')

"""Read the data by using **pandas** library and give names to the column header"""

df = pd.read_excel('iris-dataset.xlsx',header=None, names=['saple-length','saple-width','petal-length','petal-width','flower-class'])

"""View the data"""

df.head(3)

"""To find the unique values for classification"""

df['flower-class'].unique()

"""Create a new data frame for flower-class"""

y=df['flower-class']

"""Delete the flower-class column from previous data frame"""

df.drop(['flower-class'], axis=1,inplace=True)

"""View the data frame after the drop of column"""

df.head()

"""Value of the Data"""

x=df.values

type(x)

from sklearn.linear_model import LogisticRegression

lr=LogisticRegression()

lr.fit(x,y)

lr.predict([[5.1,2.3,2.1,0.7]])

lr.predict_proba([[5.1,2.3,2.1,0.7]])

lr.intercept_

lr.coef_