def quick_sort (data):
    index = len(data)    #index yang menampung panjang data
    if index <=1:
        return data
    else:
        pivot = data.pop()  #pivot diambil data terakhir dalam list

        data_kiri= [] #variabel untuk menampung data kiri  
        data_kanan= [] #variabel untuk menampung data kanan
        
        for i in data:  #untuk melakukan perulangan dan perbandingan
            if i < pivot:  #nilai dalam data < pivot
                data_kiri.append(i)  #masukan ke variabel data kiri
            else:
                data_kanan.append(i) #masukan ke variabel data kanan

        #fungsi rekursif
        return quick_sort(data_kiri) + [pivot] + quick_sort(data_kanan)
    
data =[3,2,4,6,7,9,2]
print(f"data acak {data}")
hasil = quick_sort(data)
print(f"data urut {hasil}")
