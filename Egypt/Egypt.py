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


#getting authentication code
authCode = impFunc.getAuthCode('DanishYasin','Alpha103')

#_______________________________________________________________
#Government Debt
dfResEGP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-residency-of-holders-in-egypt-chart-in-egyptian-pound.csv')
dfResUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-residency-of-holders-in-egypt-chart.csv')
#dfCenbyHoldStockEGP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/composition-of-holdings-in-egypt-chart-in-egyptian-pound.csv')
#dfCenbyHoldStockUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/composition-of-holdings-in-egypt-chart.csv')
#Local Inst
dfBankEGP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-banks-in-egypt-chart-in-egyptian-pound.csv')
dfBankUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-banks-in-egypt-chart.csv')
#External Sector
dfFXEGP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/imf-fx-reserves-in-egypt-chart-in-egyptian-pound.csv')
dfFXUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/imf-fx-reserves-in-egypt-chart.csv')
dfExtDebtByMatEGP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-maturity-in-egypt-chart-in-egyptian-pound.csv')
dfExtDebtByMatUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-maturity-in-egypt-chart.csv')
dfIIPEGP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-investment-position-in-egypt-chart-in-egyptian-pound.csv')
dfIIPUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-investment-position-in-egypt-chart.csv')
dfPortEGP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-portfolio-position-in-egypt-chart-in-egyptian-pound.csv')
dfPortUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-portfolio-position-in-egypt-chart.csv')
#_________________________________________________________________
#__________________SUMMARY_________________________
sepDate = '30/09/2019'
junDate = '30/06/2019'
marDate = '31/03/2019'
augDate = '31/08/2019'
#chapter 2
dfResEGPMar = dfResEGP.loc[dfResEGP['date'] == marDate] 
dfResUSDMar = dfResUSD.loc[dfResUSD['date'] == marDate] 
#Chapter 3
dfBankEGPAug = dfBankEGP.loc[dfBankEGP['date'] == augDate]
dfBankUSDAug = dfBankUSD.loc[dfBankUSD['date'] == augDate]
#Chapter 4
#4.1
dfFXEGPSep = dfFXEGP.loc[dfFXEGP['date'] == sepDate]
dfFXUSDSep = dfFXUSD.loc[dfFXUSD['date'] == sepDate]
#4.2
dfExtDebtByMatEGPJun = dfExtDebtByMatEGP.loc[dfExtDebtByMatEGP['date'] == junDate]
dfExtDebtByMatUSDJun = dfExtDebtByMatUSD.loc[dfExtDebtByMatUSD['date'] == junDate]
#__________________________________________________



#Starting Document
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
doc.preamble.append(Command('title','Trounceflow Countries: Egypt'))
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
    with doc.create(Tabular('l|l|r|r')) as table:
        table.add_row(('Date', 'Type', 'USD bn (Total)','EGP bn (Total)'))
        table.add_hline()
        #Sep
        table.add_row('Mar 2019','By Residency',dfResUSDMar['Total'].values[0],dfResEGPMar['Total'].values[0])
#1.2
with doc.create(Section('Domestic Sector')):
    with doc.create(Tabular('l|l|r|r')) as table:
        table.add_row(('Date', 'Type', 'USD bn (Total)','EGP bn (Total)'))
        table.add_hline()
        #Sep
        table.add_row('Aug 2019','Dom. Banks', dfBankUSDAug['Total'].values[0], dfBankEGPAug['Total'].values[0])
#1.3
with doc.create(Section('External Sector')):
    with doc.create(Tabular('l|l|r|r')) as table:
        table.add_row(('Date', 'Type', 'USD bn (Total)','EGP bn (Total)'))
        table.add_hline()
        #Sep
        table.add_row('Sep 2019','FX Reserves', dfFXUSDSep['Total'].values[0], dfFXEGPSep['Total'].values[0])
        #Jun
        table.add_row('Jun 2019','By Maturity', dfExtDebtByMatUSDJun['Total'].values[0], dfExtDebtByMatEGPJun['Total'].values[0])


#Chapter 2 
doc.append(NoEscape(r'\chapter{Central Government Debt: Bonds, Issuers and Investors}'))
doc.append(NewPage())

#2.1
with doc.create(Section('By Residency [internal/local/resident; external/foreigner/non-resident]')):
    # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
    # doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/egypt/#tab_byresidency}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Gross debt of the central administration (excluding eligible debt restructuring pending):\n')

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfResUSD.iterrows():
            table.add_row(row['date'],row['domestic creditors'], row['external creditors'],row['Total'])

    doc.append(bold('\n\nEGP bn\n'))
    with doc.create(Tabular('l|r|r|r')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfResEGP.iterrows():
            table.add_row(row['date'],row['domestic creditors'], row['external creditors'],row['Total'])

#2.2
# with doc.create(Section('By Holder [Banks, Companies and Others]')):
#     doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/egypt/#tab_lctotal}{View the chart }"))
#     doc.append('on trounceﬂow.com and download the data straight from the chart\n')
#     doc.append('Gross debt of the central administration (excluding eligible debt restructuring pending):\n')
    
#     doc.append(bold('USD bn\n'))
#     with doc.create(Tabular('l|r|r|r')) as table:
#         table.add_row(('Date', 'Domestic', 'External','Total'))
#         table.add_hline()
#         for index, row in dfResUSD.iterrows():
#             table.add_row(row['date'],row['domestic creditors'], row['external creditors'],row['Total'])

#Chapter 3
doc.append(NoEscape(r'\chapter{Domestic Sectors}'))
doc.append(NewPage())
#3.1
doc.append(NoEscape(r'\begin{landscape}'))
with doc.create(Section('Banks')):
    # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/superintendencia-de-seguros}{View the data }"))
    # doc.append('from the primary source (argentina.gob.ar/superintendencia-de-seguros)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/egypt/#tab_fininst}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn\n'))
    
    with doc.create(Tabular('l|r|r|r|r|r|r')) as table:
        table.add_row('Date', 'Balances in Egypt','Balances Abroad', 'Cash','Loans and Discounts','Securities and Investments','Other Assets')
        table.add_hline()
        for index, row in dfBankUSD.iterrows():
            table.add_row(row['date'], row['balances with banks in egypt'], row['balances with banks abroad'], row['cash'], row['loans and discount balances for customers'], row['securities & investments in tbs'], row['other assets'])

    doc.append(bold('\n\nEGP bn\n'))
    with doc.create(Tabular('l|r|r|r|r|r|r')) as table:
        table.add_row('Date', 'Balances in Egypt','Balances Abroad', 'Cash','Loans and Discounts','Securities and Investments','Other Assets')
        table.add_hline()
        for index, row in dfBankEGP.iterrows():
            table.add_row(row['date'], row['balances with banks in egypt'], row['balances with banks abroad'], row['cash'], row['loans and discount balances for customers'], row['securities & investments in tbs'], row['other assets'])
doc.append(NoEscape(r'\end{landscape}'))
#Chapter 4
doc.append(NoEscape(r'\chapter{External Sectors}'))
doc.append(NewPage())

#4.1
doc.append(NoEscape(r'\begin{landscape}'))
with doc.create(Section('FX Reserves')):
    # doc.append(NoEscape(r"\href{http://data.imf.org/regular.aspx?key=61280813}{View the data }"))
    # doc.append('from the primary source (imf.org)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/egypt/#tab_fxreserves}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r|r')) as table:
        table.add_row('Date', 'FX', 'Gold','IMF','SDRS')
        table.add_hline()
        for index, row in dfFXUSD.iterrows():
            table.add_row(row['date'], row['fx'], row['gold'], row['imf'],row['sdrs'])

    doc.append(bold('\n\nEGP bn\n'))
    with doc.create(Tabular('l|r|r|r|r')) as table:
        table.add_row('Date', 'FX', 'Gold','IMF','SDRS')
        table.add_hline()
        for index, row in dfFXEGP.iterrows():
            table.add_row(row['date'], row['fx'], row['gold'], row['imf'],row['sdrs'])

#section 4.2
with doc.create(Section('External Debt')):
    #4.1.1
    with doc.create(Subsection('By Maturity[Short-term; Long-term]')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/egypt/#tab_externaldebt}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')
        doc.append(NewPage())
        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.7}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Banks (Short)', 'Banks (Long)','Monetary Authorities (Short)','Monetary Authorities (Long)','Central Government (Short)','Central Government (Long)','Others (Short)','Others (Long)')
            table.add_hline()
            for index, row in dfExtDebtByMatUSD.iterrows():
                table.add_row(row['date'], row['banks short-term'], row['banks long-term'], row['monetary authorities short-term'], row['monetary authorities long-term'], row['central government short-term'], row['central government long-term'], row['other sectors short-term'], row['other sectors short-term'])
        doc.append(NoEscape(r'}'))

        doc.append(bold('\n\nEGP bn\n'))
        doc.append(NoEscape(r'\scalebox{0.7}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Banks (Short)', 'Banks (Long)','Monetary Authorities (Short)','Monetary Authorities (Long)','Central Government (Short)','Central Government (Long)','Others (Short)','Others (Long)')
            table.add_hline()
            for index, row in dfExtDebtByMatEGP.iterrows():
                table.add_row(row['date'], row['banks short-term'], row['banks long-term'], row['monetary authorities short-term'], row['monetary authorities long-term'], row['central government short-term'], row['central government long-term'], row['other sectors short-term'], row['other sectors short-term'])
        doc.append(NoEscape(r'}'))

with doc.create(Section('International Investment Position')):
    
    #section 4.2.2
    with doc.create(Subsection('Assets & Liabilities')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/egypt/#tab_al}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Assets-Direct','Assets-Reserve','Assets-Portfolio','Assets-Other','* IIP','Liabilities-Direct', 'Liabilities-Portfolio','Liabilities-Other')
            table.add_hline()
            for index, row in dfIIPUSD.iterrows():
                table.add_row(row['date'],row['assets - direct investment'], row['assets - reserve assets'], row['assets - portfolio investment'], row['assets - other investment'], row['international investment position'], row['liabilities - direct investment'], row['liabilities - portfolio investment'], row['liabilities - other investment'])
        doc.append(NoEscape(r'}'))
        doc.append('\n\n* International Investment Position\n')
        doc.append(NewPage())
        doc.append(bold('EGP bn\n'))
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Assets-Direct','Assets-Reserve','Assets-Portfolio','Assets-Other','* IIP','Liabilities-Direct', 'Liabilities-Portfolio','Liabilities-Other')
            table.add_hline()
            for index, row in dfIIPEGP.iterrows():
                table.add_row(row['date'],row['assets - direct investment'], row['assets - reserve assets'], row['assets - portfolio investment'], row['assets - other investment'], row['international investment position'], row['liabilities - direct investment'], row['liabilities - portfolio investment'], row['liabilities - other investment'])
        doc.append(NoEscape(r'}'))
        doc.append('\n\n* International Investment Position')

    #doc.append(NoEscape(r'\end{landscape}'))

    #4.2.1
    with doc.create(Subsection('Portfolio Liabilities')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/egypt/#tab_portfoliol}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')
        
        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('l|r|r|r')) as table:
            table.add_row('Date', 'Debt Securities', 'Equity and Investment Fund Shares','Total')
            table.add_hline()
            for index, row in dfPortUSD.iterrows():
                table.add_row(row['date'], row['debt securities'], row['equity and investment fund shares'], row['Total'])
        doc.append(NoEscape(r'}'))

        doc.append(bold('\n\nEGP bn\n'))
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('l|r|r|r')) as table:
            table.add_row('Date', 'Debt Securities', 'Equity and Investment Fund Shares','Total')
            table.add_hline()
            for index, row in dfPortEGP.iterrows():
                table.add_row(row['date'], row['debt securities'], row['equity and investment fund shares'], row['Total'])
        doc.append(NoEscape(r'}'))

    doc.append(NoEscape(r'\end{landscape}'))
    # #chapter 6
    # doc.append(NoEscape(r'\chapter{International Investment Position (Assets - Liabilities)}'))
    # doc.append(NewPage())

    
doc.generate_pdf('Egypt' ,clean=True)
