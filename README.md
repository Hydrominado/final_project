# Projet Streamlit
**Auteur:**

*Jose Ricardo Silva Leite * ergopt3@gmail.com

## First Step

- Il faut telecharge le dataset sur le doussier data.
- Vois ici le lien: https://drive.google.com/file/d/1sVGKfibWlYU6yDjSYYP4XLfNIB0lBJW2/view

## Démarrage

- Naviguez jusqu'à ce dossier : `cd projet-fil-rouge-{username_github}`
- Vérifiez que vous voyez bien les fichiers de ce dépôt lorsque vous exécutez `ls`.

### MacOS / Linux

- Dans le terminal, exécutez la commande suivante : `bash setup.sh` pour démarrer le projet. Vous n'aurez pas à le faire les prochaines fois.
- Exécutez maintenant, `bash run.sh` pour afficher le site crée à l'aide de Streamlit.

### Windows

Exécutez les commandes suivantes, dans l'ordre :
- Pour installer les librairies utiles et initialiser la base de données :

`pip install --update pip`

`pip install -r requirements.txt`

`python3 setup.py`
- Pour lancer votre application Streamlit :
`streamlit run main.py`
