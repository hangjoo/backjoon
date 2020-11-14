#include <iostream>
using namespace std;
#define day 1440

int main(){
    int hour, min;
    cin >> hour >> min;
    
    int alarm = (day + hour*60 + min - 45)%day;
    cout << alarm/60 << ' ' << alarm%60;
}