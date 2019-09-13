def main():
  t = int(input())
  
  while t > 0:
    t -= 1
    n, k = input().split()
    
    resto = int(n) % int(k)
    divi = int(n) / int(k)
    total = int(resto) + int(divi)
    
    print(total)
  
main()
