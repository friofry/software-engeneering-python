class Cell:
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
