import streamlit as st
import time
from service import Service
from .manterprodutoui import ManterProdutoUI


class ReajustarProdutoUI:
    @staticmethod
    def main():
        st.header("Reajustar preço dos produtos")
        ReajustarProdutoUI.reajustar_produto()
        ManterProdutoUI.listar()

    @staticmethod
    def reajustar_produto():
        percentual = st.number_input("Informe a percentagem de reajuste", -100, value=0, step=1, format="%i")
        if st.button("Alterar preços"):
            Service.produto_reajustar(percentual)
            st.success("Preços alterados com sucesso")
            time.sleep(2)
            st.rerun()