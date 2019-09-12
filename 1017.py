def main():
  tempo = input()
  vel = input()
  
  km = int(vel) * int(tempo)
  litros = int(km) / 12.0
  
  print("%.3f"%litros)
  
main()
