#include <iostream>
using namespace std;

void forEach() {
    int myNumbers[5] = {1, 2, 3, 4, 5};
    
    for (int num : myNumbers) {
        cout << "Number: " << num << '\n';
    }
}

int main() {
    for (int i {1}; i <= 3; i++) {
        for (int j {1}; j <= 3; j++) {
            cout << i * j << " ";
        }
        cout << "\n";
        }
    
    forEach();
}
