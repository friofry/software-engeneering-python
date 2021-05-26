from .icell import ICell
from .ilabyrinth import ILabyrinth


def all_walls(cell):
    if not isinstance(cell, ICell):
        raise Exception("Not a ICell")

    return cell.get_left_wall() and \
           cell.get_right_wall() and \
           cell.get_up_wall() and \
           cell.get_down_wall()


class EnclosedCellsCounterVisitor:
    def __init__(self):
        self._enclosed_cells = 0

    def reset(self):
        self._enclosed_cells = 0

    def visit_cell(self, cell):
        if all_walls(cell):
            self._enclosed_cells += 1

    def visit_labyrinth(self, lab):
        for k, v in lab.get_labyrinth_dict().items():
            self.visit(v)

    def visit(self, lab_item):
        if isinstance(lab_item, ILabyrinth):
            self.visit_labyrinth(lab_item)
        elif isinstance(lab_item, ICell):
            self.visit_cell(lab_item)
        else:
            raise Exception("Invalid argument: not a cell, not a labyrinth")

    def get_result(self):
        return self._enclosed_cells

