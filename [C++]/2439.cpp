#include <iostream>
using namespace std;

int main(){
    int count;
    cin >> count;

    for(int i=1; i<=count; i++){
        for(int space=1; space<=count-i; space++){
            cout << ' ';
        }
        for(int star=1; star<=i; star++){
            cout << '*';
        }
        cout << endl;
    }
}