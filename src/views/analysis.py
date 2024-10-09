import streamlit as st


def load_view():
    st.title('Analysis de données')


# Analyse de la popularité des cuisines
    st.markdown('''
### Analyse de la Popularité des Cuisines:
L'analyse des scores montre que la **cuisine italienne** est largement appréciée à travers l'Europe, en particulier en Europe occidentale. La simplicité et la saveur des plats comme les pâtes et les pizzas contribuent à cette popularité. De même, la **cuisine française**, réputée pour ses pâtisseries et ses plats gastronomiques, obtient des scores élevés, notamment dans les régions proches de la France.

**Autres résultats possibles** :
- Les **tapas espagnols** obtiennent de bons scores dans le sud de l'Europe.
- Des notes plus faibles pour les cuisines rapides ou moins traditionnelles dans certaines zones.
''')

# Analyse de l'influence culturelle
    st.markdown('''
### Analyse de l'Influence Culturelle:
Les **cuisines méditerranéennes** (comme grecque ou italienne) obtiennent des scores élevés dans les pays du sud de l'Europe tels que l'Espagne, l'Italie et la Grèce, reflétant des préférences locales fortes. En revanche, la **cuisine nordique** pourrait être plus populaire en Europe du Nord (Scandinavie), avec des plats comme le poisson fumé et les légumes marinés, alignés avec les traditions locales.

Les **cuisines internationales** comme la **cuisine japonaise** ou **indienne** pourraient obtenir de meilleurs scores dans des villes cosmopolites comme Londres ou Berlin, où les convives sont plus ouverts à des expériences culinaires diversifiées et globales.
''')


