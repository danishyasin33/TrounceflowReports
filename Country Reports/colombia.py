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
dfUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-currency-in-colombia-chart.csv')
dfCOP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-currency-in-colombia-chart-in-colombian-peso.csv')
dfResUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-residency-of-holders-in-colombia-chart.csv')
dfResCOP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-residency-of-holders-in-colombia-chart-in-colombian-peso.csv')
dfExtDebtByMatUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-maturity-in-colombia-chart.csv')
dfExtDebtByMatCOP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-maturity-in-colombia-chart-in-colombian-peso.csv')
dfExtDebtBySecFinCOP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/prototypechart/prototype-chart-id-1620-in-none.csv')
dfExtDebtBySecPrivCOP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/prototypechart/prototype-chart-id-1618-in-none.csv')
dfExtDebtByInstrCOP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/prototypechart/prototype-chart-id-1619-in-none.csv')
dfIIPCOP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-investment-position-in-colombia-chart-in-colombian-peso.csv')
dfIIPUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-investment-position-in-colombia-chart.csv')
dfPortCOP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-portfolio-position-in-colombia-chart-in-colombian-peso.csv')
dfPortUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-portfolio-position-in-colombia-chart.csv')
dfByHoldPerCOP = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/trounceflowbondholdingspercentagechart/composition-of-holdings-in-colombia-chart-in-colombian-peso.csv')
dfForHolStCOP = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/foreign-holdings-in-colombia-chart-in-colombian-peso.csv')
dfForHolStUSD = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/foreign-holdings-in-colombia-chart.csv')
dfForHolFlCOP = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingsflowchart/foreign-holdings-flow-in-colombia-chart-in-colombian-peso.csv')
dfForHolFlUSD = impFunc.get_data_TrounceFlow(authCode, 'https://www.trounceflow.com/api/v1/chart/granularbondholdingsflowchart/foreign-holdings-flow-in-colombia-chart.csv')
#_______________________________________

#__________________SUMMARY_________________________
sepDate = '30/09/2019'
junDate = '30/06/2019'
marDate = '31/03/2019'
augDate = '31/08/2019'
octDate = '31/10/2019'
#chapter 2
dfUSDMar = dfUSD.loc[dfUSD['date'] == marDate] 
dfCOPMar = dfCOP.loc[dfCOP['date'] == marDate] 
#2.2
dfResUSDAug = dfResUSD.loc[dfResUSD['date'] == augDate]
dfResCOPAug = dfResCOP.loc[dfResCOP['date'] == augDate]
#Chapter 3
dfForHolStCOPOct = dfForHolStCOP.loc[dfForHolStCOP['date'] == octDate] 
dfForHolFlCOPOct = dfForHolFlCOP.loc[dfForHolFlCOP['date'] == octDate] 

dfForHolStUSDOct = dfForHolStUSD.loc[dfForHolStUSD['date'] == octDate] 
dfForHolFlUSDOct = dfForHolFlUSD.loc[dfForHolFlUSD['date'] == octDate]

#Chapter 4
dfPortCOPJun = dfPortCOP.loc[dfPortCOP['date'] == junDate]
dfPortUSDJun = dfPortUSD.loc[dfPortUSD['date'] == junDate]

#__________________________________________________

#geometry_options = {"tmargin": "5cm"}
doc = Document(documentclass='report', document_options=['11pt, notitlepage'])

doc.preamble.append(NoEscape(r'\usepackage{appendix}'))
doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
doc.preamble.append(NoEscape(r'\usepackage{pdflscape}'))
doc.preamble.append(NoEscape(r'\usepackage[margin=1in]{geometry}'))
doc.preamble.append(NoEscape(r'\usepackage{hyperref}'))
doc.preamble.append(NoEscape(r'\hypersetup{colorlinks=true, linkcolor=blue, filecolor=magenta, urlcolor=cyan}'))
doc.preamble.append(NoEscape(r'\urlstyle{same}'))
doc.preamble.append(NoEscape(r'\linespread{1.6}'))

doc.preamble.append(Command('title','Trounceflow Countries: Colombia'))
doc.preamble.append(Command('author', 'Michael Trounce'))
doc.preamble.append(Command('date', NoEscape(r'\today')))
doc.append(NoEscape(r'\maketitle'))

doc.append(NoEscape(r'\begin{abstract}'))
doc.append("The `Trounceflow Countries' series of `living' documents provide real-time dynamic summaries of macroeconomic data relevant to the flows-and-positions analysis of emerging market debt. These macroeconomic data concentrate on the structure of the government bond market but also include other useful but hard-to-wrangle data such as the structure of the local institutional investor base. The data is obtained from the Trounceflow App (trounceflow.com) and the document data is automatically updated in line with the automatic updates on the App; links to the underlying national sources are also given in the `living' documents.")
doc.append(LargeText("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThe values presented in this report are the face values of the bonds"))
doc.append(NoEscape(r'\end{abstract}'))

doc.append(NewPage())
doc.append(NoEscape(r'\tableofcontents'))
doc.append(NewPage())


#Summary Chapter 1
doc.append(NoEscape(r'\chapter{Executive Summary}'))
doc.append(NewPage())
with doc.create(Section('Central Government Debt')):
    #1.1
    with doc.create(Tabular('l|l|r|r')) as table:
        table.add_row(('Date', 'Type', 'USD bn (Total)','COP bn (Total)'))
        table.add_hline()
        table.add_row('Aug 2019','By Residency',dfResUSDAug['Total'].values[0],dfResCOPAug['Total'].values[0])
        table.add_row('Mar 2019','By Currency',dfUSDMar['Total'].values[0],dfCOPMar['Total'].values[0])

with doc.create(Section('Other Public Debt')):
    #1.1
    with doc.create(Tabular('l|l|r|r')) as table:
        table.add_row(('Date', 'Type', 'USD bn (Total)','COP bn (Total)'))
        table.add_hline()
        table.add_row(MultiRow(2,data='Oct 2019'),'Stock',dfForHolStUSDOct['foreign holdings'].values[0],dfForHolStCOPOct['foreign holdings'].values[0])
        table.add_row('','Flow',dfForHolFlUSDOct['foreign holdings'].values[0],dfForHolFlCOPOct['foreign holdings'].values[0])

with doc.create(Section('External Sector')):
    #1.1
    with doc.create(Tabular('l|l|r|r')) as table:
        table.add_row(('Date', 'Type', 'USD bn (Total)','COP bn (Total)'))
        table.add_hline()
        table.add_row('Jun 2019','Portfolio Liabilities',dfPortUSDJun['Total'].values[0],dfPortCOPJun['Total'].values[0])
        #table.add_row('Mar 2019','By Currency',dfUSDMar['Total'].values[0],dfCOPMar['Total'].values[0])

#chapter 2
doc.append(NoEscape(r'\chapter{Central Government Debt: Bonds, Issuers and Investors}'))
doc.append(NewPage())

#section 2.1
with doc.create(Section('By Currency [Domestic (COP); External]')):
    # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-mensuales-de-la-deuda}{View the data }"))
    # doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/colombia/#tab_bycurrency}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values for the normal situation (paid) debt are as follows:\n')

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('c|c|c|c')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfUSD.iterrows():
            table.add_row(row['date'],row['domestic currency'], row['foreign currency'],row['Total'])

    doc.append(bold('\n\nCOP bn\n'))
    with doc.create(Tabular('c|c|c|c')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfCOP.iterrows():
            table.add_row(row['date'],row['domestic currency'], row['foreign currency'],row['Total'])

#section 2.2
with doc.create(Section('By Residency [internal/local/resident; external/foreigner/non-resident]')):
    # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
    # doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/colombia/#tab_byresidency}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    #doc.append('Gross debt of the central administration (excluding eligible debt restructuring pending):\n')

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfResUSD.iterrows():
            table.add_row(row['date'],row['domestic creditors'], row['external creditors'],row['Total'])
    doc.append(NewPage())
    doc.append(bold('\n\nCOP bn\n'))
    with doc.create(Tabular('l|r|r|r')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfResCOP.iterrows():
            table.add_row(row['date'],row['domestic creditors'], row['external creditors'],row['Total'])

#Chapter 3 
doc.append(NoEscape(r'\chapter{Other Public Debt}'))
doc.append(NewPage())
#3.1
doc.append(NoEscape(r'\begin{landscape}'))
with doc.create(Section('By Holder (%)')):
    # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
    # doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/colombia/#tab_lc-percent}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    #doc.append('Gross debt of the central administration (excluding eligible debt restructuring pending):\n')
    #First Table
    doc.append(bold('\nPercent (%)\n\n'))
    doc.append(NoEscape(r'\scalebox{0.6}{'))
    with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table: #11 columns - 10 remaining 
        table.add_row(('Date', 'Average Premium Funds', 'Colombian Central Bank','Commercial Banks', 'Commercial Finance Companies', 'Financial Corporations', 'Floor Broker', 'High Level Financial Cooperatives', 'Insurance and Capitalization Companies'))
        table.add_hline()
        for index, row in dfByHoldPerCOP.iterrows():
            table.add_row(row['date'],row['average premium funds'], row['colombian central bank'],row['commercial banks'], row['commercial finance companies'], row['financial corporations'], row['floor broker'], row['high level financial cooperatives'], row['insurance and capitalization companies'])
    doc.append(NoEscape(r'}'))

    doc.append("\n\n...")
    doc.append(NoEscape(r'\scalebox{0.6}{'))
    with doc.create(Tabular('r|r|r|r|r|r|r|r|r|r')) as table: 
        table.add_row(('International Investors', 'Legal Persons', 'Market Infrastructure Providers', 'Ministry of Finance', 'Mutual and Pension Fund Managers', 'Mutual Funds', 'Natural Persons', 'Other Funds', 'Pension and Retirement Funds', 'Profitless Companies'))
        table.add_hline()
        for index, row in dfByHoldPerCOP.iterrows():
            table.add_row(row['international investors'], row['legal persons'], row['market infrastructure providers'], row['ministry of finance'],row['mutual and pension fund managers'], row['mutual funds'], row['natural persons'], row['other funds'], row['pension and retirement funds'], row['profitless companies'])
    doc.append(NoEscape(r'}'))

    doc.append("\n\n...")
    doc.append(NoEscape(r'\scalebox{0.6}{'))
    with doc.create(Tabular('r|r|r')) as table: 
        table.add_row(('Public Entities', 'Public Financial Institutions', 'Public Trust Funds'))
        table.add_hline()
        for index, row in dfByHoldPerCOP.iterrows():
            table.add_row(row['public entities'], row['public financial institutions'], row['public trust funds'])
    doc.append(NoEscape(r'}'))
doc.append(NoEscape(r'\end{landscape}'))
#doc.append(NewPage())
with doc.create(Section('Flows')):
    with doc.create(Subsection('Total Stock')):
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/colombia/#tab_stock-lcy}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        #doc.append('Gross debt of the central administration (excluding eligible debt restructuring pending):\n')
        #doc.append(NewPage())
        doc.append(bold('Stock (COP bn)\n'))
        with doc.create(Tabular('l|r')) as table: 
            table.add_row(('Date', 'Foreign Holdings'))
            table.add_hline()
            for index, row in dfForHolStCOP.iterrows():
                table.add_row(row['date'], row['foreign holdings'])

        doc.append(bold('\nFlow (COP bn)\n'))
        with doc.create(Tabular('l|r')) as table: 
            table.add_row(('Date', 'Foreign Holdings'))
            table.add_hline()
            for index, row in dfForHolFlCOP.iterrows():
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






#chapter 4
doc.append(NoEscape(r'\chapter{External Sector}'))
doc.append(NewPage())
#section 4.1
doc.append(NoEscape(r'\begin{landscape}'))
with doc.create(Section('External Debt')):
    #4.1.1
    with doc.create(Subsection('By Maturity[Short-term; Long-term]')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/colombia/#tab_edmaturity}{View the chart }"))
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

        doc.append(bold('\n\nCOP bn\n'))
        doc.append(NoEscape(r'\scalebox{0.6}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Banks (Short)', 'Banks (Long)','Monetary Authorities (Short)','Monetary Authorities (Long)','Central Government (Short)','Central Government (Long)','Others (Short)','Others (Long)','Unclassified')
            table.add_hline()
            for index, row in dfExtDebtByMatCOP.iterrows():
                table.add_row(row['date'], row['banks short-term'], row['banks long-term'], row['monetary authorities short-term'], row['monetary authorities long-term'], row['central government short-term'], row['central government long-term'], row['other sectors short-term'], row['other sectors short-term'], row['unclassified'])
        doc.append(NoEscape(r'}'))
    #4.1.2
    with doc.create(Subsection('By Sector[Public/Private; Financial/Non-Financial]')):
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/colombia/#tab_edsector}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:')
        
        with doc.create(Subsubsection('Public/Private:', numbering=False)):
            doc.append(bold('COP bn\n'))
            with doc.create(Tabular('l|r|r|r|r')) as table:
                table.add_row('Date', 'Private (long-term)', 'Private (short-term)','Public (long-term)','Public (short-term)')
                table.add_hline()
                for index, row in dfExtDebtBySecPrivCOP.iterrows():
                    table.add_row(row['date'], row['private sector long-term'], row['private sector short-term'], row['public sector long-term'], row['public sector short-term'])
        
        with doc.create(Subsubsection('Financial/Non-Financial:', numbering=False)):
            doc.append(bold('COP bn\n'))
            with doc.create(Tabular('l|r|r|r|r')) as table:
                table.add_row('Date', 'Financial (long-term)', 'Financial (short-term)','Non-Financial (long-term)','Non-Financial (short-term)')
                table.add_hline()
                for index, row in dfExtDebtBySecFinCOP.iterrows():
                    table.add_row(row['date'], row['financial sector long-term'], row['financial sector short-term'], row['non-financial sector long-term'], row['non-financial sector short-term'])
    
    #4.1.3
    with doc.create(Subsection('By Instruments')):
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/colombia/#tab_edinstrument}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(bold('COP bn\n'))
        doc.append(NoEscape(r'\scalebox{0.7}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Bonds (long-term)', 'Commercial Credit (long-term)','Commercial Credit (short-term)','Loans (long-term)','Loans (short-term)','Others (long-term)', 'Others (short-term)')
            table.add_hline()
            for index, row in dfExtDebtByInstrCOP.iterrows():
                table.add_row(row['date'], row['bonds long-term'], row['commercial credit long-term'], row['commercial credit short-term'], row['loans long-term'],row['loans short-term'],row['others long-term'],row['others short-term'])
        doc.append(NoEscape(r'}'))
doc.append(NewPage())
#4.2
with doc.create(Section('International Investment Position')):
    
    #section 4.2.1
    with doc.create(Subsection('Assets & Liabilities')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/colombia/#tab_al}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.7}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Assets-Direct','Assets-Reserve','Assets-Portfolio','Assets-Financial','Assets-Other','* IIP','Liabilities-Direct', 'Liabilities-Portfolio','Liabilities-Financial','Liabilities-Other')
            table.add_hline()
            for index, row in dfIIPUSD.iterrows():
                table.add_row(row['date'],row['assets - direct investment'], row['assets - reserve assets'], row['assets - portfolio investment'],row['assets - financial derivatives (except reserves)'], row['assets - other investment'], row['international investment position'], row['liabilities - direct investment'], row['liabilities - portfolio investment'],row['liabilities - financial derivatives (except reserves)'], row['liabilities - other investment'])
        doc.append(NoEscape(r'}'))
        
        doc.append('\n\n* International Investment Position\n')
        #doc.append(NewPage())
        doc.append(bold('COP bn\n'))
        doc.append(NoEscape(r'\scalebox{0.7}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Assets-Direct','Assets-Reserve','Assets-Portfolio','Assets-Financial','Assets-Other','* IIP','Liabilities-Direct', 'Liabilities-Portfolio','Liabilities-Financial','Liabilities-Other')
            table.add_hline()
            for index, row in dfIIPCOP.iterrows():
                table.add_row(row['date'],row['assets - direct investment'], row['assets - reserve assets'], row['assets - portfolio investment'],row['assets - financial derivatives (except reserves)'], row['assets - other investment'], row['international investment position'], row['liabilities - direct investment'], row['liabilities - portfolio investment'],row['liabilities - financial derivatives (except reserves)'], row['liabilities - other investment'])
        doc.append(NoEscape(r'}'))
        doc.append('\n\n* International Investment Position')

    #doc.append(NoEscape(r'\end{landscape}'))

    #4.2.2
    with doc.create(Subsection('Portfolio Liabilities')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/colombia/#tab_portfoliol}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')
        doc.append(NewPage())
        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('l|r|r|r')) as table:
            table.add_row('Date', 'Debt Securities', 'Equity and Investment Fund Shares','Total')
            table.add_hline()
            for index, row in dfPortUSD.iterrows():
                table.add_row(row['date'], row['debt securities'], row['equity and investment fund shares'], row['Total'])
        doc.append(NoEscape(r'}'))

        doc.append(bold('\n\nCOP bn\n'))
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('l|r|r|r')) as table:
            table.add_row('Date', 'Debt Securities', 'Equity and Investment Fund Shares','Total')
            table.add_hline()
            for index, row in dfPortCOP.iterrows():
                table.add_row(row['date'], row['debt securities'], row['equity and investment fund shares'], row['Total'])
        doc.append(NoEscape(r'}'))





doc.append(NoEscape(r'\end{landscape}'))


doc.generate_pdf('Colombia' ,clean=True)
