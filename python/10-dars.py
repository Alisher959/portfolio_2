from random import randint
kodlar=[135, 132, 134, 131, 133]
yangi_kod=randint(130,135)
i=0
while yangi_kod in kodlar:
    i+=1
    yangi_kod=randint(130,135)
print('Takrrlanishlar soni ',i)
print(yangi_kod)