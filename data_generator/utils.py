import math

def normpdf(x, mean, sd):
    sd_squared = sd**2
    denom = (2*math.pi*sd_squared)**0.5
    num = math.exp(-(x-mean)**2/(2*sd_squared))
    return num / denom

def get_error_band_noise(error_band, range):
    0.99
    # retu