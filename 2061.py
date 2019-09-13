def main():
    
    abas, acoes = input().split(" ")
    abas = int(abas)
    acoes = int(acoes)
    
    while acoes > 0:
      acoes -= 1
      acao = input()
      
      if acao[0] == 'f':
        abas += 1
      elif acao[0] == 'c':
        abas -=1
    
    print("%d" %abas)
    
    
main()
