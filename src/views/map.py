import streamlit as st
from PIL import Image

def load_view():
# Title of the app
    st.title('Résultat des données obtenues')

# Create a select box for the user to choose from the available languages/nationalities
    option = st.selectbox(
    'Quelle carte souhaiteriez-vous voir ?',
    ('French', 'Spanish', 'Portuguese', 'Japanese', 'Italian','Scandinavian')
)

# Dictionary to map options to the corresponding image file names
    map_files = {
    'French': 'MFrench.png',
    'Spanish': 'MSpanish.png',
    'Portuguese': 'MPortuguese.png',
    'Japanese': 'MJapanese.png',
    'Italian': 'MItalien.png',
    'Scandinavian': 'MScandinavian.png'
}

# Get the corresponding image path based on the selection
    selected_map = map_files[option]

# Load the image using PIL
    image_path = f'IMG/{selected_map}'
    image = Image.open(image_path)

# Display the selected map
    st.image(image, caption=f'{option} Map', use_column_width=True)
