public class SelectionSort {

    public static void selectionSort(int[] list) {
        for (int index = 0; index < list.length - 1; index++) {
            int indeksMinimum = index;
            for (int indeksBanding = index + 1; indeksBanding < list.length; indeksBanding++) {
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

    public static void main(String[] args) {
        int[] listAcak = {20, 11, 56, 76, 23, 55};
        System.out.println("Data Yang belum di sortir dengan selection sort");
        for (int num : listAcak) {
            System.out.print(num + " ");
        }
        System.out.println();

        selectionSort(listAcak);
        System.out.println("Data Yang telah di sortir dengan selection sort");
        for (int num : listAcak) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
