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

    print("Output std dev: ", output_std_dev)
    print("Output std dev percent: ", output_std_dev/output_range)

    plt.hist(x, bins=50)
    plt.gca().set(title="Barometer Outputs", ylabel="Frequency")
    plt.gca().set_xlim(left=0)
    plt.gca().set_ylim(bottom=0)
    plt.show(block=True)

    # Plot Histogram on x
    # x = np.random.normal(size = 1000)
    # x = [gaussian_random(initial_offset_std_dev) for i in range(1000)]
    # plt.hist(x, bins=50)
    # plt.gca().set(title='Frequency Histogram', ylabel='Frequency');
    # plt.show(block=True)