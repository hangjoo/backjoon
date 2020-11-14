#include <iostream>
using namespace std;

int main(){
    int C;  cin >> C;
    for(int i=0; i<C; i++){
        int num;    cin >> num;
        int con[num];
        int tot = 0;
        for(int j=0; j<num; j++){
            int score;  cin >> score;
            con[j] = score;
            tot += score;
        }

        float average = tot/float(num);
        int adv = 0;
        for(int j=0; j<num; j++){
            if(con[j] > average) adv++;
        }

        float percent = float(adv)/float(num)*100;
        printf("%.3f%%\n", percent);
    }
}