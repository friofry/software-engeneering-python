from my_project.ilabyrinth import ILabyrinth
from my_project.icell import ICell
from thirdparty_project.gcell import GCell
from thirdparty_project.glabyrinth import GCellLabyrinth
from gcell_adapter import GCellAdapter
from glabyrinth_adapter import GCellLabyrinthAdapter
from my_project.count_closed_cells_visitor import EnclosedCellsCounterVisitor


def get_number_of_closed_cells(labyrinth: ILabyrinth):
    closed_cells_counter = EnclosedCellsCounterVisitor()
    closed_cells_counter.visit(labyrinth)
    return closed_cells_counter.get_result()


def print_cell(pos, cell: ICell):
    print(pos, cell.get_left_wall(), cell.get_right_wall(), cell.get_up_wall(), cell.get_down_wall())


def print_labyrinth(labyrinth: ILabyrinth, parent_pos=()):
    for pos, cell in labyrinth.get_labyrinth_dict().items():
        if isinstance(cell, ICell):
            print_cell(parent_pos + pos, cell)
        elif isinstance(cell, ILabyrinth):
            print_labyrinth(cell, pos)


def main():
    first_floor = {
        (0, 0): GCell("lrud"),
        (1, 0): GCell("lrud"),
        (0, 1): GCell("lrud"),
        (1, 1): GCell("lr")
    }

    gcell_lab = GCellLabyrinth(first_floor)

    adapted_gcell_lab = GCellLabyrinthAdapter(gcell_lab)
    print_labyrinth(adapted_gcell_lab)

    print(get_number_of_closed_cells(adapted_gcell_lab))


if __name__ == "__main__":
    main()
