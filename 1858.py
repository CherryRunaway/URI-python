def main():
    menor = 1000
    n = int(input())
    
    vet = input().split(" ")
    
    for i in range(0, len(vet)):
      if int(vet[i]) < menor:
        menor = int(vet[i])
        aux = i
      i += 2
    
    aux += 1
    print("%d" %aux)
    
main()
