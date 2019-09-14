def main(): 
    copos = input().split(" ")
      
    for i in range(0, len(copos)):
      if copos[i] == '1':
        print("%d"%(i+1))
        
main()
