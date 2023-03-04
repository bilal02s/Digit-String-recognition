import numpy as np

# Mean Squared Error and its derivative
def mse(prediction, expected):
    return np.mean(np.power(prediction - expected, 2))

def mse_prime(prediction, expected):
    return 2*(prediction - expected)/expected.size

# activation function and its derivative
def tanh(x):
    return np.tanh(x);

def tanh_prime(x):
    return 1-np.tanh(x)**2;

def accuracy(predictions, true_result):
    predictions = np.argmax(predictions, axis=1)
    true_result = np.argmax(true_result, axis=1)
    
    return np.mean(predictions == true_result)