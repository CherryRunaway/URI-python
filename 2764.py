def main(): 
    data = input()
    d = int(data[0])
    dd = int(data[1])
    m = int(data[3])
    mm = int(data[4])
    a = int(data[6])
    aa = int(data[7])
    
    print("%d%d/%d%d/%d%d" %(m, mm, d, dd, a, aa))
    print("%d%d/%d%d/%d%d" %(a, aa, m, mm, d, dd))
    print("%d%d-%d%d-%d%d" %(d, dd, m, mm, a, aa))

main()
