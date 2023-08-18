import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
from math import log,sqrt
import os
import matplotlib.pyplot as plt

tmp = np.array([1., 2., 3.])
tmp_cubed = np.power(tmp, 3)

ex_sframe = pd.DataFrame()
ex_sframe['power_1'] = tmp

def polynomial_sframe(feature, degree):
    # assume that degree >= 1
    # initialize the SFrame:
    poly_sframe = pd.DataFrame()
    # and set poly_sframe['power_1'] equal to the passed feature
    poly_sframe['power_1'] = feature
    # first check if degree > 1
    if degree > 1:
        # then loop over the remaining degrees:
        # range usually starts at 0 and stops at the endpoint-1. We want it to start at 2 and stop at degree
        for power in range(2, degree+1):
            # first we'll give the column a name:
            name = 'power_' + str(power)
            # then assign poly_sframe[name] to the appropriate power of feature
            poly_sframe[name] = np.power(feature, power)
    return poly_sframe

print( polynomial_sframe(tmp, 3))


train_data=pd.read_csv('..\Coursera\kc_house_train_data.csv')
train_data = train_data.astype(dtype= {'bathrooms':float, 'waterfront':int, 'sqft_above':int, 'sqft_living15':float, 'grade':int, 'yr_renovated':int, 'price':float, 'bedrooms':float, 'zipcode':str, 'long':float, 'sqft_lot15':float, 'sqft_living':float, 'floors':str, 'condition':int, 'lat':float, 'date':str, 'sqft_basement':int, 'yr_built':int, 'id':str, 'sqft_lot':int, 'view':int})
test_data=pd.read_csv('..\Coursera\kc_house_test_data.csv')
test_data = test_data.astype(dtype= {'bathrooms':float, 'waterfront':int, 'sqft_above':int, 'sqft_living15':float, 'grade':int, 'yr_renovated':int, 'price':float, 'bedrooms':float, 'zipcode':str, 'long':float, 'sqft_lot15':float, 'sqft_living':float, 'floors':str, 'condition':int, 'lat':float, 'date':str, 'sqft_basement':int, 'yr_built':int, 'id':str, 'sqft_lot':int, 'view':int})
train_data_1=pd.read_csv('..\Coursera\wk3_kc_house_set_1_data.csv')
train_data_1 = train_data_1.astype(dtype= {'bathrooms':float, 'waterfront':int, 'sqft_above':int, 'sqft_living15':float, 'grade':int, 'yr_renovated':int, 'price':float, 'bedrooms':float, 'zipcode':str, 'long':float, 'sqft_lot15':float, 'sqft_living':float, 'floors':str, 'condition':int, 'lat':float, 'date':str, 'sqft_basement':int, 'yr_built':int, 'id':str, 'sqft_lot':int, 'view':int})
train_data_2=pd.read_csv('..\Coursera\wk3_kc_house_set_2_data.csv')
train_data_2 = train_data_2.astype(dtype= {'bathrooms':float, 'waterfront':int, 'sqft_above':int, 'sqft_living15':float, 'grade':int, 'yr_renovated':int, 'price':float, 'bedrooms':float, 'zipcode':str, 'long':float, 'sqft_lot15':float, 'sqft_living':float, 'floors':str, 'condition':int, 'lat':float, 'date':str, 'sqft_basement':int, 'yr_built':int, 'id':str, 'sqft_lot':int, 'view':int})
train_data_3=pd.read_csv('..\Coursera\wk3_kc_house_set_3_data.csv')
train_data_3 = train_data_3.astype(dtype= {'bathrooms':float, 'waterfront':int, 'sqft_above':int, 'sqft_living15':float, 'grade':int, 'yr_renovated':int, 'price':float, 'bedrooms':float, 'zipcode':str, 'long':float, 'sqft_lot15':float, 'sqft_living':float, 'floors':str, 'condition':int, 'lat':float, 'date':str, 'sqft_basement':int, 'yr_built':int, 'id':str, 'sqft_lot':int, 'view':int})
train_data_4=pd.read_csv('..\Coursera\wk3_kc_house_set_4_data.csv')
train_data_4 = train_data_4.astype(dtype= {'bathrooms':float, 'waterfront':int, 'sqft_above':int, 'sqft_living15':float, 'grade':int, 'yr_renovated':int, 'price':float, 'bedrooms':float, 'zipcode':str, 'long':float, 'sqft_lot15':float, 'sqft_living':float, 'floors':str, 'condition':int, 'lat':float, 'date':str, 'sqft_basement':int, 'yr_built':int, 'id':str, 'sqft_lot':int, 'view':int})
test_data=pd.read_csv('..\Coursera\wk3_kc_house_test_data.csv')
test_data = test_data.astype(dtype= {'bathrooms':float, 'waterfront':int, 'sqft_above':int, 'sqft_living15':float, 'grade':int, 'yr_renovated':int, 'price':float, 'bedrooms':float, 'zipcode':str, 'long':float, 'sqft_lot15':float, 'sqft_living':float, 'floors':str, 'condition':int, 'lat':float, 'date':str, 'sqft_basement':int, 'yr_built':int, 'id':str, 'sqft_lot':int, 'view':int})
train_data=pd.read_csv('..\Coursera\wk3_kc_house_train_data.csv')
train_data = train_data.astype(dtype= {'bathrooms':float, 'waterfront':int, 'sqft_above':int, 'sqft_living15':float, 'grade':int, 'yr_renovated':int, 'price':float, 'bedrooms':float, 'zipcode':str, 'long':float, 'sqft_lot15':float, 'sqft_living':float, 'floors':str, 'condition':int, 'lat':float, 'date':str, 'sqft_basement':int, 'yr_built':int, 'id':str, 'sqft_lot':int, 'view':int})
valid_data=pd.read_csv('..\Coursera\wk3_kc_house_valid_data.csv')
valid_data = valid_data.astype(dtype= {'bathrooms':float, 'waterfront':int, 'sqft_above':int, 'sqft_living15':float, 'grade':int, 'yr_renovated':int, 'price':float, 'bedrooms':float, 'zipcode':str, 'long':float, 'sqft_lot15':float, 'sqft_living':float, 'floors':str, 'condition':int, 'lat':float, 'date':str, 'sqft_basement':int, 'yr_built':int, 'id':str, 'sqft_lot':int, 'view':int})

sales = pd.concat([train_data,test_data])
sales = sales.sort_values('sqft_living')
poly1_data = polynomial_sframe(sales['sqft_living'], 1)
poly1_data['price'] = sales['price'] # add price to the data since it's the target
model1 = LinearRegression().fit(poly1_data[['power_1']].values, poly1_data['price'].values)
print (model1.coef_)
print (model1.intercept_)

# plt.plot(poly1_data['power_1'],poly1_data['price'],'.',
#         poly1_data['power_1'], model1.predict(poly1_data['power_1'].to_numpy().reshape(-1, 1)), '-')
# plt.show()

#define predictor and response variables
x = np.array(sales['sqft_living'])
y = np.array(sales['price'])
poly = PolynomialFeatures(degree=15, include_bias=False)
poly_features = poly.fit_transform(x.reshape(-1, 1))
poly_reg_model = LinearRegression()
poly_reg_model.fit(poly_features, y)
y_predicted = poly_reg_model.predict(poly_features)

plt.plot(x,y,'.',
    x, y_predicted, color='purple')

# plt.show()


# Next you should write a loop that does the following:
#
# For degree in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] (to get this in python type range(1, 15+1))
rss = pd.DataFrame(columns = ['degree','RSS'])
for degree in range(1,16):
    x = np.array(train_data['sqft_living'])
    y = np.array(train_data['price'])
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    poly_features = poly.fit_transform(x.reshape(-1, 1))
    poly_reg_model = LinearRegression()
    poly_reg_model.fit(poly_features, y)


    x = np.array(valid_data['sqft_living'])
    poly_features = poly.fit_transform(x.reshape(-1, 1))
    y_predicted = poly_reg_model.predict(poly_features)
    RSS = np.sum(np.square(y_predicted - valid_data['price']))
    rss.loc[len(rss.index)] = [degree,sqrt(RSS)/len(valid_data)]
print (rss.sort_values('RSS'))
# Learn a polynomial regression model to sqft vs price with that degree on TRAIN data
# Compute the RSS on VALIDATION data (here you will want to use .predict()) for that degree and you will need to make a polynmial SFrame using validation data.
# Report which degree had the lowest RSS on validation data (remember python indexes from 0)

#define predictor and response variables
x = np.array(train_data['sqft_living'])
y = np.array(train_data['price'])
poly = PolynomialFeatures(degree=6, include_bias=False)
poly_features = poly.fit_transform(x.reshape(-1, 1))
poly_reg_model = LinearRegression()
poly_reg_model.fit(poly_features, y)

x = np.array(test_data['sqft_living'])
poly_features = poly.fit_transform(x.reshape(-1, 1))
y_predicted = poly_reg_model.predict(poly_features)
RSS = np.sum(np.square(y_predicted - test_data['price']))
print (sqrt(RSS)/len(test_data))
# plt.show()