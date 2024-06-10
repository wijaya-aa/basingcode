#include <iostream>
using namespace std;

void selectionSort(int list[], int length) {
    for (int index = 0; index < length - 1; index++) {
        int indeksMinimum = index;
        for (int indeksBanding = index + 1; indeksBanding < length; indeksBanding++) {
            if (list[indeksBanding] < list[indeksMinimum]) {
                indeksMinimum = indeksBanding;
            }
        }
        // Tukar elemen
        int temp = list[index];
        list[index] = list[indeksMinimum];
        list[indeksMinimum] = temp;
    }
}

int main() {
    int listAcak[] = {20, 11, 56, 76, 23, 55};
    int length = sizeof(listAcak) / sizeof(listAcak[0]);

    cout << "Data Yang belum di sortir dengan selection sort\n";
    for (int i = 0; i < length; i++) {
        cout << listAcak[i] << " ";
    }
    cout << endl;

    selectionSort(listAcak, length);

    cout << "Data Yang telah di sortir dengan selection sort\n";
    for (int i = 0; i < length; i++) {
        cout << listAcak[i] << " ";
    }
    cout << endl;

    return 0;
}
