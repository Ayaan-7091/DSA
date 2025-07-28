#include <iostream>
using namespace std;
int main(){

    int n = 3;
    for(int i=0;i<n;i++){
        for(int j=n;j>i;j--){
            cout << "*";
        }
        for(int k=0;k<2*i;k++){
            cout << " /";
        }
        cout << endl;
    }

     for(int i=n;i>0;i--){
        for(int j=n;j>=i;j--){
            cout << "*";
        }
      for(int k=i;k<2*i;k++){
            cout << " /";
        }
        cout << endl;
    }
}