#include <iostream>
using namespace std;

int main(){
    int n, m;
    cin >> n >> m;
    char** board = new char* [n + 2];
    for(int i=0; i<n; i++){
        board[i] = new char [m + 2];
        for(int j=0; j<m; j++){
            cin >> board[i][j];
        }
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cout << board[i][j];
        }
        cout << endl;
    }
}