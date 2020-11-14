#include <iostream>
using namespace std;

int main(){
    int star;
    cin >> star;
    
    for(int i=1; i<=star; i++){
        for(int j=1; j<=i; j++){
            cout << '*';
        }
        cout << endl;
    }
}