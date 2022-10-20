what= input(" (+,-,/,*)")
a=float(input("numer operacji 1"))
b=float(input("numer operacji 2"))
if what == "+":
    c=a+b
    print("wynik"+str(c))
elif what == "-":
    c=a-b
    print("wynik"+ str(c))
elif what == "*":
    c=a*b
    print("wynik"+ str(c))
elif what == "/":
    c=a/b
    print("wynik"+str(c))