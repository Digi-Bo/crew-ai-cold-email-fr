from crewai import Task

class TachesPersonnalisationEmail:
    """
    Classe pour créer des tâches de personnalisation et de rédaction d'emails.
    """

    def personnaliser_email(self, agent, destinataire, modele_email):
        """
        Crée une tâche pour personnaliser un email à partir d'un modèle et des informations du destinataire.

        :param agent: Agent responsable de la personnalisation.
        :param destinataire: Informations du destinataire.
        :param modele_email: Modèle d'email à personnaliser.
        :return: Tâche de personnalisation d'email.
        """
        return Task(
            description=f"""
                Personnaliser le modèle d'email pour le destinataire en utilisant ses informations.

                - Nom : {destinataire['prenom']} {destinataire['nom']}
                - Email : {destinataire['email']}
                - Bio : {destinataire['bio']}
                - Dernière conversation : {destinataire['derniere_conversation']}

                Informations importantes à considérer :
                - Lors de la personnalisation de l'email, utilisez seulement une phrase de la bio ou de la dernière conversation.
                  Assurez-vous de l'incorporer naturellement dans l'email, sans entrer trop dans les détails.
                - Veillez à ce que l'email personnalisé ait une longueur similaire à celle du modèle d'email.

                Le modèle d'email est le suivant :

                ```
                {modele_email}
                ```
            """,
            agent=agent,
            expected_output="Brouillon d'email personnalisé.",
            async_execution=True,
        )

    def rediger_email(self, agent, email_brouillon, destinataire):
        """
        Crée une tâche pour réviser un brouillon d'email en adoptant le style d'écriture spécifié.

        :param agent: Agent responsable de la révision.
        :param email_brouillon: Brouillon d'email à réviser.
        :param destinataire: Informations du destinataire.
        :return: Tâche de révision d'email.
        """
        return Task(
            description=f"""
                Réviser le brouillon d'email pour adopter le style d'écriture suivant.

                Style d'écriture :
                - Utiliser un ton plus informel, engageant et légèrement orienté vers la vente, en miroir du style de communication final du Ghostwriter.
                - Cette approche privilégie une communication claire et directe tout en maintenant un ton amical et accessible.
                - Utiliser un langage simple, incluant des phrases comme "Salut [Nom] !" pour commencer les emails ou messages.
                - Le ton sera optimiste et encourageant, visant à établir un rapport et motiver à l'action, tout en restant ancré dans des conseils pratiques.

                Notes importantes :
                - Ne pas utiliser d'emojis.
            """,
            agent=agent,
            context=[email_brouillon],
            expected_output="Brouillon d'email révisé dans le ton et le style spécifiés du Ghostwriter.",
            output_file=f"output/{destinataire['prenom']}_{destinataire['nom']}.txt",
        )
