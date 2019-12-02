import numpy as np
import pandas
from pylatex import Document, PageStyle, Section, MultiColumn, MultiRow, Subsection, Center, Subsubsection, Tabularx, Tabular, Math, TikZ, Axis, Plot, Figure, Matrix, Alignat, Command, NewPage, NewLine, section,HugeText, LargeText, SmallText, PageStyle
from pylatex.utils import italic, NoEscape, bold
import os
import csv 

import datetime
import requests 
import json
import impFunc

def getAuthCode(username, password):

    data = {
      'username': username,
      'password': password
    }

    res_token = requests.post('https://www.trounceflow.com/api/v1/auth-token/', data=data)

    #token=res_token.text.replace('{','').replace('}','').replace('"','').replace('token:','Token ')
    content = res_token.json()
    token = content['token']
    token = 'Token '+ token
    headers = {
        'Authorization': token,
    }
    return headers

def get_data_TrounceFlow(headers, url):
    res_data = requests.get(url, headers=headers)

    data_text=res_data.text

    data_text_list= data_text.split('\r\n')

    col_names= data_text_list[0].split(',')

    data=pandas.DataFrame()

    for i in range(len(col_names)):
        data[col_names[i]]=[data_text_list[j].split(',')[i] for j in range(1,len(data_text_list)-1)]

    data.iloc[:,1:] = data.iloc[:,1:].apply(pandas.to_numeric)

    data['date']=pandas.to_datetime(data['date'])
    data['date'] = data['date'].dt.strftime('%d/%m/%Y')

    #data['domestic currency'] = pandas.to_numeric(data['domestic currency'])
    #data['foreign currency'] = pandas.to_numeric(data['foreign currency'])
    data = data.tail(4)
    data['Total'] = data.iloc[:,1:].sum(axis=1)
    data['Total'] = data['Total'].round(2)

    data.iloc[:,1:] = data.iloc[:,1:].applymap("{:,}".format)

    return data



authCode = getAuthCode('DanishYasin','Alpha103')

dfUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-currency-in-argentina-chart.csv')
dfARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-currency-in-argentina-chart-in-argentine-peso.csv')


doc = Document(documentclass='report', document_options=['11pt'])


doc.preamble.append(NoEscape(r'\usepackage{appendix}'))
doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
doc.preamble.append(NoEscape(r'\usepackage{pdflscape}'))
doc.preamble.append(NoEscape(r'\usepackage[margin=1in]{geometry}'))
doc.preamble.append(NoEscape(r'\usepackage{hyperref}'))
doc.preamble.append(NoEscape(r'\hypersetup{colorlinks=true, linkcolor=blue, filecolor=magenta, urlcolor=cyan}'))
doc.preamble.append(NoEscape(r'\urlstyle{same}'))

doc.preamble.append(NoEscape(r'\linespread{1.6}'))

doc.append(NoEscape(r'\tableofcontents'))
doc.append(NewPage())


with doc.create(Section('By Currency [Domestic (ARS); External]')):
    doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-mensuales-de-la-deuda}{View the data }"))
    doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/argentina/#tab_bycurrency}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values for the normal situation (paid) debt are as follows:\n')

    doc.append(bold('USD bn\n\n'))
    with doc.create(Tabular('l|r|r|r')) as table:
        table.add_row(('Date', 'Domestic Ordinary Shares', 'External','Total'))
        table.add_hline()
        for index, row in dfUSD.iterrows():
            table.add_row(row['date'],row['domestic currency'], row['foreign currency'],row['Total'])

    doc.append(bold('\n\nARS bn\n\n'))
        
    with doc.create(Tabular('c|r|r|r')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfARS.iterrows():
            table.add_row(row['date'],row['domestic currency'], row['foreign currency'],row['Total'])

doc.generate_pdf('TestingMultirow', clean=True)