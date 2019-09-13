def main():
    
    ing, ing_novo = input().split(" ")
    ing = float(ing)
    ing_novo = float(ing_novo)
    
    aumento = (100.0 * ing_novo) / ing
    aumento = float(aumento) - 100
    
    print("%.2f" %aumento, end = "")
    print("%")
    
main()
