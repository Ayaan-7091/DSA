#include <iostream>
using namespace std;


int main(){
    int i,j = 0;
    int n;
    cout << "Enter the value of N : ";
    cin >> n;
    for(i=0;i<n;i++){
      for(j=0;j<n;j++){
        cout << "*";
      }
      cout << endl;
    }
}