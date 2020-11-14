#include <iostream>
using namespace std;

int main(){
    int A, B, C;
    cin >> A >> B >> C;
    int tot = A*B*C;
    int con[10] = {0,};

    for(int i=tot; i>0; i=i/10){
        con[i%10]++;
    }

    for(int i=0; i<10; i++){
        cout << con[i] << endl;
    }
}