from scipy.stats import norm
import numpy as np

def get_error_band_std_dev(error_band, error_confidence):
    std_devs = -norm.ppf((1-error_confidence)/2)

    std_dev = error_band/std_devs

    return std_dev

def gaussian_random(std_dev):
    return np.random.normal(0, std_dev)

def list_std_dev(list):
    return np.std(list)