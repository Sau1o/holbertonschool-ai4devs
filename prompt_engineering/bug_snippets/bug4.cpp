// Intended to print all elements of an array

#include <iostream>
using namespace std;

int main() {
    int nums[] = {1, 2, 3, 4, 5};
    int length = sizeof(nums) / sizeof(nums[0]);

    for (int i = 0; i <= length; i++) {
        cout << nums[i] << " ";
    }
    cout << endl;
    return 0;
}
