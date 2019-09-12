def main():
  n = int(input())
  
  while n > 0:
    aux = int(input())
    if aux > 8000:
      print('Mais de 8000!')
    else:
      print('Inseto!')
    n = n - 1
  
main()
