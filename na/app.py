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
                    page_icon="🚀",
                    #layout='wide'
)

    # Edgelist 
#filepath_edgelist = 'congress.edgelist'
#data = nx.read_edgelist(filepath_edgelist, create_using = nx.DiGraph)
#G_pandas = nx.to_pandas_edgelist(data)
#G_pandas['source'] = G_pandas['source'].astype(int)
#G_pandas['target'] = G_pandas['target'].astype(int)

#filepath_username = 'congress_network_data.json'
#username_data = pd.read_json(filepath_username)

    # Username 
#def extract_username_list(record):
#    return record
#username_data['Extracted_Username_List'] = username_data['usernameList'].apply(extract_username_list)
#username_list = username_data['usernameList'][0]
#usernames = pd.DataFrame({'username': username_list})

    # Graph Creation
#G = nx.from_pandas_edgelist(G_pandas,
#                            source='source',
#                            target='target',
#                            edge_attr='weight',
#                            create_using = nx.DiGraph)
#username_attribute = usernames.to_dict()['username']
#nx.set_node_attributes(G, username_attribute, 'username')

    # Centrality
#centrality_dgr = nx.degree_centrality(G)
#dgr = nx.degree(G)
#centrality_eig = nx.eigenvector_centrality_numpy(G, weight = 'weight')
#centrality_between = nx.betweenness_centrality(G)

#dict_dgr = dict(nx.degree(G))
#dict_centrality_dgr = dict(nx.degree_centrality(G))
#dict_centrality_eig = dict(nx.eigenvector_centrality(G))
#dict_centrality_between = dict(nx.betweenness_centrality(G))

#nx.set_node_attributes(G, dict_dgr, 'dgr')
#nx.set_node_attributes(G, dict_centrality_dgr, 'centrality_dgr')
#nx.set_node_attributes(G, dict_centrality_eig, 'centrality_eig')
#nx.set_node_attributes(G, dict_centrality_between, 'centrality_between')

#nodes_df = pd.DataFrame.from_dict(dict(G.nodes(data=True)), orient='index')

# Subset
#top_central_nodes = nodes_df[nodes_df.centrality_eig > nodes_df.centrality_eig.quantile(0.90)].index
#G_sub = nx.subgraph(G, top_central_nodes)

# Undirect
#G_und = nx.to_undirected(G_sub)
#partition = community_louvain.best_partition(G_und)
#nx.set_node_attributes(G_und, partition, 'community')

st.title('M2 EXAM ASSIGMENT')
st.header("Twitter Interaction Network for the US Congress 📊")
#st.sidebar.header("Filters 📊")

# Introduction

st.markdown("""
            For the Network analysis part, we chose the dataset “Twitter Interaction Network for the US Congress”. This social network represents the Twitter interaction network for the 117th United States Congress, both House of Representatives and Senate
""")
"""

"""

# Sidebar filter: centrality_eig
#min_centrality_eig = float(nodes_df['centrality_eig'].min())
#max_centrality_eig = float(nodes_df['centrality_eig'].max())
#centrality_eig_range = st.sidebar.slider("Select Monthly Income Range 💰", min_centrality_eig, max_centrality_eig, (min_centrality_eig, max_centrality_eig))
#filtered_df = nodes_df[(nodes_df['centrality_eig'] >= centrality_eig_range[0]) & (nodes_df['centrality_eig'] <= centrality_eig_range[1])]

# Sidebar filter: dgr
#min_dgr = float(nodes_df['dgr'].min())
#max_dgr = float(nodes_df['dgr'].max())
#drg_range = st.sidebar.slider("Select Monthly Income Range 💰", min_dgr, max_dgr, (min_dgr, max_dgr))
#filtered_df = filtered_df[(filtered_df['dgr'] >= drg_range[0]) & (filtered_df['dgr'] <= drg_range[1])]





# Subset

#top_central_nodes = nodes_df[nodes_df.centrality_eig > nodes_df.centrality_eig.quantile(0.90)].index
#G_sub = nx.subgraph(G, top_central_nodes)

# Undirect
#G_und = nx.to_undirected(G_sub)
#partition = community_louvain.best_partition(G_und)
#nx.set_node_attributes(G_und, partition, 'community')



### Make html file

#net = Network(
#    notebook=True, 
#    #cdn_resources="remote",
#    select_menu=True,
#    filter_menu=True,
#    )

#net.set_options("""
#const options = {
#  "physics": {
#    "minVelocity": 0.75,
#    "solver": "repulsion"
#  }
#}
#"""             
#)

#net.from_nx(G_und)

#net.show('nx.html')

### show the html file

HtmlFile = open("na/nx.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height = 700,width=700)