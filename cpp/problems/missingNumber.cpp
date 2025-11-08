//https://cses.fi/problemset/task/1083/
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> nums(n - 1);
    for (int i = 0; i < n - 1; i++) cin >> nums[i];

    long long sum = 1LL * n * (n + 1) / 2;
    long long x = 0;
    for (int num : nums) x += num;

    cout << (sum - x) << "\n";
    return 0;
}
