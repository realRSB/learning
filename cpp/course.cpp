#include <bits/stdc++.h>
using namespace std;

void chap1() {
	// --- OUTPUT EXAMPLE ---
	int a = 123, b = 456;
	string x = "monkey";
	cout << a << " " << b << " " << x << "\n";

	// --- TYPES ---
	int ai = 123456789;                // 32-bit int
	long long bl = 9123091238LL;       // 64-bit long long
	double xd = 0.3;                   // floating point

	// fixed decimals
	cout << fixed << setprecision(9) << xd << "\n";

	// --- Set theory reminders ---
	// intersection(A,B): in both A and B
	// union(A,B): in A or B (or both)
	// complement(A): not in A
	// difference(A,B): in A but not in B
}

void chap2() {
	// Time complexity reminders:
	// - k nested loops -> O(n^k)
	// - Halving each step -> O(log n)
	// - Sort / DS ops -> O(n log n)
	// - Subset iteration -> O(2^n)

	// Rule of thumb: maximum input size n (or b) that can be handled
    // within typical contest time limits (~1 second)
    //
    // - n ≤ 10       → algorithms up to O(n!) are fine
    // - n ≤ 20       → algorithms up to O(2^n) are fine
    // - n ≤ 500      → algorithms up to O(n^3) are fine
    // - n ≤ 5000     → algorithms up to O(n^2) are fine
    // - n ≤ 1e6      → algorithms up to O(n log n) or O(n) are fine
    // - n very large → only very fast algorithms O(log n) or O(1)
    
    // sum formula = n(n+1)/2

}

void bubbleSort(int array[], int n) {
	for (int i = 0; i < n - 1; ++i) {
		bool swapped = false;
		for (int j = 0; j < n - 1 - i; ++j) {
			if (array[j] > array[j + 1]) {
				swap(array[j], array[j + 1]);
				swapped = true;
			}
		}
		if (!swapped) break; // already sorted
	}
}

void chap3() {
	vector<int> v = {4, 2, 5, 3, 5, 8, 3};
	sort(v.begin(), v.end());

	cout << "Sorted vector: ";
	for (int x : v) cout << x << " ";
	cout << "\n";

	// Demo: std::binary_search
	int target = 5;
	if (binary_search(v.begin(), v.end(), target)) {
		cout << target << " found!\n";
	} else {
		cout << target << " not found!\n";
	}

	// Demo: std::lower_bound (get index)
	auto it = lower_bound(v.begin(), v.end(), target);
	if (it != v.end() && *it == target) {
		cout << target << " first occurs at index " << (it - v.begin()) << "\n";
	} else {
		cout << target << " not found (via lower_bound)\n";
	}

	// Upperbound (> target) vs Lowerbound (>= target)
	auto lb = lower_bound(v.begin(), v.end(), target);
	auto ub = upper_bound(v.begin(), v.end(), target);

	cout << "lower_bound index: " << (lb - v.begin()) << "\n";
	cout << "upper_bound index: " << (ub - v.begin()) << "\n";

	// To find count
	auto count = ub - lb;
	cout << "count: " << count << "\n";

	// min + max
	auto minIt = min_element(v.begin(), v.end());
	auto maxIt = max_element(v.begin(), v.end());

	cout << "Min value: " << *minIt << "\n";
	cout << "Max value: " << *maxIt << "\n";
}

void chap4() {
	// Vector = dynamic array
	vector<int> v;
	v.push_back(3); // {3}
	v.push_back(2); // {3, 2}
	cout << v[0] << '\n'; // 3
	cout << v.back() << '\n'; // 2
	v.pop_back(); // {3}

	// Set = all elements are distinct
	set<int> s;
	s.insert(3);
	s.insert(2);
	cout << s.count(3) << '\n'; // 1
	s.erase(3);
	cout << s.size() <<'\n'; // 1

	// Multiset = set but can have more than one instance of elements
	multiset<int> ms = {5, 5, 5};
	cout << ms.count(5) << '\n'; // 3
	ms.erase(ms.find(5)); // gets index of 5
	cout << ms.count(5) << '\n'; // 2

	// Map = array of key-value pairs
	map<string, int> m = {{"monkey", 4}, {"banana", 3}, {"harpsichord", 9}};
	cout << m["banana"] << "\n"; // 3
	if (m.count("aybabtu")) {
	    // if key exists
	    cout << "yay! key exists";
	} else {
	    cout << "nooo, key doesn't exist" << "\n";
	}
	
	// Iterators = functions that are given range of elements in ds
	sort(v.begin(), v.end());
    reverse(v.begin(), v.end());
    random_shuffle(v.begin(), v.end());
    auto it = s.begin(); // find smallest element in set
    cout << *it << "\n"; // using * we can access to element that iterator points to

    // Deque = dynamic array where both ends can be efficiently changed
    // has pushback and pobback but also pushfront and popfront
    deque<int> d = {5, 2};
    d.push_front(3); // [3,5, 2]
    d.pop_back(); // [3, 5]
    d.pop_front(); // [5]
    
    // Stack = add + remove element from top. only access top element
    stack<int> st;
    st.push(3);
    st.push(2);
    st.push(5);
    cout << st.top() << '\n'; // 5
    st.pop();
    cout << st.top() << '\n'; // 2
    
    // Queue = add element to end, remove first element
    queue<int> q;
    q.push(3);
    q.push(2);
    q.push(5);
    cout << q.front() << '\n'; // 3
    q.pop();
    cout << q.front() << '\n'; // 2
    
    // Priority queue = maintains set of elements
    priority_queue<int> pq;
    pq.push(3);
    pq.push(5);
    pq.push(7);
    pq.push(2);
    cout << pq.top() << '\n'; // 7; gets largest elements 
    pq.pop(); // removes largest element
    cout << pq.top() << '\n'; // 5
}


void printArray(const int* arr, int n) {
	for (int i = 0; i < n; ++i) cout << arr[i] << (i + 1 == n ? '\n' : ' ');
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	chap1();
	chap2();

	// bubble sort demo (raw array)
	int arr[] = {64, 25, 12, 22, 11};
	int n = static_cast<int>(sizeof(arr) / sizeof(arr[0]));

	cout << "Original array: ";
	printArray(arr, n);

	bubbleSort(arr, n);

	cout << "Sorted array: ";
	printArray(arr, n);

	chap3();
	chap4();

	return 0;
}
