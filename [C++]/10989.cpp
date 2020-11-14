#include <iostream>
using namespace std;

unsigned int numCount[10001] = {0,};

int main()
{
    unsigned int count;
    scanf("%d", &count);
    
    for(int i=0; i<count; i++){
        int temp;
        scanf("%d", &temp);
        numCount[temp]++;
    }

    for(int i=1; i<=10000; i++){
        for(int j=0; j<numCount[i]; j++){
            printf("%d\n", i);
        }
    }
}