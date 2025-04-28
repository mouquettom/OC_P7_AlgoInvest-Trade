# Liste des actions
actions = [
    ("ECAQ", 31.66, 39.49),
    ("IXCI", 26.32, 39.40),
    ("FWBE", 18.31, 39.82),
    ("ZOFA", 25.32, 39.78),
    ("PLLK", 19.94, 39.91),
    ("YFVZ", 22.55, 39.1),
    ("ANFX", 38.54, 39.72),
    ("PATS", 27.7, 39.97),
    ("NDKR", 33.06, 39.91),
    ("ALIY", 29.08, 39.93),
    ("JWGF", 48.69, 39.93),
    ("JGTW", 35.29, 39.43),
    ("FAPS", 32.57, 39.54),
    ("VCAX", 27.42, 38.99),
    ("LFXB", 14.83, 39.79),
    ("DWSK", 29.49, 39.65),
    ("XQII", 13.42, 39.51),
    ("ROOM", 15.06, 39.23)
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

print(f"\nBudget utilisé : {round(budget_utilise, 2)} €")
print(f"Bénéfice réalisé : {round(benefice_realise, 2)} €")
print(f"Valeur total : {round(BUDGET_MAX + benefice_realise, 2)} €")