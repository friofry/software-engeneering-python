from cell import Cell
from labyrinth import Labyrinth


def all_walls(cell):
    return cell._left and cell._right and cell._up and cell._down


class CountClosedCellsVisitor:
    def __init__(self):
        self._enclosed_cells = 0

    def reset(self):
        self._enclosed_cells = 0

    def visit_cell(self, cell):
        if isinstance(cell, Cell):
            if all_walls(cell):
                self._enclosed_cells += 1
        else:
            raise Exception("Invalid argument: not a cell")

    def visit_labyrinth(self, lab):
        if isinstance(lab, Labyrinth):
            for k, v in lab.get_labyrinth_dict().items():
                self.visit(v)
        else:
            raise Exception("Invalid argument: not a labyrinth")

    def visit(self, lab_item):
        if isinstance(lab_item, Labyrinth):
            self.visit_labyrinth(lab_item)

        if isinstance(lab_item, Cell):
            self.visit_cell(lab_item)

        if not isinstance(lab_item, Labyrinth) and \
                not isinstance(lab_item, Cell):
            raise Exception("Invalid argument: not a cell, not a labyrinth")

    def get_result(self):
        return self._enclosed_cells

