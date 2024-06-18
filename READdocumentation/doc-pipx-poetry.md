### Tutoriel Complet : Utiliser Conda avec Pipx et Poetry

Dans ce tutoriel, nous allons installer Pipx en global et utiliser Poetry pour gérer les dépendances du projet.



## A FAIRE UNE FOIS

### Étape 1 : Installation de Pipx

3. **Installer Pipx** :
   - Pipx est utilisé pour installer des outils Python en ligne de commande dans des environnements virtuels dédiés.
     ```bash
     pip install pipx
     ```

4. **Ajouter Pipx au Chemin** :
   - Ajoutez le chemin de pipx à votre environnement pour que les outils installés soient accessibles globalement.
     ```bash
     pipx ensurepath
     ```

### Étape 2 : Installation de Poetry avec Pipx

5. **Installer Poetry avec Pipx** :
   - Poetry sera installé dans un environnement virtuel géré par pipx, le rendant accessible globalement sans interférer avec les environnements de projet.
     ```bash
     pipx install poetry
     ```



## A FAIRE POUR CHAQUE ENVIRONNEMENT VIRTUEL


### Étape 3 : Création d'un Environnement Conda Local

1. **Créer un Environnement Conda Local** :
   - Cette commande crée un environnement Conda dans un dossier nommé `venv` dans le répertoire actuel et installe Python 3.12.
     ```bash
     conda create -p ./venv python=3.12 -y
     ```
   - `-p ./venv` spécifie le chemin de l'environnement, le créant dans le dossier actuel.
   - `python=3.12` installe la version 3.12 de Python.
   - `-y` accepte automatiquement les invites de confirmation.

2. **Activer l'Environnement Conda** :
   - Activez l'environnement Conda nouvellement créé :
     ```bash
     conda activate ./venv
     ```



## SI ON DEMARRE DE ZERO : Initialisation d'un Projet avec Poetry

1. **Initialiser un Nouveau Projet Poetry** :
   - Créez un nouveau projet Poetry dans le répertoire actuel. Poetry vous guidera à travers une série de questions pour configurer le projet.
     ```bash
     poetry init
     ```
   - Vous serez invité à fournir des informations telles que le nom du projet, la version, la description, etc.


2. **Ajouter des Dépendances** :
   - Utilisez Poetry pour ajouter des dépendances à votre projet. Par exemple, pour ajouter `numpy` et `pandas` :
     ```bash
     poetry add numpy pandas
     ```



3. **Le Fichier `pyproject.toml` est généré automatiquement** :
   - Le fichier `pyproject.toml` sera automatiquement mis à jour pour inclure les dépendances que vous avez ajoutées.














## SI ON A DEJA UN FICHIER `pyproject.toml` avec Toutes les Dépendances


**Installer les Dépendances** :
   - Installez toutes les dépendances spécifiées dans le fichier `pyproject.toml` :
     ```bash
     poetry install
     ```



## Exemple Complet

#### 1. Initialiser le Projet

```bash
mkdir myproject
cd myproject
poetry init
```

Lors de l'initialisation, Poetry vous demandera des informations telles que le nom du projet, la version de Python, la description, etc. Vous pouvez accepter les valeurs par défaut ou entrer vos propres valeurs.

#### 2. Ajouter des Dépendances

Ajoutez les dépendances dont vous avez besoin :

```bash
poetry add numpy pandas
```

Vous pouvez continuer à ajouter d'autres dépendances de la même manière.

#### 3. Vérifier le Fichier `pyproject.toml`

Après avoir ajouté vos dépendances, le fichier `pyproject.toml` ressemblera à ceci :

```toml
[tool.poetry]
name = "myproject"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = ">=3.10.0, <=3.12"
numpy = "^1.21.0"
pandas = "^1.3.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

### Gérer les Dépendances Déjà Installées

Si vous avez déjà un environnement avec des dépendances installées via `pip` et vous souhaitez les transférer dans un projet Poetry, vous pouvez utiliser les étapes suivantes :

1. **Exporter les Dépendances Pip** :

   ```bash
   pip freeze > requirements.txt
   ```

2. **Convertir `requirements.txt` en `pyproject.toml`** :

   Utilisez un outil comme `pipreqs-poetry` pour convertir les dépendances :

   ```bash
   pip install pipreqs-poetry
   pipreqs-poetry ./ --force
   ```

3. **Installer les Dépendances avec Poetry** :

   ```bash
   poetry install
   ```

