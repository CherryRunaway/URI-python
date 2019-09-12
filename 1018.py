def main():
  val = input()
  cem, cinq, vinte, dez, cinco, dois, um = 0, 0, 0, 0, 0, 0, 0
  aux = int(val)
  
  cem = int(val) / 100
  val = int(val)%100
  cinq = int(val) / 50
  val = int(val)%50
  vinte = int(val) / 20
  val = int(val)%20
  dez = int(val) / 10
  val = int(val)%10
  cinco = int(val) / 5
  val = int(val)%5
  dois = int(val) / 2
  val = int(val)%2
  
  print("%d"%aux)
  print("%d nota(s) de R$ 100,00"%cem)
  print("%d nota(s) de R$ 50,00"%cinq)
  print("%d nota(s) de R$ 20,00"%vinte)
  print("%d nota(s) de R$ 10,00"%dez)
  print("%d nota(s) de R$ 5,00"%cinco)
  print("%d nota(s) de R$ 2,00"%dois)
  print("%d nota(s) de R$ 1,00"%val)
  
main()
