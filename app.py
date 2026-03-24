import streamlit as st
import streamlit.components.v1 as components

st.title("Blockchain Digital Identity Simulator")

html_file = open("digital_identity_blockchain.html", "r", encoding="utf-8")
source_code = html_file.read()

components.html(source_code, height=800, scrolling=True)
