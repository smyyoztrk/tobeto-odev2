"""2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.
    Matematikte bazı pozitif tam sayıların pozitif bölenleri toplamı, sayının kendisinin iki katına eşittir.
    Bu tür sayılara “mükemmel sayı” denir.
"""
sayi=int(input(""))
toplam=0
for i in range(1,sayi+1):
    if sayi % i == 0:

        toplam+=i
if toplam==2*sayi:
    print(f"{sayi} mükemmel sayıdır")
else:
    print(f"{sayi} mükemmel sayı değildir")