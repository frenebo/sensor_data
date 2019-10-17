from .sensor import Sensor

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
        this.output_min = 0.1*(2**24)
        this.output_max = 0.9*(2**24)

        this.pressure_min = 0 # psi
        this.pressure_max = 25 # psi
        this.error_band = 0.015
        pass
    def get_reading(self, psi_value):
        """
        Pressure range
        """
        ideal_output = this.output_min + (psi_value - this.pressure_min)*(this.output_max - this.output_min)/(this.pressure_max - this.pressure_min)
