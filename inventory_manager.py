import pandas as pd
import os


class InventoryManager:
    def __init__(self):
        self._data = pd.DataFrame()  ##protection de data avec 1 _

    @property
    def data(self):
        """Getter pour accéder aux données."""
        return self._data

    @data.setter
    def data(self, new_data):
        """Setter pour modifier les données avec validation."""
        if isinstance(new_data, pd.DataFrame):
            self._data = new_data
        else:
            raise ValueError("Les données doivent être un DataFrame pandas.")