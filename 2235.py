def main():
    
    n1, n2, n3 = input().split(" ")
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    
    if n1 == n2 or n1 == n3 or n2 == n3:
      print("S")
    elif n1 > n2 and n1 > n3:
      if n2 + n3 == n1:
        print("S")
      else:
        print("N")
    elif n2 > n1 and n2 > n3:
      if n1 + n3 == n2:
        print("S")
      else:
        print("N")
    elif n3 > n2 and n3 > n1:
      if n2 + n1 == n3:
        print("S")
      else:
        print("N")   
        
main()
