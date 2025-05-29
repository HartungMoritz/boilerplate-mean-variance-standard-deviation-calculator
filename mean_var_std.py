import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')

    arr = np.array(list).reshape(3,3)

    mean = [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.mean()]
    variance = [arr.var(axis = 0).tolist(), arr.var(axis = 1).tolist(), arr.var()]
    standard_deviation = [arr.std( axis = 0).tolist(), arr.std( axis = 1).tolist(), arr.std()]
    arr_max = [arr.max( axis = 0).tolist(), arr.max( axis = 1).tolist(), arr.max()]
    arr_min = [arr.min( axis = 0).tolist(), arr.min( axis = 1).tolist(), arr.min()]
    arr_sum = [arr.sum( axis = 0).tolist(), arr.sum( axis = 1).tolist(), arr.sum()]

    calculations ={
        'mean': mean,
        'variance': variance,
        'standard deviation': standard_deviation,
        'max' : arr_max,
        'min': arr_min,
        'sum': arr_sum
    }

    return calculations