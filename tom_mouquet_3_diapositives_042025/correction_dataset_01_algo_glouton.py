import pandas as pd
from pathlib import Path

def selection_gloutonne(chemin_fichier, budget=500):
    """
    Sélection gloutonne d'actions pour maximiser le profit sous un budget donné.
    - chemin_fichier : chemin vers le fichier CSV contenant les colonnes 'name', 'price', 'profit' (pourcentage).
    - budget         : budget maximal en euros.

    Retourne une DataFrame des actions sélectionnées.
    """
    # Chargement des données
    donnees = pd.read_csv(chemin_fichier)

    # Calcul du profit en euros et du ratio profit/prix
    donnees['profit_eur'] = donnees['price'] * donnees['profit'] / 100.0
    donnees['ratio'] = donnees['profit_eur'] / donnees['price']

    # Tri par ratio décroissant
    donnees_triees = donnees.sort_values(by='ratio', ascending=False).reset_index(drop=True)

    selection = []
    cout_total = 0.0

    # Parcours glouton
    for _, action in donnees_triees.iterrows():
        if cout_total + action['price'] <= budget:
            selection.append(action)
            cout_total += action['price']

    # Résultat
    resultat = pd.DataFrame(selection)[['name', 'price', 'profit', 'profit_eur']]
    print(f"\nBudget utilisé : {cout_total:.2f} € / {budget} €")
    print(f"Profit total   : {resultat['profit_eur'].sum():.2f} €")

    return resultat

if __name__ == "__main__":
    # Exemple d'utilisation
    chemin_csv = Path(__file__).resolve().parent.parent/'data'/'dataset1_Python+P7.csv'
    df_selection = selection_gloutonne(chemin_csv, budget=500)

    # Affichage du nom de chaque action sélectionnée
    print(f"\nActions sélectionnées ({len(df_selection)}) :\n")
    for nom_action in df_selection['name']:
        print(f"- {nom_action}")