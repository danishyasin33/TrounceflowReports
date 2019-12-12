import matplotlib
import numpy as np
from pylatex import Document, Section, Figure, NoEscape, SubFigure

import pandas
from pylatex import Document,MiniPage, Foot, PageStyle, Section, MultiColumn, MultiRow, Subsection, Center, Subsubsection, Tabularx, Tabular, Math, TikZ, Axis, Plot, Figure, Matrix, Alignat, Command, NewPage, NewLine, section,HugeText, LargeText, SmallText, PageStyle
from pylatex.utils import italic, NoEscape, bold
import os
import csv 

import datetime
import requests 
import json

matplotlib.use('Agg')  # Not to use X server. For TravisCI.
import matplotlib.pyplot as plt  # noqa

def getAuthCode(username, password):
    import requests     

    data = {
      'username': username,
      'password': password
    }

    res_token = requests.post('https://www.trounceflow.com/api/v1/auth-token/', data=data)

    #token=res_token.text.replace('{','').replace('}','').replace('"','').replace('token:','Token ')
    content = res_token.json()
    token = content['token']
    token = 'Token '+ token
    headers = {
        'Authorization': token,
    }
    return headers

def get_data_TrounceFlow(headers, url):
    import requests 
    import pandas
    import csv
    from io import StringIO

    res_data = requests.get(url, headers=headers)

    data_text=res_data.text
    data_text_list=data_text.split('\r\n')  #list of entries separated by end of line 

    data_String = StringIO(data_text)
    d_reader = csv.DictReader(data_String)

    col_names = d_reader.fieldnames

    #col_names=data_text_list[0].split(',')      #extracting names of columns from first row through comma separator

    data=pandas.DataFrame()

    for i in range(len(col_names)):
        data[col_names[i]]=[data_text_list[j].split(',')[i] for j in range(1,len(data_text_list)-1)]            #inputing data into dataframe column by column
    
    data.iloc[:,1:] = data.iloc[:,1:].apply(pandas.to_numeric)      #converting all columns except date to numeric type

    data['date'] = pandas.to_datetime(data['date'])           #converting date column to datetime type
    data['date'] = data['date'].dt.strftime('%b %Y')     #formatting that date

    #data = data.tail(5)
    data['Total'] = data.iloc[:,1:].sum(axis=1)             #calculating total by adding all columns except date  
    data['Total'] = data['Total'].round(2)                  #rounding of total column
 
    #data.iloc[:,1:] = data.iloc[:,1:].applymap("{:,}".format)   #applying thousand separator formatting

    return data


def main(fname, width, *args, **kwargs):
    geometry_options = {"right": "2cm", "left": "2cm"}
    doc = Document(fname, geometry_options=geometry_options)

    doc.append('Introduction.')

    with doc.create(Section('I am a section')):
        doc.append('Take a look at this beautiful plot:')

        with doc.create(Figure(position='htbp')) as plot:
            plot.add_plot(width=NoEscape(width), *args, **kwargs)
            plot.add_caption('Chart 1')
        #doc.append('Chart 1')

        with doc.create(Figure(position='htbp')) as plot:
            plot.add_plot(width=NoEscape(width), *args, **kwargs)
            plot.add_caption('Chart 2')
        #doc.append('Chart 2')

    doc.append('Conclusion.')

    doc.generate_pdf(compiler='pdflatex', clean=False)


if __name__ == '__main__':

    #getting authentication code
    authCode = getAuthCode('DanishYasin','Alpha103')
    
    #first graph
    dfBrazil = get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/stock-of-foreign-holders-of-em-local-currency-denominated-government-debt-by-investor-type-in-brazil-chart.csv')
    objects = dfBrazil['date'].tolist()
    benchMark = dfBrazil['benchmark-driven investors'].tolist()
    unconInvest = dfBrazil['unconstrained investors'].tolist()
    y_pos = np.arange(len(objects))
    #______________________________________
    dfMexico = get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/stock-of-foreign-holders-of-em-local-currency-denominated-government-debt-by-investor-type-in-mexico-chart.csv')
    mex_obj = dfMexico['date'].tolist()
    mex_benchMark = dfMexico['benchmark-driven investors'].tolist()
    mex_unconInvest = dfMexico['unconstrained investors'].tolist()
    mex_y_pos = np.arange(len(mex_obj))
    #______________________________________
    dfIndo = get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/stock-of-foreign-holders-of-em-local-currency-denominated-government-debt-by-investor-type-in-indonesia-chart.csv')
    indo_obj = dfIndo['date'].tolist()
    indo_benchMark = dfIndo['benchmark-driven investors'].tolist()
    indo_unconInvest = dfIndo['unconstrained investors'].tolist()
    indo_y_pos = np.arange(len(indo_obj))
    #______________________________________
    dfSAfr = get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/stock-of-foreign-holders-of-em-local-currency-denominated-government-debt-by-investor-type-in-south-africa-chart.csv')
    SAfr_obj = dfSAfr['date'].tolist()
    SAfr_benchMark = dfSAfr['benchmark-driven investors'].tolist()
    SAfr_unconInvest = dfSAfr['unconstrained investors'].tolist()
    SAfr_y_pos = np.arange(len(SAfr_obj))
    #______________________________________
    dfPol = get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/stock-of-foreign-holders-of-em-local-currency-denominated-government-debt-by-investor-type-in-poland-chart.csv')
    Pol_obj = dfPol['date'].tolist()
    Pol_benchMark = dfPol['benchmark-driven investors'].tolist()
    Pol_unconInvest = dfPol['unconstrained investors'].tolist()
    Pol_y_pos = np.arange(len(Pol_obj))
    #______________________________________
    dfMal = get_data_TrounceFlow(authCode,'https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/stock-of-foreign-holders-of-em-local-currency-denominated-government-debt-by-investor-type-in-malaysia-chart.csv')
    Mal_obj = dfMal['date'].tolist()
    Mal_benchMark = dfMal['benchmark-driven investors'].tolist()
    Mal_unconInvest = dfMal['unconstrained investors'].tolist()
    Mal_y_pos = np.arange(len(Mal_obj))
    #______________________________________


    geometry_options = {"margin":"0.5in"}
    doc = Document('matplotlib_ex-dpi', geometry_options=geometry_options,documentclass='report', document_options=['12pt, notitlepage'])
    #doc.preamble.append(NoEscape(r'\linespread{1.8}'))
    Command('linespread','1.6')
    # doc.append('Introduction.')

    # with doc.create(Section('I am a section')):
    #     doc.append('Take a look at this beautiful plot:')



    with doc.create(Figure(position='h!')) as plotgrid:
        #first graph
        plt.bar(y_pos, benchMark, align='center', alpha=0.5)
        plt.bar(y_pos, unconInvest,bottom=benchMark, align='center', alpha=1, color="#f3e151")
        plt.xticks(y_pos, objects,fontsize=9, rotation=30)
        plt.ylabel('USD bn')
        plt.title('Brazil')

        with doc.create(SubFigure(position='b',width=NoEscape(r'0.5\linewidth'))) as Leftplot:
            Leftplot.add_plot(width=NoEscape(r'\linewidth'), dpi=300)

        plt.clf()
        #Second graph
        plt.bar(mex_y_pos, mex_benchMark, align='center', alpha=0.5)
        plt.bar(mex_y_pos, mex_unconInvest,bottom=mex_benchMark, align='center', alpha=1, color="#f3e151")
        plt.xticks(mex_y_pos, mex_obj, fontsize=9, rotation=30)
        plt.ylabel('USD bn')
        plt.title('Mexico')
            
        with doc.create(SubFigure(position='b',width=NoEscape(r'0.5\linewidth'))) as Rightplot:
            Rightplot.add_plot(width=NoEscape(r'\linewidth'), dpi=300)

        plt.clf()
        doc.append(NewLine())
        #third graph
        plt.bar(indo_y_pos, indo_benchMark, align='center', alpha=0.5)
        plt.bar(indo_y_pos, indo_unconInvest,bottom=indo_benchMark, align='center', alpha=1, color="#f3e151")
        plt.xticks(indo_y_pos, indo_obj,fontsize=9, rotation=30)
        plt.ylabel('USD bn')
        plt.title('Indonesia')

        with doc.create(SubFigure(position='b',width=NoEscape(r'0.5\linewidth'))) as Leftplot:
            Leftplot.add_plot(width=NoEscape(r'\linewidth'), dpi=300)
            
        plt.clf()
        #Fourth graph
        plt.bar(SAfr_y_pos, SAfr_benchMark, align='center', alpha=0.5)
        plt.bar(SAfr_y_pos, SAfr_unconInvest,bottom=SAfr_benchMark, align='center', alpha=1, color="#f3e151")
        plt.xticks(SAfr_y_pos, SAfr_obj, fontsize=9, rotation=30)
        plt.ylabel('USD bn')
        plt.title('South Africa')
            
        with doc.create(SubFigure(position='b',width=NoEscape(r'0.5\linewidth'))) as Rightplot:
            Rightplot.add_plot(width=NoEscape(r'\linewidth'), dpi=300)
        
        plt.clf()
        doc.append(NewLine())
        #Fifth graph
        plt.bar(Pol_y_pos, Pol_benchMark, align='center', alpha=0.5)
        plt.bar(Pol_y_pos, Pol_unconInvest,bottom=Pol_benchMark, align='center', alpha=1, color="#f3e151")
        plt.xticks(Pol_y_pos, Pol_obj,fontsize=9, rotation=30)
        plt.ylabel('USD bn')
        plt.title('Poland')

        with doc.create(SubFigure(position='b',width=NoEscape(r'0.5\linewidth'))) as Leftplot:
            Leftplot.add_plot(width=NoEscape(r'\linewidth'), dpi=300)

        plt.clf()
        #Sixth graph
        plt.bar(Mal_y_pos, Mal_benchMark, align='center', alpha=0.5)
        plt.bar(Mal_y_pos, Mal_unconInvest,bottom=Mal_benchMark, align='center', alpha=1, color="#f3e151")
        plt.xticks(Mal_y_pos, Mal_obj, fontsize=9, rotation=30)
        plt.ylabel('USD bn')
        plt.title('Malaysia')
            
        with doc.create(SubFigure(position='b',width=NoEscape(r'0.5\linewidth'))) as Rightplot:
            Rightplot.add_plot(width=NoEscape(r'\linewidth'), dpi=300)


        plotgrid.add_caption('Foreign Holdings of Local Currency Government Debt: benchmark-driven vs unconstrained')

        #doc.append('Chart 1')
            
    #doc.append('Conclusion.')

    doc.generate_pdf(compiler='pdflatex', clean=False)