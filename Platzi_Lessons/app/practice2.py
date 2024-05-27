import csv
import matplotlib.pyplot as plt

def generate_bar_chart(labels,values):
  if not isinstance(labels, list) or not isinstance(values, list):
    raise ValueError("Both labels and values must be lists")

  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

def read_csv(path):
  with open(path,'r') as csv_file:
    csv_reader=csv.DictReader(csv_file,delimiter=',')
    data=[]
    for row in csv_reader:
      data.append(row)

  return data

def totaller(data):
  for diccionario in data:
    diccionario['2022']=diccionario['2022 Population']
    diccionario['2020']=diccionario['2020 Population']
    diccionario['2015']=diccionario['2015 Population']
    diccionario['2010']=diccionario['2010 Population']
    diccionario['2000']=diccionario['2000 Population']
    diccionario['1990']=diccionario['1990 Population']
    diccionario['1980']=diccionario['1980 Population']
    diccionario['1970']=diccionario['1970 Population']
    del diccionario['2022 Population']
    del diccionario['2020 Population']
    del diccionario['2015 Population']
    del diccionario['2010 Population']
    del diccionario['2000 Population']
    del diccionario['1990 Population']
    del diccionario['1980 Population']
    del diccionario['1970 Population']
    del diccionario['Rank']      
    del diccionario['CCA3']      
    del diccionario['Capital']
    del diccionario['Continent']
    del diccionario['Area (km²)']
    del diccionario['Density (per km²)']
    del diccionario['Growth Rate']
    del diccionario['World Population Percentage']
    #del diccionario['Country/Territory']
  return data

def specific(data,country):
  
  pais= list(filter(lambda paises:paises['Country/Territory']==country,data))
  del pais[0]['Country/Territory']
  return pais

if __name__ == '__main__':
  country=input('Ingrese un país: ')
  #print(specific(totaller(read_csv('./app/data.csv')),country))
  pais=specific(totaller(read_csv('./app/data.csv')),country)
  
  keys=list(pais[0].keys())
  values=list(pais[0].values())
  values=[int(x) for x in values]
  #print(pais)
  generate_bar_chart(keys,values)
  