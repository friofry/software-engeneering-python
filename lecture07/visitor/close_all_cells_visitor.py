from cell import Cell
from labyrinth import Labyrinth


class CloseCellsVisitor:
    def __init__(self):
        pass

    def visit_cell(self, cell_opened, cell):
        cell.set_left_wall(not cell_opened)
        cell.set_right_wall(not cell_opened)
        cell.set_up_wall(not cell_opened)
        cell.set_down_wall(not cell_opened)

    def visit_labyrinth(self, cell_opened, lab):
        for pos, item in lab.get_labyrinth_dict().items():
            self.visit(cell_opened, item)

    def visit(self, cell_opened, lab_item):
        if isinstance(lab_item, Labyrinth):
            self.visit_labyrinth(cell_opened, lab_item)

        if isinstance(lab_item, Cell):
            self.visit_cell(cell_opened, lab_item)


