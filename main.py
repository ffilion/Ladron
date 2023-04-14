
def veces(n):
  return 'veces' if n>1 else 'vez'

politicos = ['Leonel Fernandez']

for i in range(0,5):
  print(f" {i+1} {veces(i+1)} {politicos[0]}, Corrupto.")


