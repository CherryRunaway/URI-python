def main():
  curu, boi, boto, mapi, iara = 300, 1500, 600, 1000, 150
  n = int(1)
  total = 0
  
  while n <= 5:
    aux = int(input())
    
    if n == 5:
      iara = int(iara) * aux
      total = int(total) + int(iara)
    if n == 4:
      mapi = int(mapi) * aux
      total = int(total) + int(mapi)
    if n == 3:
      boto = int(boto) * aux
      total = int(total) + int(boto)
    if n == 2:
      boi = int(boi) * aux
      total = int(total) + int(boi)
    if n == 1:
      curu = int(curu) * aux
      total = int(total) + int(curu)
      
    n += 1
  
  total = int(total) + 225
  
  print("%d"%total)
  
main()
