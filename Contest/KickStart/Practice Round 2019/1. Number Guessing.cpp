#include <iostream>
#include <string>
using namespace std;

int main() {
  int num_test_cases;
  cin >> num_test_cases;
  while(num_test_cases--) {
    int lo, hi;
    cin >> lo >> hi;
    int num_tries;
    cin >> num_tries;
    int head = lo + 1, tail = hi;
    while (true) {
      int m = (head + tail) / 2;
      cout << m << endl;
      string s;
      cin >> s;
      if (s == "CORRECT") break;
      if (s == "TOO_SMALL")
        head = m + 1;
      else
        tail = m - 1;
    }
  }
  return 0;
}
