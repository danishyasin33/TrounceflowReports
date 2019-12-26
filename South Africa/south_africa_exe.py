import south_africa_func

# Importing username and password for trounceflow

username='VaheCharchyan'

password='?????????????'

# Defining the max length of a text to appear on one line in a table cell

defined_text_w=52

# Importing general urls

url_zar='https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/\
{}-in-south-africa-chart-in-south-african-rand.csv'

url_usd='https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/\
{}-in-south-africa-chart.csv'

# Importing a list with elements which can be used to form a complete url

sub_url_list=['central-government-debt-stock-by-currency','composition-of-holdings','imf-fx-reserves',
              'external-debt-by-maturity','external-debt-by-currency',
              'international-portfolio-position','international-investment-position',
              'holdings-of-em-pension-funds','holdings-of-banks',
              'holdings-of-em-asset-management-companies','holdings-of-insurance-companies']

# Importing a list with keys for a data dictionary

key_list=['cgd_by_cur','lcgd_by_holder','fxr','ex_by_issuer',
            'ex_by_currency','ipp_pl','ipp_al','ds_pf','ds_b','ds_am','ds_ic']

# Creating a data dictionary

data_dic=south_africa_func.create_data_dic(key_list=key_list,username=username,password=password,
                                           url_zar=url_zar,url_usd=url_usd,sub_url_list=sub_url_list,
                                           defined_text_w=defined_text_w)

# Creating a tex file

south_africa_func.create_tex(file_name='south_africa.tex',data_dic=data_dic,main_dic=data_dic)

# Specifying a directory where the above created tex file is located

tmp_dir = 'C:\\Users\\Vahe\\Desktop\\Trounceflow\\latex auto\\South Africa'

# Creating a pdf doc

south_africa_func.create_pdf(file_name='new_south_africa.tex',tmp_dir=tmp_dir,pdf_name='Trounceflow_South_Africa')