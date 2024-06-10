# binary seacrh
k = [1,3,5,6,7,9,1,5,7,2,6,8]
dicari = 7

print(f"mencari nilai{dicari} dengan binary seacrh pada list {k}")
ditemukan = False
batas_awal= 0
batas_akhir = len(k) -1

while not ditemukan and batas_awal <= batas_akhir:
    pos_cari = batas_awal + (batas_akhir-batas_awal) //2
    print(f"posisi pencarian pada indeks {pos_cari} dengan nilai {k[pos_cari]}")
    if k[pos_cari] == dicari:
        ditemukan = True
    elif k[pos_cari] > dicari:
        batas_akhir = pos_cari -1
    else:
        batas_awal = pos_cari +1

if ditemukan:
    print(f"nilai {dicari} ditemukan padan indeks {pos_cari}")
else:
    print(f"nilai {dicari} tidak ditemukan")