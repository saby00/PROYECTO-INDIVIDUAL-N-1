import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix
from sklearn.preprocessing import StandardScaler

def PlayTimeGenre(genero):

    ufg = pd.read_csv('data/fusionada.csv')
    data_filtrada = ufg[ufg['clasificacion'].str.contains(genero, case=False, na=False)].copy()
    data_filtrada['playtime_hours'] = data_filtrada['playtime_forever'] / 60

    #usuario_max_horas = data_filtrada.groupby('user_id')['playtime_hours'].sum().idxmax()
    año = data_filtrada.groupby('release_date')['playtime_hours'].sum()
    
    año.sort_values(by='release_date', inplace=True, ascending=False)
    #horas_list_formatted = [{"Año": row['release_date'], "Horas": round(row['playtime_hours'], 2)} for index, row in horas_por_año.iterrows()]

    resultado = {
        "Año de lanzamiento con más horas jugadas para Género": genero + " : " + año[0]
    }
    
    return resultado

def UserForGenre(genero):

    ufg = pd.read_csv('data/fusionada.csv')
    data_filtrada = ufg[ufg['clasificacion'].str.contains(genero, case=False, na=False)].copy()
    data_filtrada['playtime_hours'] = data_filtrada['playtime_forever'] / 60

    usuario_max_horas = data_filtrada.groupby('user_id')['playtime_hours'].sum().idxmax()
    horas_por_año = data_filtrada.groupby('release_date')['playtime_hours'].sum().reset_index()
    
    horas_por_año.sort_values(by='release_date', inplace=True)
    horas_list_formatted = [{"Año": row['release_date'], "Horas": round(row['playtime_hours'], 2)} for index, row in horas_por_año.iterrows()]

    resultado = {
        "Usuario con más horas jugadas para Género": genero + " : " + usuario_max_horas,
        "Horas jugadas": horas_list_formatted
    }
    
    return resultado
