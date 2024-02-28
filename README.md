# Suivi d'une activité avec Pixela API

## Présentation
Ce projet vise à suivre le temps de méditation quotidien à l'aide de l'API Pixela. Il permet à l'utilisateur d'enregistrer, de mettre à jour et de supprimer les données de méditation sur un graphique hébergé sur Pixela. L'application est réalisée en utilisant des requêtes HTTP avec la bibliothèque Requests de Python.

## Utilisation de l'API Pixela
Pixela est un service qui permet de créer et de gérer des graphiques personnalisés pour suivre diverses activités. Voici comment fonctionne l'utilisation de l'API Pixela dans ce projet :

### Création d'un Compte Pixela
Avant de pouvoir utiliser l'API Pixela, vous devez créer un compte Pixela. Une fois le compte créé, vous obtiendrez un jeton d'authentification et un nom d'utilisateur.

### Création d'un Graphique
Après avoir créé un compte, vous pouvez créer un graphique sur Pixela. Un graphique est une représentation visuelle des données que vous souhaitez suivre. Dans ce projet, un graphique est créé pour enregistrer le temps de méditation quotidien.

### Ajout de Pixels au Graphique
Les pixels sont des points de données individuels sur le graphique. Dans ce projet, vous pouvez ajouter des pixels pour enregistrer le temps de méditation quotidien.

### Mise à Jour et Suppression de Pixels
Vous pouvez également mettre à jour ou supprimer des pixels existants sur le graphique.

## Exécution du Programme, installation et configuration
Pour exécuter le programme :
- Assurez-vous que Python est installé sur votre système.
- Installez la bibliothèque Requests si elle n'est pas déjà installée : pip install requests.
- Configurez les variables d'environnement PIXELA_API_TOKEN et PIXELA_API_USERNAME avec votre jeton d'authentification et votre nom d'utilisateur Pixela.
- Exécutez le fichier main.py.L'application vous guidera pour ajouter, mettre à jour ou supprimer des pixels sur votre graphique de méditation.

## [Visualisation du graphique sur pixela](https://pixe.la/v1/users/marionroro/graphs/graph1.html)
![image](https://github.com/marionrobert/HabitsTracker/assets/107509668/ce434b2c-c1fa-4057-93ce-d55b82749623)

## Remarque
Ce projet a été réalisé dans le cadre du cours [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) de Angela Yu sur la plateforme Udemy.


