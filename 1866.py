def main():
    
    n = int(input())
    
    while n > 0:
      n -= 1
      val = int(input())
      if val % 2 == 0:
        print("0")
      else:
        print("1")
      
main()
