#include <iostream>
using namespace std;

int main(){
    int n = 5;
    int temp = 1;

    for(int i=0;i<n;i++){
        for(int j=0;j<=i;j++){
            cout << temp << " ";
            temp = temp +1;
        }
        cout << endl;
    }
}