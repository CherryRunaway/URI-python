def main():
    nome = input()
    sal = input()
    ven = input()
    
    ven = (0.15 * float(ven))
    
    salario = float(ven) + float(sal)
    
    print("TOTAL = R$ %.2f"%(salario))
main()
