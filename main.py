import streamlit as st
import utils as utl

from src.views import home, map, analysis, login, logout
from src.router import get_route, redirect


import json



st.set_page_config(layout="wide", page_title='Navbar sample')
# st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

def navigation():  

    #Loading Cookies
    with open('session.json') as json_file:
        SESSION = json.load(json_file)
    
    #Non user in cookies 
    if SESSION["email"] == "":
        redirect("login")
    
    route = get_route()

    if route == "/home":
        home.load_view()
    elif route == "/analysis":
        analysis.load_view()
    elif route == "/map":
        map.load_view()
    elif route == "/logout":
        logout.load_view()
    elif route == "/login":
        login.load_view()

    #else:
        #redirect("/home")
        #home.load_view()

navigation()

