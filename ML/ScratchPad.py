from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

dataset = pd.read_csv('resources/Mukka.csv', skiprows=1, header=None)
dataset.columns = ['date', 'series', 'open', 'high', 'low', 'prev_close', 'ltp', 'close', 'vwap', '52_wh', '52_wl', 'vol', 'value', 'no_of_trades']
X = dataset[['date', 'prev_close', 'vol']]
X['vol'] = X['vol'].str.replace(",","").astype(float)
X['date'] = pd.to_datetime(X['date'])
#print(X)
spark = SparkSession.builder \
    .appName("TrendingHashtags") \
    .getOrCreate()

df = spark.createDataFrame(X)
df.createOrReplaceTempView("test")
#df.show()
df = spark.sql("select vol, lag(prev_close) over (order by date desc) as close from test")
#df.show()
X = df.toPandas().values
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X)
X = imputer.transform(X)
print(X)
y = dataset[['close']].values

sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)
print(X)

from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)

predict = sc_y.inverse_transform(regressor.predict(sc_X.transform([[2342764.0, 46.46]])).reshape(-1,1))
print(predict)




'''
# Create DataFrame from CSV data
df = spark.read.csv("resources/Mukka.csv", inferSchema= True, header= True, 
                    schema="date String, series String, open Double, high Double, low Double, prev_close Double, ltp Double, close Double, vwap Double, 52_wh Double, 52_wl Double, vol String, value String, no_of_trades String")
df1 = df.select("high", "low", "prev_close", "close", "vol")
df2 = df.select("open")
#df1.show()

poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.
X_poly
'''

