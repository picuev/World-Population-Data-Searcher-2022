import matplotlib
import matplotlib.pyplot as plt

def generate_bar_chart(labels,values):
  
  fig, ax = plt.subplots()
  #son dos valores que nos da la librería, fig es como la figura y ax se refire a las coordenadas donde  vamos a empezar a graficar
  ax.bar(labels,values)
  plt.show()

def generate_pie_chart(labels,values):
  fig,ax=plt.subplots()
  ax.pie(values,labels=labels) #aquí primero values yluego labels
  ax.axis('equal')#(se acomode de forma de círculos) equitativa.
  plt.show()

#Ejecutar como script
if __name__=='__main__':
  labels=['a','b','c']
  values=[50,80,300]
 #generate_bar_chart(labels,values)
  generate_pie_chart(labels,values)