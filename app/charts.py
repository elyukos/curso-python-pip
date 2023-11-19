import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
  print("charts - generate_bar_chart")
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  print("charts - generate_bar_chart 1.5")
  plt.savefig(f'./imgs/{name}.png')
  plt.close()
  #plt.show()
  print("charts - generate_bar_chart 2")
  
def generate_pie_chart(labels, values):
  print("*"*19,"generate_pie_chart","*"*19)
  fig, ax = plt.subplots()
  print("*"*19,"generate_pie_chart2","*"*19)
  ax.pie(values, labels=labels)
  print("*"*19,"generate_pie_chart3","*"*19)
  ax.axis('equal')
  print("*"*19,"generate_pie_chart4","*"*19)
  plt.savefig("pie.png")
  plt.close()
  #plt.show()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [100, 200, 80]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)