from reader import read_csv
import functools

# Load data from CSV file
data=read_csv('./My_Project/world_population.csv')

# Main function to get information
def master_info(land,option):
  database=data
  
  # Filtering for a specific country
  if option==1: 
    specific=list(filter(lambda x:x['Country/Territory']==land,database))
    specific=specific[0]
    return specific

  else:
    # Filtering countries by continent
    if option==2:
      database=list(filter(lambda x:x['Continent']==land,data))

    # Accumulate the necessary information
    Pop_2022=functools.reduce(lambda a,b: a + int(b['2022 Population']) ,database, 0)
    Pop_2020=functools.reduce(lambda a,b: a + int(b['2020 Population']) ,database, 0)
    Pop_2015=functools.reduce(lambda a,b: a + int(b['2015 Population']) ,database, 0)
    Pop_2010=functools.reduce(lambda a,b: a + int(b['2010 Population']) ,database, 0)
    Pop_2000=functools.reduce(lambda a,b: a + int(b['2000 Population']) ,database, 0)
    Pop_1990=functools.reduce(lambda a,b: a + int(b['1990 Population']) ,database, 0)
    Pop_1980=functools.reduce(lambda a,b: a + int(b['1980 Population']) ,database, 0)
    Pop_1970=functools.reduce(lambda a,b: a + int(b['1970 Population']) ,database, 0)
    Area=functools.reduce(lambda a,b: a + int(b['Area (km²)']) ,database, 0)
    WPP=functools.reduce(lambda a,b: a + float(b['World Population Percentage']) ,database, 0)
    
    # Calculate density and growth rate for continents and the world
    Density=round(Pop_2022/Area,4)
    Growth_Rate=round(((Pop_2022-Pop_2020)/Pop_2020)*100,4) # Simple model formula
    
    # notable_country: It's recognized by the number of inhabitants in 2022
    WPPL=[int(country['2022 Population']) for country in database]
    notable_country=list(filter(lambda x:int(x['2022 Population'])==int(max(WPPL)), database))
    notable_country=notable_country[0]['Country/Territory'],int(max(WPPL)) #tuple

    #Continent ranking according to WPP
    if option==2:
      
      #Abrevation for continent's name and ranking list
      CCA3_Rank={
        'Asia':('AS',1),
        'Africa':('AF',2),
        'Europe':('EU',3),
        'North America':('NA',4),
        'South America':('SA',5),
        'Oceania':('OC',6)
      }

      Continent={
        'Rank':CCA3_Rank.get(land,('Not Found','Not Found'))[1],
        'CCA3':CCA3_Rank.get(land,('Not Found','Not Found'))[0],
        'Country/Territory':land,
        'Notable country': notable_country,
        '2022 Population' : Pop_2022,
        '2020 Population' : Pop_2020,
        '2015 Population' : Pop_2015,
        '2010 Population' : Pop_2010,
        '2000 Population' : Pop_2000,
        '1990 Population' : Pop_1990,
        '1980 Population' : Pop_1980,
        '1970 Population' : Pop_1970,
        'Area (km²)':Area,
        'Density (per km²)':Density,
        'Growth Rate':Growth_Rate,
        'World Population Percentage' : WPP
      }

      return Continent
    
    elif option==3: 
      #Dictionary of information for the planet
      planet={
        'Rank':'N/A',
        'CCA3': 'N/A',
        'Country/Territory': land,
        'Notable continent': 'Asia',
        'Notable country': notable_country,
        '2022 Population' : Pop_2022,
        '2020 Population' : Pop_2020,
        '2015 Population' : Pop_2015,
        '2010 Population' : Pop_2010,
        '2000 Population' : Pop_2000,
        '1990 Population' : Pop_1990,
        '1980 Population' : Pop_1980,
        '1970 Population' : Pop_1970,
        'Area (km²)':Area,
        'Density (per km²)':Density,
        'Growth Rate':Growth_Rate,
        'World Population Percentage' : WPP
      }

      return planet

# Function to generate population percentage pie charts
def population_percentage_pie(option,land_name='Asia'):
  labels=[]
  values=[]
  top=[]
  other_countries=[]
  if option is False: #The pie chart only shows countries with a population percentage higher than the parameter
    land_data=list(filter(lambda x:x['Continent']==land_name,data))

    # Specific parameters for each continent
    parameter={
      'South America':0.15,
      'North America':0.10,
      'Oceania':0.05,
      'Africa':0.35,
      'Asia':1.2,
      'Europe':0.15
    }
    
    for country in land_data:
      if float(country['World Population Percentage'])<=parameter.get(land_name,0.05):
        other_countries.append(country)
      else:
        float(country['World Population Percentage'])
        top.append(country)

    other_countries={
      'Country/Territory':'Other countries',
      'World Population Percentage': functools.reduce(lambda x,y:x+float(y['World Population Percentage']), other_countries,0)
    }

    top.append(other_countries)
    
    labels=[country['Country/Territory'] for country in top]
    values=[country['World Population Percentage'] for country in top]
    
  elif option is True: #For the world option
    
    labels=(f"Asia ({round((master_info('Asia',2))['World Population Percentage'],2)})%",
            f"Africa ({round((master_info('Africa',2))['World Population Percentage'],2)})%",
            f"Europe ({round((master_info('Europe',2))['World Population Percentage'],2)})%",
            f"North America ({round((master_info('North America',2))['World Population Percentage'],2)})%",
            f"South America ({round((master_info('South America',2))['World Population Percentage'],2)})%",
            f"Oceania ({round((master_info('Oceania',2))['World Population Percentage'],2)})%")
    
    values=((master_info('Asia',2))['World Population Percentage'], 
            (master_info('Africa',2))['World Population Percentage'], 
            (master_info('Europe',2))['World Population Percentage'], 
            (master_info('North America',2))['World Population Percentage'], 
            (master_info('South America',2))['World Population Percentage'], 
            (master_info('Oceania',2))['World Population Percentage'])

  return labels,values
  
    