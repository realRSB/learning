// https://cses.fi/problemset/task/1068/
// input = positive integer n
// n even = algorithm divide by 2, if odd multiply by 3 and add 1
// repeat until n is one

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ll n;
    cin >> n;
    
    while (n != 1) {
        cout << n << " ";
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n = n * 3 + 1;
        }
    }
    cout << "\n";

    return 0;
}
