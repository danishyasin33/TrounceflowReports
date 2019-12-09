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

#getting data for the tables
dfUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-currency-in-mexico-chart.csv')
dfMXN = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-currency-in-mexico-chart-in-mexican-peso.csv')
dfResUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-residency-of-holders-in-mexico-chart.csv')
dfResMXN = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-residency-of-holders-in-mexico-chart-in-mexican-peso.csv')

dfGovHoldPer = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/trounceflowbondholdingspercentagechart/composition-of-holdings-in-mexico-chart-in-mexican-peso.csv')
#PEMEX
dfPEMEXByCurUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/pemex-total-debt-by-currencies-of-denomination-in-mexico-chart.csv')
dfPEMEXByCurMXN = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/pemex-total-debt-by-currencies-of-denomination-in-mexico-chart-in-mexican-peso.csv')
dfPEMEXByMatUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/pemex-total-debt-by-terms-of-maturity-in-mexico-chart.csv')
dfPEMEXByMatMXN = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/pemex-total-debt-by-terms-of-maturity-in-mexico-chart-in-mexican-peso.csv')
dfPEMEXByInterUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/pemex-total-debt-by-type-of-interest-rate-in-mexico-chart.csv')
dfPEMEXByInterMXN = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/pemex-total-debt-by-type-of-interest-rate-in-mexico-chart-in-mexican-peso.csv')
#flows
    #Total Stock
dfForHolStMXN = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/foreign-holdings-in-mexico-chart-in-mexican-peso.csv')
dfForHolStUSD = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/foreign-holdings-in-mexico-chart.csv')
dfForHolFlMXN = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingsflowchart/foreign-holdings-flow-in-mexico-chart-in-mexican-peso.csv')
dfForHolFlUSD = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingsflowchart/foreign-holdings-flow-in-mexico-chart.csv')
    #By Instrument
dfByInstruStMXN = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/composition-of-foreign-holders-by-type-of-instrument-in-mexico-chart-in-mexican-peso.csv')
dfByInstruStUSD = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/composition-of-foreign-holders-by-type-of-instrument-in-mexico-chart.csv')
dfByInstruFlMXN = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingsflowchart/composition-of-foreign-holders-by-type-of-instrument-flow-in-mexico-chart-in-mexican-peso.csv')
dfByInstruFlUSD = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingsflowchart/composition-of-foreign-holders-by-type-of-instrument-flow-in-mexico-chart.csv')
#Equities
dfEquPortFlUSD = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/equity-portfolio-flow-in-mexico-chart.csv')
dfEquPortFlMXN = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/equity-portfolio-flow-in-mexico-chart-in-mexican-peso.csv')
#External Sector
dfExtDebtByMatUSD = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-maturity-in-mexico-chart.csv')
dfExtDebtByMatMXN = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-maturity-in-mexico-chart-in-mexican-peso.csv')
dfFXUSD = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/imf-fx-reserves-in-mexico-chart.csv')
dfFXMXN = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/imf-fx-reserves-in-mexico-chart-in-mexican-peso.csv')
dfIIPUSD = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-investment-position-in-mexico-chart.csv')
dfIIPMXN = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-investment-position-in-mexico-chart-in-mexican-peso.csv')
dfPortUSD = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-portfolio-position-in-mexico-chart.csv')
dfPortMXN = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-portfolio-position-in-mexico-chart-in-mexican-peso.csv')
#Domestic Sector
dfPensionUSD = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-government-securities-of-pension-funds-by-security-type-in-mexico-chart.csv')
dfPensionMXN = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-government-securities-of-pension-funds-by-security-type-in-mexico-chart-in-mexican-peso.csv')
dfInsurUSD = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-government-securities-of-insurance-and-surety-companies-by-security-type-in-mexico-chart.csv')
dfInsurMXN = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-government-securities-of-insurance-and-surety-companies-by-security-type-in-mexico-chart-in-mexican-peso.csv')
dfBankUSD = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-government-securities-of-banks-by-security-type-in-mexico-chart.csv')
dfBankMXN = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-government-securities-of-banks-by-security-type-in-mexico-chart-in-mexican-peso.csv')
#_______________________________________________
marDate = '31/03/2019'
junDate = '30/06/2019'
julDate = '31/07/2019'
augDate = '31/08/2019'
augDate2 = '30/08/2019'
sepDate = '30/09/2019'
octDate = '01/10/2019'
octDate2 = '31/10/2019'

#___________________SUMMARY_____________________

#central government
dfUSDJun = dfUSD.loc[dfUSD['date'] == julDate]
dfMXNJun = dfMXN.loc[dfMXN['date'] == julDate]

#PEMEX Debt
dfPEMEXByCurUSDJun = dfPEMEXByCurUSD.loc[dfPEMEXByCurUSD['date'] == junDate]
dfPEMEXByCurMXNJun = dfPEMEXByCurMXN.loc[dfPEMEXByCurMXN['date'] == junDate]
dfPEMEXByMatUSDJun = dfPEMEXByMatUSD.loc[dfPEMEXByMatUSD['date'] == junDate]
dfPEMEXByMatMXNJun = dfPEMEXByMatMXN.loc[dfPEMEXByMatMXN['date'] == junDate]
dfPEMEXByInterUSDJun = dfPEMEXByInterUSD.loc[dfPEMEXByInterUSD['date'] == junDate]
dfPEMEXByInterMXNJun = dfPEMEXByInterMXN.loc[dfPEMEXByInterMXN['date'] == junDate]
#Flows
    #total stocks
dfForHolStMXNTail = dfForHolStMXN.tail(1) 
dfForHolStUSDTail = dfForHolStUSD.tail(1) 
dfForHolFlMXNTail = dfForHolFlMXN.tail(1) 
dfForHolFlUSDTail = dfForHolFlUSD.tail(1) 

Lastdate = dfForHolStMXNTail['date'].values[0]
#Lastdate =  
Lastdate = datetime.datetime.strptime(Lastdate,'%d/%m/%Y')
time = Lastdate.strftime("%b %Y")
#Equity Flow
dfEquPortFlUSDOct = dfEquPortFlUSD.loc[dfEquPortFlUSD['date'] == octDate]
dfEquPortFlMXNOct = dfEquPortFlMXN.loc[dfEquPortFlMXN['date'] == octDate]
#External Sector
dfFXUSDOct = dfFXUSD.loc[dfFXUSD['date'] == octDate2]
dfFXMXNOct = dfFXMXN.loc[dfFXMXN['date'] == octDate2]
dfExtDebtByMatUSDMar = dfExtDebtByMatUSD.loc[dfExtDebtByMatUSD['date'] == marDate]
dfExtDebtByMatMXNMar = dfExtDebtByMatMXN.loc[dfExtDebtByMatMXN['date'] == marDate]
#Domestic Sector
dfPensionUSDAug = dfPensionUSD.loc[dfPensionUSD['date'] == augDate2]
dfPensionMXNAug = dfPensionMXN.loc[dfPensionMXN['date'] == augDate2]
dfInsurUSDAug = dfInsurUSD.loc[dfInsurUSD['date'] == augDate2]
dfInsurMXNAug = dfInsurMXN.loc[dfInsurMXN['date'] == augDate2]
dfBankUSDAug = dfBankUSD.loc[dfBankUSD['date'] == augDate]
dfBankMXNAug = dfBankMXN.loc[dfBankMXN['date'] == augDate]
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
doc.preamble.append(Command('title','Trounceflow Countries: Mexico'))
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
#2.1
with doc.create(Section('Central Government Debt')):
    with doc.create(Tabular('l|l|r|r')) as table:
        table.add_row(('Date', 'Type', 'USD bn (Total)','MXN bn (Total)'))
        table.add_hline()
        #July
        table.add_row('Jul 2019','By Currency [Domestic (MXN); External]',dfUSDJun['Total'].values[0],dfMXNJun['Total'].values[0])

#3
with doc.create(Section('Other Public Debt')):
    #PEMEX Debt section 3.2
    with doc.create(Subsection('PEMEX Debt')):
        with doc.create(Tabular('l|l|r|r')) as table:
            table.add_row(('Date', 'Type', 'USD bn (Total)','MXN bn (Total)'))
            table.add_hline()
            #June
            table.add_row(MultiRow(3,data='Jun 2019'), 'Debt by Currency', dfPEMEXByCurUSDJun['Total'].values[0], dfPEMEXByCurMXNJun['Total'].values[0])
            table.add_row('', 'Debt by Maturity', dfPEMEXByMatUSDJun['Total'].values[0], dfPEMEXByMatMXNJun['Total'].values[0])
            table.add_row('', 'Debt by Interest', dfPEMEXByInterUSDJun['Total'].values[0], dfPEMEXByInterMXNJun['Total'].values[0])
    
    #3.3 Flows
    with doc.create(Subsection('Flows')):
        with doc.create(Tabular('l|l|r|r')) as table:
            table.add_row(('Date', 'Type', 'USD bn (Total)','MXN bn (Total)'))
            table.add_hline()
            #June
            table.add_row(MultiRow(2,data=time),'Stock',dfForHolStUSDTail['foreign holdings'].values[0],dfForHolStMXNTail['foreign holdings'].values[0])
            table.add_row('','Flow',dfForHolFlUSDTail['foreign holdings'].values[0],dfForHolFlMXNTail['foreign holdings'].values[0])
            table.add_hline()
            table.add_row('Oct 2019','Equity Flow',dfEquPortFlUSDOct['Total'].values[0],dfEquPortFlMXNOct['Total'].values[0])
#4
with doc.create(Section('External Sector')):
    with doc.create(Tabular('l|l|r|r')) as table:
        table.add_row(('Date','Type', 'USD bn (Total)','MXN bn (Total)'))
        table.add_hline()
        #sep
        table.add_row('Oct 2019','IMF FX Reserves', dfFXUSDOct['Total'].values[0], dfFXMXNOct['Total'].values[0])
        table.add_hline()
        #June
        table.add_row('Mar 2019', 'By Maturity', dfExtDebtByMatUSDMar['Total'].values[0], dfExtDebtByMatMXNMar['Total'].values[0])
       
#5
with doc.create(Section('Domestic Sector')):
    with doc.create(Tabular('l|l|r|r')) as table:
        table.add_row(('Date','Type', 'USD bn (Total)','MXN bn (Total)'))
        table.add_hline()
        #June
        table.add_row(MultiRow(3,data='Aug 2019'), 'Insur. Companies', dfInsurUSDAug['Total'].values[0], dfInsurMXNAug['Total'].values[0])
        table.add_row('', 'Banks', dfBankUSDAug['Total'].values[0], dfBankMXNAug['Total'].values[0])
        table.add_row('', 'Pension Funds', dfPensionUSDAug['Total'].values[0], dfPensionMXNAug['Total'].values[0])
    

#Chapter 2 
doc.append(NoEscape(r'\chapter{Central Government Debt: Bonds, Issuers and Investors}'))
doc.append(NewPage())

#section 2.1
with doc.create(Section('By Currency [Domestic (MXN); External]')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/mexico/#tab_bycurrency}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values for the normal situation (paid) debt are as follows:\n')

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('c|c|c|c')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfUSD.iterrows():
            table.add_row(row['date'],row['domestic currency'], row['foreign currency'],row['Total'])

    doc.append(bold('\n\nMXN bn\n'))
    with doc.create(Tabular('c|c|c|c')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfMXN.iterrows():
            table.add_row(row['date'],row['domestic currency'], row['foreign currency'],row['Total'])

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

#Chapter 3 
doc.append(NoEscape(r'\chapter{Other Public Debt}'))
doc.append(NewPage())


doc.append(NoEscape(r'\begin{landscape}'))
#3.1
with doc.create(Section('By Holder (%)')):
    # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
    # doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/mexico/#tab_lc-percent}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    
    doc.append(bold('\nGovernmental Holdings\n\n'))
    doc.append(NoEscape(r'\scalebox{0.7}{'))
    with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r')) as table: #11 columns - 10 remaining 
        table.add_row(('Date', 'Insurance Companies', 'Investment Funds','Banking Sector', 'Foreign Residents', 'Guarantees by Banxico', 'Repos with Banxico','Securities Held by Banxico', 'Other Residents', 'Pension Funds'))
        table.add_hline()
        for index, row in dfGovHoldPer.iterrows():
            table.add_row(row['date'],row['gubernamental, insurance and surety companies (g)'], row['gubernamental, investment funds (f)'],row['gubernamental, net positon on banking sector (b)'], row['gubernamental, net positon on foreign residents (ii)'], row['gubernamental, net positon on guarantees received by banxico (c)'], row['gubernamental, net positon on repos with banxico (a)'], row['gubernamental, securities held by banco de méxico (d)'], row['gubernamental, other residents (h)'], row['gubernamental, pension funds (siefores) (e)'])
    doc.append(NoEscape(r'}'))

#3.2
with doc.create(Section('PEMEX Debt')):
    #3.2.1
    with doc.create(Subsection('By Currency')):
        # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/mexico/#tab_pemex-currency}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')

        doc.append(bold('USD bn\n'))
        #doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r')) as table:
            table.add_row(('Date','USD','MXN','EUR','CHF','GBP','JPY','UDIs'))
            table.add_hline()
            for index, row in dfPEMEXByCurUSD.iterrows():
                table.add_row(row['date'],row['usd'],row['mxn'],row['eur'],row['chf'],row['gbp'],row['jpy'],row['udis'])
        #doc.append(NoEscape(r'}'))
        doc.append(NoEscape(r'\end{landscape}'))

        doc.append(bold('\nMXN bn\n'))
        #doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r')) as table:
            table.add_row(('Date','USD','MXN','EUR','CHF','GBP','JPY','UDIs'))
            table.add_hline()
            for index, row in dfPEMEXByCurMXN.iterrows():
                table.add_row(row['date'],row['usd'],row['mxn'],row['eur'],row['chf'],row['gbp'],row['jpy'],row['udis'])
        #doc.append(NoEscape(r'}'))
    #3.2.2
    with doc.create(Subsection('By Maturity[Short-term; Long-term]')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/mexico/#tab_pemex-maturity}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(bold('USD bn\n'))
        #doc.append(NoEscape(r'\scalebox{0.6}{'))
        with doc.create(Tabular('l|r|r')) as table:
            table.add_row('Date', 'Short-Term', 'Long-Term')
            table.add_hline()
            for index, row in dfPEMEXByMatUSD.iterrows():
                table.add_row(row['date'], row['short-term'], row['long-term'])
        #doc.append(NoEscape(r'}'))

        doc.append(bold('\nMXN bn\n'))
        #doc.append(NoEscape(r'\scalebox{0.6}{'))
        with doc.create(Tabular('l|r|r')) as table:
            table.add_row('Date', 'Short-Term', 'Long-Term')
            table.add_hline()
            for index, row in dfPEMEXByMatMXN.iterrows():
                table.add_row(row['date'], row['short-term'], row['long-term'])
        #doc.append(NoEscape(r'}'))
    
    #3.2.3
    with doc.create(Subsection('By Interest Rate[Fixed-Rate; Floating-Rate]')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/mexico/#tab_pemex-maturity}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(NewPage())
        doc.append(bold('USD bn\n'))
        #doc.append(NoEscape(r'\scalebox{0.6}{'))
        with doc.create(Tabular('l|r|r')) as table:
            table.add_row('Date', 'Fixed Rate', 'Floating Rate')
            table.add_hline()
            for index, row in dfPEMEXByInterUSD.iterrows():
                table.add_row(row['date'], row['fixed rate'], row['floating rate'])
        #doc.append(NoEscape(r'}'))

        doc.append(bold('\nMXN bn\n'))
        #doc.append(NoEscape(r'\scalebox{0.6}{'))
        with doc.create(Tabular('l|r|r')) as table:
            table.add_row('Date', 'Fixed Rate', 'Floating Rate')
            table.add_hline()
            for index, row in dfPEMEXByInterMXN.iterrows():
                table.add_row(row['date'], row['fixed rate'], row['floating rate'])
        #doc.append(NoEscape(r'}'))
#3.3
with doc.create(Section('Flows')):
    #3.3.1
    with doc.create(Subsection('Total Stock')):
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/mexico/#tab_stockfh}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        #doc.append('Gross debt of the central administration (excluding eligible debt restructuring pending):\n')
        #doc.append(NewPage())

        doc.append(bold('Stock (MXN bn)\n'))
        with doc.create(Tabular('l|r')) as table: 
            table.add_row(('Date', 'Foreign Holdings'))
            table.add_hline()
            for index, row in dfForHolStMXN.iterrows():
                table.add_row(row['date'], row['foreign holdings'])

        doc.append(bold('\nFlow (MXN bn)\n'))
        with doc.create(Tabular('l|r')) as table: 
            table.add_row(('Date', 'Foreign Holdings'))
            table.add_hline()
            for index, row in dfForHolFlMXN.iterrows():
                table.add_row(row['date'], row['foreign holdings'])

        doc.append(NoEscape(r'\begin{landscape}'))
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

    #3.3.2
    with doc.create(Subsection('By Instrument')):
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/mexico/#tab_instrument}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        #doc.append('Gross debt of the central administration (excluding eligible debt restructuring pending):\n')
        #doc.append(NewPage())

        doc.append(bold('Stock (MXN bn)\n'))
        doc.append(NoEscape(r'\scalebox{0.8}{'))
        with doc.create(Tabular('l|r|r|r|r|r')) as table: 
            table.add_row(('Date', 'Foreign Residents (BONDES)','Foreign Residents (UDIBONOS)','Foreign Residents (CETES)','Foreign Residents (BONOS)','Foreign Residents (BONDES D)'))
            table.add_hline()
            for index, row in dfByInstruStMXN.iterrows():
                table.add_row(row['date'], row['bondes, foreign residents (ii)'], row['udibonos pesos, foreign residents (ii)'], row['cetes, foreign residents (ii)'], row['bonos, foreign residents (ii)'], row['bondes d, foreign residents (ii)'])
        doc.append(NoEscape(r'}'))
        doc.append(NewPage())
        doc.append(bold('\nFlow (MXN bn)\n'))
        doc.append(NoEscape(r'\scalebox{0.8}{'))
        with doc.create(Tabular('l|r|r|r|r|r')) as table: 
            table.add_row(('Date', 'Foreign Residents (BONDES)','Foreign Residents (UDIBONOS)','Foreign Residents (CETES)','Foreign Residents (BONOS)','Foreign Residents (BONDES D)'))
            table.add_hline()
            for index, row in dfByInstruFlMXN.iterrows():
                table.add_row(row['date'], row['bondes, foreign residents (ii)'], row['udibonos pesos, foreign residents (ii)'], row['cetes, foreign residents (ii)'], row['bonos, foreign residents (ii)'], row['bondes d, foreign residents (ii)'])
        doc.append(NoEscape(r'}'))

        doc.append(bold('\n\nStock (USD bn)\n'))
        doc.append(NoEscape(r'\scalebox{0.8}{'))
        with doc.create(Tabular('l|r|r|r|r|r')) as table:
            table.add_row(('Date', 'Foreign Residents (BONDES)','Foreign Residents (UDIBONOS)','Foreign Residents (CETES)','Foreign Residents (BONOS)','Foreign Residents (BONDES D)'))
            table.add_hline()
            for index, row in dfByInstruStUSD.iterrows():
                table.add_row(row['date'], row['bondes, foreign residents (ii)'], row['udibonos pesos, foreign residents (ii)'], row['cetes, foreign residents (ii)'], row['bonos, foreign residents (ii)'], row['bondes d, foreign residents (ii)'])
        doc.append(NoEscape(r'}'))

        doc.append(bold('\nFlow (USD bn)\n'))
        doc.append(NoEscape(r'\scalebox{0.8}{'))
        with doc.create(Tabular('l|r|r|r|r|r')) as table: 
            table.add_row(('Date', 'Foreign Residents (BONDES)','Foreign Residents (UDIBONOS)','Foreign Residents (CETES)','Foreign Residents (BONOS)','Foreign Residents (BONDES D)'))
            table.add_hline()
            for index, row in dfByInstruFlUSD.iterrows():
                table.add_row(row['date'], row['bondes, foreign residents (ii)'], row['udibonos pesos, foreign residents (ii)'], row['cetes, foreign residents (ii)'], row['bonos, foreign residents (ii)'], row['bondes d, foreign residents (ii)'])
        doc.append(NoEscape(r'}'))

    doc.append(NoEscape(r'\end{landscape}'))
#3.4
with doc.create(Section('Equities')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/mexico/#tab_equity}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    #doc.append('Gross debt of the central administration (excluding eligible debt restructuring pending):\n')
    #doc.append(NewPage())

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r')) as table: 
        table.add_row(('Date', 'Equity Flow'))
        table.add_hline()
        for index, row in dfEquPortFlUSD.iterrows():
            table.add_row(row['date'], row["non-residents' holdings of equity shares issued by mexican enterprises, flows"])

    doc.append(bold('\nMXN bn\n'))
    with doc.create(Tabular('l|r')) as table: 
        table.add_row(('Date', 'Equity Flow'))
        table.add_hline()
        for index, row in dfEquPortFlMXN.iterrows():
                table.add_row(row['date'], row["non-residents' holdings of equity shares issued by mexican enterprises, flows"])



#chapter 4
doc.append(NoEscape(r'\chapter{External Sector}'))
doc.append(NewPage())

doc.append(NoEscape(r'\begin{landscape}'))
#4.1
with doc.create(Section('FX Reserves')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/mexico/#tab_fxreserves}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')   

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r|r')) as table:
        table.add_row('Date', 'FX', 'Gold','IMF','SDRS')
        table.add_hline()
        for index, row in dfFXUSD.iterrows():
            table.add_row(row['date'], row['fx'], row['gold'], row['imf'],row['sdrs'])

    doc.append(bold('\nMXN bn\n'))
    with doc.create(Tabular('l|r|r|r|r')) as table:
        table.add_row('Date', 'FX', 'Gold','IMF','SDRS')
        table.add_hline()
        for index, row in dfFXMXN.iterrows():
            table.add_row(row['date'], row['fx'], row['gold'], row['imf'],row['sdrs'])
#4.2
with doc.create(Section('External Debt')):
    #4.2.1
    with doc.create(Subsection('By Maturity[Short-term; Long-term]')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/mexico/#tab_edmaturity}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(NewPage())
        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.6}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Banks (Short)', 'Banks (Long)','Monetary Authorities (Short)','Monetary Authorities (Long)','Central Government (Short)','Central Government (Long)','Others (Short)','Others (Long)','Unclassified')
            table.add_hline()
            for index, row in dfExtDebtByMatUSD.iterrows():
                table.add_row(row['date'], row['banks short-term'], row['banks long-term'], row['monetary authorities short-term'], row['monetary authorities long-term'], row['central government short-term'], row['central government long-term'], row['other sectors short-term'], row['other sectors short-term'], row['unclassified'])
        doc.append(NoEscape(r'}'))

        doc.append(bold('\n\nMXN bn\n'))
        doc.append(NoEscape(r'\scalebox{0.6}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Banks (Short)', 'Banks (Long)','Monetary Authorities (Short)','Monetary Authorities (Long)','Central Government (Short)','Central Government (Long)','Others (Short)','Others (Long)','Unclassified')
            table.add_hline()
            for index, row in dfExtDebtByMatMXN.iterrows():
                table.add_row(row['date'], row['banks short-term'], row['banks long-term'], row['monetary authorities short-term'], row['monetary authorities long-term'], row['central government short-term'], row['central government long-term'], row['other sectors short-term'], row['other sectors short-term'], row['unclassified'])
        doc.append(NoEscape(r'}'))

#4.3
with doc.create(Section('International Investment Position')):
    
    #section 4.3.1
    with doc.create(Subsection('Assets & Liabilities')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/mexico/#tab_al}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.7}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Assets-Direct','Assets-Reserve','Assets-Portfolio','Assets-Other','* IIP','Liabilities-Direct', 'Liabilities-Portfolio','Liabilities-Other')
            table.add_hline()
            for index, row in dfIIPUSD.iterrows():
                table.add_row(row['date'],row['assets - direct investment'], row['assets - reserve assets'], row['assets - portfolio investment'], row['assets - other investment'], row['international investment position'], row['liabilities - direct investment'], row['liabilities - portfolio investment'], row['liabilities - other investment'])
        doc.append(NoEscape(r'}'))
        
        doc.append('\n\n* International Investment Position\n')
        doc.append(NewPage())
        doc.append(bold('MXN bn\n'))
        doc.append(NoEscape(r'\scalebox{0.7}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Assets-Direct','Assets-Reserve','Assets-Portfolio','Assets-Other','* IIP','Liabilities-Direct', 'Liabilities-Portfolio','Liabilities-Other')
            table.add_hline()
            for index, row in dfIIPMXN.iterrows():
                table.add_row(row['date'],row['assets - direct investment'], row['assets - reserve assets'], row['assets - portfolio investment'], row['assets - other investment'], row['international investment position'], row['liabilities - direct investment'], row['liabilities - portfolio investment'], row['liabilities - other investment'])
        doc.append(NoEscape(r'}'))
        doc.append('\n\n* International Investment Position')

    #doc.append(NoEscape(r'\end{landscape}'))

    #4.3.2
    with doc.create(Subsection('Portfolio Liabilities')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/mexico/#tab_portfoliol}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')
        #doc.append(NewPage())
        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('l|r|r|r')) as table:
            table.add_row('Date', 'Debt Securities', 'Equity and Investment Fund Shares','Total')
            table.add_hline()
            for index, row in dfPortUSD.iterrows():
                table.add_row(row['date'], row['debt securities'], row['equity and investment fund shares'], row['Total'])
        doc.append(NoEscape(r'}'))

        doc.append(bold('\n\nMXN bn\n'))
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('l|r|r|r')) as table:
            table.add_row('Date', 'Debt Securities', 'Equity and Investment Fund Shares','Total')
            table.add_hline()
            for index, row in dfPortMXN.iterrows():
                table.add_row(row['date'], row['debt securities'], row['equity and investment fund shares'], row['Total'])
        doc.append(NoEscape(r'}'))

doc.append(NoEscape(r'\end{landscape}'))


#chapter 5
doc.append(NoEscape(r'\chapter{Domestic Sectors}'))
doc.append(NewPage())

#Section 5.1
with doc.create(Section('Pension Funds')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/mexico/#tab_pensionfunds}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r|r|r')) as table:
        table.add_row('Date', 'Bonos', 'Bondes LD','Cetes','Udibonos','Bondes')
        table.add_hline()
        for index, row in dfPensionUSD.iterrows():
            table.add_row(row['date'], row['bonos'], row['bondes ld'], row['cetes'],row['udibonos'], row['bondes'])

    doc.append(bold('\n\nMXN bn\n'))
    with doc.create(Tabular('l|r|r|r|r|r')) as table:
        table.add_row('Date', 'Bonos', 'Bondes LD','Cetes','Udibonos','Bondes')
        table.add_hline()
        for index, row in dfPensionMXN.iterrows():
            table.add_row(row['date'], row['bonos'], row['bondes ld'], row['cetes'],row['udibonos'], row['bondes'])

#Section 5.2
with doc.create(Section('Insurance Companies')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/mexico/#tab_insurancecompanies}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r|r|r')) as table:
        table.add_row('Date', 'Bonos', 'Bondes LD','Cetes','Udibonos','Bondes')
        table.add_hline()
        for index, row in dfInsurUSD.iterrows():
            table.add_row(row['date'], row['bonos'], row['bondes ld'], row['cetes'],row['udibonos'], row['bondes'])

    doc.append(NewPage())
    doc.append(bold('\nMXN bn\n'))
    with doc.create(Tabular('l|r|r|r|r|r')) as table:
        table.add_row('Date', 'Bonos', 'Bondes LD','Cetes','Udibonos','Bondes')
        table.add_hline()
        for index, row in dfInsurMXN.iterrows():
            table.add_row(row['date'], row['bonos'], row['bondes ld'], row['cetes'],row['udibonos'], row['bondes'])

#Section 5.3    
with doc.create(Section('Banks')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/mexico/#tab_banks}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r|r|r')) as table:
        table.add_row('Date', 'Bonos', 'Bondes LD','Cetes','Udibonos','Bondes')
        table.add_hline()
        for index, row in dfBankUSD.iterrows():
            table.add_row(row['date'], row['bonos'], row['bondes ld'], row['cetes'],row['udibonos'], row['bondes'])

    doc.append(bold('\n\nMXN bn\n'))
    with doc.create(Tabular('l|r|r|r|r|r')) as table:
        table.add_row('Date', 'Bonos', 'Bondes LD','Cetes','Udibonos','Bondes')
        table.add_hline()
        for index, row in dfBankMXN.iterrows():
            table.add_row(row['date'], row['bonos'], row['bondes ld'], row['cetes'],row['udibonos'], row['bondes'])



doc.generate_pdf('Mexico' ,clean=True)
