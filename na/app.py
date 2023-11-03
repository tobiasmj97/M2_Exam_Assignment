import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import got 
import community.community_louvain as community_louvain

# page config

st.set_page_config(page_title='Streamlit - Network app 🤯',
                    page_icon="🚀"
)

st.title('M2 EXAM ASSIGMENT')
st.header("Twitter Interaction Network for the US Congress 📊")
#st.sidebar.header("Filters 📊")

# Introduction

st.markdown("""
            For the Network analysis part, we chose the dataset “Twitter Interaction Network for the US Congress”. This social network represents the Twitter interaction network for the 117th United States Congress, both House of Representatives and Senate
""")
"""

"""

HtmlFile = open("na/nx.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height = 700,width=700)