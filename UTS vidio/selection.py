# NAMA = EGI PUTU WIJAYA
# NPM = 23555201078
# KELAS = 2.3

def selection_sort(list):
    # Loop melalui setiap elemen dalam list kecuali elemen terakhir
    for index in range(len(list) - 1):
        # Anggap elemen saat ini sebagai yang terkecil
        indeks_minimum = index
        # Bandingkan elemen saat ini dengan elemen berikutnya
        for indeks_banding in range(index + 1, len(list)):
            # Jika elemen yang dibandingkan lebih kecil, perbarui indeks_minimum
            if list[indeks_banding] < list[indeks_minimum]:
                indeks_minimum = indeks_banding
        # Tukar elemen yang terkecil dengan elemen saat ini
        list[index], list[indeks_minimum] = list[indeks_minimum], list[index]

list_acak = [20,11,56,76,23,55,25]

print(f"Data Yang belum di sortir dengan selection sort \n {list_acak}")


selection_sort(list_acak)
print(f"Data Yang telah di sortir dengan selection sort \n {list_acak}")