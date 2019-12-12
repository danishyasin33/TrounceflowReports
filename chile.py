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
dfResUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-residency-of-holders-in-chile-chart.csv')
dfResCLP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-residency-of-holders-in-chile-chart-in-chilean-peso.csv')
dfUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-currency-in-chile-chart.csv')
dfCLP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-currency-in-chile-chart-in-chilean-peso.csv')
#other debt
dfForHolStCLP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/foreign-holdings-in-chile-chart-in-chilean-peso.csv')
dfForHolFlCLP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingsflowchart/foreign-holdings-flow-in-chile-chart-in-chilean-peso.csv')
dfForHolStUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/foreign-holdings-in-chile-chart.csv')
dfForHolFlUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingsflowchart/foreign-holdings-flow-in-chile-chart.csv')
dfEquPortFlUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/equity-portfolio-flow-in-chile-chart.csv')
dfEquPortFlCLP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/equity-portfolio-flow-in-chile-chart-in-chilean-peso.csv')
#external sector
    #fx
dfFXUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/imf-fx-reserves-in-chile-chart.csv')
dfFXCLP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/imf-fx-reserves-in-chile-chart-in-chilean-peso.csv')   
    #debt
dfExtDebtByMatUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-maturity-in-chile-chart.csv')
dfExtDebtByMatCLP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-maturity-in-chile-chart-in-chilean-peso.csv')
dfExtCurUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-currency-in-chile-chart.csv')
dfExtCurCLP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-currency-in-chile-chart-in-chilean-peso.csv')
    #IIP
dfIIPUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-investment-position-in-chile-chart.csv')
dfIIPCLP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-investment-position-in-chile-chart-in-chilean-peso.csv')
dfPortUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-portfolio-position-in-chile-chart.csv')
dfPortCLP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-portfolio-position-in-chile-chart-in-chilean-peso.csv')
 
 #Domestic Sector
dfPensionUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-em-pension-funds-in-chile-chart.csv')
dfPensionCLP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-em-pension-funds-in-chile-chart-in-chilean-peso.csv')
dfBankUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-banks-in-chile-chart.csv')
dfBankCLP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-banks-in-chile-chart-in-chilean-peso.csv')
dfMutPer = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/prototypechart/prototype-chart-id-1732-in-none.csv')
dfInsurUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-insurance-companies-in-chile-chart.csv')
dfInsurCLP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-insurance-companies-in-chile-chart-in-chilean-peso.csv')


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
dfResUSDJun = dfResUSD.loc[dfResUSD['date'] == junDate]
dfResCLPJun = dfResCLP.loc[dfResCLP['date'] == junDate]
dfUSDJun = dfUSD.loc[dfUSD['date'] == junDate]
dfCLPJun = dfCLP.loc[dfCLP['date'] == junDate]

#Other Public Debt
dfForHolStCLPOct = dfForHolStCLP.loc[dfForHolStCLP['date'] == octDate2]
dfForHolFlCLPOct = dfForHolFlCLP.loc[dfForHolFlCLP['date'] == octDate2]

dfForHolStUSDOct = dfForHolStUSD.loc[dfForHolStUSD['date'] == octDate2]
dfForHolFlUSDOct = dfForHolFlUSD.loc[dfForHolFlUSD['date'] == octDate2]

dfEquPortFlUSDSep = dfEquPortFlUSD.loc[dfEquPortFlUSD['date'] == sepDate2]
dfEquPortFlCLPSep = dfEquPortFlCLP.loc[dfEquPortFlCLP['date'] == sepDate2]

#External Sector
dfFXUSDOct = dfFXUSD.loc[dfFXUSD['date'] == octDate2]
dfFXCLPOct = dfFXCLP.loc[dfFXCLP['date'] == octDate2]

dfExtDebtByMatUSDMar = dfExtDebtByMatUSD.loc[dfExtDebtByMatUSD['date'] == marDate]
dfExtDebtByMatCLPMar = dfExtDebtByMatCLP.loc[dfExtDebtByMatCLP['date'] == marDate]

dfExtCurUSDSep = dfExtCurUSD.loc[dfExtCurUSD['date'] == sep18Date]
dfExtCurCLPSep = dfExtCurCLP.loc[dfExtCurCLP['date'] == sep18Date]

#Domestic Sector
dfPensionUSDSep = dfPensionUSD.loc[dfPensionUSD['date'] == sepDate]
dfPensionCLPSep = dfPensionCLP.loc[dfPensionCLP['date'] == sepDate]

dfBankUSDJan = dfBankUSD.loc[dfBankUSD['date'] == janDate]
dfBankCLPJan = dfBankCLP.loc[dfBankCLP['date'] == janDate]

dfInsurUSDMar18 = dfInsurUSD.loc[dfInsurUSD['date'] == mar18Date]
dfInsurCLPMar18 = dfInsurCLP.loc[dfInsurCLP['date'] == mar18Date]

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
doc.preamble.append(Command('title','Trounceflow Countries: Chile'))
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
        table.add_row(('Date', 'Type', 'USD bn (Total)','CLP bn (Total)'))
        table.add_hline()
        #Jun
        table.add_row(MultiRow(2,data='Jun 2019'),'By Residency[Internal; External]',dfResUSDJun['Total'].values[0],dfResCLPJun['Total'].values[0])
        table.add_row('','By Currency[Domestic; External]',dfUSDJun['Total'].values[0],dfCLPJun['Total'].values[0])
#3
with doc.create(Section('Other Public Debt')):
#3.4 Flows
    with doc.create(Subsection('Flows')):
        with doc.create(Tabular('l|l|r|r')) as table:
            table.add_row(('Date', 'Type', 'USD bn (Total)','CLP bn (Total)'))
            table.add_hline()
            #June
            table.add_row(MultiRow(2,data='Oct 2019'),'Stock',dfForHolStUSDOct['foreign holdings'].values[0],dfForHolStCLPOct['foreign holdings'].values[0])
            table.add_row('','Flow',dfForHolFlUSDOct['foreign holdings'].values[0],dfForHolFlCLPOct['foreign holdings'].values[0])
            table.add_hline()
            table.add_row('Sep 2019','Equity Flow',dfEquPortFlUSDSep['flow'].values[0],dfEquPortFlCLPSep['flow'].values[0])
        
#4
with doc.create(Section('External Sector')):
    with doc.create(Tabular('l|l|r|r')) as table:
        table.add_row(('Date','Type', 'USD bn (Total)','CLP bn (Total)'))
        table.add_hline()
    
        table.add_row('Oct 2019','FX Reserves', dfFXUSDOct['Total'].values[0], dfFXCLPOct['Total'].values[0])
        table.add_hline()
        table.add_row('Mar 2019', 'By Maturity', dfExtDebtByMatUSDMar['Total'].values[0], dfExtDebtByMatCLPMar['Total'].values[0])
        table.add_hline()
        table.add_row('Sep 2018', 'By Currency', dfExtCurUSDSep['Total'].values[0], dfExtCurCLPSep['Total'].values[0])

#5
with doc.create(Section('Domestic Sector')):
    with doc.create(Tabular('l|l|r|r')) as table:
        table.add_row(('Date','Type', 'USD bn (Total)','CLP bn (Total)'))
        table.add_hline()
        table.add_row('Sep 2019', 'Pension Fund', dfPensionUSDSep['Total'].values[0], dfPensionCLPSep['Total'].values[0])
        table.add_hline()
        table.add_row('Jan 2019', 'Banks', dfBankUSDJan['Total'].values[0], dfBankCLPJan['Total'].values[0])
        table.add_hline()
        table.add_row('Mar 2018', 'Ins. Comp.', dfInsurUSDMar18['Total'].values[0], dfInsurCLPMar18['Total'].values[0])


#Chapter 2 
doc.append(NoEscape(r'\chapter{Central Government Debt: Bonds, Issuers and Investors}'))
doc.append(NewPage())

#2.1
with doc.create(Section('By Residency [internal/local/resident; external/foreigner/non-resident]')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/chile/#tab_byresidency}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Gross debt of the central administration (excluding eligible debt restructuring pending):\n')

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfResUSD.iterrows():
            table.add_row(row['date'],row['domestic creditors'], row['external creditors'],row['Total'])

    doc.append(bold('\n\nCLP bn\n'))
    with doc.create(Tabular('l|r|r|r')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfResCLP.iterrows():
            table.add_row(row['date'],row['domestic creditors'], row['external creditors'],row['Total'])

#2.2
with doc.create(Section('By Currency [Domestic (CLP); External]')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/chile/#tab_bycurrency}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values for the normal situation (paid) debt are as follows:\n')

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('c|c|c|c')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfUSD.iterrows():
            table.add_row(row['date'],row['domestic currency'], row['foreign currency'],row['Total'])

    doc.append(NewPage())
    doc.append(bold('\n\nCLP bn\n'))
    with doc.create(Tabular('c|c|c|c')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfCLP.iterrows():
            table.add_row(row['date'],row['domestic currency'], row['foreign currency'],row['Total'])

#Chapter 3 
doc.append(NoEscape(r'\chapter{Other Public Debt}'))
doc.append(NewPage())
#3.1
with doc.create(Section('Flows')):
    #3.2
    with doc.create(Subsection('Total Stock')):
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/chile/#tab_stockfh}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        #doc.append('Gross debt of the central administration (excluding eligible debt restructuring pending):\n')
        #doc.append(NewPage())

        doc.append(bold('Stock (CLP bn)\n'))
        with doc.create(Tabular('l|r')) as table: 
            table.add_row(('Date', 'Foreign Holdings'))
            table.add_hline()
            for index, row in dfForHolStCLP.iterrows():
                table.add_row(row['date'], row['foreign holdings'])
        #doc.append(NewPage())
        doc.append(bold('\nFlow (CLP bn)\n'))
        with doc.create(Tabular('l|r')) as table: 
            table.add_row(('Date', 'Foreign Holdings'))
            table.add_hline()
            for index, row in dfForHolFlCLP.iterrows():
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

doc.append(NewPage())
#3.4
with doc.create(Section('Equities')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/chile/#tab_equity}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    #doc.append('Gross debt of the central administration (excluding eligible debt restructuring pending):\n')
    #doc.append(NewPage())

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r')) as table: 
        table.add_row(('Date', 'Equity Flow'))
        table.add_hline()
        for index, row in dfEquPortFlUSD.iterrows():
            table.add_row(row['date'], row["flow"])

    doc.append(bold('\nCLP bn\n'))
    with doc.create(Tabular('l|r')) as table: 
        table.add_row(('Date', 'Equity Flow'))
        table.add_hline()
        for index, row in dfEquPortFlCLP.iterrows():
                table.add_row(row['date'], row["flow"])



#chapter 4
doc.append(NoEscape(r'\chapter{External Sector}'))
doc.append(NewPage())

doc.append(NoEscape(r'\begin{landscape}'))
#4.1
with doc.create(Section('FX Reserves')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/chile/#tab_fxreserves}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')   

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r|r')) as table:
        table.add_row('Date', 'FX', 'Gold','IMF','SDRS')
        table.add_hline()
        for index, row in dfFXUSD.iterrows():
            table.add_row(row['date'], row['fx'], row['gold'], row['imf'],row['sdrs'])

    doc.append(bold('\nCLP bn\n'))
    with doc.create(Tabular('l|r|r|r|r')) as table:
        table.add_row('Date', 'FX', 'Gold','IMF','SDRS')
        table.add_hline()
        for index, row in dfFXCLP.iterrows():
            table.add_row(row['date'], row['fx'], row['gold'], row['imf'],row['sdrs'])
#4.2
with doc.create(Section('External Debt')):
    #4.2.1
    with doc.create(Subsection('By Maturity[Short-term; Long-term]')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/chile/#tab_edmaturity}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(NewPage())
        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.7}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Banks (Short)', 'Banks (Long)','Monetary Auth. (Short)','Monetary Auth. (Long)','Central Gov. (Short)','Central Gov. (Long)','Others (Short)','Others (Long)')
            table.add_hline()
            for index, row in dfExtDebtByMatUSD.iterrows():
                table.add_row(row['date'], row['banks short-term'], row['banks long-term'], row['monetary authorities short-term'], row['monetary authorities long-term'], row['central government short-term'], row['central government long-term'], row['other sectors short-term'], row['other sectors short-term'])
        doc.append(NoEscape(r'}'))

        doc.append(bold('\n\nCLP bn\n'))
        doc.append(NoEscape(r'\scalebox{0.7}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Banks (Short)', 'Banks (Long)','Monetary Auth. (Short)','Monetary Auth. (Long)','Central Gov. (Short)','Central Gov. (Long)','Others (Short)','Others (Long)')
            table.add_hline()
            for index, row in dfExtDebtByMatCLP.iterrows():
                table.add_row(row['date'], row['banks short-term'], row['banks long-term'], row['monetary authorities short-term'], row['monetary authorities long-term'], row['central government short-term'], row['central government long-term'], row['other sectors short-term'], row['other sectors short-term'])
        doc.append(NoEscape(r'}'))
    #4.2.2
    with doc.create(Subsection('By Currency [Domestic, External]')):
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/chile/#tab_edcurrency}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(bold('USD bn\n'))
        #doc.append(NoEscape(r'\scalebox{0.8}{'))
        with doc.create(Tabular('l|r|r|r|r|r')) as table:
            table.add_row('Date', 'CLP', 'USD','EUR','Other','Total')
            table.add_hline()
            for index, row in dfExtCurUSD.iterrows():
                table.add_row(row['date'],row['local currency_'], row['usd_'],row['eur_'],row['others_'], row['Total'])
        #doc.append(NoEscape(r'}'))
        doc.append(NewPage())
        doc.append(bold('\n\nCLP bn\n'))
        #doc.append(NoEscape(r'\scalebox{0.8}{'))
        with doc.create(Tabular('l|r|r|r|r|r')) as table:
            table.add_row('Date', 'CLP', 'USD','EUR','Other','Total')
            table.add_hline()
            for index, row in dfExtCurCLP.iterrows():
                table.add_row(row['date'],row['local currency_'], row['usd_'],row['eur_'],row['others_'], row['Total'])
        #doc.append(NoEscape(r'}'))

#4.3
with doc.create(Section('International Investment Position')):
    
    #section 4.3.1
    with doc.create(Subsection('Assets & Liabilities')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/chile/#tab_al}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.6}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Assets-Direct','Assets-Financial Derivatives','Assets-Reserve','Assets-Portfolio','Assets-Other','* IIP','Liabilities-Direct','Liabilities-Financial Derivatives', 'Liabilities-Portfolio','Liabilities-Other')
            table.add_hline()
            for index, row in dfIIPUSD.iterrows():
                table.add_row(row['date'],row['assets - direct investment'],row['assets - financial derivatives (except reserves)'], row['assets - reserve assets'], row['assets - portfolio investment'], row['assets - other investment'], row['international investment position'], row['liabilities - direct investment'],row['liabilities - financial derivatives (except reserves)'], row['liabilities - portfolio investment'], row['liabilities - other investment'])
        doc.append(NoEscape(r'}'))
        
        doc.append('\n\n* International Investment Position\n')
        #doc.append(NewPage())
        doc.append(bold('CLP bn\n'))
        doc.append(NoEscape(r'\scalebox{0.6}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Assets-Direct','Assets-Financial Derivatives','Assets-Reserve','Assets-Portfolio','Assets-Other','* IIP','Liabilities-Direct','Liabilities-Financial Derivatives', 'Liabilities-Portfolio','Liabilities-Other')
            table.add_hline()
            for index, row in dfIIPCLP.iterrows():
                table.add_row(row['date'],row['assets - direct investment'],row['assets - financial derivatives (except reserves)'], row['assets - reserve assets'], row['assets - portfolio investment'], row['assets - other investment'], row['international investment position'], row['liabilities - direct investment'],row['liabilities - financial derivatives (except reserves)'], row['liabilities - portfolio investment'], row['liabilities - other investment'])
        doc.append(NoEscape(r'}'))
        doc.append('\n\n* International Investment Position')

    #doc.append(NoEscape(r'\end{landscape}'))

    #4.3.2
    #doc.append(NewPage())
    with doc.create(Subsection('Portfolio Liabilities')):
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/chile/#tab_portfoliol}{View the chart }"))
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

        doc.append(bold('\n\nCLP bn\n'))
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('l|r|r|r')) as table:
            table.add_row('Date', 'Debt Securities', 'Equity and Investment Fund Shares','Total')
            table.add_hline()
            for index, row in dfPortCLP.iterrows():
                table.add_row(row['date'], row['debt securities'], row['equity and investment fund shares'], row['Total'])
        doc.append(NoEscape(r'}'))
doc.append(NoEscape(r'\end{landscape}'))


#chapter 5
doc.append(NoEscape(r'\chapter{Domestic Sectors}'))
doc.append(NewPage())

doc.append(NoEscape(r'\begin{landscape}'))
#Section 5.1
with doc.create(Section('Pension Funds')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/chile/#tab_pensionfunds}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn\n'))
    doc.append(NoEscape(r'\scalebox{0.7}{'))#32 columns #8 columns per table > 4 tables
    with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r|r|r|r|r|r|r')) as table:
        table.add_row("Date","Alameda","Aporta","Aporta Fomenta","Armoniza","Banguardia","Bannuestra","Bansander","Capital","Concordia","Cuprum","El Libertador","Fomenta","Futuro","Genera","Habitat")
        table.add_hline()
        for index, row in dfPensionUSD.iterrows():
            table.add_row(row['date'],row['alameda'],row['aporta'],row['aporta fomenta'],row['armoniza'],row['banguardia'],row['bannuestra'],row['bansander'],row['capital'],row['concordia'],row['cuprum'],row['el libertador'],row['fomenta'],row['futuro'],row['genera'],row['habitat'])
    doc.append(NoEscape(r'}'))
    doc.append("\n...")
    doc.append(NoEscape(r'\scalebox{0.7}{'))
    with doc.create(Tabular('r|r|r|r|r|r|r|r|r|r|r|r|r|r|r|r')) as table:
        table.add_row("Invierta","Laboral","Magister","Modelo","Norprevision","Planvital","Previpan","Proteccion","Provida","Qualitas","San Cristobal","Santa Maria","Summa","Summa Bansander","Union","Valora")
        table.add_hline()
        for index, row in dfPensionUSD.iterrows():
            table.add_row(row['invierta'],row['laboral'],row['magister'],row['modelo'],row['norprevision'],row['planvital'],row['previpan'],row['proteccion'],row['provida'],row['qualitas'],row['san cristobal'],row['santa maria'],row['summa'],row['summa bansander'],row['union'],row['valora'])
    doc.append(NoEscape(r'}'))
  

    doc.append(bold('\n\nCLP bn\n'))
    doc.append(NoEscape(r'\scalebox{0.7}{'))#32 columns #8 columns per table > 4 tables
    with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r|r|r|r|r|r|r')) as table:
        table.add_row("Date","Alameda","Aporta","Aporta Fomenta","Armoniza","Banguardia","Bannuestra","Bansander","Capital","Concordia","Cuprum","El Libertador","Fomenta","Futuro","Genera","Habitat")
        table.add_hline()
        for index, row in dfPensionCLP.iterrows():
            table.add_row(row['date'],row['alameda'],row['aporta'],row['aporta fomenta'],row['armoniza'],row['banguardia'],row['bannuestra'],row['bansander'],row['capital'],row['concordia'],row['cuprum'],row['el libertador'],row['fomenta'],row['futuro'],row['genera'],row['habitat'])
    doc.append(NoEscape(r'}'))
    doc.append("\n...")
    doc.append(NoEscape(r'\scalebox{0.7}{'))
    with doc.create(Tabular('r|r|r|r|r|r|r|r|r|r|r|r|r|r|r|r')) as table:
        table.add_row("Invierta","Laboral","Magister","Modelo","Norprevision","Planvital","Previpan","Proteccion","Provida","Qualitas","San Cristobal","Santa Maria","Summa","Summa Bansander","Union","Valora")
        table.add_hline()
        for index, row in dfPensionCLP.iterrows():
            table.add_row(row['invierta'],row['laboral'],row['magister'],row['modelo'],row['norprevision'],row['planvital'],row['previpan'],row['proteccion'],row['provida'],row['qualitas'],row['san cristobal'],row['santa maria'],row['summa'],row['summa bansander'],row['union'],row['valora'])
    doc.append(NoEscape(r'}'))
  


#Section 5.2    
with doc.create(Section('Banks')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/chile/#tab_banks}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn\n'))
    doc.append(NoEscape(r'\scalebox{0.7}{'))
    with doc.create(Tabular('l|r|r|r|r|r|r')) as table:
        table.add_row('Date','Central Bank Reservers','Domestic Credit','Promissory Notes Owed To Secondary Market','General Government','Other Financial Institutions','Private Sector')
        table.add_hline()
        for index, row in dfBankUSD.iterrows():
            table.add_row(row['date'],row['credito interno, banco central, reservas monetarias'], row['domestic credit, cbch, other'],row['domestic credit, cbch, promissory notes owed to secondary market'],row['domestic credit, general government'],row['domestic credit, other financial institutions'],row['domestic credit, private sector'])
    doc.append(NoEscape(r'}'))
    doc.append("\n...")
    doc.append(NoEscape(r'\scalebox{0.7}{'))
    with doc.create(Tabular('r|r')) as table:
        table.add_row('Long-Term Net External Position','Short-Term Net External Position')
        table.add_hline()
        for index, row in dfBankUSD.iterrows():
            table.add_row(row['long-term net external position'],row['short-term net external position'])
    doc.append(NoEscape(r'}'))


    doc.append(bold('\n\nCLP bn\n'))
    doc.append(NoEscape(r'\scalebox{0.7}{'))
    with doc.create(Tabular('l|r|r|r|r|r|r')) as table:
        table.add_row('Date','Central Bank Reservers','Domestic Credit','Promissory Notes Owed To Secondary Market','General Government','Other Financial Institutions','Private Sector')
        table.add_hline()
        for index, row in dfBankCLP.iterrows():
            table.add_row(row['date'],row['credito interno, banco central, reservas monetarias'], row['domestic credit, cbch, other'],row['domestic credit, cbch, promissory notes owed to secondary market'],row['domestic credit, general government'],row['domestic credit, other financial institutions'],row['domestic credit, private sector'])
    doc.append(NoEscape(r'}'))
    doc.append("\n...")
    doc.append(NoEscape(r'\scalebox{0.7}{'))
    with doc.create(Tabular('r|r')) as table:
        table.add_row('Long-Term Net External Position','Short-Term Net External Position')
        table.add_hline()
        for index, row in dfBankCLP.iterrows():
            table.add_row(row['long-term net external position'],row['short-term net external position'])
    doc.append(NoEscape(r'}'))

#Section 5.3
doc.append(NewPage())    
with doc.create(Section('Mutual Funds')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/chile/#tab_mutualfunds}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('Percent (%)\n'))
    doc.append(NoEscape(r'\scalebox{0.8}{'))
    with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table:
        table.add_row('Date','Shares and Stocks','Bank Bonds','Corporate Bonds','State Bonds','Mutual Funds','Department of Finance','Other Capitalization','Payments Issued by States')
        table.add_hline()
        for index, row in dfMutPer.iterrows():
            table.add_row(row['date'],row['acciones y derechos preferentes desuscripcion de acciones'],row['bonos bancos e inst. financieras'],row['bonos de empresas y sociedades securitizadoras'],row['bonos emitidos por estados y bcos. centrales'],row['cuotas de fondos mutuos'],row['dep. yo pag. bcos. e inst. fin.'],row['otros titulos de capitalizacion'],row['pagares emitidos por estados y bcos.centrales'])
    doc.append(NoEscape(r'}'))
#5.4
with doc.create(Section('Insurance Companies')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/chile/#tab_insurancecompanies}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn\n'))
    doc.append(NoEscape(r'\scalebox{0.7}{'))
    with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r')) as table:
        table.add_row('Date','Non-Current Assets','Insurance Accounts','Debtors','Secured Debtors','Debtors For Reinsurance','Financial Investments','Real Estate','Investments','Other Assets')
        table.add_hline()
        for index, row in dfInsurUSD.iterrows():
            table.add_row(row['date'],row['activos nocorrientesmantenidosparalaventa/non-current assets held for sale'],row['cuentasde seguros/insurance accounts'],row['debtors'],row['deudoresporprimasasegurados/secured debtors'],row['deudoresporreaseguros/debtors for reinsurance'],row['inversiones financieras/financial investments'],row['inversiones inmobiliarias/real estate investments'],row['inversiones/investments'],row['otros activos/other assets'])
    doc.append(NoEscape(r'}'))

    doc.append(NewPage())
    doc.append(bold('\nCLP bn\n'))
    doc.append(NoEscape(r'\scalebox{0.7}{'))
    with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r')) as table:
        table.add_row('Date','Non-Current Assets','Insurance Accounts','Debtors','Secured Debtors','Debtors For Reinsurance','Financial Investments','Real Estate','Investments','Other Assets')
        table.add_hline()
        for index, row in dfInsurCLP.iterrows():
            table.add_row(row['date'],row['activos nocorrientesmantenidosparalaventa/non-current assets held for sale'],row['cuentasde seguros/insurance accounts'],row['debtors'],row['deudoresporprimasasegurados/secured debtors'],row['deudoresporreaseguros/debtors for reinsurance'],row['inversiones financieras/financial investments'],row['inversiones inmobiliarias/real estate investments'],row['inversiones/investments'],row['otros activos/other assets'])
    doc.append(NoEscape(r'}'))

doc.append(NoEscape(r'\end{landscape}'))

doc.generate_pdf('Chile', clean=True)

#doc.generate_pdf('Chile',compiler='pdflatex', clean=True, clean_tex=True)