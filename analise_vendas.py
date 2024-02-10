import pandas as pd

# Importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

tabela_vendas[['Data', 'Produto']]
# Visualizar a base de dados
pd.set_option('display.max_columns', None)
#print(tabela_vendas)

# Faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)

# Quantidade de produtos vendidos por loja
print('#' * 50)
# Ticket médio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})  # Mudando o nome da coluna de zero ---> 0 para ---> Ticket Médio 
print(ticket_medio)





# DICAS
    # Para filtrar por um coluna basta usar um couchete ---> [] para filtar mais de uma coluna deve usar dois couchete ---> [[]]
    # Colocando toda expressão dentro de parenteses ---> () e no final inserindo a ---> função .to_frame()
        #Ele não tem mudança nenhuma visual apenas transforma o resultado em tabela.

