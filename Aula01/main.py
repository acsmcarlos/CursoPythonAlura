import pandas as pd

# PASSO A PASSO
# abrir os arquivos em excel
# criar uma conta no twilio
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    # print(mes)
    tabela_vendas = pd.read_excel(f'./Arquivos/{mes}.xlsx')
    # print(tabela_vendas)

# verificar se algum valor na coluna VENDAS naquele arquivos é > 55.000
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]

        print(f"Valor da venda: R$ {vendas}")
        print("Nome do vendedor: "+vendedor)

        print(f"No mes de '{mes}', o vendedor '{vendedor}' bateu a meta com 'R$ {vendas}' reais")

# ENVIAR SMS PARA O WHATSAPP




