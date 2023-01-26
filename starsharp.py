


def star(m , n) :
    jadval_asli = []
    jadval = []
    rdif , sot = m , n
    sh = "#"
    st = "*"
    t = 1
    t1 = 1
    ra = str(sot /2)

    for i in range(rdif) :
        for j in range(sot) :
            if t == 1 :
                jadval.append(sh)
                t = 2
            elif t == 2 :
                jadval.append(st)
                t = 1
            else :
                jadval.append(st)
                t = 1

                
        jadval_asli.append(jadval)
        jadval = []
        if ra[-1] == "0" and t1 == 1:
            t = 3
            t1 = 2
        elif ra[-1] == "0" and t1 == 2 :
            t1 = 1
            t = 1


    for l in jadval_asli :
        for k in l :
            print(k , end="")
        print("")


while True :
    print ("\nExit = exit\n")
    n = input("Enter n : ").lower().strip()
    if n == "exit" :
        break
    m = input("Enter m : ").lower().strip()
    if m == "exit" :
        break
    else :
        star(int(m) , int(n) )
