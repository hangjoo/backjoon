#include <iostream>
using namespace std;

int main(){
    bool diff[42];
    for(int i=0; i<42; i++) diff[i] = false;

    int count = 0;
    for(int i=0; i<10; i++){
        int num;
        cin >> num;
        if(diff[num%42] == false){
            diff[num%42] = true;
            count++;
        }
    }

    cout << count << endl;
}