import pandas as pd

times = pd.read_csv('Clubes.csv')

media_de_pontos = times['Pontos'].mean()
# print(f"A média de colocações é: {media_de_pontos: .2f}")

formato = times.describe()
print(formato)