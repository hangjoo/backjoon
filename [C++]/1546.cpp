#include <iostream>
using namespace std;

int main(){
    int N; cin >> N;
    float tot = 0;
    float max = 0;
    for(int i=0; i<N; i++){
        float score;
        cin >> score;

        if(score > max) max = score;
        tot += score;
    }

    float result = tot*100/(max*N);
    cout << result << endl;
}