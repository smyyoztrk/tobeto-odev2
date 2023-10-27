# 5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız.


sayi=int(input("")) 


def asalmi(i):
    tambolen=[]
    asallistesarti=[1,i]
    for j in range(1,i+1):
        if i%j==0:
            tambolen.append(j)
    if tambolen==asallistesarti:
        return True
    else:
        return False
    
def asalcarpan(sayi):
    asalcarpan=[]
    for i in range(1,sayi+1):
        if sayi%i==0:
            if asalmi(i)==True:
                asalcarpan.append(i)
    return asalcarpan
        
print(asalcarpan(sayi))