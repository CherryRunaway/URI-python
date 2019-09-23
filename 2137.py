def main(): 
  
  while True:
    try:
      n = int(input())
      lista = []

      for i in range(0, n):
        num = input()
        lista.append(num)

      for i in range(0, n):
        for j in range(0, n):
          if (lista[i] <= lista[j]):
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
      
      for i in range(0, n):
        print("%s"%lista[i])
        

      lista = ''
      
    except EOFError:
      break
    
main()
