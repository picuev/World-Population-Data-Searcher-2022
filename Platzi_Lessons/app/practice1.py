import csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplot

def read_csv(path):
  with open(path,'r') as csv_file:
    reader_csv=csv.DictReader(csv_file, delimiter=',')
    data=[]
    for row in reader_csv:
      data.append(row)
  return data

def prepare_data(data,name_country):
  specific_country=list(filter(lambda x:x['Country/Territory']==name_country,data))
  specific_country[0]['2022']=specific_country[0]['2022 Population']
  specific_country[0]['2020']=specific_country[0]['2020 Population']
  specific_country[0]['2015']=specific_country[0]['2015 Population']
  specific_country[0]['2010']=specific_country[0]['2010 Population']
  specific_country[0]['2000']=specific_country[0]['2000 Population']
  specific_country[0]['1990']=specific_country[0]['1990 Population']
  specific_country[0]['1980']=specific_country[0]['1980 Population']
  specific_country[0]['1970']=specific_country[0]['1970 Population']
  del specific_country[0]['2022 Population']
  del specific_country[0]['2020 Population']
  del specific_country[0]['2015 Population']
  del specific_country[0]['2010 Population']
  del specific_country[0]['2000 Population']
  del specific_country[0]['1990 Population']
  del specific_country[0]['1980 Population']
  del specific_country[0]['1970 Population']
  del specific_country[0]['Rank']      
  del specific_country[0]['CCA3']      
  del specific_country[0]['Capital']
  del specific_country[0]['Continent']
  del specific_country[0]['Area (km²)']
  del specific_country[0]['Density (per km²)']
  del specific_country[0]['Growth Rate']
  del specific_country[0]['World Population Percentage']
  del specific_country[0]['Country/Territory']
  return specific_country

def convert_to_dataset(specific_country):
  labels=list(specific_country[0].keys())
  values=list(specific_country[0].values())
  values=[int(x) for x in values]
  return labels,values
  
def generate_bar_chart(labels,values):
  fig,ax=plt.subplots()
  ax.bar(labels,values)
  plt.show()

def run():
  country=input('Enter a Country Name -> ')
  data=read_csv('./app/data.csv') #Data get all the information of all countries
  data=prepare_data(data,country) #Now the data is just about just one country
  labels,values=convert_to_dataset(data)
  generate_bar_chart(labels,values)
  
if __name__=='__main__':
  run()