# La POO en Python, une exemple concrêt avec un projet CrewAI

La Programmation Orientée Objet (POO) est un paradigme de programmation qui utilise des "objets" pour représenter des données et des méthodes. Ce cours utilisera des exemples de personnalisation d'emails pour illustrer les concepts clés de la POO en Python.

#### Table des Matières

1. Introduction à la POO
2. Classes et Objets
3. Constructeurs
4. Attributs et Méthodes
5. Héritage
6. Polymorphisme
7. Encapsulation
8. Exemple Pratique avec CrewAI

---

## 1. Introduction à la POO

La POO permet de structurer un programme en regroupant les données et les comportements associés dans des entités appelées objets. Chaque objet est une instance d'une classe.

## 2. Classes et Objets

Une **classe** est un modèle définissant la structure des objets. Un **objet** est une instance d'une classe.

### Exemple

Nous allons définir une classe `Email` pour représenter un email.

```python
class Email:
    pass

# Création d'un objet de la classe Email
email = Email()
print(type(email))  # <class '__main__.Email'>
```

## 3. Constructeurs

Le constructeur est une méthode spéciale appelée `__init__` qui est exécutée lorsque l'objet est instancié. Il permet d'initialiser les attributs de l'objet.

### Exemple

Ajoutons un constructeur à la classe `Email` pour initialiser les attributs `destinataire` et `contenu`.

```python
class Email:
    def __init__(self, destinataire, contenu):
        self.destinataire = destinataire
        self.contenu = contenu

# Création d'un objet de la classe Email avec des attributs
email = Email("Jean Dupont", "Bonjour Jean, voici votre email personnalisé.")
print(email.destinataire)  # Jean Dupont
print(email.contenu)       # Bonjour Jean, voici votre email personnalisé.
```

## 4. Attributs et Méthodes

Les **attributs** sont des variables qui appartiennent à une classe. Les **méthodes** sont des fonctions qui appartiennent à une classe.

### Exemple

Ajoutons une méthode pour afficher le contenu de l'email.

```python
class Email:
    def __init__(self, destinataire, contenu):
        self.destinataire = destinataire
        self.contenu = contenu

    def afficher(self):
        print(f"Email à : {self.destinataire}\nContenu : {self.contenu}")

# Utilisation de la méthode afficher
email = Email("Jean Dupont", "Bonjour Jean, voici votre email personnalisé.")
email.afficher()
```




### Explications : `self`

Le mot-clé `self` en Python fait référence à l'instance actuelle de la classe. Il est utilisé pour accéder aux attributs et méthodes de la classe dans son propre corps. Lorsque vous définissez des méthodes dans une classe, le premier paramètre de chaque méthode doit être `self`. Cela permet à chaque instance de la classe de faire référence à ses propres attributs et méthodes.

1. **Initialisation des Attributs :**

   ```python
   def __init__(self, destinataire, contenu):
       self.destinataire = destinataire
       self.contenu = contenu
   ```

   Ici, `self.destinataire` et `self.contenu` sont des attributs de l'instance, initialisés avec les valeurs fournies en argument lors de la création de l'instance.

2. **Accès aux Attributs :**

   ```python
   def afficher(self):
       print(f"Email à : {self.destinataire}\nContenu : {self.contenu}")
   ```

   Dans cette méthode, `self.destinataire` et `self.contenu` sont utilisés pour accéder aux attributs de l'instance actuelle de la classe.


#### En résumé
1. **Accéder aux attributs de l'instance :** Vous utilisez `self` pour accéder et modifier les attributs de l'instance de la classe.
2. **Accéder aux méthodes de l'instance :** Vous utilisez `self` pour appeler d'autres méthodes de la même instance.
3. **Différencier les instances :** `self` aide à différencier les attributs et les méthodes de différentes instances de la même classe.




## 5. Héritage

L'**héritage** permet de créer une nouvelle classe basée sur une classe existante. La nouvelle classe hérite des attributs et des méthodes de la classe parent.


Créons une classe `EmailPersonnalise` qui hérite de la classe `Email`.

```python
class Email:
    def __init__(self, destinataire, contenu):
        self.destinataire = destinataire
        self.contenu = contenu

    def afficher(self):
        print(f"Email à : {self.destinataire}\nContenu : {self.contenu}")

class EmailPersonnalise(Email):
    def __init__(self, destinataire, contenu, bio):
        super().__init__(destinataire, contenu)
        self.bio = bio

    def afficher(self):
        super().afficher()
        print(f"Bio : {self.bio}")

# Création et affichage d'un email personnalisé
email_perso = EmailPersonnalise("Jean Dupont", "Bonjour Jean, voici votre email personnalisé.", "Bio de Jean")
email_perso.afficher()

```


### Explications :`super()`

La fonction `super()` en Python est utilisée pour appeler une méthode d'une classe parente (ou superclasse). Cela est particulièrement utile dans le contexte de l'héritage, où une classe enfant hérite des attributs et des méthodes d'une classe parente. `super()` permet d'accéder à ces méthodes de manière explicite, facilitant ainsi l'extension et la personnalisation des comportements hérités.


1. **Appel au Constructeur de la Classe Parente :**

   ```python
   def __init__(self, destinataire, contenu, bio):
       super().__init__(destinataire, contenu)
       self.bio = bio
   ```

   - `super().__init__(destinataire, contenu)` appelle le constructeur de la classe parente `Email`. Cela initialise les attributs `destinataire` et `contenu` pour l'instance de la classe enfant `EmailPersonnalise`.
   - Ensuite, l'attribut `bio` est initialisé spécifiquement pour `EmailPersonnalise`.

2. **Appel à la Méthode de la Classe Parente :**

   ```python
   def afficher(self):
       super().afficher()
       print(f"Bio : {self.bio}")
   ```

   - `super().afficher()` appelle la méthode `afficher` de la classe parente `Email`. Cela affiche les attributs `destinataire` et `contenu`.
   - Ensuite, la méthode `afficher` de `EmailPersonnalise` ajoute l'affichage de l'attribut `bio`.

### Pourquoi Utiliser `super()` ?

- **Réutilisation du Code :** `super()` permet de réutiliser le code de la classe parente, ce qui évite la duplication et rend le code plus maintenable.
- **Extensibilité :** Il facilite l'extension des fonctionnalités des classes parentes sans modifier directement leur code.
- **Gestion de l'Héritage Multiple :** Dans les cas d'héritage multiple, `super()` assure que les constructeurs des classes parentes sont appelés correctement, suivant l'ordre de la méthode de résolution des mro (méthode de résolution d'ordre).

En résumé, `super()` est un outil puissant en POO qui permet d'appeler des méthodes de la classe parente, facilitant ainsi la réutilisation et l'extension des fonctionnalités dans les classes dérivées.








## 6. Polymorphisme

Le **polymorphisme** permet d'utiliser une méthode de la même manière pour des objets de classes différentes.

### Exemple

Utilisation de la méthode `afficher` pour des objets des classes `Email` et `EmailPersonnalise`.

```python
email = Email("Jean Dupont", "Bonjour Jean, voici votre email personnalisé.")
email_perso = EmailPersonnalise("Jean Dupont", "Bonjour Jean, voici votre email personnalisé.", "Bio de Jean")

def afficher_email(email_obj):
    email_obj.afficher()

afficher_email(email)
afficher_email(email_perso)
```

## 7. Encapsulation

L'**encapsulation** protège les données en les rendant privées et accessibles uniquement via des méthodes spéciales.

### Exemple

Utilisation des attributs privés et des méthodes getter/setter.

```python
class Email:
    def __init__(self, destinataire, contenu):
        self.__destinataire = destinataire  # Attribut privé
        self.__contenu = contenu  # Attribut privé

    def get_destinataire(self):
        return self.__destinataire

    def set_destinataire(self, destinataire):
        self.__destinataire = destinataire

    def get_contenu(self):
        return self.__contenu

    def set_contenu(self, contenu):
        self.__contenu = contenu

# Utilisation des getter et setter
email = Email("Jean Dupont", "Bonjour Jean, voici votre email personnalisé.")
print(email.get_destinataire())  # Jean Dupont
email.set_destinataire("Marie Martin")
print(email.get_destinataire())  # Marie Martin
```

## 8. Exemple Pratique avec CrewAI

### Classes et Objets

Dans ce projet, nous avons plusieurs classes pour organiser notre code. Voici la classe `EmailPersonalisationAgents` pour gérer les agents de personnalisation d'emails :

```python
import os
from crewai import Agent
from langchain_groq import ChatGroq

class EmailPersonalisationAgents:
    def __init__(self):
        self.llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model="mixtral-8x7b-32768")
```

### Constructeurs

Le constructeur `__init__` initialise l'agent avec un modèle de langage :

```python
class EmailPersonalisationAgents:
    def __init__(self):
        self.llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model="mixtral-8x7b-32768")
```

### Attributs et Méthodes

La classe a des méthodes pour créer des agents de personnalisation d'emails :

```python
    def personalise_email_agent(self):
        return Agent(
            role="Personnaliseur d'Emails",
            goal="Personnaliser les emails modèles pour les destinataires en utilisant leurs informations.",
            verbose=True,
            llm=self.llm,
            max_iter=2,
        )
```

### Héritage

Nous pourrions créer une sous-classe spécialisée pour des agents différents :

```python
class GhostwriterAgent(Agent):
    def __init__(self, llm):
        super().__init__(role="Rédacteur Fantôme", goal="Réviser les brouillons d'emails.", verbose=True, llm=llm, max_iter=2)
```

### Polymorphisme

Les méthodes `personalize_email` et `ghostwrite_email` de la classe `PersonalizeEmailTask` utilisent des agents de manière polymorphe :

```python
class PersonalizeEmailTask:
    def personalize_email(self, agent, recipient, email_template):
        return Task(description=f"Personnaliser l'email pour {recipient['prenom']} {recipient['nom']}.", agent=agent)

    def ghostwrite_email(self, agent, draft_email, recipient):
        return Task(description="Réviser l'email brouillon.", agent=agent)
```

### Encapsulation

Les informations du destinataire sont encapsulées dans des attributs privés et accessibles via des méthodes :

```python
class Recipient:
    def __init__(self, first_name, last_name, email):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"
```
