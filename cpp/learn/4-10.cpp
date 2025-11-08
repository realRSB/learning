#include <iostream>

int main() {
    std::cout << "enter a number: ";
    int num {};
    std::cin >> num;
    
    if (num > 0)
        std::cout << "number is postive";
    
    else if (num == 0)
        std::cout << "number is 0";
    
    else 
        std::cout << "number is negative";

    return 0;
}
