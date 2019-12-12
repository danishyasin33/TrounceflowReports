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


#central government
dfResUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-residency-of-holders-in-dominican-republic-chart.csv')
dfResDOP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-residency-of-holders-in-dominican-republic-chart-in-dominican-peso.csv')
dfUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-currency-in-dominican-republic-chart.csv')
dfDOP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-currency-in-dominican-republic-chart-in-dominican-peso.csv')

#Other Public Debt
dfByHoldPerDOP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/trounceflowbondholdingspercentagechart/composition-of-holdings-in-dominican-republic-chart-in-dominican-peso.csv')
    #flows
        #total stock
dfForHolStDOP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/foreign-holdings-in-dominican-republic-chart-in-dominican-peso.csv')
dfForHolFlDOP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingsflowchart/foreign-holdings-flow-in-dominican-republic-chart-in-dominican-peso.csv')
dfForHolStUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/foreign-holdings-in-dominican-republic-chart.csv')
dfForHolFlUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingsflowchart/foreign-holdings-flow-in-dominican-republic-chart.csv')
        #by holder sector
dfForHolbyTypeStDOP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/composition-of-foreign-holders-by-type-of-investor-in-dominican-republic-chart-in-dominican-peso.csv')
dfForHolbyTypeFlDOP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingsflowchart/composition-of-foreign-holders-by-type-of-investor-flow-in-dominican-republic-chart-in-dominican-peso.csv')
dfForHolbyTypeStUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/composition-of-foreign-holders-by-type-of-investor-in-dominican-republic-chart.csv')
dfForHolbyTypeFlUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingsflowchart/composition-of-foreign-holders-by-type-of-investor-flow-in-dominican-republic-chart.csv')


#_______________________________________________
mar18Date = '12/03/2018'
sep18Date = '30/09/2018'
janDate = '31/01/2019'
marDate = '31/03/2019'
mayDate = '31/05/2019'
junDate = '30/06/2019'
julDate = '31/07/2019'
augDate = '31/08/2019'
augDate2 = '30/08/2019'
sepDate = '30/09/2019'
sepDate2 = '01/09/2019'
octDate = '01/10/2019'
octDate2 = '31/10/2019'
novDate = '30/11/2019'

#___________________SUMMARY_____________________
#central government




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
doc.preamble.append(Command('title','Trounceflow Countries: Dominican Republic'))
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


#Chapter 2 
doc.append(NoEscape(r'\chapter{Central Government Debt: Bonds, Issuers and Investors}'))
doc.append(NewPage())

#2.1
with doc.create(Section('By Residency [internal/local/resident; external/foreigner/non-resident]')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/dominican-republic/#tab_byresidency}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Gross debt of the central administration (excluding eligible debt restructuring pending):\n')

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfResUSD.iterrows():
            table.add_row(row['date'],row['domestic creditors'], row['external creditors'],row['Total'])

    doc.append(bold('\n\nDOP bn\n'))
    with doc.create(Tabular('l|r|r|r')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfResDOP.iterrows():
            table.add_row(row['date'],row['domestic creditors'], row['external creditors'],row['Total'])

#2.2
with doc.create(Section('By Currency [Domestic (DOP); External]')):
    doc.append(NoEscape(r"\hrefhttps://www.trounceflow.com/app/dominican-republic/#tab_bycurrency}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values for the normal situation (paid) debt are as follows:\n')

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('c|c|c|c')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfUSD.iterrows():
            table.add_row(row['date'],row['domestic currency'], row['foreign currency'],row['Total'])

    doc.append(NewPage())
    doc.append(bold('\n\nDOP bn\n'))
    with doc.create(Tabular('c|c|c|c')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfDOP.iterrows():
            table.add_row(row['date'],row['domestic currency'], row['foreign currency'],row['Total'])

doc.append(NoEscape(r'\chapter{Other Public Debt}'))
doc.append(NewPage())
#3.1
doc.append(NoEscape(r'\begin{landscape}'))
with doc.create(Section('By Holder (%)')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/dominican-republic/#tab_lc-percent}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    
    doc.append(bold('\nPercent (%)\n\n'))
    doc.append(NoEscape(r'\scalebox{0.6}{'))
    with doc.create(Tabular('l|r|r|r|r|r|r|r')) as table: 
        table.add_row(('Date','Central Administration','Commercial Banks','Decentralized Public Institutions','Financial Intermediation Public Entities','Financial Public Institutions','Financial Sector','Financing And Loans Corporations'))
        table.add_hline()
        for index, row in dfByHoldPerDOP.iterrows():
            table.add_row(row['date'],row['central administration'],row['commercial banks'],row['decentralized public institutions'],row['financial intermediation public entities'],row['financial public institutions'],row['financial sector'],row['financing and loans corporations'])
    doc.append(NoEscape(r'}'))

    doc.append("\n\n...")
    doc.append(NoEscape(r'\scalebox{0.6}{'))
    with doc.create(Tabular('r|r|r|r|r|r|r|r')) as table: 
        table.add_row(('Foreign Residence','Insurance Companies','Loans And Credit Cooperatives','Mutual Funds Administration','Natural People','Non-Financial Sector','Non Financial Public Companies','Non Financial Public Sector'))
        table.add_hline()
        for index, row in dfByHoldPerDOP.iterrows():
            table.add_row(row['foreign residence'],row['insurance companies'],row['loans and credit cooperatives'],row['mutual and investments funds administration'],row['natural people'],row['non financial private sector'],row['non financial public companies'],row['non financial public sector'])
    doc.append(NoEscape(r'}'))

    doc.append("\n\n...")
    doc.append(NoEscape(r'\scalebox{0.6}{'))
    with doc.create(Tabular('r|r|r|r|r|r|r|r')) as table: 
        table.add_row(('Non-Profits Institutions Serving To Households','Other Financial','Pension Funds Administration','Private Companies','Remains Of Houses','Savings And Loan Associations','Savings,Credits And Promotion Banks','Stock Exchange'))
        table.add_hline()
        for index, row in dfByHoldPerDOP.iterrows():
            table.add_row(row['non-profits institutions serving to households'],row['other financial'],row['pension funds administration'],row['private companies'],row['remains of houses'],row['savings and loan associations'],row['savings,credits and promotion banks'],row['stock exchange'])
    doc.append(NoEscape(r'}'))
doc.append(NoEscape(r'\end{landscape}'))
#3.2
with doc.create(Section('Flows')):
    #3.2.1
    with doc.create(Subsection('Total Stock')):
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/dominican-republic/#tab_stockfh}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')   

        doc.append(bold('Stock (DOP bn)\n'))
        with doc.create(Tabular('l|r')) as table: 
            table.add_row(('Date', 'Foreign Holdings'))
            table.add_hline()
            for index, row in dfForHolStDOP.iterrows():
                table.add_row(row['date'], row['foreign holdings'])
        #doc.append(NewPage())
        doc.append(bold('\nFlow (DOP bn)\n'))
        with doc.create(Tabular('l|r')) as table: 
            table.add_row(('Date', 'Foreign Holdings'))
            table.add_hline()
            for index, row in dfForHolFlDOP.iterrows():
                table.add_row(row['date'], row['foreign holdings'])
        
        doc.append(bold('\n\nStock (USD bn)\n'))
        with doc.create(Tabular('l|r')) as table: 
            table.add_row(('Date', 'Foreign Holdings'))
            table.add_hline()
            for index, row in dfForHolStUSD.iterrows():
                table.add_row(row['date'], row['foreign holdings'])

        doc.append(bold('\nFlow (USD bn)\n'))
        with doc.create(Tabular('l|r')) as table: 
            table.add_row(('Date', 'Foreign Holdings'))
            table.add_hline()
            for index, row in dfForHolFlUSD.iterrows():
                table.add_row(row['date'], row['foreign holdings'])
    #3.2.2
    with doc.create(Subsection('By Holder Sector Type')):
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/dominican-republic/#tab_stockfh}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')   
        
        doc.append(bold('Stock (DOP bn)\n'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table: 
            table.add_row(('Date','Financial Sector','Juridical Person','Mutual Funds','Natural People','Natural Person Two','Non-Financial Sector','Private Companies','Stock Exchange'))
            table.add_hline()
            for index, row in dfForHolbyTypeStDOP.iterrows():
                table.add_row(row['date'],row['financial sector'],row['juridical person'],row['mutual and investments funds administration'],row['natural people'],row['natural person'],row['non financial private sector'],row['private companies'],row['stock exchange'])
        #doc.append(NewPage())
        doc.append(bold('\nFlow (DOP bn)\n'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table: 
            table.add_row(('Date','Financial Sector','Juridical Person','Mutual Funds','Natural People','Natural Person Two','Non-Financial Sector','Private Companies','Stock Exchange'))
            table.add_hline()
            for index, row in dfForHolbyTypeFlDOP.iterrows():
                table.add_row(row['date'],row['financial sector'],row['juridical person'],row['mutual and investments funds administration'],row['natural people'],row['natural person'],row['non financial private sector'],row['private companies'],row['stock exchange'])
        
        doc.append(bold('\n\nStock (USD bn)\n'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table: 
            table.add_row(('Date','Financial Sector','Juridical Person','Mutual Funds','Natural People','Natural Person Two','Non-Financial Sector','Private Companies','Stock Exchange'))
            table.add_hline()
            for index, row in dfForHolbyTypeStUSD.iterrows():
                table.add_row(row['date'],row['financial sector'],row['juridical person'],row['mutual and investments funds administration'],row['natural people'],row['natural person'],row['non financial private sector'],row['private companies'],row['stock exchange'])

        doc.append(bold('\nFlow (USD bn)\n'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table: 
            table.add_row(('Date','Financial Sector','Juridical Person','Mutual Funds','Natural People','Natural Person Two','Non-Financial Sector','Private Companies','Stock Exchange'))
            table.add_hline()
            for index, row in dfForHolbyTypeFlUSD.iterrows():
                table.add_row(row['date'],row['financial sector'],row['juridical person'],row['mutual and investments funds administration'],row['natural people'],row['natural person'],row['non financial private sector'],row['private companies'],row['stock exchange'])

#chapter 4
doc.append(NoEscape(r'\chapter{External Sector}'))
doc.append(NewPage())

doc.append(NoEscape(r'\begin{landscape}'))
#4.1
with doc.create(Section('FX Reserves')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/dominican-republic/#tab_fxreserves}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')   

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r|r')) as table:
        table.add_row('Date', 'FX', 'Gold','IMF','SDRS')
        table.add_hline()
        for index, row in dfFXUSD.iterrows():
            table.add_row(row['date'], row['fx'], row['gold'], row['imf'],row['sdrs'])

    doc.append(bold('\nDOP bn\n'))
    with doc.create(Tabular('l|r|r|r|r')) as table:
        table.add_row('Date', 'FX', 'Gold','IMF','SDRS')
        table.add_hline()
        for index, row in dfFXDOP.iterrows():
            table.add_row(row['date'], row['fx'], row['gold'], row['imf'],row['sdrs'])

doc.generate_pdf('Dominican Republic', clean=True)
