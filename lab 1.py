#Завдання 1 (1.py):
#• Для осіб до 4 років вхід вільний.
#• Для осіб віком від 4 до 18 років квиток коштує 10 злотих.
#• Для осіб старше 18 років квиток коштує 20 злотих.
#Приклад: Введіть вік клієнта: 5
#Вартість квитка: 10 злотих
a=int(input("pudaj wiek"))
if a < 4:
    print("wstep jest bezplatny")
elif a <= 18:
    print("bilet kosztuje 10 zt")
else:
    print("bilet kosztise 20 zt")

