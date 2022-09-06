from cgitb import reset
import pandas as pd
import requests
import bs4

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson'
params ={'serviceKey' : 'gyfLzh4Yf4kl5JwzCAxVCJOaBqnHF2zaG9xjGYYPBpTqIhGlzxqt/DI8er35/3BeasJc2QCJz3xVwObVIxzupA==', 
         'pageNo' : '1', 'numOfRows' : '100000', 'startCreateDt' : '20200815', 'endCreateDt' : '20220906'}

row_list,name_list,value_list=[],[],[]
response= requests.get(url,params=params)
bs = bs4.BeautifulSoup(response.content,'lxml-xml')
rows = bs.find_all('item')
rows.reverse()
for i in rows[0]:
    name_list.append(i.name)
    
for i in rows:
    for j in i:
        value_list.append(j.text)
    if len(value_list) != len(name_list):
        value_list.insert(7,'None')
    row_list.append(value_list)
    
    value_list=[]
  
df = pd.DataFrame(row_list,columns=name_list)
df.drop(['gubunCn','gubunEn','stdDay','updateDt','localOccCnt','overFlowCnt','qurRate','seq','isolClearCnt'],axis=1,inplace=True)
df['createDt'] = df['createDt'].str[0:10]
df = df[df['gubun']=='서울']
print(df)

