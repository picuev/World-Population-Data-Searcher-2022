import csv

""" 
def read_csv(path):
  with open(path,'r') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    header=next(csv_reader)
    data=[]
    for row in csv_reader:
      iterable=zip(header,row)
      #print(list(iterable))
      country_dict={key:value for key,value in iterable}
      data.append(country_dict)
    return data

"""
def read_csv(path):
  with open(path,'r') as csv_file:
    reader_csv=csv.DictReader(csv_file,delimiter=',')
    data=[]
    for row in reader_csv:
      data.append(row)
    return data
   
if __name__=='__main__':
  print(read_csv('./app/data.csv'))
  