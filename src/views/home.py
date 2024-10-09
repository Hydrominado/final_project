import streamlit as st
from src.router import redirect
def load_view():

    st.title("Page d'acceuil")
    st.markdown("""
    # Objectif du projet
                
    ## Restaurants européens sur Tripadvisor - Analyse des préférences culinaires par zone géographique.
                
    
    ##### Dans ce projet, les données de Tripadvisor sont analysées pour comprendre les préférences culinaires dans diverses régions géographiques d'Europe. A partir des notes des clients (de « très bien » à « terrible »), un système de notation allant de 0 à 5 a été développé pour différents types de cuisines. Cette méthode de notation permet de mettre en évidence les tendances de popularité et de préférence pour des cuisines spécifiques dans différentes régions, offrant ainsi un aperçu des goûts et des préférences culinaires régionales. Le projet exploite l'analyse des données pour révéler des tendances dans les commentaires des consommateurs à travers l'Europe.

    """)