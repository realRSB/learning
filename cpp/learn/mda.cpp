#include <iostream>
#include <limits>
using namespace std;

constexpr int ROWS = 4;
constexpr int COLS = 4;
constexpr int TOTAL_SHIPS = 4;

int main() {
	// 1 = ship, 0 = no ship. 4x4 array
	bool ships[ROWS][COLS] = {
		{ 0, 1, 1, 0 },
		{ 0, 0, 0, 0 },
		{ 0, 0, 1, 0 },
		{ 0, 0, 1, 0 }
	};

	int hits {0};
	int turns {0};

	while (hits < TOTAL_SHIPS) {
		int row, column;

		cout << "Select Coordinates \n";
		
		// row input, making sure its an int
		cout << "Choose a row number between 0 and " << ROWS - 1 << ": ";
		if (!(cin >> row)) {
		    cin.clear();
		    cin.ignore(numeric_limits<streamsize>::max(), '\n');
		    cout << "Invalid, please enter an integer\n\n";
		    continue;
		}
		
		// column input, making sure its an int
		cout << "Choose a column number between 0 and " << COLS - 1 << ": ";
		if (!(cin >> column)) {
		    cin.clear();
		    cin.ignore(numeric_limits<streamsize>::max(), '\n');
		    cout << "Invalid, please enter an integer\n\n";
		    continue;
		}
		
        
        // range check
        if (row < 0 || row >= ROWS || column < 0 || column >= COLS) {
            std::cout << "Out of range. Try again.\n\n";
            continue;
        }
        
        // counts valid turns
        turns++;
		    
	    // if there is a hit, remove it by setting val to false (0)
	    if (ships[row][column]) {
	        ships[row][column] = false;
	        hits++;
	        cout << "Hit! good job :)" << (TOTAL_SHIPS - hits) << " left.\n\n";
	    } else {
	        cout << "Miss :c\n\n";
	    }
	}
	
    cout << "Victory!\n";
	cout << "You won in " << turns << " turns\n";
	return 0;
}
