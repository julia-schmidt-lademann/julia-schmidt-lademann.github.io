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

def get_numpy_data(data_sframe, features, output):
    data_sframe['constant'] = 1 # this is how you add a constant column to an SFrame
    # add the column 'constant' to the front of the features list so that we can extract it along with the others:
    features = ['constant'] + features # this is how you combine two lists
    # select the columns of data_SFrame given by the features list into the SFrame features_sframe (now including constant):
    features_sframe = data_sframe[features]
    # the following line will convert the features_SFrame into a numpy matrix:
    feature_matrix = features_sframe.to_numpy()
    # assign the column of data_sframe associated with the output to the SArray output_sarray
    output_sarray = data_sframe[output].to_numpy()
    # the following will convert the SArray into a numpy array by first converting it to a list
    output_array = output_sarray
    return(feature_matrix, output_array)

(example_features, example_output) = get_numpy_data(sales, ['sqft_living'], 'price') # the [] around 'sqft_living' makes it a list
print (example_features) # this accesses the first row of the data the ':' indicates 'all columns'
print (example_output )# and the corresponding output

my_weights = np.array([1., 1.]) # the example weights
my_features = example_features[0,] # we'll use the first data point
predicted_value = np.dot(my_features, my_weights)
print ('predicted_value',predicted_value)


def predict_output(feature_matrix, weights):
    # assume feature_matrix is a numpy matrix containing the features as columns and weights is a corresponding numpy array
    # create the predictions vector by using np.dot()
    predictions = np.dot(feature_matrix,weights)
    return(predictions)

test_predictions = predict_output(example_features, my_weights)
print (test_predictions[0]) # should be 1181.0
print (test_predictions[1]) # should be 2571.0

def feature_derivative(errors, feature):
    # Assume that errors and feature are both numpy arrays of the same length (number of data points)
    # compute twice the dot product of these vectors as 'derivative' and return the value
    #  the derivative for the weight for feature_i is just two times the dot product between the values of feature_i and the current errors.
    derivative = 2*np.dot(feature,errors)
    return(derivative)

(example_features, example_output) = get_numpy_data(sales, ['sqft_living'], 'price')
my_weights = np.array([0., 0.]) # this makes all the predictions 0
test_predictions = predict_output(example_features, my_weights)
# just like SFrames 2 numpy arrays can be elementwise subtracted with '-':
errors = test_predictions - example_output # prediction errors in this case is just the -example_output
feature = example_features[:,0] # let's compute the derivative with respect to 'constant', the ":" indicates "all rows"
derivative = feature_derivative(errors, feature)
print (derivative)
print (-np.sum(example_output)*2) # should be the same as derivative


from math import sqrt # recall that the magnitude/length of a vector [g[0], g[1], g[2]] is sqrt(g[0]^2 + g[1]^2 + g[2]^2)


def regression_gradient_descent(feature_matrix, output, initial_weights, step_size, tolerance):
    converged = False
    weights = np.array(initial_weights)  # make sure it's a numpy array
    gradient_magnitude = 0
    while not converged:
        # compute the predictions based on feature_matrix and weights using your predict_output() function
        predictions =  predict_output(feature_matrix, weights)
        # compute the errors as predictions - output
        errors = predictions - output
        gradient_sum_squares = 0  # initialize the gradient sum of squares
        # while we haven't reached the tolerance yet, update each feature's weight

        for i in range(len(weights)):  # loop over each weight
        # Recall that feature_matrix[:, i] is the feature column associated with weights[i]
        # compute the derivative for weight[i]:
            derivative = feature_derivative(errors[i], feature_matrix[i])
        # add the squared value of the derivative to the gradient sum of squares (for assessing convergence)
            gradient_magnitude += derivative[i]**2
        # subtract the step size times the derivative from the current weight
            weights[i] -= step_size*derivative[i]
        # compute the square-root of the gradient sum of squares to get the gradient magnitude:
            gradient_magnitude = sqrt(gradient_sum_squares)
        if gradient_magnitude < tolerance:
            converged = True
        else:
            gradient_magnitude = 0
    return (weights)


simple_features = ['sqft_living']
my_output = 'price'
(simple_feature_matrix, output) = get_numpy_data(train_data, simple_features, my_output)
initial_weights = np.array([-47000., 1.])
step_size = 7e-12
tolerance = 2.5e7

gradient_descent = regression_gradient_descent(simple_feature_matrix, output, initial_weights, step_size, tolerance)
print (gradient_descent)

model_features = ['sqft_living', 'sqft_living15'] # sqft_living15 is the average squarefeet for the nearest 15 neighbors.
my_output = 'price'
(feature_matrix, output) = get_numpy_data(train_data, model_features, my_output)
initial_weights = np.array([-100000., 1., 1.])
step_size = 4e-12
tolerance = 1e9


gradient_descent = regression_gradient_descent(feature_matrix, output, initial_weights, step_size, tolerance)
print (gradient_descent)