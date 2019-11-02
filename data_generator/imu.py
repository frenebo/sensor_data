from .sensor_error_generator import SensorErrorGenerator

"""
Outputs:
- All are 16 bit words in 2's complement

Acceleration (+/- 2,4,8,16 g's)
- Linear acceleration X axis
- Linear acceleration Y axis
- Linear acceleration Z axis

Angular velocity (+/- 245/500/2000 degrees per second)
- Pitch axis (x) angular rate
- Roll axis (y) angular rate
- Yaw axis (z) angular rate

Magnetic field (+/- 4/8/12/16 Gauss)
- Magnetometer X direction
- Magnetometer Y direction
- Magnetometer Z direction

"""
class Imu:
    def __init__(
        self,
        acceleration_scale_gs = 16,
        angular_velocity_scale_dps = 500,
        magnetic_field_scale_gauss = 4,
    ):
        lin_acceleration_error_margin = 0.1
        ang_velocity_error_margin = 1
        magnetic_field_error_margin = 0.05

        all_error_band_conf = 0.9 # using same error band confidence for all

        self.lin_acc_error_gens = [
            SensorErrorGenerator(lin_acceleration_error_margin, all_error_band_conf)
            for _ in range(3)
        ]

        self.ang_vel_error_gens = [
            SensorErrorGenerator(ang_velocity_error_margin, all_error_band_conf)
            for _ in range(3)
        ]

        self.mag_field_error_gens = [
            SensorErrorGenerator(magnetic_field_error_margin, all_error_band_conf)
            for _ in range(3)
        ]

    def get_all_readings(
        self,
        x_linear_acceleration_gs,
        y_linear_acceleration_gs,
        z_linear_acceleratoin_gs,
        x_angular_velocity_dps,
        y_angular_velocity_dps,
        z_angular_velocity_dps,
        x_magnetic_field_gauss,
        y_magnetic_field_gauss,
        z_magnetic_field_gauss,
        ):

        real_lin_accs = [x_linear_acceleration_gs, y_linear_acceleration_gs, z_linear_acceleration_gs]
        real_ang_accs = [x_angular_velocity_dps, y_angular_velocity_dps, z_angular_velocity_dps]
        real_magnetic_gausses = [x_magnetic_field_gauss, y_magnetic_field_gauss, z_magnetic_field_gauss]

        noisy_lin_accs =         [self.lin_acc_error_gens[i].get_reading_error() + real for i, real in enumerate(real_lin_accs)]
        noisy_ang_accs =         [self.ang_vel_error_gens[i].get_reading_error() + real for i, real in enumerate(real_ang_accs)]
        noisy_magnetic_gausses = [self.mag_field_error_gens[i].get_reading_error() + real for i, real in enumerate(real_magnetic_gausses)]

        lin_acc_readings =
        # return {

        # }