#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <math.h>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;
typedef long long ll;
int main() {
  int t, n;
  cin >> t;
  while (t--) {
    cin >> n;
    vector<int> arr(n, -1);
    for (int i = 0; i < n; i++)
      cin >> arr[i];
    sort(arr.begin(), arr.end());
    int val = 0;
    for (int i = n / 2; i < n; i++) {
      if (arr[i] == val) {
        val++;
      }    
    }
    cout << val << endl;
  }
}
