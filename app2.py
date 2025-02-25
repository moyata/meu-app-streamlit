import streamlit as st
import pandas as pd

# Título do app
st.title("Leitor de Planilhas Excel 📊")

# Upload do arquivo Excel
arquivo = st.file_uploader("Envie um arquivo Excel", type=["xlsx", "xls"])

# Se um arquivo for enviado
if arquivo:
    df = pd.read_excel(arquivo)  # Lê a planilha como DataFrame
    st.write("📄 **Visualização dos dados:**")
    st.dataframe(df)  # Exibe os dados como tabela interativa

