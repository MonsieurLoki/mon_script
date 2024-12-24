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
        
    def load_csv_files(self, file_paths):
        """
        Charge plusieurs fichiers CSV et les fusionne en une seule base de données.
        :param file_paths: Liste des chemins des fichiers CSV.
        :return: DataFrame consolidé ou une exception en cas d'erreur.
        """
        loaded_data = []
        for file_path in file_paths:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Le fichier '{file_path}' est introuvable.")

            try:
                # Lecture en forçant le délimiteur et en nettoyant les espaces
                df = pd.read_csv(file_path, sep=";", encoding="utf-8")
                loaded_data.append(df)
            except Exception as e:
                raise ValueError(f"Erreur lors du chargement du fichier '{file_path}': {e}")

        # Vérification des colonnes
        column_sets = [set(df.columns) for df in loaded_data]
        if not all(columns == column_sets[0] for columns in column_sets):
            raise ValueError("Les colonnes des fichiers CSV ne sont pas cohérentes.")

        # Fusionner les fichiers
        self.data = pd.concat(loaded_data, ignore_index=True)
        return self.data

    def get_data(self):
        """
        Retourne les données consolidées.
        """
        return self.data