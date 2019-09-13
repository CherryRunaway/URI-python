def main():
    
    t = int(input())
    
    for i in range(0, t):
      r1, r2 = input().split(" ")
      total = int(r1) + int(r2)
      i += 1
      print("%d" %total)
      
main()
