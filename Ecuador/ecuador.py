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
dfLegUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/debt-by-legislation-in-ecuador-chart.csv')
#Public Debt
dfGrossByIssuerUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/public-debt-stock-by-issuer-in-ecuador-chart.csv')
dfGrossByInstrUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/public-debt-stock-in-ecuador-chart.csv')
dfGrossByCurUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/public-debt-stock-by-currencies-in-ecuador-chart.csv')
dfGrossByHoldResUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/public-debt-stock-by-residency-of-holders-in-ecuador-chart.csv')
dfGrossByDebttoGDP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/prototypechart/prototype-chart-id-1767-in-none.csv')
dfGrossByIntRate = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/public-debt-stock-by-type-of-interest-rate-in-ecuador-chart.csv')

dfConByIssuerUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/consolidated-public-debt-stock-by-issuer-in-ecuador-chart.csv')
dfConByInstrUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/consolidated-public-debt-stock-in-ecuador-chart.csv')
dfConByCurUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/consolidated-public-debt-stock-by-currencies-in-ecuador-chart.csv')
dfConByHoldResUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/consolidated-public-debt-stock-by-residency-of-holders-in-ecuador-chart.csv')
dfConByDebttoGDP = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/prototypechart/prototype-chart-id-1769-in-none.csv')


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
dfResUSDMar = dfLegUSD.loc[dfLegUSD['date'] == marDate] 
#3
#3.1
dfGrByIssuerUSDMar = dfGrossByIssuerUSD.loc[dfGrossByIssuerUSD['date'] == marDate]
dfGrByInstrUSDMar = dfGrossByInstrUSD.loc[dfGrossByInstrUSD['date'] == marDate]
dfGrByCurUSDMar = dfGrossByCurUSD.loc[dfGrossByCurUSD['date'] == marDate]
dfGrByHoldResUSDMar = dfGrossByHoldResUSD.loc[dfGrossByHoldResUSD['date'] == marDate] 
dfGrByIntrUSDMar = dfGrossByIntRate.loc[dfGrossByIntRate['date'] == marDate]
#dfGrByHoldResUSDMar = dfGrossByHoldResUSD.loc[dfGrossByHoldResUSD['date'] == marDate]
#3.2
dfCoByIssuerUSDMar = dfConByIssuerUSD.loc[dfConByIssuerUSD['date'] == marDate]
dfCoByInstrUSDMar = dfConByInstrUSD.loc[dfConByInstrUSD['date'] == marDate]
dfCoByCurUSDMar = dfConByCurUSD.loc[dfConByCurUSD['date'] == marDate]
dfCoByHoldResUSDMar = dfConByHoldResUSD.loc[dfConByHoldResUSD['date'] == marDate] 
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
        table.add_row('Mar 2019','By Legal Jurisdiction',dfResUSDMar['Total'].values[0])
#1.2
with doc.create(Section('Other Public Debt')):
    #1.2.1
    with doc.create(Subsection('Gross Debt')):
        with doc.create(Tabular('l|l|r')) as table:
            table.add_row(('Date', 'Type', 'USD bn (Total)'))
            table.add_hline()
            table.add_row(MultiRow(5,data='Mar 2019'),'By Issuer',dfGrByIssuerUSDMar['Total'].values[0])
            table.add_row('','By Instrument',dfGrByInstrUSDMar['Total'].values[0])
            table.add_row('','By Currency',dfGrByCurUSDMar['Total'].values[0])
            table.add_row('','By Residency',dfGrByHoldResUSDMar['Total'].values[0])
            table.add_row('','By Interest',dfGrByIntrUSDMar['Total'].values[0])
    #1.2.2
    with doc.create(Subsection('Consolidated Debt')):
        with doc.create(Tabular('l|l|r')) as table:
            table.add_row(('Date', 'Type', 'USD bn (Total)'))
            table.add_hline()
            table.add_row(MultiRow(4,data='Mar 2019'),'By Issuer',dfCoByIssuerUSDMar['Total'].values[0])
            table.add_row('','By Instrument',dfCoByInstrUSDMar['Total'].values[0])
            table.add_row('','By Currency',dfCoByCurUSDMar['Total'].values[0])
            table.add_row('','By Residency',dfCoByHoldResUSDMar['Total'].values[0])
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
with doc.create(Section('By Legal Jurisdiction')):
    # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
    # doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_govtbylegislation}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Gross debt of the central administration (excluding eligible debt restructuring pending):\n')

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r')) as table:
        table.add_row(('Date', 'International Law', 'Local Law','Total'))
        table.add_hline()
        for index, row in dfLegUSD.iterrows():
            table.add_row(row['date'],row['international law'], row['local law'],row['Total'])

#Chapter 3
doc.append(NoEscape(r'\chapter{Other Public Debt}'))
doc.append(NewPage())


doc.append(NoEscape(r'\begin{landscape}'))
#3.1
with doc.create(Section('Gross Debt')):
#3.1.1
    with doc.create(Subsection('By Issuer')):
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_grossbyissuer}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        
        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r|r|r')) as table:
            table.add_row(('Date', 'Public External Debt','Public Internal Debt', 'Petro Ecuador','Consejos Prov.','BCE','BEDE','BEV','BNF','CFN','EMETEL','Others'))
            table.add_hline()
            for index, row in dfGrossByIssuerUSD.iterrows():
                table.add_row(row['date'],row['government - external debt'],row['government - internal debt'], row['petroecuador'],row['mun. y consejos prov.'],row['bce'],row['bede'],row['bev'],row['bnf'],row['cfn'],row['emetel'],row['others'])
        doc.append(NoEscape(r'}'))
#3.1.2
    with doc.create(Subsection('By Instrument')):
        # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_grossbyinstrument}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')

        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r')) as table:
            table.add_row(('Date','Agd Bonds','Bancos Y Bonos Originales','BID','BIRF','Bonos Soberanos 2019 - 2029','Brady Bonds','CAF','CFN Bonds','Global Bonds'))
            table.add_hline()
            for index, row in dfGrossByInstrUSD.iterrows():
                table.add_row(row['date'],row['agd bonds'],row['bancos y bonos originales'],row['bid'],row['birf'],row['bonos soberanos 2019 - 2029'],row['brady bonds'],row['caf'],row['cfn bonds'],row['global bonds'])
        doc.append(NoEscape(r'}'))
        doc.append('\n...')
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('r|r|r|r|r|r|r|r|r')) as table:
            table.add_row(('Certificate Of Treasury','Club De Paris','FIDA','Filanbanco Bonds','FLAR','FMI','Gobiernos Originales','Long Term Bonds','Petroamazon Bonds'))
            table.add_hline()
            for index, row in dfGrossByInstrUSD.iterrows():
                table.add_row(row['certificate of treasury'],row['club de paris'],row['fida'],row['filanbanco bonds'],row['flar'],row['fmi'],row['gobiernos originales'],row['long term bonds'],row['petroamazon bonds'])
        doc.append(NoEscape(r'}'))
        doc.append('\n...')
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('r|r|r|r|r|r')) as table:
            table.add_row(('Petroamazon Bonds 2','Proveedores','Sovereign Bonds 2014 - 2024','Sovereign Bonds 2015 - 2020','Sovereign Bonds 2016 - 2022','Sovereign Bonds 2016 - 2026'))
            table.add_hline()
            for index, row in dfGrossByInstrUSD.iterrows():
                table.add_row(row['petroamazon bonds1'],row['proveedores'],row['sovereign bonds 2014 - 2024'],row['sovereign bonds 2015 - 2020'],row['sovereign bonds 2016 - 2022'],row['sovereign bonds 2016 - 2026'])
        doc.append(NoEscape(r'}'))
        doc.append('\n...')
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('r|r|r|r|r')) as table:
            table.add_row(('Sovereign Bonds 2017 - 2023','Sovereign Bonds 2017 - 2027 (Jun)','Sovereign Bonds 2017 - 2027 (Oct)','Sovereign Bonds 2018 - 2028','State Entities'))
            table.add_hline()
            for index, row in dfGrossByInstrUSD.iterrows():
                table.add_row(row['sovereign bonds 2017 - 2023'],row['sovereign bonds 2017 - 2027 (jun)'],row['sovereign bonds 2017 - 2027 (oct)'],row['sovereign bonds 2018 - 2028'],row['state entities'])
        doc.append(NoEscape(r'}'))
       

#3.1.3
    with doc.create(Subsection('By Currency')):
        # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_grossbycurrency}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')

        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r|r|r|r|r')) as table:
            table.add_row(('Date','USD','EUR','JPY','SDR','GBP','CAD','KRW','CNY','CHF','DKK','Currency Basket (BID)','SUCRE (Ecuador)','Other Currencies'))
            table.add_hline()
            for index, row in dfGrossByCurUSD.iterrows():
                table.add_row(row['date'],row['usd'],row['eur'],row['jpy'],row['sdr'],row['gbp'],row['cad'],row['krw'],row['cny'],row['chf'],row['dkk'],row['currency basket (bid)'],row['sucre (ecuador)'],row['other currencies'])
        doc.append(NoEscape(r'}'))
#3.1.4
    with doc.create(Subsection('By Residency')):
        # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_grossbyresidency}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')

        doc.append(NewPage())
        doc.append(bold('USD bn\n'))
        with doc.create(Tabular('l|r|r|r')) as table:
            table.add_row(('Date', 'Domestic', 'External','Total'))
            table.add_hline()
            for index, row in dfGrossByHoldResUSD.iterrows():
                table.add_row(row['date'],row['domestic creditors'], row['external creditors'],row['Total'])
#3.1.5
    with doc.create(Subsection('By Type of Interest Rate')):
        # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_grossbyrate}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')

        doc.append(bold('USD bn\n'))
        with doc.create(Tabular('l|r|r|r|r')) as table:
            table.add_row(('Date', 'External Debt - Fixed Rates', 'External Debt - Variable Rates','Internal Debt - Fixed Rates', 'Internal Debt - Variable Rates'))
            table.add_hline()
            for index, row in dfGrossByIntRate.iterrows():
                table.add_row(row['date'],row['external debt - fixed rates'], row['external debt - variable rates'],row['internal debt - fixed rates'], row['internal debt - variable rates'])
#3.1.6
    #doc.append(NewPage())
    with doc.create(Subsection('Debt to GDP Ratio')):
        # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_debtgdp}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')

        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.8}{'))
        with doc.create(Tabular('l|r|r|r')) as table:
            table.add_row(('Date', 'External Debt to GDP', 'Internal Debt to GDP','Total Debt to GDP'))
            table.add_hline()
            for index, row in dfGrossByDebttoGDP.iterrows():
                table.add_row(row['date'],row['dueda externa by pib'], row['dueda interna by pib'],row['dueda total by pib'])
        doc.append(NoEscape(r'}'))
#3.2
with doc.create(Section('Consolidated Debt')):
#3.2.1
    with doc.create(Subsection('By Issuer')):
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_conbyissuer}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        
        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r|r|r')) as table:
            table.add_row(('Date', 'Public External Debt','Public Internal Debt', 'Petro Ecuador','Consejos Prov.','BCE','BEDE','BEV','BNF','CFN','EMETEL','Others'))
            table.add_hline()
            for index, row in dfConByIssuerUSD.iterrows():
                table.add_row(row['date'],row['government - external debt'],row['government - internal debt'], row['petroecuador'],row['mun. y consejos prov.'],row['bce'],row['bede'],row['bev'],row['bnf'],row['cfn'],row['emetel'],row['others'])
        doc.append(NoEscape(r'}'))
#3.2.2
    with doc.create(Subsection('By Instrument')):
        # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_conbyinstrument}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')

        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r')) as table:
            table.add_row(('Date','Bancos Y Bonos Originales','BID','BIRF','Bonos PetroAmazonas','Brady Bonds','CAF','Cetes Sector Privado','Club De Paris','FIDA'))
            table.add_hline()
            for index, row in dfConByInstrUSD.iterrows():
                table.add_row(row['date'],row['bancos y bonos originales'],row['bid'],row['birf'],row['bonos petroamazonas1'],row['brady bonds'],row['caf'],row['cetes sector privado'],row['club de paris'],row['fida'])
        doc.append(NoEscape(r'}'))
        doc.append('\n...')
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('r|r|r|r|r|r|r|r')) as table:
            table.add_row(('Filanbanco Bonds','FLAR','FMI','Global Bonds','Gobiernos Originales','Petroamazon Bonds','Private AGD Bonds','Proveedores'))
            table.add_hline()
            for index, row in dfConByInstrUSD.iterrows():
                table.add_row(row['filanbanco bonds'],row['flar'],row['fmi'],row['global bonds'],row['gobiernos originales'],row['petroamazon bonds'],row['private sector agd bonds'],row['proveedores'])
        doc.append(NoEscape(r'}'))
       
        doc.append('\n...')
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('r|r|r|r|r')) as table:
            table.add_row(('Sovereign Bonds 2014','Sovereign Bonds 2017 - 2027 (Jun)','Sovereign Bonds 2017 - 2027 (Oct)', 'Sovereign Bonds 2018 - 2028','Sovereign Bonds 2019 - 2029'))
            table.add_hline()
            for index, row in dfConByInstrUSD.iterrows():
                table.add_row(row['sovereign bonds 2014'],row['sovereign bonds 2017 0 2027 (jun)'],row['sovereign bonds 2017 0 2027 (oct)'],row['sovereign bonds 2018 0 2028'],row['sovereign bonds 2019 0 2029'])
        doc.append(NoEscape(r'}'))
        doc.append('\n...')
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('r|r|r|r|r')) as table:
            table.add_row(('Sovereign Bonds 2020','Sovereign Bonds 2022','Sovereign Bonds 2023 - 2027','Sovereign Bonds 2026','Tenedor Primary Privado'))
            table.add_hline()
            for index, row in dfConByInstrUSD.iterrows():
                table.add_row(row['sovereign bonds 2020'],row['sovereign bonds 2022'],row['sovereign bonds 2023 / 2027'],row['sovereign bonds 2026'],row['tenedor primaro privado'])
        doc.append(NoEscape(r'}'))

#3.2.3
    with doc.create(Subsection('By Currency')):
        # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_conbycurrency}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')

        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r|r|r|r|r')) as table:
            table.add_row(('Date','USD','EUR','JPY','SDR','GBP','CAD','KRW','CNY','CHF','DKK','Currency Basket (BID)','SUCRE (Ecuador)','Other Currencies'))
            table.add_hline()
            for index, row in dfConByCurUSD.iterrows():
                table.add_row(row['date'],row['usd'],row['eur'],row['jpy'],row['sdr'],row['gbp'],row['cad'],row['krw'],row['cny'],row['chf'],row['dkk'],row['currency basket (bid)'],row['sucre (ecuador)'],row['other currencies'])
        doc.append(NoEscape(r'}'))
#3.2.4
    doc.append(NewPage())
    with doc.create(Subsection('By Residency')):
        # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_conbyresidency}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')

        doc.append(bold('USD bn\n'))
        with doc.create(Tabular('l|r|r|r')) as table:
            table.add_row(('Date', 'Domestic', 'External','Total'))
            table.add_hline()
            for index, row in dfConByHoldResUSD.iterrows():
                table.add_row(row['date'],row['domestic creditors'], row['external creditors'],row['Total'])
#3.2.5
    with doc.create(Subsection('Debt to GDP Ratio')):
        # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/ecuador/#tab_condebtgdp}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        
        #doc.append(NewPage())
        doc.append(bold('USD bn\n'))
        with doc.create(Tabular('l|r|r|r')) as table:
            table.add_row(('Date', 'External Debt to GDP', 'Internal Debt to GDP','Total Debt to GDP'))
            table.add_hline()
            for index, row in dfConByDebttoGDP.iterrows():
                table.add_row(row['date'],row['deuda externa by pib'], row['deuda interna by pib'],row['deuda total by pib'])

doc.append(NoEscape(r'\end{landscape}'))

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