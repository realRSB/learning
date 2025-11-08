#include <bits/stdc++.h>
using namespace std;

// VECTOR = dynamic array (contiguous, random access O(1))
void vectorprac() {
    vector<int> v = {3, 1, 4};           // create vector
    v.push_back(2);                      // add element at end
    v.pop_back();                        // remove last element
    cout << v[0] << " " << v.at(1) << "\n"; // access by index

    sort(v.begin(), v.end());            // sort vector O(n log n)
    bool has3 = binary_search(v.begin(), v.end(), 3); // check if 3 exists
    cout << "Found 3? " << has3 << "\n";
}

// DEQUE = double-ended queue (push/pop front + back in O(1))
void dequeprac() {
    deque<int> dq;
    dq.push_front(5);                    // add to front
    dq.push_back(7);                     // add to back
    cout << dq.front() << " " << dq.back() << "\n"; // access front/back
    dq.pop_front();                      // remove from front
}

// QUEUE = FIFO (first in, first out)
void queueprac() {
    queue<int> q;
    q.push(1); q.push(2); q.push(3);     // enqueue
    cout << q.front() << " " << q.back() << "\n"; // front=first, back=last
    q.pop();                             // dequeue
    cout << "Front now: " << q.front() << "\n";
}

// STACK = LIFO (last in, first out)
void stackprac() {
    stack<int> st;
    st.push(10); st.push(20); st.push(30); // push elements
    cout << st.top() << "\n";              // access top
    st.pop();                              // pop top
}

// PRIORITY_QUEUE = heap (max-heap by default, min-heap with greater<>)
void priorityqueueprac() {
    priority_queue<int> mx;               // max-heap
    mx.push(5); mx.push(1); mx.push(9);
    cout << "Max: " << mx.top() << "\n";  // largest element

    priority_queue<int, vector<int>, greater<int>> mn; // min-heap
    mn.push(5); mn.push(1); mn.push(9);
    cout << "Min: " << mn.top() << "\n";  // smallest element
}

// SET / MULTISET = ordered unique / ordered with duplicates
void setprac() {
    set<int> s = {5, 1, 3, 3, 2};        // duplicates dropped -> {1,2,3,5}
    s.insert(4);                         // insert element
    cout << "Count(3): " << s.count(3) << "\n"; // check presence (0/1)
    auto it = s.lower_bound(2);          // first >= 2
    if (it != s.end()) cout << *it << "\n";

    multiset<int> ms;                    // allows duplicates
    ms.insert(5); ms.insert(5); ms.insert(1);
    ms.erase(ms.find(5));                // erase one occurrence of 5
    for (int x : ms) cout << x << " ";   // print elements
    cout << "\n";
}

// MAP = ordered key->value
// UNORDERED_MAP = hash map (avg O(1))
void mapprac() {
    map<string,int> mp;
    mp["alice"] = 2;                     // insert key-value
    mp.insert({"bob", 5});               // insert another key-value
    for (auto &[k,v] : mp) cout << k << ":" << v << " "; // iterate sorted by key
    cout << "\n";

    unordered_map<string,int> ump;
    ump["cow"]++; ump["cow"]++;          // increment count
    ump["sheep"] = 3;
    for (auto &[k,v] : ump) cout << k << ":" << v << " "; // arbitrary order
    cout << "\n";
}

// PAIR = two values bundled together (used in sorting, edges, coords)
void pairprac() {
    pair<int,int> p = {2, 7};            // create pair
    cout << p.first << "," << p.second << "\n";

    vector<pair<int,int>> vp = {{2,3}, {1,4}, {2,1}};
    sort(vp.begin(), vp.end());          // sort by first, then second
    for (auto [x,y] : vp) cout << "(" << x << "," << y << ") ";
    cout << "\n";
}

// ALGORITHMS = useful functions from <algorithm> and <numeric>
void algorithmsprac() {
    vector<int> v = {5,1,4,3,2,2};
    sort(v.begin(), v.end());                       // sort ascending
    v.erase(unique(v.begin(), v.end()), v.end());   // remove duplicates
    reverse(v.begin(), v.end());                    // reverse vector

    int sum = accumulate(v.begin(), v.end(), 0);    // sum of elements
    cout << "Sum: " << sum << "\n";

    transform(v.begin(), v.end(), v.begin(), [](int x){ return x*x; }); // square each
    for (int x : v) cout << x << " ";               // print all
    cout << "\n";
}

// STRING = common operations
void stringprac() {
    string s = "ababa";
    cout << s.size() << "\n";             // length
    cout << s.substr(1,3) << "\n";        // substring (pos=1, len=3)
    cout << s.find("ba") << "\n";         // find substring (returns pos or npos)
    s.push_back('c');                     // add char at end
    s.pop_back();                         // remove last char
}

int main() {
    vectorprac();
    dequeprac();
    queueprac();
    stackprac();
    priorityqueueprac();
    setprac();
    mapprac();
    pairprac();
    algorithmsprac();
    stringprac();
    return 0;
}
