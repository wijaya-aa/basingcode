# NAMA = EGI PUTU WIJAYA
# NPM = 23555201078
# KELAS = 2.3

def selection_sort(list): 
    for index in range(len(list)-1):
        indeks_minimum = index
        for indeks_banding in range(index + 1, len(list)-1):
            if list[indeks_banding] < list[indeks_minimum]:
                indeks_minimum = indeks_banding
        list[index], list[indeks_minimum] = list[indeks_minimum], list[index]


list_acak = [20,11,56,76,23,55]
print(f"Data Yang belum di sortir dengan selection sort \n {list_acak}")


selection_sort(list_acak)
print(f"Data Yang telah di sortir dengan selection sort \n {list_acak}")