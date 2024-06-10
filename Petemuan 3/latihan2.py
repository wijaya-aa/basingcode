# squsencial searches

#deklarasi list dengan isi beberapa element
l = [144,102,100,77,122,65,80,60,78,89,12]
x = 102  #elemen yang dicari
index = -1 #posisi elemen yang dicari

# perulanangan untuk memeriksa tiap elemnt pada list
for i in range(len(l)):
    if l[i]== x:  #jika ditemukan
        index = i #index diisi dengan nilai i (nilai saat ini)
        break #dihentikan

if index == -1: #jika index masih terisi dengan nilai -1 maka tidak ditemukan
    print (f"nilai {x} tidak ditemukan")
else:  #sebaliknya berarti nilai yang dicari ditemukan pada indeks yang sama dengan nilai index
    print(f"nilai {x} ditemukan pada indeks {index}")