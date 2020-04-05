import plotly.express as px
import plotly.graph_objs as go
import streamlit as st
import numpy as np


# Die mit der die streamlit commands eingegeben werden, ist auch die, mit welcher sie online erscheinen
st.title("Einfache 3D Plots")

st.write("Diese Seite zeigt, wie einfach es ist interaktive Plots mit Streamlit zu erstellen.")

x = np.linspace(-10, 10, 10)
y = np.linspace(-10, 10, 10)
X, Y = np.meshgrid(x, y)

a = st.slider(label="Erster Exponent", min_value=-5., max_value=5., value=2., step=0.1)
b = st.slider(label="Zweiter Exponent", min_value=-5., max_value=5., value=2., step=0.1)

Z = X**a + Y**b

st.latex(f"z = f(x, y) = x**{a:.1f} + y**{b:.1f}")

fig = go.Figure(data=go.Surface({"x": X, "y":Y, "z":Z}))
st.write(fig)