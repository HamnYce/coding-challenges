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
typedef vector<int> vi;

class SegmentTree {
  vi st, A;
  int n;
  int left(int p) { return p << 1; }
  int right(int p) { return (p << 1) + 1; }

  void build(int p, int L, int R) {
    if (L == R)
      st[p] = L;
    else {
      build(left(p), L, (L + R) / 2);
      build(right(p), (L + R) / 2, R);
      int p1 = st[left(p)], p2 = st[right(p)];
      st[p] = (A[p1] <= A[p2]) ? p1 : p2;
    }
  }

  int rmq(int p, int L, int R, int i, int j) {
    if (i > R || j < L)
      return -1;
    if (L >= i && R <= j)
      return st[p];

    int p1 = rmq(left(p), L, (L + R) / 2, i, j);
    int p2 = rmq(right(p), (L + R) / 2, R, i, j);

    if (p1 == -1)
      return p2;
    if (p2 == -1)
      return p1;

    return (A[p1] <= A[p2]) ? p1 : p2;
  }

  SegmentTree(const vi &_A) {
    A = _A;
    n = (int)A.size();
    st.assign(4 * n, 0);
    build(1, 0, n - 1);
  }

  int rmq(int i, int j) { return rmq(1, 0, n - 1, i, j); }
};

void insert_and_bubble(int i, vector<int> &seg) {
  seg[i]++;
  if (i == 0)
    return;
  else if (i % 2 == 0)
    insert_and_bubble(i / 2, seg);
  else
    insert_and_bubble((i - 1) / 2, seg);
}
int query(int left, int right, vector<int> &seg) { return 0; }

int main() {
  int n;
  cin >> n;
  vector<int> points(n);
  for (int i = 0; i < n; i++) {
    cin >> points[i];
    points[i]--;
  }

  vector<int> seg(10000, 0);
  for (int i = 0; i < n; i++) {
  }
}
