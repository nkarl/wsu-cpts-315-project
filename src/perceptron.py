"""
this module contains the standard perceptron.
"""
import numpy as np
def std_tron(v_end, vectors, num_rounds=20, train_rate=1.0):
    """
    this is the standard perceptron algorithm.

    :param v_end [numpy array]: a 1-dim numpy vector
    :param vectors [numpy array]: a numpy array
    :param num_rounds [int]: number of rounds to train
    """
    D, T, eta = len(vectors), num_rounds, train_rate
    weight_v = np.zeros(len(v_end))

    # training
    for Round in range(T):
        for i in range(len(vectors)):
            v_i = vectors[i]
            prediction = np.sign(np.dot(v_end, v_i))
            if prediction < 0:
                y = 1 
                weight_v = weight_v + np.dot(eta * y, v_i)
            elif prediction > 0:
                y = -1 
                weight_v = weight_v + np.dot(eta * y, v_i)

    return weight_v
    
