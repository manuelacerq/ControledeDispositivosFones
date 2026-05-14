import pandas as pd
import streamlit as st

URL = "https://docs.google.com/spreadsheets/d/1-5bvXP3GrPCCX52XOPKSsy0pL_0WTR5COwVEtAdZHUA/export?format=csv"

def consultar_dispositivo(nome_dispositivo):
    df = pd.read_csv(URL)

    st.write(df.columns)

    df.columns = df.columns.str.strip()
st.title("🎧 Controle de Fones")

dispositivo = st.selectbox(
    "Selecione o dispositivo:",
    ["Fone 1", "Fone 2", "Fone 3", "Fone 4", "Fone 5", "Fone 6", "Fone 7", "Fone 8", "Fone 9", "Fone 10"]
)

if st.button("Consultar"):
    resultado = consultar_dispositivo(dispositivo)

    if resultado:
        nome, local = resultado
        st.success(f"Responsável: {nome}")
        st.info(f"Local: {local}")
    else:
        st.warning("Nenhum registro encontrado.")
