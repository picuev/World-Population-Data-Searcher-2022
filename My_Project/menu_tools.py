from charts import generate_bar_chart, generate_pie_chart
from data_comparison_tools import get_population, versus
from population_analysis import master_info, population_percentage_pie

def validate_option(valid_options): 
  # This function validate user's option in each submenu.
  try: 
    prompt = int(input('->')) 
    while prompt not in valid_options:
      print(f'Invalid Option. Please enter a valid option {valid_options}')
      prompt=int(input('->'))
  except ValueError:
        print('Invalid Input. Please restart the program.')
  else:
      return prompt

def ask_information():
  # Extract and display information about a specific land (country, continent, or world) from the CSV file
  print('1) Country 🗾')
  print('2) Continent 🗺')
  print('3) World 🌍 (just land territory)')
  option = validate_option((1,2,3))

  if option ==1: # Pick specific information based on the territory scale
    land=(input("Enter the country's name: ")).title().strip() # COUNTRIES

    information=master_info(land,option)
    for key,value in information.items():# Text summary
      print(key,':',value)

    labels,values=get_population(information,False)# Graphic population summary
    generate_bar_chart(labels,values)

  elif option ==2:
    land=(input("Enter the continent's name: ")).title().strip()# CONTINENTS

    information=master_info(land,option)# Graphic population percentage summary
    for key,value in information.items():
      print(key,':',value)

    labels,values=population_percentage_pie(False,land)
    generate_pie_chart(labels,values)

  elif option ==3: 
    land='Earth' # THE WORLD

    information=master_info(land,option)
    for key,value in information.items():
      print(key,':',value)

    labels,values=population_percentage_pie(True)
    generate_pie_chart(labels,values)

def compare_information():
  print('1) Population over the years 👪') # Compare population over the years
  print('2) Between lands 🆚') # Compare 1 stadistic between two lands
  option = validate_option((1,2))

  if option==1: # Pick population evolution based on the picked territory scale
    print('1) By country 🗾')
    print('2) By continent 🗺')
    print('3) By the Earth 🌍')
    option = validate_option((1,2,3))

    if option ==1:
      land=(input("Enter the country's name: ")).title().strip() # COUNTRIES
      land=master_info(land,option)
      labels,values=get_population(land,True) 
      generate_bar_chart(labels,values)
    elif option==2:
      land=(input("Enter the continent's name: ")).title().strip() # CONTINENTS
      continent=master_info(land,option)
      labels,values=get_population(continent,True)
      generate_bar_chart(labels,values)
    elif option==3:
      land='Earth'
      world=master_info(land,option) # THE WORLD
      labels,values=get_population(world,True)
      generate_bar_chart(labels,values)

  elif option==2: # Compare one stadistic between two lands

    option_population=0 # This variable is used if the user picks option 1

    print('Select a topic: ')

    print('1) Population 🌐')
    print('2) Area 📶')
    print('3) Density ⚖')
    print('4) Growth Rate 📈')
    print('5) World Population Percentage ✅')
    print('6) Rank 🏆')
    option = validate_option((1,2,3,4,5,6))

    # GRAPHICS OPTIONS
    print('Select a graph to show stadistics: ')

    print('1) Bar graph 📊')
    print('2) Circle graph 🕔')
    graph= validate_option((1,2)) 

    if option==1: # POPULATION OPTIONS
      print('1) 1970 Population')
      print('2) 1980 Population')
      print('3) 1990 Population')
      print('4) 2000 Population')
      print('5) 2010 Population')
      print('6) 2015 Population')
      print('7) 2020 Population')
      print('8) 2022 Population')
      print('9) All the Population around these years')
      option_population = validate_option((1,2,3,4,5,6,7,8,9)) 

      print('1) 🚩 Country vs Country 🚩')
      print('2) 🗺 Continent vs Continent 🗺')
      print('3) 🚩 Country vs World 🌍')
      print('4) 🚩 Country vs Continent 🗺')
      print('5) 🗺 Continent vs World 🌍')
      modality= validate_option((1,2,3,4,5))

      if modality != 3 and modality !=5: # For modality 3 and 5, user doesn't have to input land 2
        name1=(input('Enter name\'s land 1: ')).title().strip() 
        name2=(input('Enter name\'s land 2: ')).title().strip() 
        versus(graph,option,modality,option_population,name1,name2)

      else:
        name1=(input('Enter name\'s land 1: ')).title().strip()
        name2='World'
        print('Enter name\'s land 2: World')
        versus(graph,option,modality,option_population,name1,name2)

    elif option== 6: # RANK OPTIONS
      print('1) 🚩 Country vs Country 🚩')
      print('2) 🗺 Continent vs Continent 🗺')
      modality = validate_option((1,2))
      name1=(input('Enter name\'s land 1: ')).title().strip()
      name2=(input('Enter name\'s land 2: ')).title().strip()
      versus(graph,option,modality,option_population,name1,name2)

    elif option==3 or option==4: # DENSITY & GROWTH RATE OPTIONS
      print('1) 🚩 Country vs Country 🚩')
      modality=validate_option((1,1))
      name1=(input('Enter name\'s land 1: ')).title().strip()
      name2=(input('Enter name\'s land 2: ')).title().strip()
      versus(graph,option,modality,option_population,name1,name2)

    else: # AREA & WORLD POPULATION PERCENTAGE OPTIONS
      print('1) 🚩 Country vs Country 🚩')
      print('2) 🗺 Continent vs Continent 🗺')
      print('3) 🚩 Country vs World 🌍')
      print('4) 🚩 Country vs Continent 🗺')
      print('5) 🗺 Continent vs World 🌍')
      modality = validate_option((1,2,3,4,5))

      if modality != 3 and modality !=5: # For modality 3 and 5, user doesn't have to input land 2
        name1=(input('Enter name\'s land 1: ')).title().strip()
        name2=(input('Enter name\'s land 2: ')).title().strip()
        versus(graph,option,modality,option_population,name1,name2)

      else:
        name1=(input('Enter name\'s land 1: ')).title().strip()
        name2='World'
        print('Enter name\'s land 2: World')
        versus(graph,option,modality,option_population,name1,name2)