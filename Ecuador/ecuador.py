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
authCode = impFunc.getAuthCode('DanishYasin','Alpha103')

#Central Government Debt
dfResUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-residency-of-holders-in-ecuador-chart.csv')
#Public Debt
dfByIssuerUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/public-debt-stock-by-issuer-in-ecuador-chart.csv')
dfByInstrUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/public-debt-stock-in-ecuador-chart.csv')
dfByCurUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/public-debt-stock-by-currencies-in-ecuador-chart.csv')
dfByHoldResUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/public-debt-stock-by-residency-of-holders-in-ecuador-chart.csv')
#External Sector
dfExtSecUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-sector-in-ecuador-chart.csv')
dfExtDebtByMatUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-maturity-in-ecuador-chart.csv')
dfAssLiabUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-investment-position-in-ecuador-chart.csv')
dfPortUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-portfolio-position-in-ecuador-chart.csv')
dfFXUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/imf-fx-reserves-in-ecuador-chart.csv')
#_______________________________________________
sepDate = '30/09/2019'
junDate = '30/06/2019'
marDate = '31/03/2019'
augDate = '31/08/2019'
#___________________SUMMARY_____________________
#2
dfResUSDMar = dfResUSD.loc[dfResUSD['date'] == marDate] 
#3
dfByIssuerUSDMar = dfByIssuerUSD.loc[dfByIssuerUSD['date'] == marDate]
#dfByInstrUSDMar = dfByInstrUSD.loc[dfByInstrUSD['date'] == marDate]
dfByCurUSDMar = dfByCurUSD.loc[dfByCurUSD['date'] == marDate]
dfByHoldResUSDMar = dfByHoldResUSD.loc[dfByHoldResUSD['date'] == marDate] 
#4
dfFXUSDSep = dfFXUSD.loc[dfFXUSD['date'] == sepDate] 
dfExtSecUSDMar = dfExtSecUSD.loc[dfExtSecUSD['date'] == marDate] 
dfExtDebtByMatUSDMar = dfExtDebtByMatUSD.loc[dfExtDebtByMatUSD['date'] == marDate] 
#_______________________________________________

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
doc.preamble.append(Command('title','Trounceflow Countries: Ecuador'))
doc.preamble.append(Command('author', 'Michael Trounce'))
doc.preamble.append(Command('date', NoEscape(r'\today')))
doc.append(NoEscape(r'\maketitle'))

doc.append(NoEscape(r'\begin{abstract}'))
doc.append("The `Trounceflow Countries' series of `living' documents provide real-time dynamic summaries of macroeconomic data relevant to the flows-and-positions analysis of emerging market debt. These macroeconomic data concentrate on the structure of the government bond market but also include other useful but hard-to-wrangle data such as the structure of the local institutional investor base. The data is obtained from the Trounceflow App (trounceflow.com) and the document data is automatically updated in line with the automatic updates on the App; links to the underlying national sources are also given in the `living' documents.")
doc.append(LargeText("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThe values presented in this report are the face values of the bonds"))
doc.append(NoEscape(r'\end{abstract}'))
doc.append(NewPage())

#Table of Contents
doc.append(NoEscape(r'\tableofcontents'))
doc.append(NewPage())

#Summary Chapter 1
doc.append(NoEscape(r'\chapter{Executive Summary}'))
doc.append(NewPage())
#1.1
with doc.create(Section('Central Government Debt')):
    with doc.create(Tabular('l|l|r')) as table:
        table.add_row(('Date', 'Type', 'USD bn (Total)'))
        table.add_hline()
        #Sep
        table.add_row('Mar 2019','By Residency',dfResUSDMar['Total'].values[0])
#1.2
with doc.create(Section('Other Public Debt')):
    #1.1
    with doc.create(Tabular('l|l|r')) as table:
        table.add_row(('Date', 'Type', 'USD bn (Total)'))
        table.add_hline()
        table.add_row(MultiRow(3,data='Mar 2019'),'By Issuer',dfByIssuerUSDMar['Total'].values[0])
        table.add_row('','By Currency',dfByCurUSDMar['Total'].values[0])
        table.add_row('','By Residency',dfByHoldResUSDMar['Total'].values[0])
#1.3
with doc.create(Section('External Sector')):
    with doc.create(Tabular('l|l|r')) as table:
        table.add_row(('Date', 'Type', 'USD bn (Total)'))
        table.add_hline()
        #Sep
        table.add_row('Sep 2019','FX Reserves', dfFXUSDSep['Total'].values[0])
        table.add_hline()
        #Jun
        table.add_row(MultiRow(2,data='Mar 2019'),'By Issuer', dfExtSecUSDMar['Total'].values[0])
        table.add_row('','By Maturity', dfExtDebtByMatUSDMar['Total'].values[0])

#Chapter 2 
doc.append(NoEscape(r'\chapter{Central Government Debt: Bonds, Issuers and Investors}'))
doc.append(NewPage())

#section 2.1
with doc.create(Section('By Residency [internal/local/resident; external/foreigner/non-resident]')):
    # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
    # doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_byresidency}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Gross debt of the central administration (excluding eligible debt restructuring pending):\n')

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfResUSD.iterrows():
            table.add_row(row['date'],row['domestic creditors'], row['external creditors'],row['Total'])

#Chapter 3
doc.append(NoEscape(r'\chapter{Other Public Debt}'))
doc.append(NewPage())

doc.append(NoEscape(r'\begin{landscape}'))
#3.1
with doc.create(Section('By Issuer')):
    # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
    # doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_byissuer}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')

    doc.append(bold('USD bn\n'))
    doc.append(NoEscape(r'\scalebox{0.9}{'))
    with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r|r|r')) as table:
        table.add_row(('Date', 'Public External Debt','Public Internal Debt', 'Petro Ecuador','Consejos Prov.','BCE','BEDE','BEV','BNF','CFN','EMETEL','Others'))
        table.add_hline()
        for index, row in dfByIssuerUSD.iterrows():
            table.add_row(row['date'],row['government - external debt'],row['government - internal debt'], row['petroecuador'],row['mun. y consejos prov.'],row['bce'],row['bede'],row['bev'],row['bnf'],row['cfn'],row['emetel'],row['others'])
    doc.append(NoEscape(r'}'))
#3.3
with doc.create(Section('By Currency')):
    # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
    # doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_bycurrency}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')

    doc.append(bold('USD bn\n'))
    doc.append(NoEscape(r'\scalebox{0.9}{'))
    with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r|r|r|r|r')) as table:
        table.add_row(('Date','USD','EUR','JPY','SDR','GBP','CAD','KRW','CNY','CHF','DKK','Currency Basket (BID)','SUCRE (Ecuador)','Other Currencies'))
        table.add_hline()
        for index, row in dfByCurUSD.iterrows():
            table.add_row(row['date'],row['usd'],row['eur'],row['jpy'],row['sdr'],row['gbp'],row['cad'],row['krw'],row['cny'],row['chf'],row['dkk'],row['currency basket (bid)'],row['sucre (ecuador)'],row['other currencies'])
    doc.append(NoEscape(r'}'))
doc.append(NoEscape(r'\end{landscape}'))
#3.3
with doc.create(Section('By Residency')):
    # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
    # doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_byresidency}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfByHoldResUSD.iterrows():
            table.add_row(row['date'],row['domestic creditors'], row['external creditors'],row['Total'])


# #3.3
# with doc.create(Section('By Instrument')):
#     # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
#     # doc.append('from the primary source (argentina.gob.ar)\n')
#     doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_byinstrument}{View the chart }"))
#     doc.append('on trounceﬂow.com and download the data straight from the chart\n')

#     doc.append(bold('USD bn\n'))
#     with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r|r|r')) as table:
#         table.add_row(('Date', 'Public External Debt', 'Petro Ecuador','Consejos Prov.','BCE','BEDE','BEV','BNF','CFN','EMETEL','Others'))
#         table.add_hline()
#         for index, row in dfByInstrUSD.iterrows():
#             table.add_row(row['date'],row['government - external debt'], row['petroecuador'],row['mun. y consejos prov.'],row['bce'],row['bede'],row['bev'],row['bnf'],row['cfn'],row['emetel'],row['others'])


#Chapter 4
doc.append(NoEscape(r'\chapter{External Sector}'))
doc.append(NewPage())
doc.append(NoEscape(r'\begin{landscape}'))
#4.1
with doc.create(Section('FX Reserves')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_fxreserves}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')   

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r|r')) as table:
        table.add_row('Date', 'FX', 'Gold','IMF','SDRS')
        table.add_hline()
        for index, row in dfFXUSD.iterrows():
            table.add_row(row['date'], row['fx'], row['gold'], row['imf'],row['sdrs'])
#4.2
with doc.create(Section('External Debt')):
    #4.2.1
    with doc.create(Subsection('By Issuer [Banks; Government; Monetary Authorities]')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_edsector}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(bold('USD bn\n'))
        with doc.create(Tabular('l|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Banks', 'Government','Monetary Authorities','Unclassified','Other','Total')
            table.add_hline()
            for index, row in dfExtSecUSD.iterrows():
                table.add_row(row['date'], row['banks'], row['central government'], row['monetary authorities'], row['unclassified'], row['other sectors'], row['Total'])
    #4.2.2
    with doc.create(Subsection('By Maturity[Short-term; Long-term]')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_edmaturity}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.6}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Banks (Short)', 'Banks (Long)','Monetary Authorities (Short)','Monetary Authorities (Long)','Central Government (Short)','Central Government (Long)','Others (Short)','Others (Long)','Unclassified')
            table.add_hline()
            for index, row in dfExtDebtByMatUSD.iterrows():
                table.add_row(row['date'], row['banks short-term'], row['banks long-term'], row['monetary authorities short-term'], row['monetary authorities long-term'], row['central government short-term'], row['central government long-term'], row['other sectors short-term'], row['other sectors short-term'], row['unclassified'])
        doc.append(NoEscape(r'}'))

#4.3
with doc.create(Section('International Investment Position')):
    #4.3.1
    with doc.create(Subsection('Portfolio Liabilities')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_portfoliol}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')
        
        doc.append(bold('USD bn\n'))
        
        with doc.create(Tabular('l|r|r|r')) as table:
            table.add_row('Date', 'Debt Securities', 'Equity and Investment Fund Shares','Total')
            table.add_hline()
            for index, row in dfPortUSD.iterrows():
                table.add_row(row['date'], row['debt securities'], row['equity and investment fund shares'], row['Total'])

    
    #4.3.2
    with doc.create(Subsection('Assets & Liabilities')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_al}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Assets-Direct','Assets-Reserve','Assets-Portfolio','Assets-Other','* IIP','Liabilities-Direct','Liabilities-Portfolio','Liabilities-Other')
            table.add_hline()
            for index, row in dfAssLiabUSD.iterrows():
                table.add_row(row['date'],row['assets - direct investment'], row['assets - reserve assets'], row['assets - portfolio investment'], row['assets - other investment'], row['international investment position'], row['liabilities - direct investment'], row['liabilities - portfolio investment'], row['liabilities - other investment'])
        doc.append(NoEscape(r'}'))
        doc.append('\n\n* International Investment Position\n')
doc.append(NoEscape(r'\end{landscape}'))

doc.generate_pdf('Ecuador' ,clean=True)