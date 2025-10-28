import pandas as pd

dados_pilotos = {
    'Pilotos': ['Oscar Piastri','Lando Norris', 'Max Verstappen', 'George Russell', 'Charles Leclerc', 'Lewis Hamilton', 'Kimi Antonelli', 'Fernando Alonso', 'Gabriel Bortoleto', 'Franco Colapinto'],
    'Idade': [24, 25, 28, 27, 28, 40, 19, 44, 21, 22],
    'Pontos': [346, 332, 306, 252, 192, 142, 89, 37, 18, 0],
    'Equipe': ['McLaren', 'McLaren', 'Red Bull', 'Mercedes', 'Ferrari', 'Ferrari', 'Mercedes', 'Aston Martin', 'Sauber', 'Alpine'] 
}

df_pilotos = pd.DataFrame(dados_pilotos)

media = df_pilotos['Pontos'].mean()

print("---- Dataframe de Alunos ----")
print(df_pilotos)
print(f"A media de pontos dos pilostos é de: {media}")

format = df_pilotos.describe()
print(format)