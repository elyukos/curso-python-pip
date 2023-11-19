def getpop(country_dict):
  print("utils - country_dict")
  pop_dict = {
    '2022': country_dict['2022 Population'],
    '2020': country_dict['2020 Population'],
    '2015': country_dict['2015 Population'],
    '2010': country_dict['2010 Population'],
    '2000': country_dict['2000 Population'],
    '1990': country_dict['1990 Population'],
    '1980': country_dict['1980 Population'],
    '1970': country_dict['1970 Population'],
  }
  labels = list(pop_dict.keys())
  values = list(pop_dict.values())
  print("utils - country_dict 2")
  return labels, values
  
def pop_by_country(data, country):
  print("utils - pop_by_country")
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result

def global_pop(data):
  print("utils - global_pop")
  
  

