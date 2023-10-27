# 1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.


fibonacci=[1,1]
for i in range(18):
    sayi=fibonacci[-1]+fibonacci[-2]
    fibonacci.append(sayi)


print(fibonacci)
print(len(fibonacci))