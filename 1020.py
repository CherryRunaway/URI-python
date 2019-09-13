def main():
  
    n = int(input())
    
    ano = n/365
    n = n - (int(ano) * 365)
    mes = n/30
    dia = n%30
    
    print("%d ano(s)\n%d mes(es)\n%d dia(s)" % (ano, mes, dia))
    
main()
