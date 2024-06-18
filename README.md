# Tutoriel complet en français : personnalisation d'emails avec CrewAI

Ce projet utilise CrewAI pour personnaliser des emails en fonction des informations des destinataires. Il intègre des modèles de langage avancés et des agents IA pour générer et réviser des emails personnalisés.


Ce tutoriel est une adaptation française de :  CrewAI + Groq Tutorial: Crash Course for Beginners 
https://www.youtube.com/watch?v=8bAv5FQBD2M





## Création d'une équipe pour gérer des campagnes d'emails personnalisées

Nous allons créer une équipe qui enverra des emails personnalisés. Cette équipe prendra une liste de clients dans un fichier CSV et un modèle d'email, et générera des emails personnalisés pour chaque client.


## Principe de fonctionnement et structure du projet :

- `agents.py` : Définit les agents IA pour personnaliser et réviser les emails.
- `main.py` : Script principal pour exécuter la personnalisation et révision des emails.
- `tasks.py` : Définit les tâches de personnalisation et de révision d'emails.
- `data/clients_small.csv` : Fichier CSV contenant les informations des clients.




## Prérequis : les API utilisées : 

- `Conda` pour créer un environnement virtuel
- Python 3.7 ou plus
- `pip`pour installer `pipx` pour installer `poetry` pour installer les dépendances Python


- Un accès à  l'API Groq
  1. **Inscrivez-vous sur Groq Cloud** : Si vous n'avez pas encore de compte, inscrivez-vous sur Groq Cloud.
  2. **Créez une clé API** :
     - Accédez à l'onglet des clés API.
     - Cliquez sur "Créer une clé API".
     - Nommez la clé (par exemple, "Tutoriel") et copiez la clé créée.

   - **Qu'est-ce que Groq?**

       Groq est une startup spécialisée dans l'IA qui a développé une nouvelle puce appelée unité de traitement du langage (LPU), conçue pour exécuter des modèles de langage à grande échelle de manière plus rapide et économique. Par exemple, une LPU utilisant Mixl peut traiter 500 tokens par seconde, ce qui est 25 fois plus rapide que ChatGPT et 10 fois plus rapide que Gemini 1.5 de Google. Groq est gratuit pour les développeurs.



## Installation de l'environnement python avec Conda

1. **Créer un environnement virtuel avec conda**
    ```
    conda create -p ./venv python==3.12 -y
    ```
le `p`implique qu'il sera créé dans le dossier de travail


- **Pour l'activer**

    ```
    conda activate ./venv
    ```

- **Si vous souhaitez le supprimer par la suite**
    ```
    rm -rf ./venv
    ```


2. **Initialisation des dépendance avec `poetry`** 

    CONSULTER LA DOC : doc-pipx-poetry.md

    Pour installer les dépendances une fois `poetry` installé sur votre machine
    ```
    poetry install
    ```


 
3. **Configurez les variables d'environnement :**

    Créez un fichier `.env` à la racine du projet avec les clés API nécessaires :
    ```
    GROQ_API_KEY=votre_cle_api
    ```

4. **Lancez le programme :**
    ```bash
    python main.py
    ```



## Revue du code

### Configuration des Agents

Les agents sont définis dans `agents.py` :

```python
import os
from crewai import Agent
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

class AgentsPersonnalisationEmail:
    def __init__(self):
        self.llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model="mixtral-8x7b-32768")

    def agent_personnalisation_email(self):
        return Agent(
            role="Personnaliseur d'Emails",
            goal="Personnaliser les emails modèles pour les destinataires en utilisant leurs informations.",
            backstory="En tant que Personnaliseur d'Emails, vous êtes responsable de la personnalisation des emails modèles.",
            verbose=True,
            llm=self.llm,
            max_iter=2,
        )

    def agent_ghostwriter(self):
        return Agent(
            role="Rédacteur Fantôme",
            goal="Réviser les brouillons d'emails pour adopter le style d'écriture du Rédacteur Fantôme.",
            backstory="En tant que Rédacteur Fantôme, vous êtes responsable de la révision des brouillons d'emails.",
            verbose=True,
            llm=self.llm,
            max_iter=2,
        )
```

### Définition des Tâches

Les tâches sont définies dans `tasks.py` :

```python
from crewai import Task

class TachesPersonnalisationEmail:
    def personnaliser_email(self, agent, destinataire, modele_email):
        return Task(
            description=f"Personnaliser le modèle d'email pour {destinataire['prenom']} {destinataire['nom']}.",
            agent=agent,
            expected_output="Brouillon d'email personnalisé.",
            async_execution=True,
        )

    def rediger_email(self, agent, email_brouillon, destinataire):
        return Task(
            description="Réviser le brouillon d'email pour adopter le style d'écriture du Rédacteur Fantôme.",
            agent=agent,
            context=[email_brouillon],
            expected_output="Brouillon d'email révisé.",
            output_file=f"output/{destinataire['prenom']}_{destinataire['nom']}.txt",
        )
```

### Exécution du Script Principal

Le script principal `main.py` orchestre la création des agents et l'exécution des tâches :

```python
import os
import time
import csv
from crewai import Crew
from langchain_groq import ChatGroq
from agents import AgentsPersonnalisationEmail
from tasks import TachesPersonnalisationEmail

# 0. Configuration de l'environnement
from dotenv import load_dotenv
load_dotenv()

modele_email = """
Bonjour [Nom] !

Juste un petit rappel que nous avons une communauté Skool où vous pouvez nous rejoindre pour des appels de coaching hebdomadaires.
Cordialement, Brandon Hancock
"""

# 1. Création des agents
agents = AgentsPersonnalisationEmail()
agent_personnalisation_email = agents.agent_personnalisation_email()
agent_ghostwriter = agents.agent_ghostwriter()

# 2. Création des tâches
taches = TachesPersonnalisationEmail()
taches_personnalisation_email = []
taches_ghostwriter_email = []

# Chemin vers le fichier CSV contenant les informations des clients
chemin_fichier_csv = 'data/clients_small.csv'

# Ouverture du fichier CSV
with open(chemin_fichier_csv, mode='r', newline='') as fichier:
    lecteur_csv = csv.DictReader(fichier)
    for ligne in lecteur_csv:
        destinataire = {
            'prenom': ligne['first_name'],
            'nom': ligne['last_name'],
            'email': ligne['email'],
            'bio': ligne['bio'],
            'derniere_conversation': ligne['last_conversation']
        }
        tache_personnalisation_email = taches.personnaliser_email(agent=agent_personnalisation_email, destinataire=destinataire, modele_email=modele_email)
        tache_ghostwriter_email = taches.rediger_email(agent=agent_ghostwriter, email_brouillon=tache_personnalisation_email, destinataire=destinataire)
        taches_personnalisation_email.append(tache_personnalisation_email)
        taches_ghostwriter_email.append(tache_ghostwriter_email)

# Configuration de Crew
crew = Crew(agents=[agent_personnalisation_email, agent_ghostwriter], tasks=[*taches_personnalisation_email, *taches_ghostwriter_email], max_rpm=29)

# Lancement de Crew
start_time = time.time()
resultats = crew.kickoff()
end_time = time.time()
temps_ecoule = end_time - start_time

print(f"Le lancement de Crew a pris {temps_ecoule} secondes.")
print("Utilisation de Crew", crew.usage_metrics)
```

### Fichier CSV des Clients

Le fichier `data/clients_small.csv` contient les informations des clients. Voici un exemple de contenu :

```csv
first_name,last_name,email,bio,last_conversation
Jean,Durand,jean.durand@example.com,Bio de Jean,Dernière conversation avec Jean
Marie,Martin,marie.martin@example.com,Bio de Marie,Dernière conversation avec Marie
```

### Exécution du Projet

1. Assurez-vous que le fichier CSV des clients est dans le dossier `data`.
2. Exécutez le script principal :

    ```bash
    python main.py
    ```

Vous verrez les résultats des emails personnalisés et révisés dans la console et dans le dossier `output`.

