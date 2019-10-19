from .sensor import Sensor
from .sensor_error_generator import SensorErrorGenerator

"""
Part number: MPRLS0025PA00001A
source: Honeywell datasheet
- MPR Series Pressure Sensor
- Long port
- Silicone gel
- 0 psi to 25 psi absolute pressure range
- I2C protocol, address 0x18
- Transfer function 10% to 90% of 2^24 counts
- Pressure output function:
    Pressure = P_min + (Output - Output_min)*(P_max-P_min)/(Output_max-Output_min)
    rearranging gives:
    Output = Output_min + (Pressure - Pressure_min)*(Output_max - Output_min)/(Pressure_max - Pressure_min)

    Output_min = 0.1*2^24
    Output_max = 0.9*2^24

    Pressure_min = 0 psi
    Pressure_max = 25 psi

    Error band: +/- 1.5% of full scale span (Output_max - Output_min)
"""
class Barometer(Sensor):
    def __init__(self):
        self.output_min = 0.1*(2**24)
        self.output_max = 0.9*(2**24)

        output_range = self.output_max - self.output_min

        self.pressure_min = 0 # psi
        self.pressure_max = 25 # psi

        pressure_range = self.pressure_max - self.pressure_min

        total_error_band = 0.015*output_range
        total_error_band_confidence = 0.99

        self.error_generator = SensorErrorGenerator(total_error_band, total_error_band_confidence)

    def get_reading(self, real_psi):
        """
        Pressure range
        """
        # psi_value = self.initial_offset + real_psi + gaussian_random(self.reading_std_dev)
        ideal_output = self.output_min + (real_psi - self.pressure_min)*(self.output_max - self.output_min)/(self.pressure_max - self.pressure_min)

        error = self.error_generator.get_reading_error()

        return int(ideal_output + error)

        # return int(ideal_output)
