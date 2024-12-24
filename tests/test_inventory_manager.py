import unittest
import pandas as pd
from inventory_manager import InventoryManager


class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        """Configuration avant chaque test"""
        self.manager = InventoryManager()
        self.sample_data = pd.DataFrame({
            "Id": [1, 2, 3, 4],
            "Nom du produit": ["Smartphone", "Table", "Chaise", "TV"],
            "Quantite": [50, 30, 70, 15],
            "Prix": [699.99, 150.00, 89.99, 499.99],
            "Categorie": ["Electronique", "Maison", "Maison", "Electronique"]
        })
        self.manager.data = self.sample_data

    def test_load_csv_files(self):
        """Test du chargement et de la fusion des fichiers CSV"""
        # Simule des fichiers CSV chargés
        df1 = pd.DataFrame({
            "Id": [1, 2],
            "Nom du produit": ["Laptop", "Smartphone"],
            "Quantite": [10, 20],
            "Prix": [999.99, 699.99],
            "Categorie": ["Electronique", "Electronique"]
        })
        df2 = pd.DataFrame({
            "Id": [3, 4],
            "Nom du produit": ["Table", "Chaise"],
            "Quantite": [15, 25],
            "Prix": [150.00, 89.99],
            "Categorie": ["Maison", "Maison"]
        })
        self.manager.data = pd.concat([df1, df2], ignore_index=True)
        self.assertEqual(len(self.manager.data), 4)

    def test_search_by_name(self):
        """Test de la recherche par nom du produit"""
        results = self.manager.search_by_name("Smartphone")
        self.assertEqual(len(results), 1)
        self.assertEqual(results.iloc[0]["Nom du produit"], "Smartphone")

    def test_search_by_category(self):
        """Test de la recherche par catégorie"""
        results = self.manager.search_by_category("Maison")
        self.assertEqual(len(results), 2)
        self.assertIn("Table", results["Nom du produit"].values)
        self.assertIn("Chaise", results["Nom du produit"].values)

    def test_search_by_price_range(self):
        """Test de la recherche dans une plage de prix"""
        results = self.manager.search_by_price_range(100, 700)
        self.assertIn("Table", results["Nom du produit"].values)

    def test_generate_report(self):
        """Test de la génération de rapport"""
        output_file = "test_report.csv"
        self.manager.generate_report(output_file)

        # Vérifie si le fichier a été créé
        with open(output_file, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("Nombre total de produits", content)
        self.assertIn("Quantite_totale", content)
        self.assertIn("Valeur_totale", content)

    def test_empty_data_handling(self):
        """Test de gestion des données vides"""
        self.manager.data = pd.DataFrame()  # Données vides
        with self.assertRaises(ValueError):
            self.manager.generate_report()


if __name__ == "__main__":
    unittest.main()