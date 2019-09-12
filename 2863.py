def main():
  while True:
    try:
      n = int(input())
      menor = float(1000.0)
      while n > 0:
        n = n - 1
        tempo = float(input())
        if tempo < menor:
          menor = tempo
      print("%.02f"%menor)
    except EOFError:
      break
  
main()
