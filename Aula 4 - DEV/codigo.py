# Título - Sistema de Vendas 
# Seção Cadastrar Vendas
    # Campo Data
    # Campo Vendedor - Ana, Bruno, Carla
    # Campo Produto - Notebook, Celular, Fone
    # Campo Quantidade
    # Campo Valor
    # Botão Cadastrar Venda
        # Quando clicar -> adicionar a venda na tabela
# Seção Vendas Cadastradas
    # Tabela com as Vendas
# Seção Dashboard    
    # Card/Métrica com o Faturamento Total
    # Gráfico de Barra/Coluna com o Faturamento por Vendedor
    # Gráfico de Pizza com o Venda por Produto

import streamlit as st
import pandas as pd
import plotly.express as px
# Passo 1: Criar a tela do sistema

# Carregar a tabela de vendas

tabela_vendas = pd.read_csv("vendas.csv")

    # Título - Sistema de Vendas    
st.write("# Sistema de Vendas")


    # Seção Cadastrar Vendas
# Barra Lateral
st.sidebar.write("## Cadastrar venda") 

# Passo 2: Criar o formulário de cadastro
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

# Lógica para cadastrar a venda
if botao_cadastrar:
    if valor <= 0:
        st.warning("O valor da venda deve ser maior que zero.")
    else:
        # Colocar na mesma ordem das colunas da tabela
        nova_venda = [str(data), vendedor, produto, quantidade, valor]
        print(nova_venda)

        # Pega a última linha da tabela
        ultima_linha = len(tabela_vendas)

        # Adiciona a nova venda na tabela. loc = localizar
        tabela_vendas.loc[ultima_linha] = nova_venda

        # Atualiza a tabela de vendas no arquivo CSV
        tabela_vendas.to_csv("vendas.csv",
                             # nao salvar o índice da tabela no arquivo CSV
                              index=False)

        st.success("Venda cadastrada com sucesso!")

    # Seção Vendas Cadastradas
st.write("## Vendas Cadastradas")

# Passo 4: Mostrar a base de dados na tela
st.dataframe(tabela_vendas)

    # Seção Dashboard
st.write("## Dashboard")

    # Card/Métrica com o Faturamento Total
faturamento = tabela_vendas["valor"].sum()

st.metric("Faturamento Total", f"R${faturamento}")

    # Gráfico de Barra/Coluna com o Faturamento por Vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")

st.plotly_chart(grafico1)

    # Gráfico de Pizza com o Venda por Produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5)

st.plotly_chart(grafico2)

# Passo 3: Salvar a venda na base de dados
# Passo 5: Criar o dashboard com os gráficos