import pandas as pd
import random

INPUT_ROOT = "C:\\Users\\sclerc\\github\\INPUT_FILES\\"
OUTPUT_ROOT = "C:\\Users\\sclerc\\github\\OUTPUT_FILES\\"
FILE = "nat2018.csv"

df = pd.read_csv(INPUT_ROOT+FILE,sep=';')                                       # Mise en forme csv

columns_name = df.columns.to_list()                                             # Liste les titres des colonnes

df.rename(columns={'preusuel':'prenom',
                   'annais':'annee'}, inplace=True)                             # Modifier les titres des colonnes

def convert_to_str(number):
    if number == 1:
        return "M"
    else:
        return "F"
df['sexe'] = df['sexe'].apply(convert_to_str)                                   # Modifier la valeur d'une colonne par fonction


df_M = df[df['sexe'] == "M"]                                                    # selection des valeurs selon un critère
df_F = df[df['sexe'] == "F"]

df_M = df_M.groupby(['prenom']).sum()                                           # Groupe et somme les occurances des valeurs de la colonne prenom
df_M.sort_values(by=['nombre'], inplace=True, ascending=True)                   # Tri par ordre croissant
df_M['Pourcentage'] = df_M['nombre']/df_M['nombre'].sum()*100                   # Ajoute le % des valeurs d'une colonnes

df_F = df_F.groupby(['prenom']).sum()
df_F.sort_values(by=['nombre'], inplace=True, ascending=True)
df_F['Pourcentage'] = df_F['nombre']/df_F['nombre'].sum()*100

#df_M.loc['SYLVAIN']                                                             # Affiche la ligne d'index 'SYLVAIN'

lim_min = 1000
lim_max = 20000
df_selec_M = df_M.loc[(df_M['nombre'] > lim_min) & (df_M['nombre'] < lim_max)]
df_selec_F = df_F.loc[(df_F['nombre'] > lim_min) & (df_F['nombre'] < lim_max)]
prenom_M = random.sample(set(df_selec_M.index.tolist()),10)
prenom_F = random.sample(set(df_selec_F.index.tolist()),10)

print(prenom_M)
print(prenom_F)
