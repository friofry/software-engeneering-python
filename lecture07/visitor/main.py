from cell import Cell
from labyrinth import Labyrinth
from close_all_cells_visitor import CloseCellsVisitor
from count_closed_cells_visitor import CountClosedCellsVisitor


def get_number_of_closed_cells(labyrinth: Labyrinth):
    closed_cells_counter = CountClosedCellsVisitor()
    closed_cells_counter.visit(labyrinth)
    return closed_cells_counter.get_result()


def print_cell(pos, cell: Cell):
    print(pos, cell._left, cell._right, cell._up, cell._down)


def print_labyrinth(labyrinth: Labyrinth, parent_pos = ()):
    for pos, cell in labyrinth.get_labyrinth_dict().items():
        if isinstance(cell, Cell):
            print_cell(parent_pos + pos, cell)
        elif isinstance(cell, Labyrinth):
            print_labyrinth(cell, pos)


def main():
    internal_labyrinth_dict = {
        (0, 0): Cell(True, True, True, True),
        (1, 0): Cell(True, True, False, True),
        (0, 1): Cell(True, True, True, True),
        (1, 1): Cell(True, True, True, False)
    }

    # labyrinth in labyrinth
    labyrinth_dict = {
        (0, 0): Cell(True, True, True, True),
        (1, 0): Cell(True, True, True, True),
        (0, 1): Cell(True, True, True, True),
        (1, 1): Labyrinth(internal_labyrinth_dict)
    }

    multi_labyrinth = Labyrinth(labyrinth_dict)

    print("labyrinth ", multi_labyrinth.get_labyrinth_dict())
    print_labyrinth(multi_labyrinth)

    # 1. Count closed cells
    closed_number = get_number_of_closed_cells(multi_labyrinth)
    print("Initial number of closed cells in the labyrinth: ", closed_number)

    # 2. Close all cells
    wall_visitor = CloseCellsVisitor()
    wall_visitor.visit(False, multi_labyrinth)
    print("Closing all cells...")
    print_labyrinth(multi_labyrinth)

    # 3. Count closed in the updated labyrinth
    closed_number = get_number_of_closed_cells(multi_labyrinth)
    print("Updated number of closed cells in the labyrinth: ", closed_number)

    # 4. Open all cells
    wall_visitor.visit(True, multi_labyrinth)
    print("Open all cells...")
    print_labyrinth(multi_labyrinth)

    # 5. Count closed in the updated labyrinth
    closed_number = get_number_of_closed_cells(multi_labyrinth)
    print("Updated number of closed cells in the labyrinth: ", closed_number)


if __name__ == "__main__":
    main()
