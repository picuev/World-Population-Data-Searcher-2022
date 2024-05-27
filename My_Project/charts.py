import matplotlib.pyplot as plt

def generate_bar_chart(labels,values): #Create a bar graph

  fig, ax = plt.subplots()
  
  ax.bar(labels,values)
  plt.show()

def generate_pie_chart(labels,values): #Create a pie graph
  
  fig,ax=plt.subplots()
  ax.pie(values,labels=labels) 
  
  ax.axis('equal')
  plt.show()