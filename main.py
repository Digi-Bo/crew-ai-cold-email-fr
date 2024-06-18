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

# Modèle d'email en français
modele_email = """
Bonjour [Nom] !

Juste un petit rappel que nous avons une communauté Skool où vous pouvez nous rejoindre 
pour des appels de coaching hebdomadaires chaque mardi à 18h, heure de l'Est. 
La communauté est complètement gratuite et nous sommes sur le point d'atteindre le cap des 500 utilisateurs. 
Nous serions ravis de vous y accueillir !

Si vous avez des questions ou besoin d'aide pour vos projets, 
c'est un excellent endroit pour vous connecter avec d'autres et obtenir du soutien.

Si vous appréciez le contenu lié à l'IA, assurez-vous de consulter 
d'autres vidéos sur ma chaîne. N'oubliez pas de cliquer sur le bouton 
J'aime et de vous abonner pour rester informé des dernières nouveautés. 
Au plaisir de vous voir dans la communauté !

Cordialement,
Brandon Hancock
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
    # Création d'un objet lecteur CSV
    lecteur_csv = csv.DictReader(fichier)

    # Itération sur chaque ligne du fichier CSV
    for ligne in lecteur_csv:
        # Accès à chaque champ de la ligne
        destinataire = {
            'prenom': ligne['first_name'],
            'nom': ligne['last_name'],
            'email': ligne['email'],
            'bio': ligne['bio'],
            'derniere_conversation': ligne['last_conversation']
        }

        # Création d'une tâche de personnalisation d'email pour chaque destinataire
        tache_personnalisation_email = taches.personnaliser_email(
            agent=agent_personnalisation_email,
            destinataire=destinataire,
            modele_email=modele_email
        )

        # Création d'une tâche de rédaction fantôme pour chaque destinataire
        tache_ghostwriter_email = taches.rediger_email(
            agent=agent_ghostwriter,
            email_brouillon=tache_personnalisation_email,
            destinataire=destinataire
        )

        # Ajout de la tâche à la liste
        taches_personnalisation_email.append(tache_personnalisation_email)
        taches_ghostwriter_email.append(tache_ghostwriter_email)


# Configuration de Crew
crew = Crew(
    agents=[
        agent_personnalisation_email,
        agent_ghostwriter
    ],
    tasks=[
        *taches_personnalisation_email,
        *taches_ghostwriter_email
    ],
    max_rpm=29
)

# Lancement de Crew
start_time = time.time()

resultats = crew.kickoff()

end_time = time.time()
temps_ecoule = end_time - start_time

print(f"Le lancement de Crew a pris {temps_ecoule} secondes.")
print("Utilisation de Crew", crew.usage_metrics)
