#include <iostream>
using namespace std;

int main(){
    int i,j = 0;
    int n;
    cout << "Enter N : ";
    cin >> n;

    for(i=1;i<=n;i++){
        for(j=1;j<=i;j++){
            cout << j;
        }
        cout << endl;
    }
}