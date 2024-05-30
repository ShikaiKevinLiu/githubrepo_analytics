import streamlit as st
import streamlit.components.v1 as components

from ipysigma import Sigma
import networkx as nx

# Create an empty graph
G = nx.Graph()

# Add nodes "foo" and "bar"
G.add_node("foo")
G.add_node("bar")

# Add an edge between nodes "foo" and "bar"
G.add_edge("foo", "bar")

# Write the Sigma graph
Sigma.write_html(graph=G,
            background_color="white",
            path="./foobar_gr.html",
            fullscreen=True 
            )

st.markdown(
    """
    # Graph
    """
)

with open("foobar_gr.html", "r") as f: 
    html_data = f.read()

components.html(html_data, height=1000, width=1000)