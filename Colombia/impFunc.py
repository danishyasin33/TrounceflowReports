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

    data['date']=pandas.to_datetime(data['date'])           #converting date column to datetime type
    data['date'] = data['date'].dt.strftime('%d/%m/%Y')     #formatting that date

    data = data.tail(4)
    data['Total'] = data.iloc[:,1:].sum(axis=1)             #calculating total by adding all columns except date  
    data['Total'] = data['Total'].round(2)                  #rounding of total column
 
    data.iloc[:,1:] = data.iloc[:,1:].applymap("{:,}".format)   #applying thousand separator formatting

    return data
