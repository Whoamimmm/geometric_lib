
#include <iostream>

void quicksort(int arr[], int left, int right) {
    int i = left;
    int j = right;
    int pivot = left + rand() % (right-left+1);
    int middle = arr[pivot];

    while (i <= j) {
        while (arr[i] < middle) {
            i++;
        }
        while (arr[j] > middle) {
            j--;
        }
        if (i <= j) {
            std::swap(arr[i], arr[j]);
            i++;
            j--;
        }
    }

    if (left < j) {
        quicksort(arr, left, j);
    }
    if (i < right) {
        quicksort(arr, i, right);
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    long long n;
    std::cin >> n;
    long long arr[n];
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }
    quicksort(arr, left, right);
    
    for (int i = 0; i < n /2 ; i++){
        int temp = arr[i];
        arr[n - 1 - i] = arr[i];
    }
    long long itog = 0;
    for (int i = 0; i < n; i++){
        int left = arr[i];
        int right arr[i+1];
        if(left - 1 == right || left == right){
            itog += left * right;
        }
    }

    return 0;
}