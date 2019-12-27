import israel_func

# Importing username and password for trounceflow

username='VaheCharchyan'

password='?????????????'

# Defining the max length of a text to appear on one line in a table cell

defined_text_w=52

# Importing general urls

url_ils='https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/{}-in-israel-chart-in-israeli-new-sheqel.csv'

url_usd='https://www.trounceflow.com/api/v1/chart/granularbondholdingschart/{}-in-israel-chart.csv'

# Importing a list with elements which can be used to form a complete url

sub_url_list=['central-government-debt-stock-by-residency-of-holders','central-government-debt-stock-by-currency',
              'composition-of-holdings','imf-fx-reserves',
              'international-portfolio-position','international-investment-position']

# Importing a list with keys for a data dictionary

key_list=['cgd_by_holder','cgd_by_cur','lcgd_by_holder','fxr','ipp_pl','ipp_al']

# Creating a data dictionary

data_dic=israel_func.create_data_dic(key_list=key_list,username=username,password=password,
                                           url_ils=url_ils,url_usd=url_usd,sub_url_list=sub_url_list,
                                           defined_text_w=defined_text_w)

# Creating a tex file

israel_func.create_tex(file_name='israel.tex',data_dic=data_dic,main_dic=data_dic)

# Specifying a directory where the above created tex file is located

tmp_dir = 'C:\\Users\\Vahe\\Desktop\\Trounceflow\\latex auto\\Israel'

# Creating a pdf doc

israel_func.create_pdf(file_name='new_israel.tex',tmp_dir=tmp_dir,pdf_name='Trounceflow_Israel')