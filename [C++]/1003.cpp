#include <iostream>
using namespace std;

pair<int, int> count01[40];

void fib_count(const int num) {
    count01[0] = make_pair(1, 0);
    count01[1] = make_pair(0, 1);
    for (int i = 2; i <= num; i++) {
        count01[i] = make_pair(count01[i - 1].first + count01[i - 2].first,
                               count01[i - 1].second + count01[i - 2].second);
    }

    cout << count01[num].first << ' ' << count01[num].second << endl;
}

int main() {
    int cases;
    cin >> cases;
    for (int i = 0; i < cases; i++) {
        int num;
        cin >> num;

        fib_count(num);
    }
}