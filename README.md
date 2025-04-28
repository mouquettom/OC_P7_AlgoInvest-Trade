# OC_P7_AlgoInvest&Trade

## Optimisez vos investissements avec AlgoInvest&Trade !

Dans le cadre du Projet 7 de la formation Développeur Python OpenClassrooms, nous avons 
développé deux algorithmes puissants pour booster la rentabilité de portefeuilles financiers, 
tout en respectant des contraintes strictes :


    • Budget maximal : 500 €

    • Pas de fractions d’actions

    • Une seule acquisition par action


## Bruteforce
Explore toutes les combinaisons possibles pour trouver le portefeuille parfait. Ultra-précis, 
mais réservé aux petits datasets (20 actions maximum) sous peine d’exploser votre processeur !

## Optimisé
Une approche gloutonne inspirée du problème du sac à dos : trie les actions les plus rentables 
et construit le portefeuille idéal sans dépasser le budget.

## Rapport d'exploration
Après avoir vérifié l'exactitude des calculs de Sienna, il a été constaté que sa solution n'était 
pas optimale. Un nouvel algorithme basé sur une approche gloutonne a été développé, permettant 
d'obtenir une solution plus rentable dans un temps de calcul réduit, bien que sans garantir 
l'optimalité globale.

## Prérequis

- **Python 3** installé sur votre machine.
- Connexion Internet

## Installation et Lancement

1. **Cloner le dépôt du projet :**

    Lancez la console, placez-vous dans le dossier de votre choix et clonez le dépôt :
    ```
    • git clone https://github.com/mouquettom/OpenClassrooms_P6_JustStreamIt.git
    ```

3. **Installer les packages :**

    ```
    • pip install -r requirements.txt
    ```
   
3. **Lancer les fichiers suivants :**

    ```
    • bruteforce.py
   
    • optimized.py
   
    • correction_dataset_01_algo_glouton.py
   
    • correction_dataset_02_algo_glouton.py
    ```