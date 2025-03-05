import streamlit as st
import pandas as pd
import requests

API_KEY = "oflivros@oficinadelivros.iam.gserviceaccount.com"  # Chave do Gepeto 🔑

# Função para buscar dados pela API do Google Books
def buscar_google_books(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&maxResults=5&key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        st.json(data)  # Exibe a resposta completa para depuração
        if "items" in data and len(data["items"]) > 0:
            for item in data["items"]:
                livro = item.get("volumeInfo", {})
                titulo = livro.get("title", "Título não encontrado")
                autor = ", ".join(livro.get("authors", ["Autor não encontrado"]))
                categoria = ", ".join(livro.get("categories", ["Categoria não encontrada"]))
                preco = "Preço não disponível"
                if titulo != "Título não encontrado" and autor != "Autor não encontrado":
                    return titulo, autor, categoria, preco
    return "Não encontrado", "Não encontrado", "Não encontrado", "Não disponível"

# Carregar planilha
@st.cache_data
def carregar_planilha(arquivo):
    return pd.read_excel(arquivo, sheet_name="GERAL", dtype={"ISBN": str})

st.title("Pesquisa de Livros por ISBN")

# Upload da planilha
arquivo = st.file_uploader("Envie a planilha de livros", type=["xlsx"])

if arquivo:
    df = carregar_planilha(arquivo)
    isbn = st.text_input("Digite o ISBN para pesquisar:")

    if st.button("Pesquisar") and isbn:
        resultado = df[df["ISBN"] == isbn]
        if not resultado.empty:
            st.write("Livro encontrado na planilha:")
            st.write(resultado)
        else:
            st.warning("ISBN não encontrado na planilha. Buscando na internet...")
            titulo, autor, categoria, preco = buscar_google_books(isbn)
            if titulo == "Não encontrado":
                st.error("Livro não encontrado na internet.")
            else:
                st.write(f"**Título:** {titulo}")
                st.write(f"**Autor:** {autor}")
                st.write(f"**Categoria:** {categoria}")
                st.write(f"**Preço:** {preco}")
