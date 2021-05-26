from my_project.ilabyrinth import ILabyrinth
from thirdparty_project.glabyrinth import GCellLabyrinth
from gcell_adapter import GCellAdapter


class GCellLabyrinthAdapter(ILabyrinth):
    def __init__(self, gcelllab):
        if isinstance(gcelllab, GCellLabyrinth):
            self._gcelllab = gcelllab
        else:
            raise Exception("Not a GCell labyrinth.")

    def get_labyrinth_dict(self):
        adapted_dict = dict()
        for k, v in self._gcelllab.get_labyrinth_dict().items():
            adapted_dict[k] = GCellAdapter(v)
        return adapted_dict
