#include <iostream>
using namespace std;

int main(){
    int min = 1000000;
    int max = -1000000;

    int N;
    cin >> N;
    for(int i=0; i<N; i++){
        int num;
        cin >> num;
        if(num <= min) min = num;
        if(num >= max) max = num;
    }

    cout << min << ' ' << max << endl;
}