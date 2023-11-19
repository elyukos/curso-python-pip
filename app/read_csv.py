import csv

def read_csv(path):
  print("read_csv - read_csv")
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      #print(list(iterable))
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    print("read_csv - read_csv 2")
    return data

def read_csv_col(path): # funcion para leer csv completo
  with open(path, 'r') as file: #abrir
    reader = list(csv.reader(file, delimiter=',')) #leer (como objeto)
    data = [] #lista que se va a regresar
    columns = [2,16]
    for row in reader: #iterar por cada fila
      country_dict = list(row[i] for i in columns)
      data.append(country_dict) #agregar dict a lista
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  #print(data[0])
