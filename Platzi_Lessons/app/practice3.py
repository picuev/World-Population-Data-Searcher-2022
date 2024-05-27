import csv
import charts
def read_csv(path):
  with open(path,'r') as csv_file:
    reader_csv=csv.DictReader(csv_file,delimiter=',')
    data=[]
    for row in reader_csv:
      data.append(row)
  return data

def convert(data):
  
  data=list(filter(lambda x:x['Continent']=='South America',data))
  countries=list(map(lambda x:x['Country/Territory'],data))
  percentage=list(map(lambda x:x['World Population Percentage'],data))
  
  """for country in data:
    country[country['Country/Territory']]=country['World Population Percentage']
    
    del country['2022 Population']
    del country['2020 Population']
    del country['2015 Population']
    del country['2010 Population']
    del country['2000 Population']
    del country['1990 Population']
    del country['1980 Population']
    del country['1970 Population']
    del country['Rank']      
    del country['CCA3']      
    del country['Capital']
    del country['Continent']
    del country['Area (km²)']
    del country['Density (per km²)']
    del country['Growth Rate']
    del country['World Population Percentage']
    del country['Country/Territory']
  
  labels=[str(country.keys()).replace("dict_keys(['","").replace("'])","")for country in data]
  values=[str(country.values()).replace("dict_values(['","").replace("'])","") for country in data]
  values=[float(x) for x in values]"""
  labels=countries
  values=percentage
  return labels,values
  #return data

def run():
  data=read_csv('./app/data.csv')
  #data=convert(data)
  #print(data)
  
  labels,values=convert(data)
  #print(data)
  #print(values)
  charts.generate_pie_chart(labels,values)

if __name__=='__main__':
  run()  