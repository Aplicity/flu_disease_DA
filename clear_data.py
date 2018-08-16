import pandas as pd

data01=pd.read_csv('疾病数据01.csv')
data02=pd.read_csv('疾病数据02.csv')
data03=pd.read_csv('疾病数据03.csv')
data04=pd.read_csv('疾病数据04.csv')
data05=pd.read_csv('疾病数据05.csv')

data=pd.merge(data01,data02,how='outer')
data=pd.merge(data,data03,how='outer')
data=pd.merge(data,data04,how='outer')
data=pd.merge(data,data05,how='outer')

data.to_csv('merge_data.csv')

year=[]
month=[]
k=1
for line in data['检测日期']:
    lineArr=line.split('-')
    year.append(lineArr[0])
    month.append(lineArr[1])
data['year']=year
data['month']=month
data['date-city']=data['year'].map(str)+'-'+data['month'].map(str)+data['医疗机构市']

weather_city=pd.read_csv('weather_city.csv')
for i in range(len(weather_city['month'])):
    if weather_city.iloc[i,6]==1:
        weather_city.iloc[i,6]='01'
    elif weather_city.iloc[i,6]==2:
        weather_city.iloc[i,6]='02'
    elif weather_city.iloc[i,6]==3:
        weather_city.iloc[i,6]='03'
    elif weather_city.iloc[i,6]==4:
        weather_city.iloc[i,6]='04'
    elif weather_city.iloc[i,6]==5:
        weather_city.iloc[i,6]='05'
    elif weather_city.iloc[i,6]==6:
        weather_city.iloc[i,6]='06'
    elif weather_city.iloc[i,6]==7:
        weather_city.iloc[i,6]='07'
    elif weather_city.iloc[i,6]==8:
        weather_city.iloc[i,6]='08'
    elif weather_city.iloc[i,6]==9:
        weather_city.iloc[i,6]='09'
weather_city['date-city']=weather_city['year'].map(str)+'-'+weather_city['month'].map(str)+weather_city['tzm']

data=data[['患者性别','患者职业','是否为疑似食源性病例', '是否采集生物样本','初步诊断','食品名称', '食品分类','医疗机构市']]
data.to_csv('DT_data.csv')


patient_data=data.groupby('date-city').count()
patient_data.to_csv('patient_data.csv')

patient_data['date-city']=patient_data.index
totData=pd.merge(weather_city,patient_data,left_on='date-city',right_on='date-city')
