## Système de Gestion d'Inventaire

### Introduction
Ce système interactif de gestion d'inventaire a été conçu pour faciliter l'organisation, la recherche et l'analyse des stocks. Il permet :

- De regrouper plusieurs fichiers CSV dans une base consolidée.
- D'effectuer des recherches avancées sur les produits en fonction de différents critères.
- De générer des rapports exportables avec des statistiques claires et détaillées.

Ce projet est idéal pour les entreprises souhaitant optimiser leur gestion d'inventaire tout en utilisant un outil léger et facile à déployer.

### Fonctionnalités

#### 1. Consolidation des données
- Fusionne plusieurs fichiers CSV en un seul fichier organisé.
- Supprime automatiquement les doublons pour garantir une base propre.
- Vérifie la cohérence des colonnes entre les fichiers.

#### 2. Recherches dynamiques
- Recherche les produits par nom complet ou partiel.
- Affiche les produits appartenant à une catégorie spécifique.
- Filtre les produits selon une plage de prix définie.

#### 3. Analyse des données
- Affiche toutes les données consolidées directement dans la console.
- Fournit une vue d'ensemble des produits et des catégories.

#### 4. Génération de rapports
Produit un fichier CSV récapitulatif contenant :
- Le nombre total de produits.
- La quantité totale de produits en stock.
- La valeur totale des stocks.
- Les statistiques regroupées par catégorie.

### Exemple d'utilisation

#### Format attendu pour les fichiers CSV
Les fichiers doivent respecter une structure cohérente. Voici un exemple :

```csv
Id;Nom du produit;Quantite;Prix;Categorie
1;Smartphone;50;699.99;Electronique
2;Table;30;150.00;Maison
3;Chaise;70;89.99;Maison
4;TV;15;499.99;Electronique
```

#### Lancement du programme
1. Exécutez le fichier principal :

```bash
python main.py
```
2. Suivez les instructions dans le menu interactif pour :

- Charger des fichiers CSV.
- Rechercher des produits.
- Générer un rapport.

### Rapport généré
Le rapport est sauvegardé sous forme de fichier CSV. Voici un aperçu des informations contenues :

```yaml
#Rapport de Gestion d'Inventaire
Nombre total de produits : 4
Quantité totale : 165
Valeur totale des stocks : 46 148.50 €
#Statistiques par catégorie

Categorie,Quantite_totale,Valeur_totale
Electronique,65,45198.50
Maison,100,950.00
```

### Installation
#### Prérequis
Avoir Python 3.x installé sur votre système.
Installer la bibliothèque pandas :

```bash
pip install pandas
```

#### Configuration
1. Clonez ce dépôt ou téléchargez les fichiers nécessaires.
2. Placez vos fichiers CSV dans un dossier nommé data à la racine du projet.
3. Créez un dossier outputs pour les fichiers consolidés et les rapports générés :

```bash
mkdir data outputs
```

### Tester le système
Des tests unitaires sont fournis pour vérifier le bon fonctionnement du programme. Pour les exécuter, utilisez la commande suivante :

```bash
python -m unittest discover tests
```

### Structure du projet
Voici la structure du projet pour une meilleure compréhension :

```bash
.
├── data/                     # Contient les fichiers CSV d'entrée
├── outputs/                  # Contient les rapports générés et les fichiers consolidés
├── src/
│   inventory_manager.py  # Contient la classe principale de gestion d'inventaire
│   main.py               # Point d'entrée du programme
├── tests/
│   ├── test_inventory_manager.py  # Tests unitaires
├── README.md                 # Documentation principale
```