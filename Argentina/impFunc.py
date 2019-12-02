def getAuthCode(username, password):
    import requests 
    import pandas
    import json

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
    import json


    res_data = requests.get(url, headers=headers)

    data_text=res_data.text

    data_text_list=data_text.split('\r\n')

    col_names=data_text_list[0].split(',')

    data=pandas.DataFrame()

    for i in range(len(col_names)):
        data[col_names[i]]=[data_text_list[j].split(',')[i] for j in range(1,len(data_text_list)-1)]
    
    data.iloc[:,1:] = data.iloc[:,1:].apply(pandas.to_numeric)

    data['date']=pandas.to_datetime(data['date'])
    data['date'] = data['date'].dt.strftime('%d/%m/%Y')

    data = data.tail(4)
    data['Total'] = data.iloc[:,1:].sum(axis=1)
    data['Total'] = data['Total'].round(2)
 
    data.iloc[:,1:] = data.iloc[:,1:].applymap("{:,}".format)

    return data
