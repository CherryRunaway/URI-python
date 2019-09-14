def main(): 
    n = int(input())
    r = input().split(" ")
    li = []
    li2 = []
    i = int(0)
    
    while i < len(r):
      li.append(int(r[i]))
      i += 1
    
    for i in range(1, len(li)):
        if int(li[i-1]) > int(li[i]):
          li2.append(int(i))
    
    if li2 == []:
      print("0")
    else:
      li2[0] = int(li2[0]+1)
      print(li2[0])
      
main()
