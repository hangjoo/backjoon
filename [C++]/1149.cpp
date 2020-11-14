#include <iostream>
using namespace std;
#define INF 987654321

int value[1000][3];

int pre_val(int** house, const int idx, const int color);

int main(){
    for(int i=0; i<1000; i++){
        for(int j=0; j<3; j++){
            value[i][j] = -1;
        }
    }

    int count;
    cin >> count;
    int **house = new int* [count];
    for(int i=0; i<count; i++){
        house[i] = new int [3];
        for(int j=0; j<3; j++){
            cin >> house[i][j];
        }
    }

    int num0 = pre_val(house, count-1, 0);
    int num1 = pre_val(house, count-1, 1);
    int num2 = pre_val(house, count-1, 2);

    cout << min(num0, min(num1, num2));
    
}

int pre_val(int ** house, const int idx, const int color){
    if(idx == 0){
        if(value[idx][color] != -1){
            return value[idx][color];
        }
        else{
            return value[idx][color] = house[idx][color];
        }
    }
    else{
        int num[3] = {INF, INF, INF};
        if(value[idx][color] != -1){
            return value[idx][color];
        }
        else{
            for(int i=0; i<3; i++){
                if(color != i){
                    num[i] = pre_val(house, idx-1, i);
                }
            }
            return value[idx][color] = house[idx][color] + min(num[0], min(num[1], num[2]));
        }        
    }
}