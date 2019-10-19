import matplotlib.pyplot as plt
import numpy as np
from data_generator.barometer import Barometer
from data_generator.utils import list_std_dev

if __name__ == "__main__":
    barometer = Barometer()

    real_psi = 1

    output_range = barometer.output_max - barometer.output_min

    x = [barometer.get_reading(real_psi) for i in range(10000)]
    output_std_dev = list_std_dev(x)

    plt.hist(x, bins=50)
    plt.gca().set(title="Barometer Outputs", ylabel="Frequency")
    plt.gca().set_xlim(left=0)
    plt.gca().set_ylim(bottom=0)
    plt.show(block=True)