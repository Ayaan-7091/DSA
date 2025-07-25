#include <iostream>
using namespace std;
int main(){
    int n = 3;

    for(int i=n;i>0;i--){

        for(int j=1;j<i;j++){
            cout << " ";
        }

        int temp = n-i;
        for(int j=0;j<((2*n-2*i)+1);j++){
            char ch = 'A' + j;
            if (j > temp){
                ch = 'A' + ((2*temp) - j);
            }
            cout<<ch;
        }

        
        for(int j=1;j<i;j++){
            cout << " ";
        }
        cout << endl;
    }
}