# La liste 'actions' contient 20 tuples, chacun représentant une action
actions = [
    ("Action-1", 20, 5),
    ("Action-2", 30, 10),
    ("Action-3", 50, 15),
    ("Action-4", 70, 20),
    ("Action-5", 60, 17),
    ("Action-6", 80, 25),
    ("Action-7", 22, 7),
    ("Action-8", 26, 11),
    ("Action-9", 48, 13),
    ("Action-10", 34, 27),
    ("Action-11", 42, 17),
    ("Action-12", 110, 9),
    ("Action-13", 38, 23),
    ("Action-14", 14, 1),
    ("Action-15", 18, 3),
    ("Action-16", 8, 8),
    ("Action-17", 4, 12),
    ("Action-18", 10, 14),
    ("Action-19", 24, 21),
    ("Action-20", 114, 18),
]

# La somme des coûts des actions choisies ne doit pas dépasser 500 €
BUDGET_MAX = 500

# Initialise le meilleur bénéfice à 0.0
meilleur_benefice = 0.0
# La liste des actions qui compose le meilleur panier (combinaison optimale)
meilleur_panier = []

# n représente le nombre total d'actions, ici 20
n = len(actions)

# Parcours de toutes les combinaisons possibles : de 0 à 2^n -1
for mask in range(1 << n):
    cout_total = 0
    benefice_total = 0
    panier_courant = []

    # Vérification bit par bit
    for j in range(n):
        # Vérifie si j-ième bit de 'mask' est à 1
        if (mask & (1 << j)) != 0:
            action_name, cout, pourcentage = actions[j]
            cout_total += cout
            benefice_total += cout * (pourcentage / 100.0)
            panier_courant.append(action_name)

    # On vérifie si la somme des coûts est <= 500
    if cout_total <= BUDGET_MAX:
        # On compare le bénéfice obtenu au meilleur bénéfice actuel
        if benefice_total > meilleur_benefice:
            meilleur_benefice = benefice_total
            meilleur_panier = panier_courant

print("Meilleur bénéfice = ", meilleur_benefice)
print("Paniers d'actions optimal = ", meilleur_panier)