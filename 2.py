literka= input("wprowadz literke")
if len(literka)>1 or len(literka)==0:
    print("niepoprawny dany")
    exit()
if literka <='a' and literka <='z':
    #print("literka jest mala")
elif literka <='A' and literka <="z":
    print("Literka jest duza")
else:
    print("podany znak nie jest litera")