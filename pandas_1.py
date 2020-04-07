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

#-----------------------------------------------------------------------------#
# France_df = df[df['Pays'] == "France"]
# France_df = France_df.set_index("Date")
# ax = France_df.plot(y=['Deces', 'Infections','Guerisons'], figsize=(10,5), grid=True, kind='line', title="France")
#
# Espagne_df = df[df['Pays'] == "Espagne"]
# Espagne_df = Espagne_df.set_index("Date")
# Espagne_df.plot(ax = ax, y=['Deces', 'Infections','Guerisons'], figsize=(10,5), grid=True, kind='line', legend=True)

#-----------------------------------------------------------------------------#
data = "Infections"
crietere = 100000
title = data + " > " + str(crietere)
df_selec = df.loc[df[data] > crietere]
countries = set(df_selec["Pays"].values.tolist())


# print(set(df["Pays"].values.tolist())) #Affichie les valuers unique d'une colonne
# countries = ["France", "Espagne", "Italie"]


graph_df = pd.DataFrame()

for country in countries:
    pays_df = df.copy()[df["Pays"]==country]
    pays_df.set_index('Date', inplace=True)
    pays_df[f"{country}"] = pays_df[data]

    if graph_df.empty:
        graph_df = pays_df[[f"{country}"]]
    else:
        graph_df = graph_df.join(pays_df[f"{country}"])

# graph_df.plot(y=countries, figsize=(10,5), grid=True, kind='line', title=title)
graph_df.plot(y=countries, figsize=(10,5), grid=True, kind='area', title=title)
plt.show()
#-----------------------------------------------------------------------------#
# data = "Deces"
# crietere = 1000
# title = data + " > " + str(crietere)
# df_selec = df.loc[df[data] > crietere]
# countries = set(df_selec["Pays"].values.tolist())
#
# graph_df = pd.DataFrame()
#
# for country in countries:
#     pays_df = df.copy()[df["Pays"]==country]
#     pays_df.set_index('Date', inplace=True)
#     pays_df[f"{country}"] = pays_df[data]
#
#     if graph_df.empty:
#         graph_df = pays_df[[f"{country}"]]
#     else:
#         graph_df = graph_df.join(pays_df[f"{country}"])
#
# graph_df = graph_df.fillna(0)
# graph_df.loc[:,'Total'] = graph_df.sum(axis=1) #Total sum per row:
#
# for col in graph_df.columns:
#     graph_df[f"{col}_"] = graph_df[col]/graph_df["Total"]
# for country in countries:
#     graph_df.drop(columns = country, inplace=True)
# graph_df.drop(columns = ["Total",'Total_'], inplace=True)
# graph_df = graph_df.fillna(0)
#
# graph_df.plot(figsize=(10,5), grid=True, kind='area', title=title)
#
# plt.show()
