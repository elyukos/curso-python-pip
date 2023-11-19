import utils
import read_csv
import charts

def run():
  print("run")
  data = read_csv.read_csv('./data.csv')
  country = input("Ingrese el pais: ")
  result = utils.pop_by_country(data, country)
  print("run 2")
  if len(result) > 0:
    country = result[0]
    labels, values = utils.getpop(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
  print("run 3")

def run2():
  print("run")
  data = read_csv.read_csv('./data.csv')
  country = list(map(lambda y : y['Country/Territory'], data))
  percentages = list(map(lambda y : y['World Population Percentage'], data))
  charts.generate_pie_chart(country, percentages)
#si se ejecuta directo desde la terminal ejecuta run()
if __name__ == '__main__':
  run()
  #run2()