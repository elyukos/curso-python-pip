import utils
import read_csv
import charts

def run():
  print("*"*19,"run","*"*19)
  data = dict(read_csv.read_csv_col('./app/data.csv'))
  print(data)
  print("*"*19,"run2","*"*19)
  #labels = dict(data).keys
  labels = list(data.keys())[1:-1]
  print(labels)
  print("*"*19,"run3","*"*19)
  #values = (dict(data).values)
  values=list(map(float,list(data.values())[1:-1]))
  
  print("*"*19,"run4","*"*19)
  charts.generate_pie_chart(labels,values)

#si se ejecuta directo desde la terminal ejecuta run()
if __name__ == '__main__':
  run()