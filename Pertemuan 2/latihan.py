# NAMA = EGI PUTU WIJAYA
# NPM = 2355201078
# KELAS = 2.3

def insertion_sort(list):
    for i in range(1,len(list)):
        kunci = list[i]
        j = i - 1
        while j >= 0 and kunci < list[j]:
            list[j + 1] = list[j]
            j -=1
            list[j + 1] =kunci


list= [10,23,45,23,41]
print(f"List Acak {list}")

insertion_sort(list)
print(f"Insertion list {list}")