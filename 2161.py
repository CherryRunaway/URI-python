def main(): 
    n = int(input())
    raiz = 0
    
    for i in range(0, n):
      raiz = float(raiz) + 6.0
      raiz = 1.0/raiz
    
    raiz += 3.0
    print("%.10f"%raiz)

main()
