import pandas as pd
import matplotlib.pyplot as plt

INPUT_ROOT = "C:\\Users\\sclerc\\github\\INPUT_FILES\\"
OUTPUT_ROOT = "C:\\Users\\sclerc\\github\\OUTPUT_FILES\\"
FILE = "COVID-2020-04-07.csv"

df = pd.read_csv(INPUT_ROOT+FILE,sep=';')                                       # Mise en forme csv


#print(df['Date'].head())                                                       # Affiche les 5 premières lignes de la colonne 'Date'
# print(df.head())                                                              # Affiche les 5 premières lignes


tmp = df["Date"].str.split("/",n = 2, expand = True)                            # Split une str en liste
df["Year"] = tmp[2]                                                             # Ajoute à df principal la colonne tmp[2]
df["Month"] = tmp[1]
df["Day"] = tmp[0]
df.drop(columns = ["Date"], inplace=True)                                       # Supprime une colonne
df['Date'] = pd.to_datetime(df[['Year','Month','Day']], errors = 'coerce')
df.drop(columns = ["Year","Month","Day"], inplace=True)
df.sort_values(by=['Date'], inplace=True, ascending=True)

France_df = df[df['Pays'] == "France"]
France_df = France_df.set_index("Date")
ax = France_df.plot(y=['Deces', 'Infections','Guerisons'], figsize=(10,5), grid=True, kind='line', title="France")

Espagne_df = df[df['Pays'] == "Espagne"]
Espagne_df = Espagne_df.set_index("Date")
Espagne_df.plot(ax = ax, y=['Deces', 'Infections','Guerisons'], figsize=(10,5), grid=True, kind='line', legend=True)


plt.show()

# df_fr_esp = df.loc[df['Pays'].isin(['France','Espagne'])]
# df_fr_esp.plot(y=['Deces', 'Infections','Guerisons'], figsize=(10,5), grid=True)
# plt.show()
