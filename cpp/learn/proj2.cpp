#include <iostream>

void doWhile() {
    int posnum {};

    do {
        std::cout << "enter a positive number: ";
        std::cin >> posnum;
        } while (posnum <= 0);
}


int main() {
    int num {0};
    
    while (num < 5) {
        std::cout << num << '\n';
        num++;
    }
    
    doWhile();
}
