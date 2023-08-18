import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from math import log
import os

train_data=pd.read_csv('..\Coursera\kc_house_train_data.csv')
train_data = train_data.astype(dtype= {'bathrooms':float, 'waterfront':int, 'sqft_above':int, 'sqft_living15':float, 'grade':int, 'yr_renovated':int, 'price':float, 'bedrooms':float, 'zipcode':str, 'long':float, 'sqft_lot15':float, 'sqft_living':float, 'floors':str, 'condition':int, 'lat':float, 'date':str, 'sqft_basement':int, 'yr_built':int, 'id':str, 'sqft_lot':int, 'view':int})
test_data=pd.read_csv('..\Coursera\kc_house_test_data.csv')
test_data = test_data.astype(dtype= {'bathrooms':float, 'waterfront':int, 'sqft_above':int, 'sqft_living15':float, 'grade':int, 'yr_renovated':int, 'price':float, 'bedrooms':float, 'zipcode':str, 'long':float, 'sqft_lot15':float, 'sqft_living':float, 'floors':str, 'condition':int, 'lat':float, 'date':str, 'sqft_basement':int, 'yr_built':int, 'id':str, 'sqft_lot':int, 'view':int})

example_features = ['sqft_living', 'bedrooms', 'bathrooms']
# example_model = graphlab.linear_regression.create(train_data, target = 'price', features = example_features, validation_set = None)


example_model = LinearRegression().fit(train_data[['sqft_living', 'bedrooms', 'bathrooms']].values, train_data['price'].values)


example_weight_summary = example_model.coef_
print (example_weight_summary)

example_predictions=example_model.predict(np.array(train_data[['sqft_living', 'bedrooms', 'bathrooms']]))


# example_predictions = example_model.predict(train_data)
print (example_predictions[0]) # should be 271789.505878



def get_residual_sum_of_squares(model, data, outcome):
    # compute predictions
    y_pred = model.predict(data)
    # Then compute the residuals/errors
    # Then square and add them up
    RSS = np.sum(np.square(y_pred- outcome))
    return(RSS)


rss_example_train = get_residual_sum_of_squares(example_model, np.array(test_data[['sqft_living', 'bedrooms', 'bathrooms']].values), test_data['price'])
print (rss_example_train) # should be 2.7376153833e+14

train_data['bedrooms_squared'] = train_data['bedrooms'].apply(lambda x: x**2)
test_data['bedrooms_squared'] = test_data['bedrooms'].apply(lambda x: x**2)

train_data['bed_bath_rooms'] = train_data['bedrooms']*train_data['bathrooms']
test_data['bed_bath_rooms'] = train_data['bedrooms']*train_data['bathrooms']

train_data['log_sqft_living'] = train_data['sqft_living'].apply(lambda x: log(x))
test_data['log_sqft_living'] = test_data['sqft_living'].apply(lambda x: log(x))

train_data['lat_plus_long'] = train_data['lat']+train_data['long']
test_data['lat_plus_long'] = train_data['lat']+train_data['long']



model_1_features = ['sqft_living', 'bedrooms', 'bathrooms', 'lat', 'long']
model_2_features = model_1_features + ['bed_bath_rooms']
model_3_features = model_2_features + ['bedrooms_squared', 'log_sqft_living', 'lat_plus_long']
# Learn the three models: (don't forget to set validation_set = None)
example_1_model = LinearRegression().fit(train_data[model_1_features].values, train_data['price'].values)
example_2_model = LinearRegression().fit(train_data[model_2_features].values, train_data['price'].values)
example_3_model = LinearRegression().fit(train_data[model_3_features].values, train_data['price'].values)

# Examine/extract each model's coefficients:

print (example_1_model.coef_)
print (example_2_model.coef_)
print (example_3_model.coef_)

# Compute the RSS on TRAINING data for each of the three models and record the values:

print (get_residual_sum_of_squares(example_1_model, np.array(train_data[model_1_features].values), train_data['price']))
print (get_residual_sum_of_squares(example_2_model, np.array(train_data[model_2_features].values), train_data['price']))
print (get_residual_sum_of_squares(example_3_model, np.array(train_data[model_3_features].values), train_data['price']))


# Compute the RSS on TESTING data for each of the three models and record the values:

print (get_residual_sum_of_squares(example_1_model, np.array(test_data[model_1_features].values), test_data['price']))
print (get_residual_sum_of_squares(example_2_model, np.array(test_data[model_2_features].values), test_data['price']))
print (get_residual_sum_of_squares(example_3_model, np.array(test_data[model_3_features].values), test_data['price']))
