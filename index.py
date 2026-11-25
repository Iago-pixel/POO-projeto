from templates.manterclienteui import ManterClienteUI
from templates.mantercategoriaui import ManterCategoriaUI
from templates.manterprodutoui import ManterProdutoUI
from templates.reajustarprodutoui import ReajustarProdutoUI
import streamlit as st


class IndexUI:
    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Categorias", "Produtos", "Reajustar produtos"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Categorias": ManterCategoriaUI.main()
        if op == "Produtos": ManterProdutoUI.main()
        if op == "Reajustar produtos": ReajustarProdutoUI.main()

    @staticmethod
    def sidebar():
        IndexUI.menu_admin()

    @staticmethod
    def main():
        IndexUI.sidebar()

IndexUI.main()