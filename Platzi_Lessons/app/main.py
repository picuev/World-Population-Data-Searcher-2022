#import utils as us
#from utils import get_population (same carpets level)
import utils as us

data=[
  {
    'Country':'Colombia',
    'Population':54
  },
  {
    'Country':'Bolivia',
    'Population':47
  },
  {
    'Country':'Estados_Unidos',
    'Population':110
  }
]



def run():
  keys,values=us.get_population()
  print(keys,values)
  
  country=input('Ingrese el nombre de un pais:').title().strip()
  
  result=(us.population_by_country(data, country))
  print(result)

#El nombre del siguiente comando es -> Entry point y ayuda a no tener ambiguedad (script y llamado desde otro modulo)
if __name__=='__main__': 
  #execute archivo as script 
  run()
#solo si archivo está siendo ejecutado desde la terminal entonces que se ejecute
#script -> comando desde la terminal
#ejecutar una función desde otro archivo es la forma "modular"

#Evita que por el simple hecho de importar un módulo, este se empiece a ejecutar.
#Para evitar esto se puede modularizar los componentes