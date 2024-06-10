def bubble_sort(list):
    for i in range(len(list)-1):
        for index in range(len(list)-1 -i):
            print(len(list) -1 -i)
            if list[index]< list[index+1]:
                list[index],list[index+1] = list[index+1], list[index]




list = [9,17,2,42,1,7,3,4,67]
print(f"Data yang akan di sort {list}" )
bubble_sort(list)
print(f"Bubble sort {list}")
