import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# 1. Carregar os dados

df = pd.read_csv('funcionarios_lgpd.csv')

# 2. Processar os dados
total_funcionarios = df.shape[0]
integrados = df[df['Participou'] == 'Sim'].shape[0]
nao_integrados = total_funcionarios - integrados

# 3. Criar o dashboard com Streamlit
st.title("Dashboard de Integração dos Funcionários à LGPD")

# Exibir informações gerais
st.metric("Total de Funcionários", total_funcionarios)
st.metric("Funcionários Integrados", integrados)
st.metric("Funcionários Não Integrados", nao_integrados)

# 4. Criar um gráfico de pizza para visualização
fig, ax = plt.subplots()
labels = ['Integrados', 'Não Integrados']
sizes = [integrados, nao_integrados]
colors = ['#4CAF50', '#F44336']  
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  

# Exibir o gráfico de pizza no dashboard
st.pyplot(fig)

# 5. Mostrar a lista de funcionários não integrados
st.subheader("Funcionários que Ainda Não Participaram da Integração")
nao_integrados_df = df[df['Participou'] == 'Não']
st.dataframe(nao_integrados_df[['Nome']])
