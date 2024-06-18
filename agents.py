import os
from crewai import Agent
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

class AgentsPersonnalisationEmail:
    """
    Classe pour créer des agents de personnalisation d'emails utilisant CrewAI et les modèles Groq ou OpenAI.
    """

    def __init__(self):
        """
        Initialisation de la classe avec le modèle de langage Groq.
        """
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="mixtral-8x7b-32768"
        )

        # Option pour utiliser OpenAI
        # self.llm = ChatOpenAI(
        #     model="gpt-4-turbo-preview",
        # )

    def agent_personnalisation_email(self):
        """
        Crée un agent pour personnaliser des emails à partir d'un modèle et des informations du destinataire.

        :return: Agent configuré pour personnaliser des emails.
        """
        return Agent(
            role="Personnaliseur d'Emails",
            goal="""
                Personnaliser les modèles d'email pour les destinataires en utilisant leurs informations, tout doit être rédigé en français.

                A partir du modèle d'email et des informations du destinataire (nom, email, bio, dernière conversation), 
                personnaliser l'email en incorporant les détails du destinataire tout en conservant le message et la structure de l'email original.
                Cela implique de mettre à jour l'introduction, le corps et la conclusion de l'email pour le rendre plus personnel et engageant pour chaque destinataire.
                """,
            backstory="""
                En tant que Personnaliseur d'Emails, vous êtes responsable de la personnalisation des emails modèles pour chaque destinataire en fonction de leurs informations et interactions précédentes.
                """,
            verbose=True,
            llm=self.llm,
            max_iter=2,
        )

    def agent_ghostwriter(self):
        """
        Crée un agent pour réviser des brouillons d'emails en adoptant le style d'écriture d'un Ghostwriter.

        :return: Agent configuré pour réviser des emails.
        """
        return Agent(
            role="Ghostwriter",
            goal="""
                Réviser les brouillons d'emails pour adopter le style d'écriture du Ghostwriter. Le message doit impérativement être rédigé en français.

                Utiliser un ton informel, engageant et légèrement orienté vers la vente, en miroir du style de communication final du Ghostwriter.
                """,
            backstory="""
                En tant que Ghostwriter, vous êtes responsable de la révision des brouillons d'emails pour correspondre au style d'écriture du Ghostwriter, en vous concentrant sur une communication claire et directe avec un ton amical et accessible.
                """,
            verbose=True,
            llm=self.llm,
            max_iter=2,
        )
