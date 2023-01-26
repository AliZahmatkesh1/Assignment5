import math

def m_daraje2():
    a = input("Enter Namber a = \n_").lower().strip()
    if a == "exit" :
        exit()
    elif a == "0" :
        print("\n namber a != 0\n")
        return "B"

    b = input("Enter Namber b = \n_").lower().strip()
    if b == "exit":
        exit()

    c = input("Enter Namber c = \n_").lower().strip()
    if c == "exit":
        exit()
    else :
        a = int(a)
        b = int(b)
        c = int(c)

    d = ((-b)**2 - 4*a*c)
    if d < 0 :
        print("\nrishe haghighi nadarad\n")
        j = (-b + math.sqrt(abs(d)))/(2*a)
        j1 = (-b - math.sqrt(abs(d)))/(2*a)
        print("rishe = ",j)
        print("rishe = ",j1)
        print("\n")
    
    elif d == 0 :
        print("\nyek rishe haghighi darad\n")
        j = (-b + math.sqrt(abs(d)))/(2*a)
        j1 = (-b - math.sqrt(abs(d)))/(2*a)
        print("rishe = ",j)
        print("rishe = ",j1)
        print("\n")
    
    else :
        print("\ndo rishe haghighi darad\n")
        j = (-b + math.sqrt(d))/(2*a)
        j1 = (-b - math.sqrt(d))/(2*a)
        print("rishe = ",int(j))
        print("rishe = ",int(j1))
        print("\n")

while True :
    m_daraje2()
