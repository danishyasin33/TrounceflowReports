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

#getting data for the tables
# dfUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-currency-in-argentina-chart.csv')
# dfARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-currency-in-argentina-chart-in-argentine-peso.csv')
# dfCurUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/public-debt-by-currency-in-argentina-chart.csv')
# dfCurARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/public-debt-by-currency-in-argentina-chart-in-argentine-peso.csv')
# dfLegUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/debt-by-legislation-in-argentina-chart.csv')
# dfLegARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/debt-by-legislation-in-argentina-chart-in-argentine-peso.csv')
# dfResUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-residency-of-holders-in-argentina-chart.csv')
# dfResARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-residency-of-holders-in-argentina-chart-in-argentine-peso.csv')
# dfExtCurUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-currency-in-argentina-chart.csv')
# dfExtCurARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-currency-in-argentina-chart-in-argentine-peso.csv')
# dfExtSecUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-sector-in-argentina-chart.csv')
# dfExtSecARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-sector-in-argentina-chart-in-argentine-peso.csv')
# dfPortUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-portfolio-position-in-argentina-chart.csv')
# dfPortARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-portfolio-position-in-argentina-chart-in-argentine-peso.csv')
# dfIIPUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-investment-position-in-argentina-chart.csv')
# dfIIPARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-investment-position-in-argentina-chart-in-argentine-peso.csv')
# #dfBopUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/current-account-in-argentina-chart.csv')
# #dfBopARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/current-account-in-argentina-chart-in-argentine-peso.csv')
# dfFXUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/imf-fx-reserves-in-argentina-chart.csv')
# dfFXARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/imf-fx-reserves-in-argentina-chart-in-argentine-peso.csv')
# dfPensionUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-em-pension-funds-in-argentina-chart.csv')
# dfPensionARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-em-pension-funds-in-argentina-chart-in-argentine-peso.csv')
# dfInsurUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-insurance-companies-in-argentina-chart.csv')
# dfInsurARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-insurance-companies-in-argentina-chart-in-argentine-peso.csv')
# dfBankUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-banks-in-argentina-chart.csv')
# dfBankARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-banks-in-argentina-chart-in-argentine-peso.csv')
dfMenHolUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/mendoza-total-debt-by-category-of-holder-in-argentina-chart.csv')
dfMenHolARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/mendoza-total-debt-by-category-of-holder-in-argentina-chart-in-argentine-peso.csv')
dfMenCurUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/mendoza-total-debt-by-currency-of-denomination-in-argentina-chart.csv')
dfMenCurARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/mendoza-total-debt-by-currency-of-denomination-in-argentina-chart-in-argentine-peso.csv')
dfMenMatUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/mendoza-total-debt-by-years-to-maturity-in-argentina-chart.csv')
dfMenMatARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/mendoza-total-debt-by-years-to-maturity-in-argentina-chart-in-argentine-peso.csv')


doc = Document(documentclass='report', document_options=['11pt, notitlepage'])

doc.preamble.append(NoEscape(r'\usepackage{appendix}'))
doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
doc.preamble.append(NoEscape(r'\usepackage{pdflscape}'))
doc.preamble.append(NoEscape(r'\usepackage[margin=1in]{geometry}'))
doc.preamble.append(NoEscape(r'\usepackage{hyperref}'))
doc.preamble.append(NoEscape(r'\hypersetup{colorlinks=true, linkcolor=blue, filecolor=magenta, urlcolor=cyan}'))
doc.preamble.append(NoEscape(r'\urlstyle{same}'))

doc.preamble.append(NoEscape(r'\linespread{1.6}'))

doc.preamble.append(Command('title','Trounceflow Countries: Argentina'))
doc.preamble.append(Command('author', 'Michael Trounce'))
doc.preamble.append(Command('date', NoEscape(r'\today')))
doc.append(NoEscape(r'\maketitle'))

doc.append(NoEscape(r'\begin{abstract}'))
doc.append("The 'Trounceflow Countries' series of 'living' documents provide real-time dynamic summaries of macroeconomic data relevant to the flows-and-positions analysis of emerging market debt. These macroeconomic data concentrate on the structure of the government bond market but also include other useful but hard-to-wrangle data such as the structure of the local institutional investor base. The data is obtained from the Trounceflow App (trounceflow.com) and the document data is automatically updated in line with the automatic updates on the App; links to the underlying national sources are also given in the 'living' documents.")
doc.append(NoEscape(r'\end{abstract}'))
doc.append(NewPage())

doc.append(NoEscape(r'\tableofcontents'))
doc.append(NewPage())
#chapter 4
doc.append(NoEscape(r'\chapter{Other Government Debt}'))
doc.append(NewPage())

doc.append(NoEscape(r'\begin{landscape}'))

#section 4.1 no info
with doc.create(Section('Mendoza')):
    doc.append('Argentina is a federal country divided into 23 States (Provincias) and one autonomous city (Buenos Aires). Subnational governments in Argentina are playing a major role in the ﬁnancing and implementation of public policies. Being one of the most decentralized country on the South American continent, Argentina has made its provinces a key level for services delivery, and the share of subnational level to general government spendings is still growing.')
    #section 4.1.1
    with doc.create(Subsection('Mendoza government debt by category of holder')):
        doc.append(NoEscape(r"\href{http://www.hacienda.mendoza.gov.ar/deudapublica/#titulos-publicos}{View the data }"))
        doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/argentina/#tab_mendozagovdebtbyholdersector}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')
        
        doc.append(bold('USD bn\n'))
     
        doc.append(NoEscape(r'\scalebox{0.7}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Bondholders', 'Federal Government','Multilateral Organizations','National Bank of Argentina','National and International Banks','Total')
            table.add_hline()
            for index, row in dfMenHolUSD.iterrows():
                table.add_row(row['date'], row['bondholders'], row['federal government'], row['multilateral organizations'], row['national and international banks'], row['national bank of argentina'], row['Total'])
        doc.append(NoEscape(r'}'))
        doc.append(bold('\n\nARS bn\n'))
        doc.append(NoEscape(r'\scalebox{0.7}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Bondholders', 'Federal Government','Multilateral Organizations','National Bank of Argentina','National and International Banks','Total')
            table.add_hline()
            for index, row in dfMenHolARS.iterrows():
                table.add_row(row['date'], row['bondholders'], row['federal government'], row['multilateral organizations'], row['national and international banks'], row['national bank of argentina'], row['Total'])
        doc.append(NoEscape(r'}'))
            
    doc.append(NoEscape(r'\end{landscape}'))
    doc.append(NewPage())
    #section 4.1.2
    with doc.create(Subsection('Mendoza government debt by currency')):
        doc.append(NoEscape(r"\href{http://www.hacienda.mendoza.gov.ar/deudapublica/#titulos-publicos}{View the data }"))
        doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/argentina/#tab_bycurrency}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values for the normal situation (paid) debt are as follows:\n')

        doc.append(bold('USD bn\n'))
        with doc.create(Tabular('l|r|r|r')) as table:
            table.add_row(('Date', 'Pesos', 'USD','Total'))
            table.add_hline()
            for index, row in dfMenCurUSD.iterrows():
                table.add_row(row['date'],row['pesos'], row['usd'],row['Total'])

        doc.append(bold('\n\nARS bn\n'))
        with doc.create(Tabular('l|r|r|r')) as table:
            table.add_row(('Date', 'Pesos', 'USD','Total'))
            table.add_hline()
            for index, row in dfMenCurARS.iterrows():
                table.add_row(row['date'],row['pesos'], row['usd'],row['Total'])
    #Section 4.1.3
    with doc.create(Subsection('Mendoza government debt by maturity')):
        doc.append(NoEscape(r"\href{http://www.hacienda.mendoza.gov.ar/deudapublica/#titulos-publicos}{View the data }"))
        doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/argentina/#tab_bycurrency}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values for the normal situation (paid) debt are as follows:\n')

        doc.append(bold('USD bn\n'))
        with doc.create(Tabular('l|r|r|r|r|r|r')) as table:
            table.add_row(('Date', 'Up to 1 Year', '1-2 Years','2-3 Years','3-4 Years','4-5 Years','5+ Years'))
            table.add_hline()
            for index, row in dfMenMatUSD.iterrows():
                table.add_row(row['date'],row['up to 1 year'], row['1-2 years'],row['2-3 years'], row['3-4 years'], row['4-5 years'], row['5+years'])
        
        doc.append(NewPage())
        doc.append(bold('ARS bn\n'))
        with doc.create(Tabular('l|r|r|r|r|r|r')) as table:
            table.add_row(('Date', 'Up to 1 Year', '1-2 Years','2-3 Years','3-4 Years','4-5 Years','5+ Years'))
            table.add_hline()
            for index, row in dfMenMatARS.iterrows():
                table.add_row(row['date'],row['up to 1 year'], row['1-2 years'],row['2-3 years'], row['3-4 years'], row['4-5 years'], row['5+years'])

doc.generate_pdf('Tables_test' ,clean=True)