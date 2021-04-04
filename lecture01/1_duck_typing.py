## ------------------------------------------------------------------------- ##
# Option 1: Duck-typed interface implemented

class SphericalCoords:
    def __init__(self, dst, polar, azmth):
        self.distance = dst
        self.polarAngle = polar
        self.azimuthAngle = azmth

    # Duck-typed interface implemented.
    def get_components(self):
        return [('distance', self.distance),
                ('polarAngle', self.polarAngle),
                ('azimuthAngle', self.azimuthAngle)]

    # def distance(self):
    #     return self.distance