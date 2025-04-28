# Liste des actions
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

BUDGET_MAX = 500

# Trier les actions par rentabilité : bénéfice par euro investi
objets_tries = sorted(actions, key=lambda x: (x[1] * x[2] / 100) / x[1], reverse=True)

# Initialisations
budget_utilise = 0
benefice_realise = 0
investissements = []

for nom, cout, rendement in objets_tries:
    if budget_utilise + cout <= BUDGET_MAX:
        # On achète l'action
        budget_utilise += cout
        benefice_realise += cout * rendement / 100
        investissements.append(nom)

# Affichage des résultats
print("\nInvestissements réalisés :\n")
for nom in investissements:
    print(f" - {nom}")

print(f"\nBudget utilisé : {budget_utilise} €")
print(f"Bénéfice réalisé : {round(benefice_realise, 2)} €")
print(f"Valeur total : {BUDGET_MAX + benefice_realise} €")