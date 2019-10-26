from .sensor_error_generator import SensorErrorGenerator

"""
Horizontal distance margin: 2.5 m

"""
class Gps:
    def __init__(self):
        total_dist_margin = 2.5 # meters
        x_dist_margin = y_dist_margin = 2.5 / (2**0.5)
        x_dist_margin_confidence = y_dist_margin_confidence = 0.99 # lazy

        z_dist_margin = 2.5*10*(2**0.6)
        z_dist_margin_confidence = 0.99

        # alternative is to generate single distance error, then apply it
        # to a random angle 0 to 2pi

        self.x_error_gen = SensorErrorGenerator(x_dist_margin, x_dist_margin_confidence)
        self.y_error_gen = SensorErrorGenerator(y_dist_margin, y_dist_margin_confidence)
        self.z_error_gen = SensorErrorGenerator(z_dist_margin, z_dist_margin_confidence)

    def get_reading(self, real_x_meters, real_y_meters, real_z_meters):
        return (
            real_x_meters + self.x_error_gen.get_reading_error(),
            real_y_meters + self.y_error_gen.get_reading_error(),
            real_z_meters + self.z_error_gen.get_reading_error(),
        )