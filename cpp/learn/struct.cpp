#include <iostream>
#include <string>

using namespace std;

// // Declare a structure named "car" if using way 1
struct car {
  string brand;
  string model;
  int year;
};

// way 1
void way1() {
//   Create a car structure and store it in myCar1;
//   car myCar1;
//   myCar1.brand = "BMW";
//   myCar1.model = "X5";
//   myCar1.year = 1999;

//   Create another car structure and store it in myCar2;
//   car myCar2;
//   myCar2.brand = "Ford";
//   myCar2.model = "Mustang";
//   myCar2.year = 1969;
 
//   Print the structure members
//   cout << myCar1.brand << " " << myCar1.model << " " << myCar1.year << "\n";
//   cout << myCar2.brand << " " << myCar2.model << " " << myCar2.year << "\n";
}


// way 2
void way2() {
    struct {
      string brand;
      string model;
      int year;
    } myCar1, myCar2; // We can add variables by separating them with a comma here
    
    // Put data into the first structure
    myCar1.brand = "BMW";
    myCar1.model = "X5";
    myCar1.year = 1999;
    
    // Put data into the second structure
    myCar2.brand = "Ford";
    myCar2.model = "Mustang";
    myCar2.year = 1969;
    
    // Print the structure members
    cout << myCar1.brand << " " << myCar1.model << " " << myCar1.year << "\n";
    cout << myCar2.brand << " " << myCar2.model << " " << myCar2.year << "\n";
}

// practice problem
int main() {
    struct {
        string name;
        int age;
        char grade;
    } myStruct;
    
    myStruct.name = "Liam";
    myStruct.age = 35;
    myStruct.grade = 'A';
    
    cout << "Name: " << myStruct.name << '\n';
    cout << "Age: " << myStruct.age << '\n';
    cout << "Grade: " << myStruct.grade << '\n';
    
    return 0;
}
