import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data= pd.DataFrame(np.random.randn(100,2),columns=['A','B'])

st.header("App Anne")
st.write(data.head(10))
st.header("Grafico 1")
fig, ax=plt.subplots()
ax.scatter(data['A'],data['B'])
st.pyplot(fig)
bar=st.progress(0)
bar.progress(100)


#barra lateral
st.sidebar.header("Progress")
bar=st.sidebar.slider(
    label=("Barra"),
    min_value=0,
    max_value=100)


if bar < 50:
    st.sidebar.error("Suspenso")
    #st.sidebar.warning()
else:
    st.sidebar.success("Aprobado")  
    #st.sidebar.success()  

st.selectbox("Selecciona una letra", ["A","B","C"])
