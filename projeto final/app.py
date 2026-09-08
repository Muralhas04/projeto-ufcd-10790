import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Gestor de Finanças Express", page_icon="💰", layout="centered")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "financas.csv")

def carregar_dados():
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        df = pd.DataFrame(columns=["Data", "Descrição", "Categoria", "Tipo", "Valor"])
        df.to_csv(FILE_PATH, index=False)
        return df
    return pd.read_csv(FILE_PATH)

def guardar_registo(descricao, categoria, tipo, valor):
    df = carregar_dados()
    novo_registo = pd.DataFrame([{
        "Data": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Descrição": descricao,
        "Categoria": categoria,
        "Tipo": tipo,
        "Valor": float(valor)
    }])
    df = pd.concat([df, novo_registo], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)

def apagar_registo(index_para_apagar):
    df = carregar_dados()
    if index_para_apagar in df.index:
        df = df.drop(index_para_apagar)
        df.to_csv(FILE_PATH, index=False)
        return True
    return False

st.title("💰 Gestor de Finanças Pessoais")

st.subheader("Adicionar Novo Registo")

with st.form("form_financas", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        descricao = st.text_input("Descrição", placeholder="Ex: Compras de Supermercado")
        categoria = st.selectbox("Categoria", ["Alimentação", "Transporte", "Habitação", "Lazer", "Saúde", "Outro"])
    with col2:
        tipo = st.selectbox("Tipo", ["Despesa", "Receita"])
        valor = st.number_input("Valor (€)", min_value=0.01, step=0.50, format="%.2f")
    
    submetido = st.form_submit_button("Adicionar Transação")
    
    if submetido:
        if descricao.strip() == "":
            st.warning("Por favor, insere uma descrição.")
        else:
            guardar_registo(descricao, categoria, tipo, valor)
            st.success("Registo adicionado com sucesso!")
            st.rerun()

df = carregar_dados()

if not df.empty:
    st.divider()
    
    total_receitas = df[df["Tipo"] == "Receita"]["Valor"].sum()
    total_despesas = df[df["Tipo"] == "Despesa"]["Valor"].sum()
    saldo_atual = total_receitas - total_despesas

    c1, c2, c3 = st.columns(3)
    c1.metric("Receitas Totais", f"{total_receitas:.2f} €")
    c2.metric("Despesas Totais", f"{total_despesas:.2f} €")
    c3.metric("Saldo Atual", f"{saldo_atual:.2f} €", delta=f"{saldo_atual:.2f} €")

    st.divider()

    st.subheader("Análise de Despesas por Categoria")
    
    despesas_df = df[df["Tipo"] == "Despesa"]
    
    if not despesas_df.empty:
        gastos_por_cat = despesas_df.groupby("Categoria")["Valor"].sum()
        st.bar_chart(gastos_por_cat)
    else:
        st.info("Ainda não existem despesas registadas para mostrar no gráfico.")

    st.divider()

    st.subheader("Histórico de Transações")
    st.dataframe(df, use_container_width=True)

    with st.expander("🗑️ Apagar uma Transação"):
        opcoes_transacoes = {i: f"ID {i} | {row['Data']} - {row['Descrição']} ({row['Valor']:.2f} €)" for i, row in df.iterrows()}
        
        id_selecionado = st.selectbox(
            "Seleciona a transação que queres apagar:",
            options=list(opcoes_transacoes.keys()),
            format_func=lambda x: opcoes_transacoes[x]
        )
        
        if st.button("Confirmar Eliminação", type="primary"):
            if apagar_registo(id_selecionado):
                st.success("Transação apagada com sucesso!")
                st.rerun()
else:
    st.info("Ainda não existem registos. Adiciona a tua primeira transação acima!")