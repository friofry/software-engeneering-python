from icell import ICell


class Cell(ICell):
    def __init__(self, l, r, u, d):
        self._left = l
        self._right = r
        self._up = u
        self._down = d

    def set_left_wall(self, opened):
        self._left = opened

    def set_right_wall(self, opened):
        self._right = opened

    def set_up_wall(self, opened):
        self._up = opened

    def set_down_wall(self, opened):
        self._down = opened

    # from ICell
    def get_left_wall(self):
        return self._left

    def get_right_wall(self):
        return self._right

    def get_up_wall(self):
        return self._up

    def get_down_wall(self):
        return self._down
