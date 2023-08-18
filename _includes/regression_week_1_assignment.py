import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from math import log
import os

train_data=pd.read_csv('..\Coursera\kc_house_train_data.csv')
train_data = train_data.astype(dtype= {'bathrooms':float, 'waterfront':int, 'sqft_above':int, 'sqft_living15':float, 'grade':int, 'yr_renovated':int, 'price':float, 'bedrooms':float, 'zipcode':str, 'long':float, 'sqft_lot15':float, 'sqft_living':float, 'floors':str, 'condition':int, 'lat':float, 'date':str, 'sqft_basement':int, 'yr_built':int, 'id':str, 'sqft_lot':int, 'view':int})
test_data=pd.read_csv('..\Coursera\kc_house_test_data.csv')
test_data = test_data.astype(dtype= {'bathrooms':float, 'waterfront':int, 'sqft_above':int, 'sqft_living15':float, 'grade':int, 'yr_renovated':int, 'price':float, 'bedrooms':float, 'zipcode':str, 'long':float, 'sqft_lot15':float, 'sqft_living':float, 'floors':str, 'condition':int, 'lat':float, 'date':str, 'sqft_basement':int, 'yr_built':int, 'id':str, 'sqft_lot':int, 'view':int})
sales = pd.concat([train_data,test_data])
prices = sales['price'] # extract the price column of the sales SFrame -- this is now an SArray

# recall that the arithmetic average (the mean) is the sum of the prices divided by the total number of houses:
sum_prices = prices.sum()
num_houses = prices.shape[0] # when prices is an SArray .size() returns its length
avg_price_1 = sum_prices/num_houses
avg_price_2 = prices.mean() # if you just want the average, the .mean() function
print ("average price via method 1: " + str(avg_price_1))
print ("average price via method 2: " + str(avg_price_2))


half_prices = 0.5*prices
# Let's compute the sum of squares of price. We can multiply two SArrays of the same length elementwise also with *
prices_squared = prices*prices
sum_prices_squared = prices_squared.sum() # price_squared is an SArray of the squares and we want to add them up.
print ("the sum of price squared is: " + str(sum_prices_squared))


def simple_linear_regression(input_feature, output):
    X=input_feature
    Y=output
    N=len(input_feature)
    numerator = (sum(Y*X)) - (1 / N) * ((sum(X)) * (sum(Y)))
    denominator = (sum((X*X))) - (1 / N) * ((sum(X)) * (sum(X)))
    # # use the formula for the slope
    slope=numerator/denominator
    # use the formula for the intercept
    intercept = (sum(Y)/N) - slope * (sum(X)/N)
    return (intercept, slope)

test_feature = np.array(range(5))
test_output = np.array([1 + 1*test_feature])
(test_intercept, test_slope) =  simple_linear_regression(test_feature, test_output)
print ("Intercept: " + str(test_intercept))
print ("Slope: " + str(test_slope))

sqft_intercept, sqft_slope = simple_linear_regression(train_data['sqft_living'], train_data['price'])

## Something doesn't seem to be working here even when using the same function as above
print ("Intercept: " + str(sqft_intercept))
print ("Slope: " + str(sqft_slope))

def get_regression_predictions(input_feature, intercept, slope):
    predicted_values = input_feature*slope * intercept

    return predicted_values
my_house_sqft = 2650
estimated_price = get_regression_predictions(my_house_sqft, sqft_intercept, sqft_slope)
print ("The estimated price for a house with %d squarefeet is $%.2f" % (my_house_sqft, estimated_price))

def get_residual_sum_of_squares(input_feature, output, intercept, slope):
    # compute predictions
    y_pred = input_feature*slope + intercept

    RSS = np.sum(np.square(y_pred- output))
    return(RSS)

print (get_residual_sum_of_squares(test_feature, test_output, test_intercept, test_slope)) # should be 0.0

rss_prices_on_sqft = get_residual_sum_of_squares(train_data['sqft_living'], train_data['price'], sqft_intercept, sqft_slope)
print ('The RSS of predicting Prices based on Square Feet is : ' + str(rss_prices_on_sqft))

def inverse_regression_predictions(output, intercept, slope):
    # solve output = intercept + slope*input_feature for input_feature. Use this equation to compute the inverse predictions:
    estimated_feature = output/slope-intercept
    return estimated_feature

my_house_price = 800000
estimated_squarefeet = inverse_regression_predictions(my_house_price, sqft_intercept, sqft_slope)
print ("The estimated squarefeet for a house worth $%.2f is %d" % (my_house_price, estimated_squarefeet))