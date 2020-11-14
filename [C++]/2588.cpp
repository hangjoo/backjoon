#include <iostream>
using namespace std;

int main(){
    int a, b, b_1, b_10, b_100;
    cin >> a >> b;

    b_1 = b%10;
    b_10 = (b-b_1)%100/10;
    b_100 = (b-b_1-b_10)/100;
    
    cout << a*b_1 << endl << a*b_10 << endl << a*b_100 << endl << a*b;
}