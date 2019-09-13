def main():
    h, t, f = input().split(" ")
    h = int(h)
    t = int(t)
    f = int(f)
    
    if h == 0:
      h = 24
    
    result = h + t + f
    
    if result == 24:
      print("0")
    elif result > 24:
      result = int (result) - 24
      print("%d" %result)
    else:
      print("%d" %result)
    
main()
