import sys


class ICoords:
    def get_components(self):
        raise NotImplementedError('ICoords::get_components() not implemented')


# Option 2: OOP interface implemented
class HorizontalCoords(ICoords):
    def __init__(self, alt, azmth):
        self.altitude = alt
        self.azimuth = azmth

    def get_components(self):
        return [('altitude', self.altitude), ('azimuth', self.azimuth)]
