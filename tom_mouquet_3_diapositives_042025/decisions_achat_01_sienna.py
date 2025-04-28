# Liste des actions
actions = [
    ("GRUT", 498.76, 39.42)
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
print(f"Valeur total : {round(BUDGET_MAX + benefice_realise, 2)} €")