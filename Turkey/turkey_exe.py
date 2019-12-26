import turkey_func

# Importing username and password for trounceflow

username='VaheCharchyan'

password='?????????????'

# Defining the max length of a text to appear on one line in a table cell

defined_text_w=52

# Importing general urls

url_try='https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/{}-in-turkey-chart-in-turkish-lira.csv'

url_usd='https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/{}-in-turkey-chart.csv'

# Importing a list with elements which can be used to form a complete url

sub_url_list=['central-government-debt-stock-by-instrument','central-government-debt-stock-by-currency',
              'composition-of-holdings','bank-deposits-by-currency',
              'holdings-of-insurance-companies','holdings-of-banks',
              'composition-of-holdings-domestic-debt-securities-issued-by-banks',
              'composition-of-holdings-domestic-debt-securities-issued-by-non-financial-companies']

# Importing a list with keys for a data dictionary

key_list=['cgd_by_inst','cgd_by_cur','lcgd_by_holder','bd_by_cur','ds_ic',
          'ds_b','dds_by_banks','dds_by_nfc']

# Creating a data dictionary

data_dic=turkey_func.create_data_dic(key_list=key_list,username=username,password=password,
                                           url_try=url_try,url_usd=url_usd,sub_url_list=sub_url_list,
                                           defined_text_w=defined_text_w)

# Creating a tex file

turkey_func.create_tex(file_name='turkey.tex',data_dic=data_dic,main_dic=data_dic)

# Specifying a directory where the above created tex file is located

tmp_dir = 'C:\\Users\\Vahe\\Desktop\\Trounceflow\\latex auto\\Turkey'

# Creating a pdf doc

turkey_func.create_pdf(file_name='new_turkey.tex',tmp_dir=tmp_dir,pdf_name='Trounceflow_Turkey')