#include <iostream>
using namespace std;

int main(){
    int count;
    cin >> count;
    getchar();

    for(int i=0; i<count; i++){
        int score = 1;
        int tot = 0;

        char ch;
        while((ch = getchar()) != '\n'){
            if(ch == 'O'){
                tot += score;
                score++;
            }
            else{
                score = 1;
            }
        }
        
        cout << tot << endl;
    }
}