#a=int(input("pudaj wiek"))
#if a < 4:
  #  cena = 0
#elif a <= 18:
 #   cena = 10
#else:
  #  cena = 20
#print(f"Cena biletu: {cena}")


#literka= input("wprowadz literke")
#if len(literka)>1 or len(literka)==0:
  #  print("niepoprawny dany")
  #  exit()
#if literka <='a' and literka <='z':
    #print("literka jest mala")
#elif literka <='A' and literka <="z":
  #  print("Literka jest duza")
#else:
   # print("podany znak nie jest litera")
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

