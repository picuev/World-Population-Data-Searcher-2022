from menu_tools import ask_information, compare_information, validate_option

def initial():
  # Main menu of the World Population Data Searcher 2022
  try:
    print('🔍Welcome to the World Population Data Searcher 2022🌎')
    print('Choose an option 👇: ')
    print('1) Ask information ❓')
    print('2) Compare information ⚖')
    option = validate_option((1,2))
      
    if option==1:
      ask_information()
    elif option==2:
      compare_information()
  except (IndexError, ZeroDivisionError):
    print('Invalid Input. Please restart the program.')
    
if __name__=='__main__':
  initial() 