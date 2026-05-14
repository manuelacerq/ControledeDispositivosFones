import pandas as pd
import streamlit as st

URL = "https://docs.google.com/spreadsheets/d/1-5bvXP3GrPCCX52XOPKSsy0pL_0WTR5COwVEtAdZHUA/export?format=csv"

def consultar_dispositivo(nome_dispositivo):
    df = pd.read_csv(URL)

    # remove espaços invisíveis dos nomes das colunas
    df.columns = df.columns.str.strip()

    st.write(df.columns)

    col_dispositivo = "Qual fone de ouvido você está tomando posse?"
    col_nome = "Qual o seu nome completo?"
    col_local = "Em qual localidade o dispositivo estará sendo utilizado? (ex: EAJ, LAIS, etc)"

    df_filtrado = df[df[col_dispositivo] == nome_dispositivo]

    if df_filtrado.empty:
        return None

    ultimo = df_filtrado.iloc[-1]

    st.write(ultimo)

    return ultimo[col_nome], ultimo[col_local]
    
st.title("🎧 Controle de Fones")

dispositivo = st.selectbox(
    "Selecione o dispositivo:",
    ["Fone 1", "Fone 2", "Fone 3", "Fone 4", "Fone 5",
     "Fone 6", "Fone 7", "Fone 8", "Fone 9", "Fone 10"]
)

if st.button("Consultar"):
    resultado = consultar_dispositivo(dispositivo)

    if resultado:
        nome, local = resultado
        st.success(f"Responsável: {nome}")
        st.info(f"Local: {local}")
    else:
        st.warning("Nenhum registro encontrado.")
