def getAuthCode(username, password):
    import requests     

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
    import requests 
    import pandas
    import csv
    from io import StringIO
    res_data = requests.get(url, headers=headers)


    data_text=res_data.text
    data_String = StringIO(data_text)
    d_reader = csv.DictReader(data_String)

    data_text_list=data_text.split('\r\n')  #list of entries separated by end of line 

    col_names = d_reader.fieldnames
    #print(col_names)
    #col_names=data_text_list[0].split(',')      #extracting names of columns from first row through comma separator

    data=pandas.DataFrame()

    for i in range(len(col_names)):
        data[col_names[i]]=[data_text_list[j].split(',')[i] for j in range(1,len(data_text_list)-1)]            #inputing data into dataframe column by column
    
    data.iloc[:,1:] = data.iloc[:,1:].apply(pandas.to_numeric)      #converting all columns except date to numeric type

    data['date']=pandas.to_datetime(data['date'])           #converting date column to datetime type
    data['date'] = data['date'].dt.strftime('%d/%m/%Y')     #formatting that date

    data = data.tail(4)
    data['Total'] = data.iloc[:,1:].sum(axis=1)             #calculating total by adding all columns except date  
    data['Total'] = data['Total'].round(2)                  #rounding of total column
 
    data.iloc[:,1:] = data.iloc[:,1:].applymap("{:,}".format)   #applying thousand separator formatting

    return data

import numpy as np
import pandas
from pylatex import Document, Foot, PageStyle, Section, MultiColumn, MultiRow, Subsection, Center, Subsubsection, Tabularx, Tabular, Math, TikZ, Axis, Plot, Figure, Matrix, Alignat, Command, NewPage, NewLine, section,HugeText, LargeText, SmallText, PageStyle
from pylatex.utils import italic, NoEscape, bold
import os
import csv 

import datetime
import requests 
import json
import impFunc


#getting authentication code
authCode = getAuthCode('DanishYasin','Alpha103')

#dfGovHoldPer = get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/trounceflowbondholdingspercentagechart/composition-of-holdings-in-mexico-chart-in-mexican-peso.csv')
dfResUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-residency-of-holders-in-mexico-chart.csv')
dfResMXN = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-residency-of-holders-in-mexico-chart-in-mexican-peso.csv')



doc = Document(documentclass='report', document_options=['11pt, notitlepage'])

#doc.preamble.append(NoEscape(r'\usepackage{appendix}'))
doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
doc.preamble.append(NoEscape(r'\usepackage{pdflscape}'))
doc.preamble.append(NoEscape(r'\usepackage[margin=1in]{geometry}'))
doc.preamble.append(NoEscape(r'\usepackage{hyperref}'))
doc.preamble.append(NoEscape(r'\hypersetup{colorlinks=true, linkcolor=blue, filecolor=magenta, urlcolor=cyan}'))
doc.preamble.append(NoEscape(r'\urlstyle{same}'))

doc.preamble.append(NoEscape(r'\linespread{1.6}'))

#Generating Title
doc.preamble.append(Command('title','Trounceflow Countries: Mexico'))
doc.preamble.append(Command('author', 'Michael Trounce'))
doc.preamble.append(Command('date', NoEscape(r'\today')))
doc.append(NoEscape(r'\maketitle'))

doc.append(NoEscape(r'\begin{abstract}'))
doc.append("The `Trounceflow Countries' series of `living' documents provide real-time dynamic summaries of macroeconomic data relevant to the flows-and-positions analysis of emerging market debt. These macroeconomic data concentrate on the structure of the government bond market but also include other useful but hard-to-wrangle data such as the structure of the local institutional investor base. The data is obtained from the Trounceflow App (trounceflow.com) and the document data is automatically updated in line with the automatic updates on the App; links to the underlying national sources are also given in the `living' documents.")
doc.append(LargeText("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThe values presented in this report are the face values of the bonds"))
doc.append(NoEscape(r'\end{abstract}'))
doc.append(NewPage())


#Chapter 3 
doc.append(NoEscape(r'\chapter{Other Public Debt}'))
doc.append(NewPage())


#section 2.2
with doc.create(Section('By Residency [internal/local/resident; external/foreigner/non-resident]')):
    # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
    # doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/mexico/#tab_byresidency}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfResUSD.iterrows():
            table.add_row(row['date'],row['domestic creditors'], row['external creditors'],row['Total'])

    doc.append(bold('\n\nMXN bn\n'))
    with doc.create(Tabular('l|r|r|r')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfResMXN.iterrows():
            table.add_row(row['date'],row['domestic creditors'], row['external creditors'],row['Total'])


doc.generate_pdf('MexicoTest' ,clean=True)