def main():
  
    n = int(input())
    
    minu = n/60
    n = n - (int(minu) * 60)
    seg = n
    hora = minu/60
    minu = int(minu)%60
    
    print("%d:%d:%d" % (hora, minu, seg))
    
main()
