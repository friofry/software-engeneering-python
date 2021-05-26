from my_project.icell import ICell
from thirdparty_project.gcell import GCell


class GCellAdapter(ICell):
    def __init__(self, gcell):
        if isinstance(gcell, GCell):
            self._gcell = gcell
        else:
            raise Exception("Not a GCell.")

    def get_left_wall(self):
        return self._gcell._content.count("l") == 1

    def get_right_wall(self):
        return self._gcell._content.count("r") == 1

    def get_up_wall(self):
        return self._gcell._content.count("u") == 1

    def get_down_wall(self):
        return self._gcell._content.count("d") == 1

