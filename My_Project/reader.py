import csv

#CSV to list
def read_csv(path):
  with open(path,'r') as csv_file:
    csv_reader=csv.DictReader(csv_file,delimiter=',')
    data=[]
    for country in csv_reader:
      data.append(country)
  return data

#data=read_csv('./My_Project/world_population.csv')