import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
import math
import random
import matplotlib.pyplot as plt

random.seed(98103)
n = 30
x = sorted(np.array([random.random() for i in range(n)]))
y = np.array([math.sin(4*x) for x in x])
random.seed(1)
e = np.array([random.gauss(0,1.0/3.0) for i in range(n)])
# this adds noise to the data to create something similar to real life
y = y + e
data = pd.DataFrame({'X1':x,'Y':y})
def plot_data(data):
    plt.plot(data['X1'],data['Y'],'k.')
    plt.xlabel('x')
    plt.ylabel('y')

plot_data(data)
# plt.show()

def graplab_polynomial_features(data, deg):
    data_copy=data.copy()
    for i in range(1,deg):
        data_copy['X'+str(i+1)]=data_copy['X'+str(i)]*data_copy['X1']
    return data_copy
def graplab_polynomial_regression(data, deg):
    model = graphlab.linear_regression.create(polynomial_features(data,deg),
                                              target='Y', l2_penalty=0.,l1_penalty=0.,
                                              validation_set=None,verbose=False)
    return model
def graphlab_plot_poly_predictions(data, model):
    plot_data(data)

    # Get the degree of the polynomial
    deg = len(model.coefficients['value']) - 1

    # Create 200 points in the x axis and compute the predicted value for each point
    x_pred = graphlab.SFrame({'X1': [i / 200.0 for i in range(200)]})
    y_pred = model.predict(polynomial_features(x_pred, deg))

    # plot predictions
    plt.plot(x_pred['X1'], y_pred, 'g-', label='degree ' + str(deg) + ' fit')
    plt.legend(loc='upper left')
    plt.axis([0, 1, -1.5, 2])
def graphlab_print_coefficients(model):
    # Get the degree of the polynomial
    deg = len(model.coefficients['value'])-1

    # Get learned parameters as a list
    w = list(model.coefficients['value'])

    # Numpy has a nifty function to print out polynomials in a pretty way
    # (We'll use it, but it needs the parameters in the reverse order)
    print ('Learned polynomial for degree ' + str(deg) + ':')
    w.reverse()
    print (np.poly1d(w))

def polynomial_regression(data, deg):
    poly = PolynomialFeatures(degree=deg, include_bias=False)
    poly_features = poly.fit_transform(data['X1'].to_numpy().reshape(-1, 1))
    model = LinearRegression()
    model.fit(poly_features, data['Y'])
    return model


def plot_poly_predictions(data, model):
    plot_data(data)
    deg = len(model.coef_)
    poly = PolynomialFeatures(degree=deg, include_bias=False)
    poly_features = poly.fit_transform(data['X1'].to_numpy().reshape(-1, 1))
    # Get the degree of the polynomial


    # Create 200 points in the x axis and compute the predicted value for each point
    x_pred = pd.DataFrame({'X1': [i / 200.0 for i in range(200)]})
    y_pred = model.predict(poly_features)
    # plot predictions
    plt.plot(x_pred['X1'], y_pred, 'g-', label='degree ' + str(deg) + ' fit')
    plt.legend(loc='upper left')
    plt.axis([0, 1, -1.5, 2])
    # plt.show()

def print_coefficients(model):
    # Get the degree of the polynomial
    deg = len(model.coef_)
    # Get learned parameters as a list
    w = list(model.coef_)

    # Numpy has a nifty function to print out polynomials in a pretty way
    # (We'll use it, but it needs the parameters in the reverse order)
    print ('Learned polynomial for degree ' + str(deg) + ':')
    w.reverse()
    print (np.poly1d(w))

model = polynomial_regression(data, 2)
#deg 2 = -5.129 x + 4.147
# deg 3 = -8.504 x + 7.392 x - 0.7994
print_coefficients(model)
# plot_poly_predictions(data,model)