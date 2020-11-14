#include <iostream>
using namespace std;

int main(){
    int max = 0, max_i = 0;

    for(int i=1; i<10; i++){
        int num;
        cin >> num;
        if(num > max){
            max = num;
            max_i = i;
        }
    }

    cout << max << endl << max_i << endl;
}