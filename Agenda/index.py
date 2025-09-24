from templates.manterClienteUI import ManterClienteUI
from templates.manterServicoUI import ManterServicoUI
import streamlit as st

class IndexUI:
    def main():
        st.sidebar.title("Menu")
        op = st.sidebar.selectbox("Escolha uma opção", ["Clientes", "Serviços"])

        if op == "Clientes":
            ManterClienteUI.main()
        elif op == "Serviços":
            ManterServicoUI.main()

IndexUI.main()
