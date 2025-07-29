#include <iostream>
using namespace std;

int main(){
    int n = 6;

    for(int i=n-1;i>=0;i--){
        for(int j=i;j<n;j++){
            cout << "*";
        }
        for(int k=0;k<2*i;k++){
            cout<<" ";
        }
        for(int j=i;j<n;j++){
            cout << "*";
        }
        cout << endl;
    }
    for(int i=1;i<n;i++){
        for(int j=n-1;j>=i;j--){
            cout<<"*";
        }
        for(int k=0;k<2*i;k++){
            cout << " ";
        }
         for(int j=n-1;j>=i;j--){
            cout<<"*";
        }
        cout << endl;
    }
}