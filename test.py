import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from data_generator.barometer import Barometer
from data_generator.imu import Imu
from data_generator.gps import Gps
from data_generator.utils import list_std_dev
import sys

def test_barometer():
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

def test_gps():
    gps = Gps()

    real_x_meters = 2.5
    real_y_meters = 2.5
    real_z_meters = 10

    readings = [gps.get_reading(real_x_meters, real_y_meters, real_z_meters) for i in range(10000)]
    readings = np.array(readings)

    x = readings[:,0]
    y = readings[:,1]
    print(np.mean(x))
    print(np.mean(y))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    hist, xedges, yedges = np.histogram2d(
        x,
        y,
        bins=20,
        range=[[0,5],[0,5]])

    xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
    xpos = xpos.ravel()
    ypos = ypos.ravel()
    zpos = 0

    # Construct arrays with the dimensions for the 16 bars.
    dx = dy = 0.5 * np.ones_like(zpos)
    dz = hist.ravel()

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
    print("showing")
    plt.show(block=True)

def test_imu():
    raise Exception("Unimplemented")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise ValueError("Takes one argument: thing to test (e.x. barometer, gps...)")
    elif len(sys.argv) > 2:
        raise ValueError("Takes only one argument: thing to test")

    if sys.argv[1] == "barometer":
        test_barometer()
    elif sys.argv[1] == "gps":
        test_gps()
    elif sys.argv[1] == "imu":
        test_imu()
    else:
        raise Exception("invalid arg")