def main(): 
    l = int(input())
    c = int(input())
    
    t1 = (l*c) + ((l-1) * (c-1))
    t2 = ((l-1) * 2) + ((c-1) * 2)
    
    print("%d"%t1)
    print("%d"%t2)
main()
