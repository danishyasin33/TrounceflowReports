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
#Public Debt Section
dfCenCurUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-currency-in-nigeria-chart.csv')
dfCenCurNGN = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-currency-in-nigeria-chart-in-nigerian-naira.csv')
dfCenBanOmoIsUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-bank-lending-in-nigeria-chart.csv')
dfCenBanOmoIsNGN = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-bank-lending-in-nigeria-chart-in-nigerian-naira.csv')
dfCenBanOmoHoUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-omos-in-nigeria-chart.csv')
dfCenBanOmoHoNGN = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-omos-in-nigeria-chart-in-nigerian-naira.csv')
#Local Financial institutions
dfPensionUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-em-pension-funds-in-nigeria-chart.csv')
dfPensionNGN = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-em-pension-funds-in-nigeria-chart-in-nigerian-naira.csv')
dfBankUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-banks-in-nigeria-chart.csv')
dfBankNGN = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-banks-in-nigeria-chart-in-nigerian-naira.csv')
#External Sector
dfAssLiabUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-investment-position-in-nigeria-chart.csv')
dfAssLiabNGN = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-investment-position-in-nigeria-chart-in-nigerian-naira.csv')
dfPortUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-portfolio-position-in-nigeria-chart.csv')
dfPortNGN = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-portfolio-position-in-nigeria-chart-in-nigerian-naira.csv')

#For Summary
NovDate = '13/11/2019'
AugDate = '31/08/2019'
JunDate = '30/06/2019'
SepDate = '30/09/2019'
OctDate = '31/10/2019'
#table 2.1
dfCenCurUSDJun = dfCenCurUSD.loc[dfCenCurUSD['date'] == JunDate]
dfCenCurNGNJun = dfCenCurNGN.loc[dfCenCurNGN['date'] == JunDate]
#table 2.2.1
dfCenBanOmoIsNovUSD = dfCenBanOmoIsUSD.loc[dfCenBanOmoIsUSD['date'] == NovDate]
dfCenBanOmoIsNovNGN = dfCenBanOmoIsNGN.loc[dfCenBanOmoIsNGN['date'] == NovDate]
#table 2.2.2
dfCenBanOmoHoUSDNov = dfCenBanOmoHoUSD.loc[dfCenBanOmoHoUSD['date'] == AugDate]
dfCenBanOmoHoNGNNov = dfCenBanOmoHoNGN.loc[dfCenBanOmoHoNGN['date'] == AugDate]
#table 3.1
dfPensionUSDSep = dfPensionUSD.loc[dfPensionUSD['date'] == SepDate]
dfPensionNGNSep = dfPensionNGN.loc[dfPensionNGN['date'] == SepDate]
#table 3.2
dfBankUSDOct = dfBankUSD.loc[dfBankUSD['date'] == OctDate]
dfBankNGNOct = dfBankNGN.loc[dfBankNGN['date'] == OctDate]



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
doc.preamble.append(Command('title','Trounceflow Countries: Nigeria'))
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
        table.add_row(('Date', 'Type', 'USD bn (Total)','ARS bn (Total)'))
        table.add_hline()
        #Nov
        table.add_row('Nov 2019','OMO Issuance',dfCenBanOmoIsNovUSD['Total'].values[0],dfCenBanOmoIsNovNGN['Total'].values[0])
        #Aug
        table.add_row('Aug 2019','OMO Holding',dfCenBanOmoHoUSDNov['Total'].values[0],dfCenBanOmoHoNGNNov['Total'].values[0])
        #Jun
        table.add_row('Jun 2019','By Currency',dfCenCurUSDJun['Total'].values[0],dfCenCurNGNJun['Total'].values[0])
#1.2
with doc.create(Section('Domestic Sector')):
    with doc.create(Tabular('l|l|r|r')) as table:
        table.add_row(('Date', 'Type', 'USD bn (Total)','ARS bn (Total)'))
        table.add_hline()
        #Oct
        table.add_row('Oct 2019','Banks',dfBankUSDOct['Total'].values[0],dfBankNGNOct['Total'].values[0])
        #Sep
        table.add_row('Sep 2019','Pension Funds',dfPensionUSDSep['Total'].values[0],dfPensionUSDSep['Total'].values[0])
        

#Chapter 2 
doc.append(NoEscape(r'\chapter{Central Government Debt: Bonds and Issuers}'))
doc.append(NewPage())

#2.1
with doc.create(Section('By Currency [Domestic (NGN); External]')):
    #doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-mensuales-de-la-deuda}{View the data }"))
    #doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/nigeria/#tab_publicdebt}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values for the normal situation (paid) debt are as follows:\n')
    
    doc.append(bold('USD bn\n'))
    with doc.create(Tabular('l|r|r|r')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfCenCurUSD.iterrows():
            table.add_row(row['date'],row['domestic currency'], row['foreign currency'],row['Total'])
    
    doc.append(bold('\n\nNGN bn\n'))
    with doc.create(Tabular('l|r|r|r')) as table:
        table.add_row(('Date', 'Domestic', 'External','Total'))
        table.add_hline()
        for index, row in dfCenCurNGN.iterrows():
            table.add_row(row['date'],row['domestic currency'], row['foreign currency'],row['Total'])
#doc.append(NewPage())
#2.2
with doc.create(Section('Central Bank Holdings')):
    with doc.create(Subsection('OMO issuance')):
        doc.append(NoEscape(r"\href{https://www.cbn.gov.ng/rates/GovtSecurities.asp}{View the data }"))
        doc.append('from the primary source (cbn.gov.ng)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/nigeria/#tab_omoissue}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values for the normal situation (paid) debt are as follows:\n')
    
        doc.append(bold('USD bn\n'))
        with doc.create(Tabular('l|r|r|r|r')) as table:
            table.add_row(('Date', 'FGN Bonds', 'NTB', 'OMO', 'Total'))
            table.add_hline()
            for index, row in dfCenBanOmoIsUSD.iterrows():
                table.add_row(row['date'], row['fgn bonds'], row['ntb'], row['omo'], row['Total'])
        doc.append(NewPage())
        doc.append(bold('\n\nNGN bn\n'))
        with doc.create(Tabular('l|r|r|r|r')) as table:
            table.add_row(('Date', 'FGN Bonds', 'NTB', 'OMO', 'Total'))
            table.add_hline()
            for index, row in dfCenBanOmoIsNGN.iterrows():
                table.add_row(row['date'], row['fgn bonds'], row['ntb'], row['omo'], row['Total'])

    with doc.create(Subsection('OMO holdings')):
        doc.append(NoEscape(r"\href{http://statistics.cbn.gov.ng/cbn-onlinestats/DataBrowser.aspx}{View the data }"))
        doc.append('from the primary source (statistics.cbn.gov.ng)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/nigeria/#tab_omohold}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values for the normal situation (paid) debt are as follows:\n')
        
        doc.append(bold('USD bn\n'))
        with doc.create(Tabular('l|r|r|r|r')) as table:
            table.add_row(('Date', 'Banks', 'Foreigners', 'Others', 'Total'))
            table.add_hline()
            for index, row in dfCenBanOmoHoUSD.iterrows():
                table.add_row(row['date'], row['banks'], row['foreigners'], row['others'], row['Total'])
        
        doc.append(bold('\n\nNGN bn\n'))
        with doc.create(Tabular('l|r|r|r|r')) as table:
            table.add_row(('Date', 'Banks', 'Foreigners', 'Others', 'Total'))
            table.add_hline()
            for index, row in dfCenBanOmoHoNGN.iterrows():
                    table.add_row(row['date'], row['banks'], row['foreigners'], row['others'], row['Total'])

#Chapter 3
doc.append(NoEscape(r'\chapter{Domestic Sector}'))
doc.append(NewPage())
doc.append(NoEscape(r'\begin{landscape}'))
#3.1
with doc.create(Section('Pension Funds')):
    #doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/superintendencia-de-seguros}{View the data }"))
    #doc.append('from the primary source (argentina.gob.ar/superintendencia-de-seguros)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/nigeria/#tab_pensionfunds}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn\n'))
    doc.append(NoEscape(r'\scalebox{0.6}{'))
    with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table:
        table.add_row('Date', 'Domestic Ordinary Shares', 'Foreign Ordinary Shares','FGN Securities','State Government Securities','Corporate Debt Securities','Local Money Market Securities', 'Foreign Money Market Securities', 'Supra-National Bonds')
        table.add_hline()
        for index, row in dfPensionUSD.iterrows():
            table.add_row(row['date'], row['domestic ordinary shares'], row['foreign ordinary shares'], row['fgn securities'], row['state government securities'], row['corporate debt securities'], row['local money market securities'], row['foreign money market securities'], row['supra-national bonds'])
    doc.append(NoEscape(r'}'))
    doc.append(NewLine())
    doc.append('\n\n...')
    doc.append(NoEscape(r'\scalebox{0.6}{'))
    with doc.create(Tabular('r|r|r|r|r|r')) as table:
        table.add_row('Mutual Funds', 'Real Estate Properties', 'Private Equity Fund', 'Infrastructure Fund', 'Cash & Other Assets', 'Other Liabilities')
        table.add_hline()
        for index, row in dfPensionUSD.iterrows():
            table.add_row(row['mutual funds'], row['real estate properties'], row['private equity fund'], row['infrastructure fund'], row['cash & other assets'], row['other liabilities'])
    doc.append(NoEscape(r'}'))

    doc.append(bold('\n\nNGN bn\n'))
    doc.append(NoEscape(r'\scalebox{0.6}{'))
    with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table:
        table.add_row('Date', 'Domestic Ordinary Shares', 'Foreign Ordinary Shares','FGN Securities','State Government Securities','Corporate Debt Securities','Local Money Market Securities', 'Foreign Money Market Securities', 'Supra-National Bonds')
        table.add_hline()
        for index, row in dfPensionNGN.iterrows():
            table.add_row(row['date'], row['domestic ordinary shares'], row['foreign ordinary shares'], row['fgn securities'], row['state government securities'], row['corporate debt securities'], row['local money market securities'], row['foreign money market securities'], row['supra-national bonds'])
    doc.append(NoEscape(r'}'))
    doc.append(NewLine())
    doc.append('\n\n...')
    doc.append(NoEscape(r'\scalebox{0.6}{'))
    with doc.create(Tabular('r|r|r|r|r|r')) as table:
        table.add_row('Mutual Funds', 'Real Estate Properties', 'Private Equity Fund', 'Infrastructure Fund', 'Cash & Other Assets', 'Other Liabilities')
        table.add_hline()
        for index, row in dfPensionNGN.iterrows():
            table.add_row(row['mutual funds'], row['real estate properties'], row['private equity fund'], row['infrastructure fund'], row['cash & other assets'], row['other liabilities'])
    doc.append(NoEscape(r'}'))
    doc.append(NewPage())
#3.2
with doc.create(Section('Banks')):
    # doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/superintendencia-de-seguros}{View the data }"))
    # doc.append('from the primary source (argentina.gob.ar/superintendencia-de-seguros)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/nigeria/#tab_banks}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn\n\n'))
    doc.append(NoEscape(r'\scalebox{0.8}{'))
    with doc.create(Tabular('l|r|r|r|r|r|r|r')) as table:
        table.add_row('Date', 'Claims on Central Gov.', 'Claims on Other Fin. Inst.','Claims on Other Pvt. Sector','Claims on State & Local Gov.','Foreign Assets','Reserves','Unclassified Assets')
        table.add_hline()
        for index, row in dfBankUSD.iterrows():
            table.add_row(row['date'], row['claims on central government'], row['claims on other financial institutions/financial derivatives'], row['claims on other private sector'], row['claims on state & local government'],row['foreign assets'],row['reserves'],row['unclassified assets'])
    doc.append(NoEscape(r'}'))
    doc.append(bold('\n\nNGN bn\n\n'))
    doc.append(NoEscape(r'\scalebox{0.8}{'))
    with doc.create(Tabular('l|r|r|r|r|r|r|r')) as table:
        table.add_row('Date', 'Claims on Central Gov.', 'Claims on Other Fin. Inst.','Claims on Other Pvt. Sector','Claims on State & Local Gov.','Foreign Assets','Reserves','Unclassified Assets')
        table.add_hline()
        for index, row in dfBankNGN.iterrows():
            table.add_row(row['date'], row['claims on central government'], row['claims on other financial institutions/financial derivatives'], row['claims on other private sector'], row['claims on state & local government'],row['foreign assets'],row['reserves'],row['unclassified assets'])
    doc.append(NoEscape(r'}'))

doc.append(NoEscape(r'\end{landscape}'))

#Chapter 4
doc.append(NoEscape(r'\chapter{External Sector}'))
doc.append(NewPage())
#4.1
with doc.create(Section('International Investment Position')):
    with doc.create(Subsection('Assets & Liabilities')):
        # doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        # doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/nigeria/#tab_al}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(bold('USD bn\n'))
        doc.append(NoEscape(r'\scalebox{0.7}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Assets-Direct','Assets-Portfolio','Assets-Reserve','Assets-Other','* IIP','Liabilities-Direct','Liabilities-Portfolio','Liabilities-Other')
            table.add_hline()
            for index, row in dfAssLiabUSD.iterrows():
                table.add_row(row['date'],row['assets - direct investment'], row['assets - portfolio investment'], row['assets - reserve assets'], row['assets - other investment'],  row['international investment position'], row['liabilities - direct investment'],  row['liabilities - portfolio investment'], row['liabilities - other investment'])
        doc.append(NoEscape(r'}'))
        doc.append('\n\n* International Investment Position\n')

        doc.append(bold('NGN bn\n'))
        doc.append(NoEscape(r'\scalebox{0.7}{'))
        with doc.create(Tabular('l|r|r|r|r|r|r|r|r')) as table:
            table.add_row('Date', 'Assets-Direct','Assets-Portfolio','Assets-Reserve','Assets-Other','* IIP','Liabilities-Direct','Liabilities-Portfolio','Liabilities-Other')
            table.add_hline()
            for index, row in dfAssLiabNGN.iterrows():
                table.add_row(row['date'],row['assets - direct investment'], row['assets - portfolio investment'], row['assets - reserve assets'], row['assets - other investment'],  row['international investment position'], row['liabilities - direct investment'],  row['liabilities - portfolio investment'], row['liabilities - other investment'])
        doc.append(NoEscape(r'}'))
        doc.append('\n\n* International Investment Position')
        #doc.append(NewPage())
    with doc.create(Subsection('Portfolio Liabilities')):
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/nigeria/#tab_al}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

        doc.append(bold('USD bn\n'))
        with doc.create(Tabular('l|r|r')) as table:
            table.add_row('Date', 'Equity and Investment Fund Shares', 'Debt Securities')
            table.add_hline()
            for index, row in dfPortUSD.iterrows():
                table.add_row(row['date'], row['debt securities'], row['equity and investment fund shares'])
        doc.append(NewPage())
        doc.append(bold('\n\nNGN bn\n'))
        with doc.create(Tabular('l|r|r')) as table:
            table.add_row('Date', 'Equity and Investment Fund Shares', 'Debt Securities')
            table.add_hline()
            for index, row in dfPortNGN.iterrows():
                table.add_row(row['date'], row['debt securities'], row['equity and investment fund shares'])    



#Appendices
#doc.append(NoEscape(r'\appendix'))
#doc.append(NoEscape(r'\appendixpage'))
# doc.append(NoEscape(r'\chapter*{Appendix}'))
# doc.append(NoEscape(r'\addcontentsline{toc}{chapter}{Appendix}'))
# doc.append(NewPage())
# #section 1.1 
# with doc.create(Section('By Bond [LETES; LECAP; NOBAC; LECER; LELINKS; Other]', numbering=False)):
#     with doc.create(Subsection('Domestic currency only bonds', numbering=False)):
#         doc.append(bold('Of which ﬁxed-rate\n'))
#         doc.append('The Capitalizable Letters (LECAPs) are short term securities issued by the National Treasury, ARS-denominated ﬁxed-rate bond.' )
#         doc.append(bold('\nOf which variable-rate\n'))
#         doc.append('National Treasury LECER bonds: Inﬂation-adjusted \nNational Treasury BONCER bonds: Adjustment by CER (benchmark inﬂation stabilization coefficient)\nNational Treasury BOTAPO: at Monetary Policy Rate\nNational Treasury BOGAR: Adjustment by CER')
#     with doc.create(Subsection('External currency only bonds', numbering=False)):
#         doc.append('BIRAD are International bonds of the Argentine in US dollars ﬁxed-rate bond.\nBIRAE are International bonds of the Argentine in Euros, ﬁxed-rate bond.\nBIRAF are International bonds of the Argentine in Swiss Francos, ﬁxed-rate bond.')
#     with doc.create(Subsection('Other currency bonds', numbering=False)):
#         doc.append('BONAR are Argentine Nation bonds issued in US Dollars and in pesos. The dollar denomination pay a ﬁxed coupon rate every six months and securities in pesos pays a variable rate according to spread plus BADLAR rate (is an average rate regarding the nominal annual interest rate in peso-denominated time deposits of more than 1.0 million ARS from 30 to 35 days).\n')
#         doc.append('National Treasury LETES: short-term debt securities denominated in US dollars or in pesos that are issued by the National Treasury.\nBONTE are Treasury bonds issued before 2001, ﬁxed-rate.\n')
#         doc.append('The Notes of the Central Bank (NOBACs) are One-year Central Bank BCRA-issued ﬁxedrate bond reserved for banks.\nThe National Treasury LELINKS bonds are securities linked to the US dollar.\nBOCONES or bonds of Consolidation of Pension Debts are bills issued by The national Executive Branch, to cancel the consolidated obligations. Bonds will be issued to sixteen (16) year term.\n')
#         doc.append(bold('BOAT\n'))
#         doc.append('Reference Stabilization Coefficient (CER)\nThe Reference Stabilization Coeﬃcient (CER) is a daily adjustment index, which is prepared by the Central Bank of the Argentine Republic (BCRA). This indicator reﬂects the evolution of inﬂation, for which the variation recorded in the Consumer Price Index (CPI) is taken as the basis of calculation, which is prepared by the INDEC (National Institute of Statistics and Censuses).\n' )

# #The first table
# doc.append(NoEscape(r'\scalebox{0.7}{'))
# with doc.create(Tabular('l|c|c|c|c|c',row_height=1.5)) as table:
#     #first row
#     table.add_row((LargeText(bold('Issuer Entity')), LargeText(bold('Name')), LargeText(bold('Currency')),LargeText(bold('Coupon')),LargeText(bold('Maturity')),LargeText(bold('Adjustment'))))
#     table.add_hline()
#     table.add_row((MultiRow(2,data='BCRA'),MultiRow(2,data='Nobacs'),MultiRow(2,data='ARS'),'Fixed','2 to 4 years','CER'))
#     table.add_hline(4,6)
#     table.add_row(('','','','Variable','2 to 4 years','-'))
#     table.add_hline()
#     #second row (13 rows)
#     table.add_row((MultiRow(13,data='National Government'),'LECAPS','ARS','Fixed','1 to 12 years','-'))
#     table.add_hline(2,6)
#     table.add_row(('','BONCER','ARS','Fixed','4 to 5 years','CER'))
#     table.add_hline(2,6)
#     table.add_row(('','BOGAR','ARS','Fixed','10 to 16 years','CER'))
#     table.add_hline(2,6)
#     table.add_row(('','BOTAPO','ARS','Variable','2 to 4 years','Monetary Policy Rate'))
#     table.add_hline(2,6)
#     table.add_row(('',MultiRow(2,data='BODEN'),'ARS','Fixed','5 to 10 years','CER*'))
#     table.add_hline(3,6)
#     table.add_row(('','','USD','Variable','5 to 10 years','-'))
#     table.add_hline(2,6)
#     table.add_row(('',MultiRow(2,data='BOCON'),'ARS','Fixed','5 to 20 years','CER*'))
#     table.add_hline(3,6)
#     table.add_row(('','','ARS','Variable','10 to 16 years','-'))
#     table.add_hline(2,6)
#     table.add_row(('',MultiRow(2,data='BONAR'),'USD','Fixed','2 to 4 years','-'))
#     table.add_hline(3,6)
#     table.add_row(('','','ARS','Variable','1 to 12 months','BADLAR**'))
#     table.add_hline(2,6)
#     table.add_row(('','LETES','ARS','At Discount','2 to 12 months','-'))
#     table.add_hline(2,6)
#     table.add_row(('','LECER','ARS','-','-','-'))
#     table.add_hline(2,6)
#     table.add_row(('','LELINKS','USD','-','-','-'))
#     table.add_hline()
#     table.add_row((MultiRow(2,data='Provinces'),'-','ARS','Fixed','16 years','CER*'))
#     table.add_hline(2,6)
#     table.add_row(('','-','ARS','Variable','16 years','-'))
#     table.add_hline()
# doc.append(NoEscape(r'}'))
# doc.append('\n\nOverview of Debt Securities in Argentina Market\n')
# doc.append('*CER: refers to benchmark inﬂation stabilization coeﬃcient\n**BADLAR: is an average rate regarding the nominal annual interest rate in peso-denominated time deposits of more than 1.0 million ARS from 30 to 35 days\n')

# #Future Additions Table
# # with doc.create(Section('Sections to be Added')):
# #     with doc.create(Center()) as centered:
# #         with centered.create(Tabular('c|l',row_height=1.5)) as table:
# #             table.add_row('-', LargeText(bold('Section Name')))
# #             table.add_hline()
# #             table.add_row('1','Internal Debt Held by Local/Residents')
# #             table.add_row('2','External Currency Central Government Debt: Investors')
# #             table.add_row('3','Equities')
# #             table.add_row('4','Deposits and Reserves')


# # doc.append(NewPage())
# # doc.append(NoEscape(r'\addappheadtotoc'))


doc.generate_pdf('Nigeria' ,clean=True)