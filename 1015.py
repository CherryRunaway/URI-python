#import math

def main():
  eixo1 = input().split(" ")
  eixo2 = input().split(" ")
  x1, y1 = eixo1
  x2, y2 = eixo2
  
  x = float(x2) - float(x1)
  y = float(y2) - float(y1)
  distancia = float(x)**2 + float(y)**2
  #distancia = math.sqrt(float(distancia))
  distancia = float(distancia)**2
  distancia = float(distancia)**(1/2)
  distancia = float(distancia)**0.5
  
  print("%0.4f" %distancia)
main()
