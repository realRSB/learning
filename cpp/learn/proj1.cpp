#include <iostream>
#include <string>

using namespace std;

void happyDetector (int day) {
	string result = (day == 6 || day == 7) ? "happy" : "sad";
	cout << "Mood: " << result << '\n';
}

int main () {

	cout << "What day number is it today (1-7): ";
	int day {};
	if (!(cin >> day) || day < 1 || day > 7) {
		cout << "Please enter a valid number (1-7)";
        return 1;
	}

	happyDetector(day);

    switch (day) {
        case 6: 
            cout << "Today is Saturday\n"; 
            break;
        case 7: 
            cout << "Today is Sunday\n"; 
            break;
        default: 
            cout << "Looking forward to the weekend\n"; 
            break;
	}
}
