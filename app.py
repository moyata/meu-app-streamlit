import streamlit as st

# Título do app
st.title("Meu Primeiro App com Streamlit 🚀")

# Texto simples
st.write("Olá, bem-vindo ao meu primeiro aplicativo!")

# Entrada de texto
nome = st.text_input("Digite seu nome:")

# Botão de ação
if st.button("Enviar"):
    st.write(f"Olá, {nome}! 👋")

# Exibir um gráfico simples com Matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)
