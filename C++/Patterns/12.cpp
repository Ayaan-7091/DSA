#include <iostream>
using namespace std;

int main(){
    int n = 4;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=i;j++){
            cout << i;
        }
        for(int j=1;j<= ((2*n) - (2*i));j++){
            cout << " ";
        }
        for(int j=1;j<=i;j++){
            cout << i;
        }
        cout << endl;
    }
}