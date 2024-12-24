from inventory_manager import InventoryManager


def main():
    print("Bienvenue dans le système de gestion d'inventaire !")

    # Initialiser l'InventoryManager
    manager = InventoryManager()

    # Demander les fichiers CSV à l'utilisateur
    file_input = input("Entrez les chemins des fichiers CSV à fusionner (séparés par des virgules) : ")
    file_paths = [file.strip() for file in file_input.split(",")]

    try:
        # Charger et fusionner les fichiers CSV
        manager.load_csv_files(file_paths)
        print("\nDonnées consolidées chargées avec succès.")
    except Exception as e:
        print(f"Erreur : {e}")
        return

    while True:
        print("\nOptions disponibles :")
        print("1. Rechercher par nom du produit")
        print("2. Rechercher par catégorie")
        print("3. Rechercher par plage de prix")
        print("4. Afficher toutes les données")
        print("5. Générer un rapport récapitulatif exportable")
        print("6. Quitter")

        choice = input("Choisissez une option : ")

        if choice == "1":
            name = input("Entrez le nom (ou partie du nom) du produit à rechercher : ")
            results = manager.search_by_name(name)
            print("\nRésultats de la recherche par nom :")
            print(results if not results.empty else "Aucun produit trouvé.")

        elif choice == "2":
            category = input("Entrez la catégorie à rechercher : ")
            results = manager.search_by_category(category)
            print("\nRésultats de la recherche par catégorie :")
            print(results if not results.empty else "Aucun produit trouvé.")

        elif choice == "3":
            min_price = input("Entrez le prix minimum : ")
            max_price = input("Entrez le prix maximum : ")
            try:
                results = manager.search_by_price_range(min_price, max_price)
                print("\nRésultats de la recherche par plage de prix :")
                print(results if not results.empty else "Aucun produit trouvé.")
            except ValueError as e:
                print(f"Erreur : {e}")

        elif choice == "4":
            print("\nDonnées consolidées :")
            print(manager.get_data())

        elif choice == "5":
            output_file = input(
                "Entrez le nom du fichier pour le rapport (par défaut : rapport_recapitulatif.csv) : ").strip()
            output_file = output_file if output_file else "rapport_recapitulatif.csv"
            try:
                manager.generate_report(output_file)
            except Exception as e:
                print(f"Erreur : {e}")

        elif choice == "6":
            print("Merci d'avoir utilisé le système de gestion d'inventaire. À bientôt !")
            break
        else:
            print("Option invalide, veuillez réessayer.")


if __name__ == "__main__":
    main()