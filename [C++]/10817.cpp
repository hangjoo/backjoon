#include <iostream>
#include <queue>
using namespace std;

int main(){
    priority_queue<int> nums;
    int num_1, num_2, num_3;
    cin >> num_1 >> num_2 >> num_3;

    nums.push(num_1);
    nums.push(num_2);
    nums.push(num_3);

    nums.pop();
    cout << nums.top();
}