def main():
  peca1 = input().split(" ")
  peca2 = input().split(" ")

  cod1, qtde1, valor1 = peca1
  cod2, qtde2, valor2 = peca2

  total = (int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2))

  print("VALOR A PAGAR: R$ %0.2f" %total)
 
main()
