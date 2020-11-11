#include <iostream>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    int* num_list = new int[N];
    for (int i = 0; i < N; i++) {
        cin >> num_list[i];
    }

    int res_sum = 0;
    for (int i = 0; i < N - 2; i++) {
        for (int j = i + 1; j < N - 1; j++) {
            for (int k = j + 1; k < N; k++) {
                int sum = num_list[i] + num_list[j] + num_list[k];
                if (sum <= M && (M - sum) < (M - res_sum)) {
                    res_sum = sum;
                }
            }
        }
    }
    cout << res_sum;
}