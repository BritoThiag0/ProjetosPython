# Projeto 11
# Análise de dados em arquivo

import pandas as pd
import win32com.client as win32

# Importando a base de dados
tabela_vendas = pd.read_excel('Proj11_Analise_Arquivo.xlsx')

# Visualizando a base de dados
# Mostrar o máximo de colunnas que puder | O none nesse caso seria o valor, ou seja, sem limite, sem máximo
# pd.set_option('display.max_columns', None)
# print(tabela_vendas)


# Faturamento por loja
tab_faturamento = tabela_vendas[['ID Loja',
                                 'Valor Final']].groupby('ID Loja').sum()
print(tab_faturamento)
print('-' * 50)


# Quantidade de produtos vendidos por loja
tab_quantidade = tabela_vendas[['ID Loja',
                                'Quantidade']].groupby('ID Loja').sum()
print(tab_quantidade)
print('-' * 50)


# Ticket médio por produto em cada loja
tab_ticket_medio = (tab_faturamento['Valor Final'] /
                    tab_quantidade['Quantidade']).to_frame()
# To_frame tranforma a serie em um data frame (tabela)
tab_ticket_medio = tab_ticket_medio.rename(columns={0: 'Ticket Médio'})
print(tab_ticket_medio)
print('-' * 50)


# Enviar um e-mail com o relatório
# Conectando o Python com o Outlook do computador
# Precisa ter o Outlook instalado na máquina
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)  # Cria um e-mail
mail.To = 'Endereço de e-mail'  # Pra quem enviar
mail.Suject = 'Assunto do e-mail'  # Assunto do e-mail
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o Relatório de Vendas por cada Loja.</p>

<p>Faturamento:</p>
{tab_faturamento.to_html(formatters={'Valor Final' : 'R$ {:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{tab_quantidade.to_html(formatters={'Quantidade' : '{:,.0f}'.format})}

<p>Ticket Médio:</p>
{tab_ticket_medio.to_html(formatters={'Ticket Médio' : 'R$ {:,.2f}'.format})}

<p>Qualquer dúvida, estou à disposição.</p>

'''  # Corpo do e-mail | É um HTML body
print('E-mail enviado')

mail.Send()
