import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv') # lendo os dados

st.header('Car Informations!')
hist_button = st.button('Criar Histograma') #criando botão
if hist_button: #se o botão for clicado
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros') #escreva

    #criar histograma
    fig = px.histogram(car_data, x="odometer")

    #grafico interativo
    st.plotly_chart(fig, use_container_width=True)

#criando outro botão
dis_button = st.button('Criar Gráfico de Dispesão')
if dis_button: #se o botão for clicado
    st.write('Criando gráfico de dispersão para o conjunto de dados de anúncio de vendas de caros') #escreva
    #criar gráfico de dispersão
    fig_scatter = px.scatter(car_data, x="odometer", y="price")  # Especificar ambos os eixos x e y
    st.plotly_chart(fig_scatter, use_container_width=True)

# Mensagem se nenhum botão for clicado
if not hist_button and not dis_button:
    st.write('Clique nos botões acima para gerar visualizações.')
