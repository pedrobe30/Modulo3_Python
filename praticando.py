import pandas as pd

times = pd.read_excel('premier_top8.xlsx')

media_de_pontos = times['Pts'].mean()
print(f"A média de pontos é: {media_de_pontos: .2f}")