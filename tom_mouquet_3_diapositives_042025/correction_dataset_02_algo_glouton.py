import pandas as pd
from pathlib import Path

def selection_gloutonne(chemin_fichier, budget=500):
    """
    Sélection gloutonne d'actions pour maximiser le profit sous un budget donné.
    - chemin_fichier : Path ou str vers le CSV contenant 'name', 'price', 'profit' (en %).
    - budget         : budget maximal en euros.

    Retourne une DataFrame des actions sélectionnées.
    """
    # 1) Chargement et filtre des prix valides
    df = pd.read_csv(chemin_fichier)
    df = df[df['price'] > 0].copy()

    # 2) Calcul du profit en euros et du ratio profit/prix
    df['profit_eur'] = df['price'] * df['profit'] / 100.0
    df['ratio'] = df['profit_eur'] / df['price']

    # 3) Tri des actions par ratio décroissant
    df_trie = df.sort_values(by='ratio', ascending=False).reset_index(drop=True)

    # 4) Parcours glouton
    selection = []
    cout_total = 0.0
    for _, action in df_trie.iterrows():
        if cout_total + action['price'] <= budget:
            selection.append(action)
            cout_total += action['price']

    # 5) Construction du résultat
    resultat = pd.DataFrame(selection)[['name', 'price', 'profit', 'profit_eur']]
    print(f"\nBudget utilisé : {cout_total:.2f} € / {budget} €")
    print(f"Profit total   : {resultat['profit_eur'].sum():.2f} €")
    return resultat

if __name__ == "__main__":
    # Construction d'un chemin relatif vers data/dataset2_Python+P7.csv
    chemin_csv = Path(__file__).resolve().parent.parent/'data'/'dataset2_Python+P7.csv'
    df_selection = selection_gloutonne(chemin_csv, budget=500)

    # Affichage du nom de chaque action sélectionnée
    print(f"\nActions sélectionnées ({len(df_selection['name'])}) :\n")
    for nom_action in df_selection['name']:
        print(f"- {nom_action}")