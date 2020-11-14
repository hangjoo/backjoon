#include <iostream>
using namespace std;

int main(){
    int T;
    scanf("%d", &T);

    for(int i=0; i<T; i++){
        int a, b;
        scanf("%d %d", &a, &b);
        printf("%d\n", a+b);
    }
}