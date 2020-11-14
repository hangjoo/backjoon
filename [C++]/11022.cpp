#include <iostream>
using namespace std;

int main(){
    int T; cin >> T;
    for(int i=1; i<=T; i++){
        int a,b;
        cin >> a >> b;

        printf("Case #%d: %d + %d = %d\n", i, a, b, a+b);
    }
}