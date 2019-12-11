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
dfResUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-residency-of-holders-in-brazil-chart.csv')
dfResRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-residency-of-holders-in-brazil-chart-in-brazilian-real.csv')
dfByMatUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-by-maturity-in-brazil-chart.csv')
dfByMatRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-by-maturity-in-brazil-chart-in-brazilian-real.csv')
dfByStockUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-in-brazil-chart.csv')
dfByStockRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-in-brazil-chart-in-brazilian-real.csv')

#other public Debt
dfCenBankPorUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/public-debt-in-central-bank-portfolio-in-brazil-chart.csv')
dfCenBankPorRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/public-debt-in-central-bank-portfolio-in-brazil-chart-in-brazilian-real.csv')
    #held by public
dfUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/public-debt-by-currency-in-brazil-chart.csv')
dfRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/public-debt-by-currency-in-brazil-chart-in-brazilian-real.csv')
dfPubMatUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/public-debt-by-maturity-in-brazil-chart.csv')
dfPubMatRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/public-debt-by-maturity-in-brazil-chart-in-brazilian-real.csv')
    #local currency
dflocByInsUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/composition-of-outstanding-local-currency-sovereign-bonds-by-type-of-instrument-in-brazil-chart.csv')
dflocByInsRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/composition-of-outstanding-local-currency-sovereign-bonds-by-type-of-instrument-in-brazil-chart-in-brazilian-real.csv')

dflocBySecUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/composition-of-holdings-in-brazil-chart.csv')
dflocBySecRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/composition-of-holdings-in-brazil-chart-in-brazilian-real.csv')

dflocByLFTUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/lft-holders-in-brazil-chart.csv')
dflocByLFTRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/lft-holders-in-brazil-chart-in-brazilian-real.csv')

dflocByLTNUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/ltn-holders-in-brazil-chart.csv')
dflocByLTNRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/ltn-holders-in-brazil-chart-in-brazilian-real.csv')

dflocByNTNUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/ntn-b-holders-in-brazil-chart.csv')
dflocByNTNRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/ntn-b-holders-in-brazil-chart-in-brazilian-real.csv')

#Flows
    #total stock
dfForHolStBRL = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/foreign-holdings-in-brazil-chart-in-brazilian-real.csv')
dfForHolFlBRL = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingsflowchart/foreign-holdings-flow-in-brazil-chart-in-brazilian-real.csv')
dfForHolStUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/foreign-holdings-in-brazil-chart.csv')
    #by instrument
dfByInstruStBRL = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/composition-of-foreign-holders-by-type-of-instrument-in-brazil-chart-in-brazilian-real.csv')
dfByInstruFlBRL = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingsflowchart/composition-of-foreign-holders-by-type-of-instrument-flow-in-brazil-chart-in-brazilian-real.csv')
dfByInstruStUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/composition-of-foreign-holders-by-type-of-instrument-in-brazil-chart.csv')
#Equities
dfEquPortFlUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/equity-portfolio-flow-in-brazil-chart.csv')
dfEquPortFlBRL = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/equity-portfolio-flow-in-brazil-chart-in-brazilian-real.csv')

#External Sector
dfFXUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/imf-fx-reserves-in-brazil-chart.csv')
dfFXRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/imf-fx-reserves-in-brazil-chart-in-brazilian-real.csv')
dfExtDebtByMatUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-maturity-in-brazil-chart.csv')
dfExtDebtByMatRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-maturity-in-brazil-chart-in-brazilian-real.csv')
dfExtCurUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-currency-in-brazil-chart.csv')
dfExtCurRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-currency-in-brazil-chart-in-brazilian-real.csv')
dfIIPUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-investment-position-in-brazil-chart.csv')
dfIIPRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-investment-position-in-brazil-chart-in-brazilian-real.csv')
dfPortUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-portfolio-position-in-brazil-chart.csv')
dfPortRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-portfolio-position-in-brazil-chart-in-brazilian-real.csv')

#Domestic Sector
dfPensionUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-em-pension-funds-in-brazil-chart.csv')
dfPensionRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-em-pension-funds-in-brazil-chart-in-brazilian-real.csv')

dfBankUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-banks-in-brazil-chart.csv')
dfBankRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-banks-in-brazil-chart-in-brazilian-real.csv')

dfInvFuFlUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/fund-flows-to-local-investment-funds-in-brazil-chart.csv')
dfInvFuFlRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/fund-flows-to-local-investment-funds-in-brazil-chart-in-brazilian-real.csv')

dfInvAUMUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/aum-of-local-investment-funds-in-brazil-chart.csv')
dfInvAUMRD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/aum-of-local-investment-funds-in-brazil-chart-in-brazilian-real.csv')

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
doc.preamble.append(Command('title','Trounceflow Countries: Brazil'))
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
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_cggd-residency}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Gross debt of the central administration (excluding eligible debt restructuring pending):\n')

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfResUSD.iterrows():
            table.add_row(row['date'],row['domestic creditors'], row['external creditors'],row['Total'])

    doc.append(bold('\n\nBRL bn\n'))
    with doc.create(Tabular('l|r|r|r')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfResRD.iterrows():
            table.add_row(row['date'],row['domestic creditors'], row['external creditors'],row['Total'])
#2.2
with doc.create(Section('By Maturity[Short-term; Long-term]')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_cggd-maturity}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(bold('USD bn\n'))
        with doc.create(Tabular('l|r|r')) as table:
            table.add_row('Date', 'Short-Term', 'Long-Term')
            table.add_hline()
            for index, row in dfByMatUSD.iterrows():
                table.add_row(row['date'], row['short term'], row['medium or long term'])
        doc.append(NoEscape(r'\begin{landscape}'))
        doc.append(bold('\nBRL bn\n'))
        with doc.create(Tabular('l|r|r')) as table:
            table.add_row('Date', 'Short-Term', 'Long-Term')
            table.add_hline()
            for index, row in dfByMatRD.iterrows():
                table.add_row(row['date'], row['short term'], row['medium or long term'])


with doc.create(Section('By Total Stock')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_cggd-stock}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.6}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Non-Res. Long-Term Contrac.', 'Non-Res. Long-Term Sec.','Non-Res. Short-Term Contrac.','Non-Res. Short-Term Sec.','Res. Long-Term Contrac.','Res. Long-Term Sec.','Res. Short-Term Contrac.','Res. Short-Term Sec.')
            table.add_hline()
            for index, row in dfByStockUSD.iterrows():
                table.add_row(row['date'], row['non-residents - medium or long term contractual'], row['non-residents - medium or long term securities'], row['non-residents - short term contractual'], row['non-residents - short term securities'], row['residents - medium or long term contractual'], row['residents - medium or long term securities'], row['residents - short term contractual'], row['residents - short term securities'])
        doc.append(NoEscape(r'}'))

        doc.append(bold('\nBRL bn\n'))
        doc.append(NoEscape(r'\scalebox{0.6}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Non-Res. Long-Term Contrac.', 'Non-Res. Long-Term Sec.','Non-Res. Short-Term Contrac.','Non-Res. Short-Term Sec.','Res. Long-Term Contrac.','Res. Long-Term Sec.','Res. Short-Term Contrac.','Res. Short-Term Sec.')
            table.add_hline()
            for index, row in dfByStockRD.iterrows():
                table.add_row(row['date'], row['non-residents - medium or long term contractual'], row['non-residents - medium or long term securities'], row['non-residents - short term contractual'], row['non-residents - short term securities'], row['residents - medium or long term contractual'], row['residents - medium or long term securities'], row['residents - short term contractual'], row['residents - short term securities'])
        doc.append(NoEscape(r'}'))
doc.append(NoEscape(r'\end{landscape}'))

#Chapter 3 
doc.append(NoEscape(r'\chapter{Other Public Debt}'))
doc.append(NewPage())
#3.1
with doc.create(Section('In Central Bank')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_fpd-cb}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r|r|r')) as table:
        table.add_row(('Date', 'NTN-F', 'NTN-B','LFT','LTN','Other'))
        table.add_hline()
        for index, row in dfCenBankPorUSD.iterrows():
            table.add_row(row['date'],row['ntn-f'], row['ntn-b'],row['lft'],row['ltn'],row['other'])

    doc.append(bold('\n\nBRL bn\n'))
    with doc.create(Tabular('l|r|r|r|r|r')) as table:
        table.add_row(('Date', 'NTN-F', 'NTN-B','LFT','LTN','Other'))
        table.add_hline()
        for index, row in dfCenBankPorRD.iterrows():
            table.add_row(row['date'],row['ntn-f'], row['ntn-b'],row['lft'],row['ltn'],row['other'])
#3.2
with doc.create(Section('Held by Public')):
    #3.2.1
    with doc.create(Subsection('By Currency')):
            
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_fpd-currency}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(bold('USD bn\n'))
    with doc.create(Tabular('c|c|c|c')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfUSD.iterrows():
            table.add_row(row['date'],row['domestic currency'], row['foreign currency'],row['Total'])

    doc.append(NewPage())
    doc.append(bold('\n\nBRL bn\n'))
    with doc.create(Tabular('c|c|c|c')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfRD.iterrows():
            table.add_row(row['date'],row['domestic currency'], row['foreign currency'],row['Total'])
    #3.2.2
    with doc.create(Subsection('By Maturity')):
                
            doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_fpd-maturity}{View the chart }"))
            doc.append('on trounceﬂow.com and download the data straight from the chart\n')
            doc.append('Recent values are as follows:\n')

            doc.append(bold('USD bn\n'))
            with doc.create(Tabular('l|r|r|r|r|r|r')) as table:
                table.add_row(('Date', 'Up to 1 Year', '1-2 Years','2-3 Years','3-4 Years','4-5 Years','5+ Years'))
                table.add_hline()
                for index, row in dfPubMatUSD.iterrows():
                    table.add_row(row['date'],row['up to 1 year'], row['1-2 years'],row['2-3 years'], row['3-4 years'], row['4-5 years'], row['over 5 years'])
            
            doc.append(bold('\nBRL bn\n'))
            with doc.create(Tabular('l|r|r|r|r|r|r')) as table:
                table.add_row(('Date', 'Up to 1 Year', '1-2 Years','2-3 Years','3-4 Years','4-5 Years','5+ Years'))
                table.add_hline()
                for index, row in dfPubMatRD.iterrows():
                    table.add_row(row['date'],row['up to 1 year'], row['1-2 years'],row['2-3 years'], row['3-4 years'], row['4-5 years'], row['over 5 years'])
    #3.2.3               
    with doc.create(Subsection('Local Currency')):
        #3.2.3.1
        with doc.create(Subsubsection('By Instrument')):
            doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_efpd-instruments}{View the chart }"))
            doc.append('on trounceﬂow.com and download the data straight from the chart\n')
            doc.append('Recent values are as follows:\n')
            
            doc.append(NewPage())
            doc.append(bold('USD bn\n'))
            with doc.create(Tabular('l|r|r|r|r|r')) as table:
                table.add_row(('Date', 'NTN-F', 'NTN-B','LFT','LTN','Other'))
                table.add_hline()
                for index, row in dflocByInsUSD.iterrows():
                    table.add_row(row['date'],row['ntn-f'], row['ntn-b'],row['lft'],row['ltn'],row['others'])

            doc.append(bold('\n\nBRL bn\n'))
            with doc.create(Tabular('l|r|r|r|r|r')) as table:
                table.add_row(('Date', 'NTN-F', 'NTN-B','LFT','LTN','Other'))
                table.add_hline()
                for index, row in dflocByInsRD.iterrows():
                    table.add_row(row['date'],row['ntn-f'], row['ntn-b'],row['lft'],row['ltn'],row['others'])
        #3.2.3.2
        with doc.create(Subsubsection('By Holder Sector')):
            doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_efpd-holders}{View the chart }"))
            doc.append('on trounceﬂow.com and download the data straight from the chart\n')
            doc.append('Recent values are as follows:\n')

            doc.append(bold('USD bn\n'))
            with doc.create(Tabular('l|r|r|r|r|r|r|r')) as table:
                table.add_row(('Date', 'Financial Institutions', 'Funds','Government','Insurance','Non-Residents','Pension','Others'))
                table.add_hline()
                for index, row in dflocBySecUSD.iterrows():
                    table.add_row(row['date'],row['financial institutions'],row['funds'], row['government'],row['insurance'],row['non-residents'],row['pension'],row['others'])

            doc.append(bold('\n\nBRL bn\n'))
            with doc.create(Tabular('l|r|r|r|r|r|r|r')) as table:
                table.add_row(('Date', 'Financial Institutions', 'Funds','Government','Insurance','Non-Residents','Pension','Others'))
                table.add_hline()
                for index, row in dflocBySecRD.iterrows():
                    table.add_row(row['date'],row['financial institutions'],row['funds'], row['government'],row['insurance'],row['non-residents'],row['pension'],row['others'])
        #3.2.3.3
        with doc.create(Subsubsection('By LFT')):
            doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_lft}{View the chart }"))
            doc.append('on trounceﬂow.com and download the data straight from the chart\n')
            doc.append('Recent values are as follows:\n')

            doc.append(bold('USD bn\n'))
            with doc.create(Tabular('l|r|r|r|r|r|r|r')) as table:
                table.add_row(('Date', 'Financial Institutions', 'Funds','Government','Insurance','Non-Residents','Pension','Others'))
                table.add_hline()
                for index, row in dflocByLFTUSD.iterrows():
                    table.add_row(row['date'],row['financial institutions'],row['funds'], row['government'],row['insurance'],row['non-residents'],row['pension'],row['others'])

            doc.append(bold('\n\nBRL bn\n'))
            with doc.create(Tabular('l|r|r|r|r|r|r|r')) as table:
                table.add_row(('Date', 'Financial Institutions', 'Funds','Government','Insurance','Non-Residents','Pension','Others'))
                table.add_hline()
                for index, row in dflocByLFTRD.iterrows():
                    table.add_row(row['date'],row['financial institutions'],row['funds'], row['government'],row['insurance'],row['non-residents'],row['pension'],row['others'])
        #3.2.3.4
        with doc.create(Subsubsection('By LTN')):
            doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_ltn}{View the chart }"))
            doc.append('on trounceﬂow.com and download the data straight from the chart\n')
            doc.append('Recent values are as follows:\n')

            doc.append(bold('USD bn\n'))
            with doc.create(Tabular('l|r|r|r|r|r|r|r')) as table:
                table.add_row(('Date', 'Financial Institutions', 'Funds','Government','Insurance','Non-Residents','Pension','Others'))
                table.add_hline()
                for index, row in dflocByLTNUSD.iterrows():
                    table.add_row(row['date'],row['financial institutions'],row['funds'], row['government'],row['insurance'],row['non-residents'],row['pension'],row['others'])

            doc.append(bold('\n\nBRL bn\n'))
            with doc.create(Tabular('l|r|r|r|r|r|r|r')) as table:
                table.add_row(('Date', 'Financial Institutions', 'Funds','Government','Insurance','Non-Residents','Pension','Others'))
                table.add_hline()
                for index, row in dflocByLTNRD.iterrows():
                    table.add_row(row['date'],row['financial institutions'],row['funds'], row['government'],row['insurance'],row['non-residents'],row['pension'],row['others'])
        #3.2.3.5
        with doc.create(Subsubsection('By NTN-B')):
            doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_ntn-b}{View the chart }"))
            doc.append('on trounceﬂow.com and download the data straight from the chart\n')
            doc.append('Recent values are as follows:\n')

            doc.append(bold('USD bn\n'))
            with doc.create(Tabular('l|r|r|r|r|r|r|r')) as table:
                table.add_row(('Date', 'Financial Institutions', 'Funds','Government','Insurance','Non-Residents','Pension','Others'))
                table.add_hline()
                for index, row in dflocByNTNUSD.iterrows():
                    table.add_row(row['date'],row['financial institutions'],row['funds'], row['government'],row['insurance'],row['non-residents'],row['pension'],row['others'])

            doc.append(bold('\n\nBRL bn\n'))
            with doc.create(Tabular('l|r|r|r|r|r|r|r')) as table:
                table.add_row(('Date', 'Financial Institutions', 'Funds','Government','Insurance','Non-Residents','Pension','Others'))
                table.add_hline()
                for index, row in dflocByNTNRD.iterrows():
                    table.add_row(row['date'],row['financial institutions'],row['funds'], row['government'],row['insurance'],row['non-residents'],row['pension'],row['others'])

#3.3
with doc.create(Section('Flows')):
    #3.3.1
    with doc.create(Subsection('Total Stock')):
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_stockfh}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        #doc.append('Gross debt of the central administration (excluding eligible debt restructuring pending):\n')
        #doc.append(NewPage())

        doc.append(bold('Stock (BRL bn)\n'))
        with doc.create(Tabular('l|r')) as table: 
            table.add_row(('Date', 'Foreign Holdings'))
            table.add_hline()
            for index, row in dfForHolStBRL.iterrows():
                table.add_row(row['date'], row['foreign holdings'])
        doc.append(NewPage())
        doc.append(bold('\nFlow (BRL bn)\n'))
        with doc.create(Tabular('l|r')) as table: 
            table.add_row(('Date', 'Foreign Holdings'))
            table.add_hline()
            for index, row in dfForHolFlBRL.iterrows():
                table.add_row(row['date'], row['foreign holdings'])
        
        doc.append(bold('\n\nStock (USD bn)\n'))
        with doc.create(Tabular('l|r')) as table: 
            table.add_row(('Date', 'Foreign Holdings'))
            table.add_hline()
            for index, row in dfForHolStUSD.iterrows():
                table.add_row(row['date'], row['foreign holdings'])

        # doc.append(bold('\nFlow (USD bn)\n'))
        # with doc.create(Tabular('l|r')) as table: 
        #     table.add_row(('Date', 'Foreign Holdings'))
        #     table.add_hline()
        #     for index, row in dfForHolFlUSD.iterrows():
        #         table.add_row(row['date'], row['foreign holdings'])

    #3.3.2
    with doc.create(Subsection('By Instrument')):
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_instrument}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        #doc.append('Gross debt of the central administration (excluding eligible debt restructuring pending):\n')
        #doc.append(NewPage())

        doc.append(bold('Stock (BRL bn)\n'))
        with doc.create(Tabular('l|r|r|r|r|r')) as table:
            table.add_row(('Date', 'NTN-F', 'NTN-B','LFT','LTN','Other'))
            table.add_hline()
            for index, row in dfByInstruStBRL.iterrows():
                table.add_row(row['date'],row['ntn-f'], row['ntn-b'],row['lft'],row['ltn'],row['others'])
       
        doc.append(bold('\nFlow (BRL bn)\n'))
        with doc.create(Tabular('l|r|r|r|r|r')) as table:
            table.add_row(('Date', 'NTN-F', 'NTN-B','LFT','LTN','Other'))
            table.add_hline()
            for index, row in dfByInstruFlBRL.iterrows():
                table.add_row(row['date'],row['ntn-f'], row['ntn-b'],row['lft'],row['ltn'],row['others'])
        
        doc.append(NewPage())
        doc.append(bold('\n\nStock (USD bn)\n'))
        with doc.create(Tabular('l|r|r|r|r|r')) as table:
            table.add_row(('Date', 'NTN-F', 'NTN-B','LFT','LTN','Other'))
            table.add_hline()
            for index, row in dfByInstruStUSD.iterrows():
                table.add_row(row['date'],row['ntn-f'], row['ntn-b'],row['lft'],row['ltn'],row['others'])
    

        # doc.append(bold('\nFlow (USD bn)\n'))
        # doc.append(NoEscape(r'\scalebox{0.8}{'))
        # with doc.create(Tabular('l|r|r|r|r|r')) as table: 
        #     table.add_row(('Date', 'Foreign Residents (BONDES)','Foreign Residents (UDIBONOS)','Foreign Residents (CETES)','Foreign Residents (BONOS)','Foreign Residents (BONDES D)'))
        #     table.add_hline()
        #     for index, row in dfByInstruFlUSD.iterrows():
        #         table.add_row(row['date'], row['bondes, foreign residents (ii)'], row['udibonos pesos, foreign residents (ii)'], row['cetes, foreign residents (ii)'], row['bonos, foreign residents (ii)'], row['bondes d, foreign residents (ii)'])
        # doc.append(NoEscape(r'}'))

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
            table.add_row(row['date'], row["flow"])

    doc.append(bold('\nBRL bn\n'))
    with doc.create(Tabular('l|r')) as table: 
        table.add_row(('Date', 'Equity Flow'))
        table.add_hline()
        for index, row in dfEquPortFlBRL.iterrows():
                table.add_row(row['date'], row["flow"])


#chapter 4
doc.append(NoEscape(r'\chapter{External Sector}'))
doc.append(NewPage())


doc.append(NoEscape(r'\begin{landscape}'))
#4.1
with doc.create(Section('FX Reserves')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_fxreserves}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')   

    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r|r')) as table:
        table.add_row('Date', 'FX', 'Gold','IMF','SDRS')
        table.add_hline()
        for index, row in dfFXUSD.iterrows():
            table.add_row(row['date'], row['fx'], row['gold'], row['imf'],row['sdrs'])

    doc.append(bold('\nBRL bn\n'))
    with doc.create(Tabular('l|r|r|r|r')) as table:
        table.add_row('Date', 'FX', 'Gold','IMF','SDRS')
        table.add_hline()
        for index, row in dfFXRD.iterrows():
            table.add_row(row['date'], row['fx'], row['gold'], row['imf'],row['sdrs'])
#4.2
with doc.create(Section('External Debt')):
    #4.2.1
    with doc.create(Subsection('By Maturity[Short-term; Long-term]')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_edmaturity}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(NewPage())
        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.7}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Banks (Short)', 'Banks (Long)','Monetary Authorities (Short)','Monetary Authorities (Long)','Central Government (Short)','Central Government (Long)','Others (Short)','Others (Long)','Unclassified')
            table.add_hline()
            for index, row in dfExtDebtByMatUSD.iterrows():
                table.add_row(row['date'], row['banks short-term'], row['banks long-term'], row['monetary authorities short-term'], row['monetary authorities long-term'], row['central government short-term'], row['central government long-term'], row['other sectors short-term'], row['other sectors short-term'], row['unclassified'])
        doc.append(NoEscape(r'}'))

        doc.append(bold('\n\nBRL bn\n'))
        doc.append(NoEscape(r'\scalebox{0.7}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Banks (Short)', 'Banks (Long)','Monetary Authorities (Short)','Monetary Authorities (Long)','Central Government (Short)','Central Government (Long)','Others (Short)','Others (Long)','Unclassified')
            table.add_hline()
            for index, row in dfExtDebtByMatRD.iterrows():
                table.add_row(row['date'], row['banks short-term'], row['banks long-term'], row['monetary authorities short-term'], row['monetary authorities long-term'], row['central government short-term'], row['central government long-term'], row['other sectors short-term'], row['other sectors short-term'], row['unclassified'])
        doc.append(NoEscape(r'}'))
    #4.2.2
    with doc.create(Subsection('By Currency [Domestic, External]')):
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_edcurrency}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(bold('USD bn\n'))
        #doc.append(NoEscape(r'\scalebox{0.8}{'))
        with doc.create(Tabular('l|r|r|r|r|r')) as table:
            table.add_row('Date', 'ARS', 'USD','EUR','Other','Total')
            table.add_hline()
            for index, row in dfExtCurUSD.iterrows():
                table.add_row(row['date'],row['local currency_'], row['usd_'],row['eur_'],row['others_'], row['Total'])
        #doc.append(NoEscape(r'}'))
        doc.append(NewPage())
        doc.append(bold('\n\nBRL bn\n'))
        #doc.append(NoEscape(r'\scalebox{0.8}{'))
        with doc.create(Tabular('l|r|r|r|r|r')) as table:
            table.add_row('Date', 'ARS', 'USD','EUR','Other','Total')
            table.add_hline()
            for index, row in dfExtCurRD.iterrows():
                table.add_row(row['date'],row['local currency_'], row['usd_'],row['eur_'],row['others_'], row['Total'])
        #doc.append(NoEscape(r'}'))
#4.3
with doc.create(Section('International Investment Position')):
    
    #section 4.3.1
    with doc.create(Subsection('Assets & Liabilities')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_iip-al}{View the chart }"))
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
        doc.append(bold('BRL bn\n'))
        doc.append(NoEscape(r'\scalebox{0.6}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Assets-Direct','Assets-Financial Derivatives','Assets-Reserve','Assets-Portfolio','Assets-Other','* IIP','Liabilities-Direct','Liabilities-Financial Derivatives', 'Liabilities-Portfolio','Liabilities-Other')
            table.add_hline()
            for index, row in dfIIPRD.iterrows():
                table.add_row(row['date'],row['assets - direct investment'],row['assets - financial derivatives (except reserves)'], row['assets - reserve assets'], row['assets - portfolio investment'], row['assets - other investment'], row['international investment position'], row['liabilities - direct investment'],row['liabilities - financial derivatives (except reserves)'], row['liabilities - portfolio investment'], row['liabilities - other investment'])
        doc.append(NoEscape(r'}'))
        doc.append('\n\n* International Investment Position')

    #doc.append(NoEscape(r'\end{landscape}'))

    #4.3.2
    #doc.append(NewPage())
    with doc.create(Subsection('Portfolio Liabilities')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_ipp-liabilities}{View the chart }"))
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

        doc.append(bold('\n\nBRL bn\n'))
        doc.append(NoEscape(r'\scalebox{0.9}{'))
        with doc.create(Tabular('l|r|r|r')) as table:
            table.add_row('Date', 'Debt Securities', 'Equity and Investment Fund Shares','Total')
            table.add_hline()
            for index, row in dfPortRD.iterrows():
                table.add_row(row['date'], row['debt securities'], row['equity and investment fund shares'], row['Total'])
        doc.append(NoEscape(r'}'))
doc.append(NoEscape(r'\end{landscape}'))


#chapter 5
doc.append(NoEscape(r'\chapter{Domestic Sectors}'))
doc.append(NewPage())

doc.append(NoEscape(r'\begin{landscape}'))
#Section 5.1
with doc.create(Section('Pension Funds')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_pensionfunds}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn\n'))
    doc.append(NoEscape(r'\scalebox{0.7}{'))
    with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r|r')) as table:
        table.add_row('Date', 'Gov. Bonds', 'Private Loans','SPE','Fixed Income Inv. Funds ','Stocks','Variable Income Inv. Funds','Alternative Investments','Real Estate','Operations with Participants','Others')
        table.add_hline()
        for index, row in dfPensionUSD.iterrows():
            table.add_row(row['date'], row['government bonds'], row['private loans and deposits'], row['spe'],row['fixed income investment funds'], row['stocks'], row['variable income investment funds'],row['alternative investments'],row['real estate'],row['operations with participants'],row['others'])
    doc.append(NoEscape(r'}'))

    doc.append(bold('\n\nBRL bn\n'))
    doc.append(NoEscape(r'\scalebox{0.7}{'))
    with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r|r')) as table:
        table.add_row('Date', 'Gov. Bonds', 'Private Loans','SPE','Fixed Income Inv. Funds ','Stocks','Variable Income Inv. Funds','Alternative Investments','Real Estate','Operations with Participants','Others')
        table.add_hline()
        for index, row in dfPensionRD.iterrows():
            table.add_row(row['date'], row['government bonds'], row['private loans and deposits'], row['spe'],row['fixed income investment funds'], row['stocks'], row['variable income investment funds'],row['alternative investments'],row['real estate'],row['operations with participants'],row['others'])
    doc.append(NoEscape(r'}'))
#Section 5.2    
with doc.create(Section('Banks')):
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_banks}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn\n'))
    doc.append(NoEscape(r'\scalebox{0.8}{'))
    with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r')) as table:
        table.add_row('Date', 'Central Gov.', 'Non-Residents','Financial Corp.','Other Sectors','Private Sector','Public Non-Financial Corp.','Local Gov.','Domestic','Net Foreign Assets')
        table.add_hline()
        for index, row in dfBankUSD.iterrows():
            table.add_row(row['date'], row['claims on central government'], row['claims on non residents'], row['claims on other financial corporations'],row['claims on other sectors'], row['claims on private sector'], row['claims on public non-financial corporations'], row['claims on state and local governments'], row['domestic claims'], row['net foreign assets'])
    doc.append(NoEscape(r'}'))
    
    doc.append(NewPage())
    doc.append(bold('\n\nBRL bn\n'))
    doc.append(NoEscape(r'\scalebox{0.8}{'))
    with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r')) as table:
        table.add_row('Date', 'Central Gov.', 'Non-Residents','Financial Corp.','Other Sectors','Private Sector','Public Non-Financial Corp.','Local Gov.','Domestic','Net Foreign Assets')
        table.add_hline()
        for index, row in dfBankRD.iterrows():
            table.add_row(row['date'], row['claims on central government'], row['claims on non residents'], row['claims on other financial corporations'],row['claims on other sectors'], row['claims on private sector'], row['claims on public non-financial corporations'], row['claims on state and local governments'], row['domestic claims'], row['net foreign assets'])
    doc.append(NoEscape(r'}'))

#Section 5.3
with doc.create(Section('Investment Funds')):
    #5.3.1
    with doc.create(Subsection('Fund Flows')):
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_fund-flows}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.8}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Fixed Income', 'Equity','Multimercados','ETF','Pension Funds', 'Foreign Exchange', 'Private Equity Funds', 'Credit Receivables')
            table.add_hline()
            for index, row in dfInvFuFlUSD.iterrows():
                table.add_row(row['date'], row['fixed income'], row['equity'], row['multimercados'],row['etf'], row['pension funds'], row['foreign exchange'], row['private equity funds (fip)'], row['credit receivables (fidc)'])
        doc.append(NoEscape(r'}'))

        doc.append(bold('\n\nBRL bn\n'))
        doc.append(NoEscape(r'\scalebox{0.8}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Fixed Income', 'Equity','Multimercados','ETF','Pension Funds', 'Foreign Exchange', 'Private Equity Funds', 'Credit Receivables')
            table.add_hline()
            for index, row in dfInvFuFlRD.iterrows():
                table.add_row(row['date'], row['fixed income'], row['equity'], row['multimercados'],row['etf'], row['pension funds'], row['foreign exchange'], row['private equity funds (fip)'], row['credit receivables (fidc)'])
        doc.append(NoEscape(r'}'))
    #5.3.2
    with doc.create(Subsection('AUMs')):
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/brazil/#tab_fund-aum}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')
       
        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.8}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Fixed Income', 'Equity','Multimercados','ETF','Pension Funds', 'Foreign Exchange', 'Private Equity Funds', 'Credit Receivables', 'Real Estate', 'Offshore')
            table.add_hline()
            for index, row in dfInvAUMUSD.iterrows():
                table.add_row(row['date'], row['fixed income'], row['equity'], row['multimercados'],row['etf'], row['pension funds'], row['foreign exchange'], row['private equity funds (fip)'], row['credit receivables (fidc)'], row['real estate (fii)'], row['offshore'])
        doc.append(NoEscape(r'}'))

        doc.append(bold('\n\nBRL bn\n'))
        doc.append(NoEscape(r'\scalebox{0.8}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Fixed Income', 'Equity','Multimercados','ETF','Pension Funds', 'Foreign Exchange', 'Private Equity Funds', 'Credit Receivables', 'Real Estate', 'Offshore')
            table.add_hline()
            for index, row in dfInvAUMRD.iterrows():
                table.add_row(row['date'], row['fixed income'], row['equity'], row['multimercados'],row['etf'], row['pension funds'], row['foreign exchange'], row['private equity funds (fip)'], row['credit receivables (fidc)'], row['real estate (fii)'], row['offshore'])
        doc.append(NoEscape(r'}'))

doc.append(NoEscape(r'\end{landscape}'))

doc.generate_pdf('Brazil' ,clean=True)