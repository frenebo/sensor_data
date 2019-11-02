from .utils import get_error_band_std_dev, gaussian_random

class SensorErrorGenerator:
    def __init__(
        self,
        total_error_band,
        total_error_band_confidence,
    ):
        total_std_dev = get_error_band_std_dev(total_error_band, total_error_band_confidence)

        # Including initial offset and further reading offsets
        # total_std_dev^2 = initial_std_dev^2 + reading_std_dev^2
        # we assume initial_std_dev = reading_std_dev, giving
        # (total_std_dev^2)/2 = initial_std_dev^2 = reading_std_dev^2
        # initial_std_dev = reading_std_dev = sqrt((total_std_dev^2)/2)
        initial_offset_std_dev = self.reading_std_dev = ( (total_std_dev**2) / 2 )**0.5

        # Puts half randomness in initial offset, half in subsequent readings - arbitrary decision, can be changed

        self.initial_offset = gaussian_random(initial_offset_std_dev)

    def get_reading_error(self):
        return self.initial_offset + gaussian_random(self.reading_std_dev)