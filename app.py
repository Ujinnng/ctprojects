import streamlit as st
import pandas as pd
#import plotly.figure_factory as ff
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title = "My Page")

html = '''
<html>
    <head>
        <title>This is HTML App</title>
    </head>
    <body>
        <h1>This is long Text!!!</h1>
        <br></br>
        <hr></hr>
        <h3>This is small text</h3>
    </body>
</html>
'''
with open('./home_html.html', 'r', encoding='UTF-8') as f:
    filehtml = f.read()
    f.close()

url = "https://youtu.be/XyEOEBsa8I4?si=W2quRhkokXlJVCBj"
df = pd.read_csv('data/data.csv')


st.title('This is my first webpage')
col1, col2 = st.columns((4,1))
with col1:
    with st.expander("Content...."):
        st.subheader("Content....")
        st.video(url)
    with st.expander("Content2..."):
        st.subheader("Content2...")
        st.table(df)
    with st.expander("Content3_image..."):
        st.subheader("Content3_image...")
        st.image('images/catdog.jpg')

    with st.expander("Content4_htmlContent..."):
        st.subheader("Content4_htmlContent...")
        import streamlit.components.v1 as htmlviewer
        htmlviewer.html(filehtml, height = 800)

    #st.markdown("<h1>This is new title</h1>", unsafe_allow_html=True)
    #st.markdown(html, unsafe_allow_html=True)
        
with col2:
    with st.expander("Tips...."):
        st.subheader("Tips....")


