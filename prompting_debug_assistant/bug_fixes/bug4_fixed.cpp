#include <iostream>
using namespace std;

// Fixed Off-by-one error: changed loop condition to i < size
int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int size = sizeof(arr) / sizeof(arr[0]);

    for (int i = 0; i < size; i++) { // Fix: < instead of <=
        cout << arr[i] << endl;
    }

    return 0;
}
