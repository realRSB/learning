#include <iostream>

int main () {
    std::cout << "Enter 3 numbers: ";
    
    int x {};
    int y {};
    int z{};
    
    std::cin >> x >> y >> z;
    
    std::cout << "Your entered " << x << ", " << y << ", and " << z << '\n';

    return 0;
}
