def main():
  anao, elfo, humano, mago, hobbit = 0, 0, 0, 0, 0
  n = int(input())
  
  while n > 0:
    n -= 1
    ser = input()
    tam = int(len(ser))
    
    if ser[tam-1] == 'A':
      anao += 1
    if ser[tam-1] == 'E':
      elfo += 1
    if ser[tam-1] == 'H':
      humano += 1
    if ser[tam-1] == 'M':
      mago += 1
    if ser[tam-1] == 'X':
      hobbit += 1
  
  print("%d Hobbit(s)"%hobbit)
  print("%d Humano(s)"%humano)
  print("%d Elfo(s)"%elfo)
  print("%d Anao(s)"%anao)
  print("%d Mago(s)"%mago)
  
main()
