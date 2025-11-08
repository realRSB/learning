#include <iostream>

void printHi() {
    std::cout << "Hi!\n";
}

int getValueFromUser() {
    std::cout << "Enter an integer: ";
    int input {};
    
    std::cin >> input;
    
    return input;
}

int main() {
    printHi();
    
    int num {getValueFromUser()};
    
    std::cout << num << " doubled is: " << num * 2 << '\n';
    
    return 0;
}
