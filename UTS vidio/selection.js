function selectionSort(list) {
    for (let index = 0; index < list.length - 1; index++) {
        let indeksMinimum = index;
        for (let indeksBanding = index + 1; indeksBanding < list.length; indeksBanding++) {
            if (list[indeksBanding] < list[indeksMinimum]) {
                indeksMinimum = indeksBanding;
            }
        }
        [list[index], list[indeksMinimum]] = [list[indeksMinimum], list[index]];
    }
}

let listAcak = [20, 11, 56, 76, 23, 55];
console.log("Data Yang belum di sortir dengan selection sort\n", listAcak);

selectionSort(listAcak);
console.log("Data Yang telah di sortir dengan selection sort\n", listAcak);
