def main():
  linha1 = input().split(" ")
  
  a, b, c = linha1
  
  maiorab = (int(a)+int(b)+abs(int(a)-int(b)))/2
  maiorc = (int(maiorab)+int(c)+abs(int(maiorab)-int(c)))/2
  
  print("%d eh o maior" %maiorc)
main()
