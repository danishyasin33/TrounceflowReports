def col_names_extract(x):

    col_names=[]

    if len(x)%2!=0:

        for i in range(len(x)):

            if i%2==0:

                x2=x[i].split(',')

                for j in range(len(x2)):

                    col_names.append(x2[j])

            else:

                col_names.append(x[i])

    else:

        for i in range(len(x)):

            if i%2!=0:

                x2=x[i].split(',')

                for j in range(len(x2)):

                    col_names.append(x2[j])

            else:

                col_names.append(x[i])

    col_names=[i for i in col_names if i!='']
    
    return col_names

#####################################################################################

def get_data(username,password,url):

    import requests 

    import pandas as pd

    data = {
      'username': username,
      'password': password
    }

    res_token = requests.post('https://www.trounceflow.com/api/v1/auth-token/', data=data)

    token=res_token.text.replace('{','').replace('}','').replace('"','').replace('token:','Token ')

    headers = {
        'Authorization': token,
    }

    res_data = requests.get(url, headers=headers)

    data_text=res_data.text

    data_text_list=data_text.split('\r\n')
    
    try:

        col_names=data_text_list[0].split(',')

        data=pd.DataFrame()

        for i in range(len(col_names)):

            if col_names[i]=='date':

                data[col_names[i]]=[data_text_list[j].split(',')[i] for j in range(1,len(data_text_list)-1)]

            else:

                data[col_names[i]]=[data_text_list[j].split(',')[i] for j in range(1,len(data_text_list)-1)]
                
    except:
        
        temp_split=data_text_list[0].split('"')
        
        col_names=col_names_extract(temp_split)

        data=pd.DataFrame()

        for i in range(len(col_names)):

            if col_names[i]=='date':

                data[col_names[i]]=[data_text_list[j].split(',')[i] for j in range(1,len(data_text_list)-1)]

            else:

                data[col_names[i]]=[data_text_list[j].split(',')[i] for j in range(1,len(data_text_list)-1)]
            
    return data

####################################################################################################

def str_to_num(x):
    
    if x=='':
        
        return None
    
    else:
        
        return float(x)

#####################################################################################################

def month_year_extract(x):
    
    ml=['January','February','March','April','May','June','July','August','September','October','November','December']
    
    nm=int(x.split('-')[::-1][1])
    
    year=' '+x.split('-')[::-1][2]
    
    return ml[nm-1][:3]+year

####################################################################################################

def comma_placement(a):

    before_dot=str(a).split('.')[0]

    after_dot=str(a).split('.')[1]

    minus_out=before_dot.split('-')[-1]

    if len(before_dot.split('-'))==2:

        psign='-'

    else:

        psign=''

    if len(minus_out)>3:

        minus_out=','.join([minus_out[:-3],minus_out[-3:]])

    before_dot=psign+minus_out

    a='.'.join([before_dot,after_dot]) #before_dot

    return a

###################################################################################################

def manipulate_num(x): #sub_name,
    
    import pandas as pd
    
    if pd.isnull(x):
        
        return ''
    
    else:

        x="{0:.2f}".format(x)#\hspace{0.1cm}

        x=comma_placement(x)

    return x

###################################################################################################

def make_camel(x):
    
    sx=x.split(' ')
    
    no_camel_list=['and','to','in','with','(except','reserves)','of','for','from']
    
    abb_list=['Fx','Sdrs','Imf','Ils']
    
    sx=[i if i in no_camel_list else i.title() for i in sx]
    
    sx=[i.replace('Sdrs','Sdr').upper() if i in abb_list else i for i in sx]
    
    nx=' '.join(sx)
    
    return nx

####################################################################################################

def augment_data(data):
    
    import pandas as pd

    data.sort_values(by='date',ascending=False,inplace=True)

    data.reset_index(inplace=True)

    del data['index']

    for i in list(data.columns):
        
        if i=='date':
            
            continue

        elif i=='local currency_':

            data['zar']=data[i].apply(str_to_num)

            data.drop(i,axis=1,inplace=True)

        elif i=='others_':

            data['other']=data[i].apply(str_to_num)

            data.drop(i,axis=1,inplace=True)

        else:

            data[i]=data[i].apply(str_to_num)

    col_names_list=list(data.columns)

    col_names_list.remove('date')

    data['total']=data[col_names_list].sum(axis=1)

    return data

####################################################################################################

def specific_augment_data(data):
    
    import pandas as pd

    data.sort_values(by='date',ascending=False,inplace=True)

    data.reset_index(inplace=True)

    del data['index']

    col_names_list=list(data.columns)

    col_names_list.remove('date')

    for i in col_names_list:

        data[i]=data[i].apply(str_to_num)

    data['total']=data[col_names_list].sum(axis=1)

    new_col_names_list=list(set([i.replace('short-term','').replace('long-term','').strip() 
                                             for i in data.columns]))

    for i in new_col_names_list:

        try:

            data[i]=data[i+' short-term']+data[i+' long-term']

            data.drop([i+' short-term',i+' long-term'],axis=1,inplace=True)

        except:

            print('{} is unique'.format(i))

    temp_merge=data[['date','other sectors','unclassified','total']]

    data.drop(['other sectors','unclassified','total'],axis=1,inplace=True)

    data=pd.merge(data,temp_merge,on='date')
    
    return data
#########################################################################################

def create_data_dic(key_list,username,password,url_ils,url_usd,sub_url_list,defined_text_w):
    
    import pandas as pd
    
    import textwrap
    
    data_dic={}

    data_dic['exe_sum']={}

    for i in range(len(key_list)):
        
        ils_data=get_data(username=username,password=password,url=url_ils.format(sub_url_list[i]))

        usd_data=get_data(username=username,password=password,url=url_usd.format(sub_url_list[i]))
        
        if key_list=='ex_by_issuer':
            
            ils_data=specific_augment_data(ils_data)
            
            usd_data=specific_augment_data(usd_data)
            
        else:
            
            ils_data=augment_data(ils_data)
            
            usd_data=augment_data(usd_data)

        data_dic['exe_sum'][key_list[i]]={}

        data_dic['exe_sum'][key_list[i]]['date']=month_year_extract(ils_data.iloc[0]['date'])

        data_dic['exe_sum'][key_list[i]]['usd']=manipulate_num(usd_data.iloc[0]['total'])

        data_dic['exe_sum'][key_list[i]]['ils']=manipulate_num(ils_data.iloc[0]['total'])
    
        data_dic[key_list[i]]={}

        data_dic[key_list[i]]['usd']={}

        data_dic[key_list[i]]['ils']={}

        temp_name_list=[]

        temp_name_list2=[]

        usd_col_name=list(usd_data.columns)

        ils_col_name=list(ils_data.columns)

        for j in range(len(ils_col_name)):

            temp_name_usd=usd_col_name[j].replace(',','').replace(' - ','_').replace(' ','_').replace('-','_').replace('(','').replace(')','')

            temp_name_ils=ils_col_name[j].replace(',','').replace(' - ','_').replace(' ','_').replace('-','_').replace('(','').replace(')','')

            if usd_col_name[j]=='date':

                data_dic[key_list[i]]['usd'][temp_name_usd]=[month_year_extract(usd_data.iloc[k][usd_col_name[j]]) for k in range(5)]

            else:

                data_dic[key_list[i]]['usd'][temp_name_usd]=[manipulate_num(usd_data.iloc[k][usd_col_name[j]]) for k in range(5)]

            if ils_col_name[j]=='date':

                data_dic[key_list[i]]['ils'][temp_name_ils]=[month_year_extract(ils_data.iloc[k][ils_col_name[j]]) for k in range(5)]

            else:

                temp_name_list.append(textwrap.fill(make_camel(ils_col_name[j]),defined_text_w).replace('\n','\\\\'))

                data_dic[key_list[i]]['ils'][temp_name_ils]=[manipulate_num(ils_data.iloc[k][ils_col_name[j]]) for k in range(5)]

                temp_name_list2.append(temp_name_ils)

        data_dic[key_list[i]]['name2']=temp_name_list2

        data_dic[key_list[i]]['name']=temp_name_list
        
    return data_dic

########################################################################################

def create_tex(file_name,data_dic,main_dic):
    
    import jinja2

    import os

    from jinja2 import Template
    
    #from pdflatex import PDFLaTeX
    
    latex_jinja_env = jinja2.Environment(
    block_start_string = '\BLOCK{',
    block_end_string = '}',
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    comment_start_string = '\#{',
    comment_end_string = '}',
    line_statement_prefix = '%%',
    line_comment_prefix = '%#',
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.FileSystemLoader(os.path.abspath('.')))
    
    
    template = latex_jinja_env.get_template(file_name)

    #os.path.realpath('./templates/template.tex')

    options = data_dic
    renderer_template = template.render(**options,main_dic=main_dic)

    project = "./"

    #build_d = "{}build/".format(project)

    out_file = "new_"+file_name

    #if not os.path.exists(build_d):  # create the build directory if not existing
        #os.makedirs(build_d)

    with open(out_file, "w") as f:  # saves tex_code to outpout file
        f.write(renderer_template)
        
########################################################################################

def create_pdf(file_name,tmp_dir,pdf_name):

    from subprocess import Popen

    import subprocess
    
    import os

    for i in range(2):

        in_tmp_path = os.path.join(tmp_dir, file_name)

        p = Popen(['pdflatex', in_tmp_path, '-job-name', pdf_name, '-output-directory', tmp_dir],stdout=subprocess.PIPE)

        p.communicate()
        
        if i==1:

            os.unlink(pdf_name+'.log')

            os.unlink(pdf_name+'.aux')

            os.unlink(pdf_name+'.toc')

            os.unlink(pdf_name+'.out')
            
########################################################################################