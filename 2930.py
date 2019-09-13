def main():
    e, d = input().split()
    e = int(e)
    d = int(d)
    
    if e > d:
      print("Eu odeio a professora!")
    elif e+3 <= d:
      print("Muito bem! Apresenta antes do Natal!")
    else:
      print("Parece o trabalho do meu filho!")
      if e+2 < 24:
        print("TCC Apresentado!")
      else :
        print("Fail! Entao eh nataaaaal!")
        
main()
