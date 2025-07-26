#include <iostream>
using namespace std;

int main(){
    int n = 6;
    
    for(int i=0;i<n;i++){
        char ch = 'A' + (n-i-1);
        for(int j=0;j<=i;j++){
            cout << ch << " ";
            ch =  ch + 1;
        }
        cout << endl;
    }
}