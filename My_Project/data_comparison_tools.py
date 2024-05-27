from population_analysis import master_info
from charts import generate_bar_chart, generate_pie_chart

def get_population(country_dict,summary):
  # Creates a dictionary of population data for a given country 
  population_dict={
    '2022':int(country_dict['2022 Population']),
    '2020':int(country_dict['2020 Population']),
    '2015':int(country_dict['2015 Population']),
    '2010':int(country_dict['2010 Population']),
    '2000':int(country_dict['2000 Population']),
    '1990':int(country_dict['1990 Population']),
    '1980':int(country_dict['1980 Population']),
    '1970':int(country_dict['1970 Population'])
  }
  # Optionally print a summary of the population data
  if summary is True:
    for key,value in population_dict.items():
      print(key,':',value)

  # Return the population data as labels and values
  labels=population_dict.keys() 
  values=population_dict.values()
  return labels,values

def get_specific_info(land_data,option,option_population):
  options={
    1:'Population',
    2:'Area (km²)',
    3:'Density (per km²)',
    4:'Growth Rate',
    5:'World Population Percentage',
    6:'Rank'
  }  

  options_population={
    1 :'1970 Population',
    2 :'1980 Population',
    3 :'1990 Population',
    4 :'2000 Population',
    5 :'2010 Population',
    6 :'2015 Population',
    7 :'2020 Population',
    8 :'2022 Population',
    9 :'All the Population around these years'
  }
  # Extract information based on the selected options
  if option==1 and option_population!=9: 
    option_key = options_population.get(option_population)
    if option_key is not None:
      label=option_key  + " of " + land_data['Country/Territory']
      value=int(land_data[option_key]) 
    else:
      label='Not Found'
      value=0
      
  elif option==1 and option_population==9:
    iterador=0
    # Sum the population of all years
    for x in range(1,9): 
      iterador+=int(land_data[options_population.get(x)])

    label='Sum of population of all years (' + land_data['Country/Territory'] +')'
    value=iterador

  else:
    option_key = options.get(option)
    if option_key is not None:
      label=option_key + " (" + land_data['Country/Territory']+ ")" 
      if option==6:
        value=int(land_data[option_key])
      else:
        value=float(land_data[option_key])
    else:
      label='Not Found'
      value=0
  return label,value

def versus(graph,option,modality,option_population,land_name1,land_name2):
  option_for_master_info1=0
  option_for_master_info2=0
  
  # "master_info" function understand what type of lands are being compared
  if modality==1:
    option_for_master_info1=1
    option_for_master_info2=1
  elif modality==2:
    option_for_master_info1=2
    option_for_master_info2=2
  elif modality==3:
    option_for_master_info1=1
    option_for_master_info2=3
  elif modality==4:
    option_for_master_info1=1
    option_for_master_info2=2
  elif modality==5:
    option_for_master_info1=2
    option_for_master_info2=3

  # Retrieve information for both lands
  land_data1 = master_info(land_name1,option_for_master_info1)
  label1,value1=get_specific_info(land_data1,option,option_population)

  land_data2 = master_info(land_name2,option_for_master_info2)
  label2,value2=get_specific_info(land_data2,option,option_population)

  # Adjust values if one land belongs to the other (for specific modalities)
  if modality in (3,5) or (modality==4 and land_data1 and land_data2 and land_data1['Continent']==land_data2['Country/Territory']):
    value2=value2-value1

  # Prepare labels and values for the graph
  labels=[label1,label2]
  values=[value1,value2]

  # Print a summary of the comparison
  option_dict={
    1:'Population',
    2:'Area',
    3:'Density',
    4:'Growth Rate',
    5:'World Population Percentage',
    6:'Rank'
  }

  # Generate the appropriate graph
  print(f'\n{option_dict.get(option)} Summary:')
  print(labels[0],'=',values[0])
  print(labels[1],'=',values[1])
  
  if graph==1:
    generate_bar_chart(labels,values)
  else:
    generate_pie_chart(labels,values)