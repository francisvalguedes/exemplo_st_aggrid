import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode

# Adicionando título à página
st.title('Exemplo de Tabela Interativa com Selecção Múltipla')

# Adicionando um cabeçalho
st.header('Tabela de Dados de Pessoas')

# Texto explicativo
st.write("""
Este exemplo utiliza o **AgGrid** no Streamlit para criar uma tabela interativa.
A tabela permite selecionar múltiplas linhas usando checkboxes. 
Depois de selecionar as linhas, você verá as informações das linhas selecionadas abaixo.
""")

# Exemplo de DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)

# Configurando o grid
gb = GridOptionsBuilder.from_dataframe(df)

# Habilitar a seleção múltipla com checkboxes
gb.configure_selection(selection_mode="multiple", use_checkbox=True)

# Adicionar um checkbox no cabeçalho para selecionar todas as linhas na primeira coluna
gb.configure_column(df.columns[0], headerCheckboxSelection=True)

# Construindo as opções de grid
gridoptions = gb.build()

# Criando a tabela AgGrid
grid_table = AgGrid(
    df,
    height=250,
    gridOptions=gridoptions,
    update_mode=GridUpdateMode.SELECTION_CHANGED
)

# Exibindo as linhas selecionadas
st.write('## Linhas Selecionadas')

selected_row = grid_table["selected_rows"]

# Convertendo para DataFrame
selected_row = pd.DataFrame(selected_row)

# Exibindo as linhas selecionadas
st.dataframe(selected_row)

