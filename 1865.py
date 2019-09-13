def main():
  
    n = int(input())
    
    while n > 0:
      n -= 1
      nome, forca = input().split(" ")
      
      if nome == 'Thor':
        print("Y")
      else:
        print("N")

    
main()
