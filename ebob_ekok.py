# 3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.

sayi1=int(input(""))
sayi2=int(input(""))
sirala=[sayi1,sayi2]
sirala.sort()
sayi1=sirala[0]
sayi2=sirala[1]

def ebobEkok(sayi1,sayi2):
    for i in range(1,sayi1+1):
        if sayi1%i==0 and sayi2%i==0:
            ebob=i

    ekok=(sayi1*sayi2)//ebob

    print(f"{sayi1} ile {sayi2} nin ebobu: {ebob} \n             ekoku: {ekok}")

ebobEkok(sayi1,sayi2)