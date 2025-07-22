#include <iostream>
using namespace std;

int main(){
    int n = 5;
    for(int i=0;i<n;i++){
        for(int j=n;j>i;j--){
            char ch = 'A' + n - j;
            cout << ch << " ";
        }
        cout << endl;
    }
}