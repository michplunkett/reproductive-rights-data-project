"""
This file contains the abstract class that will be used to build all the
visualizations for this repository.
"""

from collections.abc import MutableMapping
from abc import abstractmethod


class Visualization(MutableMapping):
    """
    This abstract class is the one that all visualizations will be built on.

    Author(s): Kate Habich, Michael Plunkett
    """

    @abstractmethod
    def __init__(self, files):
        pass

    @abstractmethod
    def _import_files(self):
        """
        This method accesses a JSON file(s) and returns a dictionary of data for
        the visualization.
        """
        pass

    @abstractmethod
    def create(self):
        """
        This method takes the dictionary made in the _import_file() method and
        creates a visualization with it.
        """
        pass