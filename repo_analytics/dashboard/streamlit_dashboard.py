import streamlit as st
import plotly.express as px
import pandas as pd
import streamlit.components.v1 as components
import random


df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 30, 40, 50]
})


fig = px.line(df, x='x', y='y', title='Example Line Chart')


url_2020 = "https://static-webpage-sliu.s3.amazonaws.com/dataset_2020.html"
url_2021 = "https://static-webpage-sliu.s3.amazonaws.com/dataset_2021.html"
url_2022 = "https://static-webpage-sliu.s3.amazonaws.com/dataset_2022.html"
url_2023 = "https://static-webpage-sliu.s3.amazonaws.com/dataset_2023.html"


# this first tab is a place holder, it will show some plots such as the most popular topics in each year
st.title("this first tab is a place holder, it will show some plots such as the most popular topics in each year")
tab1, tab2 = st.tabs(["Plots", "Network HTML Pages"])

with tab1:
    st.header("Line Chart")
    st.plotly_chart(fig)  

with tab2:
    st.header("HTML Pages")

    selected_html = st.radio("Select HTML Page", ["2020", "2021", "2022", "2023"], horizontal=True)

    if selected_html == "2020":
        components.iframe(f"{url_2020}?r={random.randint(0, 100000)}", height=900,width=900, scrolling=True)
    elif selected_html == "2021":
        components.iframe(f"{url_2021}?r={random.randint(0, 100000)}", height=600, width=900, scrolling=True)
    elif selected_html == "2022":
        components.iframe(f"{url_2022}?r={random.randint(0, 100000)}", height=600,width=900, scrolling=True)
    elif selected_html == "2023":
        components.iframe(f"{url_2023}?r={random.randint(0, 100000)}", height=600,width=900, scrolling=True)
