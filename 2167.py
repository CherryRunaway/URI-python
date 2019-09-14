def main(): 
    n = int(input())
    v = input().split(" ")
    li = []
    li2 = []
    i = int(0)
    aux = int(1)
    
    while i < len(v):
      li.append(int(v[i]))
      i += 1
    
    i = int(0)
    
    for i in range(0, len(li)):
      if aux < len(li):
        if int(li[i]) > int(li[aux]):
          li2.append(int(aux))
      aux += 1
    
    if li2 == []:
      print("0")
    else:
      li2[0] = int(li2[0]+1)
      print(li2[0])
      
main()
