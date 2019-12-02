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
dfUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-currency-in-argentina-chart.csv')
dfARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-currency-in-argentina-chart-in-argentine-peso.csv')
dfCurUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/public-debt-by-currency-in-argentina-chart.csv')
dfCurARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/public-debt-by-currency-in-argentina-chart-in-argentine-peso.csv')
dfLegUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/debt-by-legislation-in-argentina-chart.csv')
dfLegARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/debt-by-legislation-in-argentina-chart-in-argentine-peso.csv')
dfResUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-residency-of-holders-in-argentina-chart.csv')
dfResARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/central-government-debt-stock-by-residency-of-holders-in-argentina-chart-in-argentine-peso.csv')
dfExtCurUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-currency-in-argentina-chart.csv')
dfExtCurARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-currency-in-argentina-chart-in-argentine-peso.csv')
dfExtSecUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-sector-in-argentina-chart.csv')
dfExtSecARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/external-debt-by-sector-in-argentina-chart-in-argentine-peso.csv')
dfPortUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-portfolio-position-in-argentina-chart.csv')
dfPortARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-portfolio-position-in-argentina-chart-in-argentine-peso.csv')
dfIIPUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-investment-position-in-argentina-chart.csv')
dfIIPARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/international-investment-position-in-argentina-chart-in-argentine-peso.csv')
#dfBopUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/current-account-in-argentina-chart.csv')
#dfBopARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/current-account-in-argentina-chart-in-argentine-peso.csv')
dfFXUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/imf-fx-reserves-in-argentina-chart.csv')
dfFXARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/imf-fx-reserves-in-argentina-chart-in-argentine-peso.csv')
dfPensionUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-em-pension-funds-in-argentina-chart.csv')
dfPensionARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-em-pension-funds-in-argentina-chart-in-argentine-peso.csv')
dfInsurUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-insurance-companies-in-argentina-chart.csv')
dfInsurARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-insurance-companies-in-argentina-chart-in-argentine-peso.csv')
dfBankUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-banks-in-argentina-chart.csv')
dfBankARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/holdings-of-banks-in-argentina-chart-in-argentine-peso.csv')
dfMenHolUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/mendoza-total-debt-by-category-of-holder-in-argentina-chart.csv')
dfMenHolARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/mendoza-total-debt-by-category-of-holder-in-argentina-chart-in-argentine-peso.csv')
dfMenCurUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/mendoza-total-debt-by-currency-of-denomination-in-argentina-chart.csv')
dfMenCurARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/mendoza-total-debt-by-currency-of-denomination-in-argentina-chart-in-argentine-peso.csv')
dfMenMatUSD = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/mendoza-total-debt-by-years-to-maturity-in-argentina-chart.csv')
dfMenMatARS = impFunc.get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/mendoza-total-debt-by-years-to-maturity-in-argentina-chart-in-argentine-peso.csv')


#last rows of september data
sepDate = '30/09/2019'
#table 1.2
dflastUSD = dfUSD.loc[dfUSD['date'] == sepDate]
dflastARS = dfARS.loc[dfARS['date'] == sepDate]
#table 10.1
dflastFXUSD = dfFXUSD.loc[dfFXUSD['date'] == sepDate]
dflastFXARS = dfFXARS.loc[dfFXARS['date'] == sepDate]

#Last rows of June Data
junDate = '30/06/2019'
#table 1.2
dflastUSD2 = dfUSD.loc[dfUSD['date'] == junDate]
dflastARS2 = dfARS.loc[dfARS['date'] == junDate]
#table 1.3
dflastCurUSD = dfCurUSD.loc[dfCurUSD['date'] == junDate]
dflastCurARS = dfCurARS.loc[dfCurARS['date'] == junDate]
#table 1.4
dflastLegUSD = dfLegUSD.loc[dfLegUSD['date'] == junDate]
dflastLegARS = dfLegARS.loc[dfLegARS['date'] == junDate]
#table 2.1
dflastResUSD = dfResUSD.loc[dfResUSD['date'] == junDate]
dflastResARS = dfResARS.loc[dfResARS['date'] == junDate]
#table 2.3
dflastExtUSD = dfExtCurUSD.loc[dfExtCurUSD['date'] == junDate]
dflastExtARS = dfExtCurARS.loc[dfExtCurARS['date'] == junDate]
#table 4.1
dflastMenHolUSD = dfMenHolUSD.loc[dfMenHolUSD['date'] == junDate]
dflastMenHolARS = dfMenHolARS.loc[dfMenHolARS['date'] == junDate]
#table 4.2
dflastMenCurUSD = dfMenCurUSD.loc[dfMenCurUSD['date'] == junDate]
dflastMenCurARS = dfMenCurARS.loc[dfMenCurARS['date'] == junDate]
#table 4.3
dflastMenMatUSD = dfMenMatUSD.loc[dfMenMatUSD['date'] == junDate]
dflastMenMatARS = dfMenMatARS.loc[dfMenMatARS['date'] == junDate]
#Table 5.1 foreign
dfJunExSecUSD = dfExtSecUSD.loc[dfExtSecUSD['date'] == junDate]
dfJunExSecARS = dfExtSecARS.loc[dfExtSecARS['date'] == junDate]
#table 6.1
dfJunPorUSD = dfPortUSD.loc[dfPortUSD['date'] == junDate]
dfJunPorARS = dfPortARS.loc[dfPortARS['date'] == junDate]
#table 8.1
dfJunFXUSD = dfFXUSD.loc[dfFXUSD['date'] == junDate]
dfJunFXARS = dfFXARS.loc[dfFXARS['date'] == junDate]
#table 9.1
dfJunPenUSD = dfPensionUSD.loc[dfPensionUSD['date'] == junDate]
dfJunPenARS = dfPensionARS.loc[dfPensionARS['date'] == junDate]
#table 9.2
dfJunInsUSD = dfInsurUSD.loc[dfInsurUSD['date'] == junDate]
dfJunInsARS = dfInsurARS.loc[dfInsurARS['date'] == junDate]
#table 9.3
dfJunBankUSD = dfBankUSD.loc[dfBankUSD['date'] == junDate]
dfJunBankARS = dfBankARS.loc[dfBankARS['date'] == junDate]
#last rows of september data
# mask = dflastUSD['date'] == sepDate
# dflastCurUSD = dflastUSD.loc[mask]
# print(dflastCurUSD.dtypes)
# Lastdate = dflastCurUSD['date'].values[0]
# print(Lastdate)
# #Lastdate = Lastdate.to_string()
# Lastdate = datetime.datetime.strptime(Lastdate,'%d/%m/%Y')

# time = Lastdate.strftime("%B %Y")

#_______________________________________

#geometry_options = {"tmargin": "5cm"}
doc = Document(documentclass='report', document_options=['11pt'])

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
doc.append(NewPage())

doc.append(NoEscape(r'\tableofcontents'))
doc.append(NewPage())

#Summary Chapter
doc.append(NoEscape(r'\chapter{Executive Summary}'))
doc.append(NewPage())

#The recent data table
#central debt
with doc.create(Section('Central Government Debt Stock')):
    with doc.create(Center()) as centered: 
        with doc.create(Center()) as centered: 
            with centered.create(Tabular('c|l|c|c')) as table:
                table.add_row(('Date', 'Type', 'USD Bn (Total)','ARS Bn (Total)'))
                table.add_hline()
                #Sep
                table.add_row(MultiRow(2,data='Sep 2019'),'* Debt',dflastUSD['Total'].values[0],dflastARS['Total'].values[0])
                table.add_row('','FX Reserves', dflastFXUSD['Total'].values[0], dflastFXARS['Total'].values[0])
                table.add_hline()
                #June
                table.add_row(MultiRow(5,data='Jun 2019'), '* Debt', dflastUSD2['Total'].values[0], dflastARS2['Total'].values[0])
                table.add_row('', '** Debt', dflastCurUSD['Total'].values[0], dflastCurARS['Total'].values[0])
                table.add_row('', '*** Debt', dflastLegUSD['deuda bruta'].values[0], dflastLegARS['deuda bruta'].values[0])
                table.add_row('', '**** Debt', dflastResUSD['Total'].values[0], dflastResARS['Total'].values[0])
                table.add_row('', '***** Foreign', dflastExtUSD['Total'].values[0], dflastExtARS['Total'].values[0])
                #table.add_row('','FX Reserves', dfJunFXUSD['Total'].values[0], dfJunFXARS['Total'].values[0]) NO JUNE VALUE

    doc.append('* Central Government Debt By Currency [Domestic (ARS); External]\n')
    doc.append('** Central Government Debt By Currency [ARS; EUR; JPY; USD; SDR]\n')
    doc.append('*** Central Government Debt By Legislation Type [Domestic; External]\n')
    doc.append('**** Central Government Debt By Residency[internal/local/resident; external/foreigner/nonresident]\n')
    doc.append('***** Foreign Holdings of Domestic Currency Bonds')
    
#Mendoza Debt
with doc.create(Section('Mendoza Government Debt')):
    with doc.create(Center()) as centered: 
        with doc.create(Center()) as centered: 
            with centered.create(Tabular('c|l|c|c')) as table:
                table.add_row(('Date', 'Type', 'USD Bn (Total)','ARS Bn (Total)'))
                table.add_hline()
                #June
                table.add_row(MultiRow(3,data='Jun 2019'), 'Mendoza Debt by Holder', dflastMenHolUSD['Total'].values[0], dflastMenHolARS['Total'].values[0])
                table.add_row('', 'Mendoza Debt by Currency', dflastMenCurUSD['Total'].values[0], dflastMenCurARS['Total'].values[0])
                table.add_row('', 'Mendoza Debt by Maturity', dflastMenMatUSD['Total'].values[0], dflastMenMatARS['Total'].values[0])
    

with doc.create(Section('External & Domestic Sector')):
    with doc.create(Center()) as centered: 
        with doc.create(Center()) as centered: 
            with centered.create(Tabular('c|l|c|c')) as table:
                table.add_row(('Date', 'Type', 'USD Bn (Total)','ARS Bn (Total)'))
                table.add_hline()
                #June
                table.add_row(MultiRow(3,data='Jun 2019'), '* Foreign', dfJunExSecUSD['Total'].values[0], dfJunExSecARS['Total'].values[0])
                #table.add_row('', 'Int. Portfolio', dfJunPorUSD['Total'].values[0], dfJunPorARS['Total'].values[0])    NO JUNE VALUE
                #table.add_row('', 'Pension Funds', dfJunPenUSD['Total'].values[0], dfJunPenARS['Total'].values[0])     NO JUNE VALUE
                table.add_row('', 'Ins. Companies', dfJunInsUSD['Total'].values[0], dfJunInsARS['Total'].values[0])
                table.add_row('', 'Banks', dfJunBankUSD['Total'].values[0], dfJunBankARS['Total'].values[0])
    doc.append('* Foreign-held Debt by Issuer [Banks; Government; Monetary Authorities]')


#chapter 2
doc.append(NoEscape(r'\chapter{Central Government Debt: Bonds and Issuers}'))
doc.append(NewPage())

#section 1.1
with doc.create(Section('By Currency [Domestic (ARS); External]')):
    doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-mensuales-de-la-deuda}{View the data }"))
    doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/argentina/#tab_bycurrency}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values for the normal situation (paid) debt are as follows:\n')

    doc.append(bold('USD bn'))
    with doc.create(Center()) as centered: 
        with centered.create(Tabular('c|c|c|c')) as table:
            table.add_row(('Date', 'Domestic', 'External','Total'))
            table.add_hline()
            for index, row in dfUSD.iterrows():
                table.add_row(row['date'],row['domestic currency'], row['foreign currency'],row['Total'])

    doc.append(bold('ARS bn'))
    with doc.create(Center()) as centeredARS: 
        with centeredARS.create(Tabular('c|c|c|c')) as table:
            table.add_row(('Date', 'Domestic', 'External','Total'))
            table.add_hline()
            for index, row in dfARS.iterrows():
                table.add_row(row['date'],row['domestic currency'], row['foreign currency'],row['Total'])
#section 1.2
with doc.create(Section('By Currency [ARS; EUR; JPY; USD; SDR]')):
    doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
    doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/argentina/#tab_byspecificcurrency}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')
    
    doc.append(bold('USD bn'))
    with doc.create(Center()) as centered: 
        with centered.create(Tabular('c|c|c|c|c|c|c|c')) as table:
            table.add_row(('Date', 'ARS', 'SDR','EUR','USD','JPY','OTHER','Total'))
            table.add_hline()
            for index, row in dfCurUSD.iterrows():
                table.add_row(row['date'],row['ars'], row['debt sdr'],row['euros'],row['usd'],row['yen'], row['other currencies'], row['Total'])
    doc.append(NewPage())
    doc.append(bold('ARS bn'))
    with doc.create(Center()) as centeredARS: 
        with centeredARS.create(Tabular('c|c|c|c|c|c|c|c')) as table:
            table.add_row(('Date', 'ARS', 'SDR','EUR','USD','JPY','OTHER','Total'))
            table.add_hline()
            for index, row in dfCurARS.iterrows():
                table.add_row(row['date'],row['ars'], row['debt sdr'],row['euros'],row['usd'],row['yen'], row['other currencies'], row['Total'])

#section 1.3

with doc.create(Section('By Legislation Type [Domestic; External]')):
    doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
    doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/argentina/#tab_bylegislation-usd}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')
    
    doc.append(bold('USD bn'))
    with doc.create(Center()) as centered: 
        with centered.create(Tabular('c|c c|c c c|c')) as table:
            table.add_row('Date', 'Domestic', 'Bonds*','External','Bonds**','Orgs***','Total')
            table.add_hline()
            for index, row in dfLegUSD.iterrows():
                table.add_row(row['date'], row['legislation argentina'], row['legislation argentina - of which títulos públicos y letras del tesoro'], row['legislation extranjera'], row['legislation extranjera - of which títulos públicos y letras del tesoro'], row['legislation extranjera - of which organismos internacionales'], row['deuda bruta'])
    doc.append('* Public securities and Treasury letters\n')
    doc.append('** Public securities and Treasury letters\n')
    doc.append('*** International Organizations\n')

    doc.append(bold('ARS bn'))
    with doc.create(Center()) as centeredARS: 
        with centeredARS.create(Tabular('c|c c|c c c|c')) as table:
            table.add_row('Date', 'Domestic', 'Bonds*','External','Bonds**','Orgs***','Total')
            table.add_hline()
            for index, row in dfLegARS.iterrows():
                table.add_row(row['date'], row['legislation argentina'], row['legislation argentina - of which títulos públicos y letras del tesoro'], row['legislation extranjera'], row['legislation extranjera - of which títulos públicos y letras del tesoro'], row['legislation extranjera - of which organismos internacionales'], row['deuda bruta'])


#Chapter 2 

doc.append(NoEscape(r'\chapter{Domestic Currency Central Government Debt: Investors}'))
doc.append(NewPage())

#section 2.1
with doc.create(Section('By Residency [internal/local/resident; external/foreigner/nonresident]')):
    doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/hacienda/finanzas/deudapublica/informes-trimestrales-de-la-deuda}{View the data }"))
    doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/argentina/#tab_byresidency-usd}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Gross debt of the central administration (excluding eligible debt restructuring pending):\n')

    doc.append(bold('USD bn'))
    with doc.create(Center()) as centered: 
        with centered.create(Tabular('c|c|c|c')) as table:
            table.add_row(('Date', 'Domestic', 'External','Total'))
            table.add_hline()
            for index, row in dfResUSD.iterrows():
                table.add_row(row['date'],row['domestic creditors'], row['external creditors'],row['Total'])

    doc.append(bold('ARS bn'))
    with doc.create(Center()) as centeredARS: 
        with centeredARS.create(Tabular('c|c|c|c')) as table:
            table.add_row(('Date', 'Domestic', 'External','Total'))
            table.add_hline()
            for index, row in dfResARS.iterrows():
                table.add_row(row['date'],row['domestic creditors'], row['external creditors'],row['Total'])
#Section 2.2 Empty
# with doc.create(Section('Internal Debt (held by locals/residents)')):
#     with doc.create(Subsection('Local holdings of domestic currency bonds')):
#         doc.append('No Info')
#     with doc.create(Subsection('By sector of holder [banks; pension funds; insurers]')):
#         doc.append('No Info')
    #section 2.2 no info
#Section 2.3
with doc.create(Section('External Debt (held by foreigners/non-residents)')):
    with doc.create(Subsection('Foreign holdings of domestic currency bonds')):
        doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
        doc.append('from the primary source (argentina.gob.ar)\n')
        doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/argentina/#tab_edcurrency}{View the chart }"))
        doc.append('on trounceﬂow.com and download the data straight from the chart\n')
        doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn'))
    with doc.create(Center()) as centered: 
        with centered.create(Tabular('c|c|c|c|c|c')) as table:
            table.add_row('Date', 'ARS', 'USD','EUR','Other','Total')
            table.add_hline()
            for index, row in dfExtCurUSD.iterrows():
                table.add_row(row['date'],row['local currency_'], row['usd_'],row['eur_'],row['others_'], row['Total'])

    doc.append(bold('ARS bn'))
    with doc.create(Center()) as centeredARS: 
        with centeredARS.create(Tabular('c|c|c|c|c|c')) as table:
            table.add_row('Date', 'ARS', 'USD','EUR','Other','Total')
            table.add_hline()
            for index, row in dfExtCurARS.iterrows():
                table.add_row(row['date'],row['local currency_'], row['usd_'],row['eur_'],row['others_'], row['Total'])
    
    # with doc.create(Subsection('By sector of holder [dedicated; crossover]')):
    #     doc.append('No Info')
    #section 2.3.2 no info
#chapter 3
# doc.append(NoEscape(r'\chapter{External Currency Central Government Debt: Investors}'))
# doc.append(NewPage())
# #section 3.1 no info
# with doc.create(Section('By Residency [internal/local/resident; external/foreigner/nonresident]')):
#     doc.append('No Info')
    

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
        
        doc.append(bold('USD bn'))
        with doc.create(Center()) as centered: 
            doc.append(NoEscape(r'\scalebox{0.7}{'))
            with centered.create(Tabular('c|c|c|c|c|c|c')) as table:
                table.add_row('Date', 'Bondholders', 'Federal Government','Multilateral Organizations','National Bank of Argentina','National and International Banks','Total')
                table.add_hline()
                for index, row in dfMenHolUSD.iterrows():
                    table.add_row(row['date'], row['bondholders'], row['federal government'], row['multilateral organizations'], row['national and international banks'], row['national bank of argentina'], row['Total'])
            doc.append(NoEscape(r'}'))
        doc.append(bold('ARS bn'))
        with doc.create(Center()) as centeredARS: 
            doc.append(NoEscape(r'\scalebox{0.7}{'))
            with centeredARS.create(Tabular('c|c|c|c|c|c|c')) as table:
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

        doc.append(bold('USD bn'))
        with doc.create(Center()) as centered: 
            with centered.create(Tabular('c|c|c|c')) as table:
                table.add_row(('Date', 'Pesos', 'USD','Total'))
                table.add_hline()
                for index, row in dfMenCurUSD.iterrows():
                    table.add_row(row['date'],row['pesos'], row['usd'],row['Total'])

        doc.append(bold('ARS bn'))
        with doc.create(Center()) as centeredARS: 
            with centeredARS.create(Tabular('c|c|c|c')) as table:
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

        doc.append(bold('USD bn'))
        with doc.create(Center()) as centered: 
            with centered.create(Tabular('c|c|c|c|c|c|c')) as table:
                table.add_row(('Date', 'Up to 1 Year', '1-2 Years','2-3 Years','3-4 Years','4-5 Years','5+ Years'))
                table.add_hline()
                for index, row in dfMenMatUSD.iterrows():
                    table.add_row(row['date'],row['up to 1 year'], row['1-2 years'],row['2-3 years'], row['3-4 years'], row['4-5 years'], row['5+years'])
        doc.append(NewPage())
        doc.append(bold('ARS bn'))
        with doc.create(Center()) as centeredARS: 
            with centeredARS.create(Tabular('c|c|c|c|c|c|c')) as table:
                table.add_row(('Date', 'Up to 1 Year', '1-2 Years','2-3 Years','3-4 Years','4-5 Years','5+ Years'))
                table.add_hline()
                for index, row in dfMenMatARS.iterrows():
                    table.add_row(row['date'],row['up to 1 year'], row['1-2 years'],row['2-3 years'], row['3-4 years'], row['4-5 years'], row['5+years'])

#chapter 5
doc.append(NoEscape(r'\chapter{External Debt (Foreign-Held Debt of Public and Private Sector)}'))
doc.append(NewPage())

#section 5.1 
with doc.create(Section('Foreign-held Debt by Issuer [Banks; Government; Monetary Authorities]')):
    doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
    doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/argentina/#tab_edsector}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn'))
    with doc.create(Center()) as centered: 
        with centered.create(Tabular('c|c|c|c|c|c')) as table:
            table.add_row('Date', 'Banks', 'Government','Monetary Authorities','Other','Total')
            table.add_hline()
            for index, row in dfExtSecUSD.iterrows():
                table.add_row(row['date'], row['banks'], row['central government'], row['monetary authorities'], row['other sectors'], row['Total'])

    doc.append(bold('ARS bn'))
    with doc.create(Center()) as centeredARS: 
        with centeredARS.create(Tabular('c|c|c|c|c|c')) as table:
            table.add_row('Date', 'Banks', 'Government','Monetary Authorities','Other','Total')
            table.add_hline()
            for index, row in dfExtSecARS.iterrows():
                table.add_row(row['date'], row['banks'], row['central government'], row['monetary authorities'], row['other sectors'], row['Total'])

#chapter 6
# doc.append(NoEscape(r'\chapter{Equities}'))
# doc.append(NewPage())
# #section 6.2 and 6.2
# with doc.create(Section('Internal Equities (held by locals/residents)')):
#     doc.append('No Info')
# with doc.create(Section('External Equities (held by foreigners/non-residents)')):
#     doc.append('No Info')

#chapter 7
doc.append(NoEscape(r'\chapter{International Investment Liabilities (External Debt, Equity, Other)}'))
doc.append(NewPage())

#section 7.1
with doc.create(Section('International Portfolio Position')):
    doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
    doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/argentina/#tab_portfoliol-usd}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')
    
    doc.append(bold('USD bn'))
    with doc.create(Center()) as centered: 
        with centered.create(Tabular('c|c|c|c')) as table:
            table.add_row('Date', 'Debt Securities', 'Equity and Investment Fund Shares','Total')
            table.add_hline()
            for index, row in dfPortUSD.iterrows():
                table.add_row(row['date'], row['debt securities'], row['equity and investment fund shares'], row['Total'])

    doc.append(bold('ARS bn'))
    with doc.create(Center()) as centeredARS: 
        with centeredARS.create(Tabular('c|c|c|c')) as table:
            table.add_row('Date', 'Debt Securities', 'Equity and Investment Fund Shares','Total')
            table.add_hline()
            for index, row in dfPortARS.iterrows():
                table.add_row(row['date'], row['debt securities'], row['equity and investment fund shares'], row['Total'])


#chapter 8
doc.append(NoEscape(r'\chapter{International Investment Position (Assets - Liabilities)}'))
doc.append(NewPage())


doc.append(NoEscape(r'\begin{landscape}'))
#section 8.1
with doc.create(Section('International Investment Position')):
    doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
    doc.append('from the primary source (argentina.gob.ar)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/international-investment-position-argentina}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn'))
    with doc.create(Center()) as centered: 
        doc.append(NoEscape(r'\scalebox{0.6}{'))
        with centered.create(Tabular('c|c|c|c|c|c|c|c|c|c|c')) as table:
            table.add_row('Date', 'Assets-Direct', 'Assets-Financial Derivatives','Assets-Reserve','Assets-Portfolio','Assets-Other','* IIP','Liabilities-Direct','Liabilities-Financial Derivatives','Liabilities-Portfolio','Liabilities-Other')
            table.add_hline()
            for index, row in dfIIPUSD.iterrows():
                table.add_row(row['date'],row['assets - direct investment'], row['assets - financial derivatives (except reserves)'], row['assets - other investment'], row['assets - portfolio investment'], row['assets - reserve assets'], row['international investment position'], row['liabilities - direct investment'], row['liabilities - financial derivatives (except reserves)'], row['liabilities - other investment'], row['liabilities - portfolio investment'])
        doc.append(NoEscape(r'}'))
    doc.append('* International Investment Position\n')
    doc.append(bold('\nARS bn'))
    with doc.create(Center()) as centeredARS: 
        doc.append(NoEscape(r'\scalebox{0.6}{'))
        with centeredARS.create(Tabular('c|c|c|c|c|c|c|c|c|c|c')) as table:
            table.add_row('Date', 'Assets-Direct', 'Assets-Financial Derivatives','Assets-Reserve','Assets-Portfolio','Assets-Other','* IIP','Liabilities-Direct','Liabilities-Financial Derivatives','Liabilities-Portfolio','Liabilities-Other')
            table.add_hline()
            for index, row in dfIIPARS.iterrows():
                table.add_row(row['date'], row['assets - direct investment'], row['assets - financial derivatives (except reserves)'], row['assets - other investment'], row['assets - portfolio investment'], row['assets - reserve assets'], row['international investment position'], row['liabilities - direct investment'], row['liabilities - financial derivatives (except reserves)'], row['liabilities - other investment'], row['liabilities - portfolio investment'])
        doc.append(NoEscape(r'}'))
    doc.append('* International Investment Position')

doc.append(NoEscape(r'\end{landscape}'))

#REMOVED FROM SITE ---------------------------------------------------------- 
# #chapter 9 REMOVED FROM SITE 
# doc.append(NoEscape(r'\chapter{Balance of payments (Change in Assets and Liabilities)}'))
# doc.append(NewPage())


# doc.append(NoEscape(r'\begin{landscape}'))

# doc.append(NoEscape(r"\href{https://www.indec.gob.ar/}{View the data }"))
# doc.append('from the primary source (argentina.gob.ar)\n')
# doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/argentina/#tab_bop}{View the chart }"))
# doc.append('on trounceﬂow.com and download the data straight from the chart\n')
# doc.append('Recent values are as follows:\n')


# doc.append(bold('USD bn'))


# with doc.create(Center()) as centered: 
#     #with centered.create(Tabularx('c|c|c|c|c|c|c|c|c|c')) as table:
#     #doc.append(NoEscape(r'\small'))
#     doc.append(NoEscape(r'\scalebox{0.7}{'))
#     with centered.create(Tabular('c|c|c|c|c|c|c|c|c|c')) as table:
#         table.add_row('Date', 'Current Account', 'Goods-Export','Goods-Import','Primary Income-Credit','Primary Income-Debit','Secondary Income-Credit','Secondary Income-Debit','Services-Credit','Services-Debit')
#         table.add_hline()
#         for index, row in dfBopUSD.iterrows():
#             table.add_row(row['date'], row['current account'], row['goods - export'],row['goods - import'],row['primary income - credit'],row['primary income - debit'],row['secondary income - credit'],row['secondary income - debit'], row['services - credit'],row['services - debit'])
#     doc.append(NoEscape(r'}'))

# doc.append(bold('ARS bn'))
# with doc.create(Center()) as centeredARS: 
#     doc.append(NoEscape(r'\scalebox{0.7}{'))
#     with centeredARS.create(Tabular('c|c|c|c|c|c|c|c|c|c')) as table:
#         table.add_row('Date', 'Current Account', 'Goods-Export','Goods-Import','Primary Income-Credit','Primary Income-Debit','Secondary Income-Credit','Secondary Income-Debit','Services-Credit','Services-Debit')
#         table.add_hline()
#         for index, row in dfBopARS.iterrows():
#             table.add_row(row['date'], row['current account'], row['goods - export'],row['goods - import'],row['primary income - credit'],row['primary income - debit'],row['secondary income - credit'],row['secondary income - debit'], row['services - credit'],row['services - debit'])
#     doc.append(NoEscape(r'}'))


# doc.append(NoEscape(r'\end{landscape}'))
#----------------------------------------------------------------------

#chapter 10
doc.append(NoEscape(r'\chapter{FX Reserves}'))
doc.append(NewPage())

with doc.create(Section('Argentina FX Reserves')):
    doc.append(NoEscape(r"\href{http://data.imf.org/regular.aspx?key=61280813}{View the data }"))
    doc.append('from the primary source (imf.org)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/argentina/#tab_fxreserves}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn'))
    with doc.create(Center()) as centered: 
        with centered.create(Tabular('c|c|c|c|c')) as table:
            table.add_row('Date', 'FX', 'Gold','IMF','SDRS')
            table.add_hline()
            for index, row in dfFXUSD.iterrows():
                table.add_row(row['date'], row['fx'], row['gold'], row['imf'],row['sdrs'])

    doc.append(bold('ARS bn'))
    with doc.create(Center()) as centeredARS: 
        with centeredARS.create(Tabular('c|c|c|c|c')) as table:
            table.add_row('Date', 'FX', 'Gold','IMF','SDRS')
            table.add_hline()
            for index, row in dfFXARS.iterrows():
                table.add_row(row['date'], row['fx'], row['gold'], row['imf'],row['sdrs'])

#chapter 11 
doc.append(NoEscape(r'\chapter{Domestic sectors}'))
doc.append(NewPage())

#Section 11.1
with doc.create(Section('Pension Funds')):
    doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/superintendencia-de-seguros}{View the data }"))
    doc.append('from the primary source (argentina.gob.ar/superintendencia-de-seguros)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/financial-sector-data-argentina/#chart1}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn'))
    with doc.create(Center()) as centered: 
        with centered.create(Tabular('c|c|c|c|c|c')) as table:
            table.add_row('Date', 'Estrella', 'HSBC','Metlife','Nacion','Origenes')
            table.add_hline()
            for index, row in dfPensionUSD.iterrows():
                table.add_row(row['date'], row['estrella retiro'], row['hsbc retiro'], row['metlife retiro'],row['nacion retiro'], row['origenes retiro'])

    doc.append(bold('ARS bn'))
    with doc.create(Center()) as centeredARS: 
        with centeredARS.create(Tabular('c|c|c|c|c|c')) as table:
            table.add_row('Date', 'Estrella', 'HSBC','Metlife','Nacion','Origenes')
            table.add_hline()
            for index, row in dfPensionARS.iterrows():
                table.add_row(row['date'], row['estrella retiro'], row['hsbc retiro'], row['metlife retiro'],row['nacion retiro'], row['origenes retiro'])

with doc.create(Section('Insurance Companies')):
    doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/superintendencia-de-seguros}{View the data }"))
    doc.append('from the primary source (argentina.gob.ar/superintendencia-de-seguros)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/financial-sector-data-argentina/#chart2}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn'))
    with doc.create(Center()) as centered: 
        with centered.create(Tabular('c|c|c|c|c|c|c')) as table:
            table.add_row('Date', 'Fixed Income', 'Credits','Reserves','Property','Investments','Other')
            table.add_hline()
            for index, row in dfInsurUSD.iterrows():
                table.add_row(row['date'], row['bienes de uso/fixed assets'], row['creditos/credits'], row['disponibilidades/reserves'],row['inmuebles/estate'], row['inversiones/investments'], row['otros activos/other assets'])
    doc.append(NewPage())
    doc.append(bold('ARS bn'))
    with doc.create(Center()) as centeredARS: 
        with centeredARS.create(Tabular('c|c|c|c|c|c|c')) as table:
            table.add_row('Date', 'Fixed Income', 'Credits','Reserves','Property','Investments','Other')
            table.add_hline()
            for index, row in dfInsurARS.iterrows():
                table.add_row(row['date'], row['bienes de uso/fixed assets'], row['creditos/credits'], row['disponibilidades/reserves'],row['inmuebles/estate'], row['inversiones/investments'], row['otros activos/other assets'])

with doc.create(Section('Banks')):
    doc.append(NoEscape(r"\href{https://www.argentina.gob.ar/superintendencia-de-seguros}{View the data }"))
    doc.append('from the primary source (argentina.gob.ar/superintendencia-de-seguros)\n')
    doc.append(NoEscape(r"\href{https://www.trounceflow.com/app/financial-sector-data-argentina/#chart3}{View the chart }"))
    doc.append('on trounceﬂow.com and download the data straight from the chart\n')
    doc.append('Recent values are as follows:\n')

    doc.append(bold('USD bn'))
    with doc.create(Center()) as centered: 
        with centered.create(Tabular('c|c|c|c|c|c')) as table:
            table.add_row('Date', 'Assets abroad', 'Cash','Credit (Private)','Credit (Public)','Other')
            table.add_hline()
            for index, row in dfBankUSD.iterrows():
                table.add_row(row['date'], row['assets with residents abroad'], row['cash holdings'], row['credit to the private sector'], row['credit to the public sector'],row['other accounts'])

    doc.append(bold('ARS bn'))
    with doc.create(Center()) as centeredARS: 
        with centeredARS.create(Tabular('c|c|c|c|c|c')) as table:
            table.add_row('Date', 'Assets abroad', 'Cash','Credit (Private)','Credit (Public)','Other')
            table.add_hline()
            for index, row in dfBankARS.iterrows():
                table.add_row(row['date'], row['assets with residents abroad'], row['cash holdings'], row['credit to the private sector'], row['credit to the public sector'],row['other accounts'])

#chapter 12
# doc.append(NoEscape(r'\chapter{Deposits and Reserves}'))
# doc.append(NewPage())

#Appendices
doc.append(NoEscape(r'\appendix'))
doc.append(NoEscape(r'\appendixpage'))

#section 1.1 
with doc.create(Section('By Bond [LETES; LECAP; NOBAC; LECER; LELINKS; Other]')):
    with doc.create(Subsection('Domestic currency only bonds')):
        doc.append(bold('Of which ﬁxed-rate\n'))
        doc.append('The Capitalizable Letters (LECAPs) are short term securities issued by the National Treasury, ARS-denominated ﬁxed-rate bond.' )
        doc.append(bold('\nOf which variable-rate\n'))
        doc.append('National Treasury LECER bonds: Inﬂation-adjusted \nNational Treasury BONCER bonds: Adjustment by CER (benchmark inﬂation stabilization coefficient)\nNational Treasury BOTAPO: at Monetary Policy Rate\nNational Treasury BOGAR: Adjustment by CER')
    with doc.create(Subsection('External currency only bonds')):
        doc.append('BIRAD are International bonds of the Argentine in US dollars ﬁxed-rate bond.\nBIRAE are International bonds of the Argentine in Euros, ﬁxed-rate bond.\nBIRAF are International bonds of the Argentine in Swiss Francos, ﬁxed-rate bond.')
    with doc.create(Subsection('Other currency bonds')):
        doc.append('BONAR are Argentine Nation bonds issued in US Dollars and in pesos. The dollar denomination pay a ﬁxed coupon rate every six months and securities in pesos pays a variable rate according to spread plus BADLAR rate (is an average rate regarding the nominal annual interest rate in peso-denominated time deposits of more than 1.0 million ARS from 30 to 35 days).\n')
        doc.append('National Treasury LETES: short-term debt securities denominated in US dollars or in pesos that are issued by the National Treasury.\nBONTE are Treasury bonds issued before 2001, ﬁxed-rate.\n')
        doc.append('The Notes of the Central Bank (NOBACs) are One-year Central Bank BCRA-issued ﬁxedrate bond reserved for banks.\nThe National Treasury LELINKS bonds are securities linked to the US dollar.\nBOCONES or bonds of Consolidation of Pension Debts are bills issued by The national Executive Branch, to cancel the consolidated obligations. Bonds will be issued to sixteen (16) year term.\n')
        doc.append(bold('BOAT\n'))
        doc.append('Reference Stabilization Coefficient (CER)\nThe Reference Stabilization Coeﬃcient (CER) is a daily adjustment index, which is prepared by the Central Bank of the Argentine Republic (BCRA). This indicator reﬂects the evolution of inﬂation, for which the variation recorded in the Consumer Price Index (CPI) is taken as the basis of calculation, which is prepared by the INDEC (National Institute of Statistics and Censuses).' )

#The first table
with doc.create(Center()) as centered: 
    doc.append(NoEscape(r'\scalebox{0.8}{'))
    with centered.create(Tabular('c|c|c|c|c|c',row_height=1.5)) as table:
        #first row
        table.add_row((LargeText(bold('Issuer Entity')), LargeText(bold('Name')), LargeText(bold('Currency')),LargeText(bold('Coupon')),LargeText(bold('Maturity')),LargeText(bold('Adjustment'))))
        table.add_hline()
        table.add_row((MultiRow(2,data='BCRA'),MultiRow(2,data='Nobacs'),MultiRow(2,data='ARS'),'Fixed','2 to 4 years','CER'))
        table.add_hline(4,6)
        table.add_row(('','','','Variable','2 to 4 years','-'))
        table.add_hline()
        #second row (13 rows)
        table.add_row((MultiRow(13,data='National Government'),'LECAPS','ARS','Fixed','1 to 12 years','-'))
        table.add_hline(2,6)
        table.add_row(('','BONCER','ARS','Fixed','4 to 5 years','CER'))
        table.add_hline(2,6)
        table.add_row(('','BOGAR','ARS','Fixed','10 to 16 years','CER'))
        table.add_hline(2,6)
        table.add_row(('','BOTAPO','ARS','Variable','2 to 4 years','Monetary Policy Rate'))
        table.add_hline(2,6)
        table.add_row(('',MultiRow(2,data='BODEN'),'ARS','Fixed','5 to 10 years','CER*'))
        table.add_hline(3,6)
        table.add_row(('','','USD','Variable','5 to 10 years','-'))
        table.add_hline(2,6)
        table.add_row(('',MultiRow(2,data='BOCON'),'ARS','Fixed','5 to 20 years','CER*'))
        table.add_hline(3,6)
        table.add_row(('','','ARS','Variable','10 to 16 years','-'))
        table.add_hline(2,6)
        table.add_row(('',MultiRow(2,data='BONAR'),'USD','Fixed','2 to 4 years','-'))
        table.add_hline(3,6)
        table.add_row(('','','ARS','Variable','1 to 12 months','BADLAR**'))
        table.add_hline(2,6)
        table.add_row(('','LETES','ARS','At Discount','2 to 12 months','-'))
        table.add_hline(2,6)
        table.add_row(('','LECER','ARS','-','-','-'))
        table.add_hline(2,6)
        table.add_row(('','LELINKS','USD','-','-','-'))
        table.add_hline()
        table.add_row((MultiRow(2,data='Provinces'),'-','ARS','Fixed','16 years','CER*'))
        table.add_hline(2,6)
        table.add_row(('','-','ARS','Variable','16 years','-'))
        table.add_hline()
    doc.append(NoEscape(r'}'))
doc.append('Overview of Debt Securities in Argentina Market\n')
doc.append('*CER: refers to benchmark inﬂation stabilization coeﬃcient\n**BADLAR: is an average rate regarding the nominal annual interest rate in peso-denominated time deposits of more than 1.0 million ARS from 30 to 35 days\n')

#Future Additions Table
with doc.create(Section('Sections to be Added')):
    with doc.create(Center()) as centered:
        with centered.create(Tabular('c|l',row_height=1.5)) as table:
            table.add_row('-', LargeText(bold('Section Name')))
            table.add_hline()
            table.add_row('1','Internal Debt Held by Local/Residents')
            table.add_row('2','External Currency Central Government Debt: Investors')
            table.add_row('3','Equities')
            table.add_row('4','Deposits and Reserves')


doc.append(NewPage())
doc.append(NoEscape(r'\addappheadtotoc'))


doc.generate_pdf('Nigeria' ,clean=True)