import streamlit as st
import pandas as pd

# Título do app
st.title("Pesquisa de Livros por ISBN")

# Carregar o arquivo Excel
arquivo = st.file_uploader("Envie o arquivo de livros", type=["xlsx", "xls"])

if arquivo:
    # Lê a planilha na aba GERAL e força a coluna ISBN a ser tratada como string
    df = pd.read_excel(arquivo, sheet_name="GERAL", dtype={"ISBN": str})

    # Exibe as primeiras linhas da tabela (opcional)
    st.write("**Dados carregados da planilha (aba GERAL):**")
    st.dataframe(df.head())

    # Entrada do usuário para pesquisar o ISBN
    isbn_pesquisa = st.text_input("Digite o ISBN para pesquisa:")

    # Verifica se o usuário digitou algo
    if isbn_pesquisa:
        # Filtra a coluna ISBN e encontra o livro correspondente
        resultado = df[df['ISBN'] == isbn_pesquisa]

        # Verifica se o ISBN foi encontrado
        if not resultado.empty:
            st.write("**Livro encontrado:**")
            st.dataframe(resultado)  # Exibe o livro encontrado
        else:
            st.write("Nenhum livro encontrado com esse ISBN.")
