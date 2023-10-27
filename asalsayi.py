# 4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

sayi=int(input(""))

def asalsayi(sayi):
    tambolen=[]
    asalliste=[1,sayi]
    for i in range(1,sayi+1):
        if sayi%i==0:
            tambolen.append(i)
    print(tambolen)

    if tambolen==asalliste:
        print(f"{sayi} asaldır")
    else:
        print(f"{sayi} asal değildir")

asalsayi(sayi)



    





"""liste1=[1,2]
liste2=[1,2]

sonuc=liste1==liste2
print(sonuc)"""